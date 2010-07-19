# $Id$
#
# This is the checkpkg library, common for all checkpkg tests written in
# Python.

import copy
import cPickle
import errno
import itertools
import logging
import operator
import optparse
import os
import os.path
import re
import pprint
import progressbar
import socket
import sqlite3
import sqlobject
import time
from sqlobject import sqlbuilder
import subprocess
import textwrap
import yaml
from Cheetah import Template
import opencsw
import overrides
import package_checks
import models as m
import configuration as c
import tag

DEBUG_BREAK_PKGMAP_AFTER = False
DB_SCHEMA_VERSION = 5L
PACKAGE_STATS_VERSION = 9L
SYSTEM_PKGMAP = "/var/sadm/install/contents"
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"
SONAME = "soname"
CONFIG_MTIME = "mtime"
CONFIG_DB_SCHEMA = "db_schema_version"
DO_NOT_REPORT_SURPLUS = set([u"CSWcommon", u"CSWcswclassutils", u"CSWisaexec"])
DO_NOT_REPORT_MISSING = set([])
DO_NOT_REPORT_MISSING_RE = [r"\*?SUNW.*"]
DUMP_BIN = "/usr/ccs/bin/dump"
PSTAMP_RE = r"(?P<username>\w+)@(?P<hostname>[\w\.-]+)-(?P<timestamp>\d+)"
DESCRIPTION_RE = r"^([\S]+) - (.*)$"
BAD_CONTENT_REGEXES = (
    # Slightly obfuscating these by using the default concatenation of
    # strings.
    r'/export' r'/medusa',
    r'/opt' r'/build',
)

SYSTEM_SYMLINKS = (
    ("/opt/csw/bdb4",     ["/opt/csw/bdb42"]),
    ("/64",               ["/amd64", "/sparcv9"]),
    ("/opt/csw/lib/i386", ["/opt/csw/lib"]),
)
INSTALL_CONTENTS_AVG_LINE_LENGTH = 102.09710677919261
SYS_DEFAULT_RUNPATH = [
    "/usr/lib/$ISALIST",
    "/usr/lib",
    "/lib/$ISALIST",
    "/lib",
]

CONTENT_PKG_RE = r"^\*?(CSW|SUNW)[0-9a-zA-Z\-]?[0-9a-z\-]+$"

# This shared library is present on Solaris 10 on amd64, but it's missing on
# Solaris 8 on i386.  It's okay if it's missing.
ALLOWED_ORPHAN_SONAMES = set([u"libm.so.2"])

REPORT_TMPL = u"""#if $missing_deps or $surplus_deps or $orphan_sonames
Dependency issues of $pkgname:
#end if
#if $missing_deps
#for $pkg, $reasons in $sorted($missing_deps)
$pkg, reasons:
#for $reason in $reasons
 - $reason
#end for
RUNTIME_DEP_PKGS_$pkgname += $pkg
#end for
#end if
#if $surplus_deps
If you don't know of any reasons to include these dependencies, you might remove them:
#for $pkg in $sorted($surplus_deps)
? $pkg
#end for
#end if
"""

SCREEN_ERROR_REPORT_TMPL = u"""#if $errors
#if $debug
ERROR: One or more errors have been found by $name.
#end if
#for $pkgname in $errors
$pkgname:
#for $error in $errors[$pkgname]
#if $debug
  $repr($error)
#elif $error.msg
$textwrap.fill($error.msg, 78, initial_indent="# ", subsequent_indent="# ")
# -> $repr($error)

#end if
#end for
#end for
#else
#if $debug
OK: $repr($name) module found no problems.
#end if
#end if
#if $messages
#for $msg in $messages
$textwrap.fill($msg, 78, initial_indent=" * ", subsequent_indent="   ")
#end for
#end if
#if $gar_lines

# Checkpkg suggests adding the following lines to the GAR recipe:
# This is a summary; see above for details.
#for $line in $gar_lines
$line
#end for
#end if
"""

# http://www.cheetahtemplate.org/docs/users_guide_html_multipage/language.directives.closures.html
TAG_REPORT_TMPL = u"""#if $errors
# Tags reported by $name module
#for $pkgname in $errors
#for $tag in $errors[$pkgname]
#if $tag.msg
$textwrap.fill($tag.msg, 70, initial_indent="# ", subsequent_indent="# ")
#end if
$pkgname: ${tag.tag_name}#if $tag.tag_info# $tag.tag_info#end if#
#end for
#end for
#end if
"""


class Error(Exception):
  pass


class ConfigurationError(Error):
  pass


class PackageError(Error):
  pass


class StdoutSyntaxError(Error):
  pass


def GetOptions():
  parser = optparse.OptionParser()
  parser.add_option("-b", "--stats-basedir", dest="stats_basedir",
                    help=("The base directory with package statistics "
                          "in yaml format, e.g. ~/.checkpkg/stats"))
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-p", "--profile", dest="profile",
                    default=False, action="store_true",
                    help=("Turn on profiling"))
  parser.add_option("-q", "--quiet", dest="quiet",
                    default=False, action="store_true",
                    help=("Print less messages"))
  (options, args) = parser.parse_args()
  if not options.stats_basedir:
    raise ConfigurationError("ERROR: the -b option is missing.")
  # Using set() to make the arguments unique.
  return options, set(args)


def ExtractDescription(pkginfo):
  desc_re = re.compile(DESCRIPTION_RE)
  m = re.match(desc_re, pkginfo["NAME"])
  return m.group(2) if m else None


def ExtractMaintainerName(pkginfo):
  maint_re = re.compile("^.*for CSW by (.*)$")
  m = re.match(maint_re, pkginfo["VENDOR"])
  return m.group(1) if m else None


def ExtractBuildUsername(pkginfo):
  m = re.match(PSTAMP_RE, pkginfo["PSTAMP"])
  return m.group("username") if m else None


class DatabaseClient(object):

  CHECKPKG_DIR = ".checkpkg"
  SQLITE3_DBNAME_TMPL = "checkpkg-db-%(fqdn)s"
  TABLES_THAT_NEED_UPDATES = (m.CswFile,)
  TABLES = TABLES_THAT_NEED_UPDATES + (
            m.Pkginst,
            m.CswConfig,
            m.Srv4FileStats,
            m.CheckpkgOverride,
            m.CheckpkgErrorTag,
            m.Architecture,
            m.OsRelease,
            m.Maintainer)
  sqo_conn = None
  db_path = None

  def __init__(self, debug=False):
    self.debug = debug

  @classmethod
  def GetDatabasePath(cls):
    if not cls.db_path:
      dbname_dict = {'fqdn': socket.getfqdn()}
      db_filename = cls.SQLITE3_DBNAME_TMPL % dbname_dict
      home_dir = os.environ["HOME"]
      cls.db_path = os.path.join(home_dir, cls.CHECKPKG_DIR, db_filename)
    return cls.db_path

  @classmethod
  def InitializeSqlobject(cls):
    """Establishes a database connection and stores it as a class member.

    The idea is to share the database connection between instances.  It would
    be solved even better if the connection was passed to the class
    constructor.
    """
    if not cls.sqo_conn:
      db_path = cls.GetDatabasePath()
      cls.sqo_conn = sqlobject.connectionForURI('sqlite:%s' % db_path)
      sqlobject.sqlhub.processConnection = cls.sqo_conn

  def CreateTables(self):
    for table in self.TABLES:
      table.createTable(ifNotExists=True)

  def IsDatabaseGoodSchema(self):
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    return good_version


class SystemPkgmap(DatabaseClient):
  """A class to hold and manipulate the /var/sadm/install/contents file."""

  STOP_PKGS = ["SUNWbcp", "SUNWowbcp", "SUNWucb"]

  def __init__(self, system_pkgmap_files=None, debug=False):
    """There is no need to re-parse it each time.

    Read it slowly the first time and cache it for later."""
    super(SystemPkgmap, self).__init__(debug=debug)
    self.cache = {}
    self.pkgs_by_path_cache = {}
    self.file_mtime = None
    self.cache_mtime = None
    self.initialized = False
    if not system_pkgmap_files:
      self.system_pkgmap_files = [SYSTEM_PKGMAP]
    else:
      self.system_pkgmap_files = system_pkgmap_files
    self.csw_pkg_re = re.compile(CONTENT_PKG_RE)
    self.digits_re = re.compile(r"^[0-9]+$")

  def _LazyInitializeDatabase(self):
    if not self.initialized:
      self.InitializeDatabase()

  def InitializeRawDb(self):
    """It's necessary for low level operations."""
    if True:
      logging.debug("Connecting to sqlite")
      self.sqlite_conn = sqlite3.connect(self.GetDatabasePath())

  def InitializeDatabase(self):
    """Established the connection to the database.

    TODO: Refactor this class to first create CswFile with no primary key and
          no indexes.
    """
    need_to_create_tables = False
    db_path = self.GetDatabasePath()
    checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    if not os.path.exists(db_path):
      logging.info("Building the  cache database %s.", self.system_pkgmap_files)
      logging.info("The cache will be kept in %s.", db_path)
      if not os.path.exists(checkpkg_dir):
        logging.debug("Creating %s", checkpkg_dir)
        os.mkdir(checkpkg_dir)
      need_to_create_tables = True
    self.InitializeRawDb()
    self.InitializeSqlobject()
    if not self.IsDatabaseGoodSchema():
      logging.info("Old database schema detected.")
      self.PurgeDatabase(drop_tables=True)
      need_to_create_tables = True
    if need_to_create_tables:
      self.CreateTables()
      self.PerformInitialDataImport()
    if not self.IsDatabaseUpToDate():
      logging.debug("Rebuilding the package cache, can take a few minutes.")
      self.ClearTablesForUpdates()
      self.RefreshDatabase()
    self.initialized = True

  def RefreshDatabase(self):
    for pkgmap_path in self.system_pkgmap_files:
      self._ProcessSystemPkgmap(pkgmap_path)
    self.PopulatePackagesTable()
    self.SetDatabaseMtime()

  def PerformInitialDataImport(self):
    """Imports data into the database.

    Original bit of code from checkpkg:
    egrep -v 'SUNWbcp|SUNWowbcp|SUNWucb' /var/sadm/install/contents |
        fgrep -f $EXTRACTDIR/liblist >$EXTRACTDIR/shortcatalog
    """
    for pkgmap_path in self.system_pkgmap_files:
      self._ProcessSystemPkgmap(pkgmap_path)
    self.SetDatabaseSchemaVersion()
    self.PopulatePackagesTable()
    self.SetDatabaseMtime()

  def _ProcessSystemPkgmap(self, pkgmap_path):
    """Update the database using data from pkgmap.

    The strategy to only update the necessary bits:
      - for each new row
        - look it up in the db
          - if doesn't exist, create it
          - if exists, check the
          TODO: continue this description
    """
    INSERT_SQL = """
    INSERT INTO csw_file (basename, path, line)
    VALUES (?, ?, ?);
    """
    sqlite_cursor = self.sqlite_conn.cursor()
    break_after = DEBUG_BREAK_PKGMAP_AFTER
    contents_length = os.stat(pkgmap_path).st_size
    if break_after:
      estimated_lines = break_after
    else:
      estimated_lines = contents_length / INSTALL_CONTENTS_AVG_LINE_LENGTH
    # The progressbar library doesn't like handling larger numbers
    # It displays up to 99% if we feed it a maxval in the range of hundreds of
    # thousands.
    progressbar_divisor = int(estimated_lines / 1000)
    if progressbar_divisor < 1:
      progressbar_divisor = 1
    update_period = 1L
    # To help delete old records
    system_pkgmap_fd = open(pkgmap_path, "r")
    stop_re = re.compile("(%s)" % "|".join(self.STOP_PKGS))
    # Creating a data structure:
    # soname - {<path1>: <line1>, <path2>: <line2>, ...}
    logging.debug("Building database cache db of the %s file",
                  pkgmap_path)
    logging.info("Processing %s, it can take a few minutes", pkgmap_path)
    count = itertools.count()
    bar = progressbar.ProgressBar()
    bar.maxval = estimated_lines / progressbar_divisor
    bar.start()
    # I tried dropping the csw_file_basename_idx index to speed up operation,
    # but after I measured the times, it turned out that it doesn't make any
    # difference to the total runnng time.
    # logging.info("Dropping csw_file_basename_idx")
    # sqlite_cursor.execute("DROP INDEX csw_file_basename_idx;")
    for line in system_pkgmap_fd:
      i = count.next()
      if not i % update_period and (i / progressbar_divisor) <= bar.maxval:
        bar.update(i / progressbar_divisor)
      if stop_re.search(line):
        continue
      if line.startswith("#"):
        continue
      fields = re.split(c.WS_RE, line)
      pkgmap_entry_path = fields[0].split("=")[0]
      pkgmap_entry_dir, pkgmap_entry_base_name = os.path.split(pkgmap_entry_path)
      # The following SQLObject-driven inserts are 60 times slower than the raw
      # sqlite API.
      # pkgmap_entry = m.CswFile(basename=pkgmap_entry_base_name,
      #                          path=pkgmap_entry_dir, line=line.strip())
      # This page has some hints:
      # http://www.mail-archive.com/sqlobject-discuss@lists.sourceforge.net/msg04641.html
      # "These are simple straightforward INSERTs without any additional
      # high-level burden - no SELECT, no caching, nothing. Fire and forget."
      # sql = self.sqo_conn.sqlrepr(
      #   sqlobject.sqlbuilder.Insert(m.CswFile.sqlmeta.table, values=record))
      # self.sqo_conn.query(sql)
      # ...unfortunately, it isn't any faster in practice.
      # The fastest way is:
      sqlite_cursor.execute(INSERT_SQL, [pkgmap_entry_base_name,
                                         pkgmap_entry_dir,
                                         line.strip()])
      if break_after and i > break_after:
        logging.warning("Breaking after %s for debugging purposes.", break_after)
        break
    bar.finish()
    self.sqlite_conn.commit()
    logging.debug("All lines of %s were processed.", pkgmap_path)

  def _ParsePkginfoLine(self, line):
    fields = re.split(c.WS_RE, line)
    pkgname = fields[1]
    pkg_desc = u" ".join(fields[2:])
    return pkgname, pkg_desc

  def PopulatePackagesTable(self):
    logging.info("Updating the packages table")
    args = ["pkginfo"]
    pkginfo_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = pkginfo_proc.communicate()
    ret = pkginfo_proc.wait()
    lines = stdout.splitlines()
    bar = progressbar.ProgressBar()
    bar.maxval = len(lines)
    bar.start()
    count = itertools.count()
    INSERT_SQL = """
    INSERT INTO pkginst (pkgname, pkg_desc)
    VALUES (?, ?);
    """
    # If self.GetInstalledPackages calls out to the initialization,
    # the result is an infinite recursion.
    installed_pkgs = self.GetInstalledPackages(initialize=False)
    for line in stdout.splitlines():
      pkgname, pkg_desc = self._ParsePkginfoLine(line)
      if pkgname not in installed_pkgs:
        # This is slow:
        # pkg = m.Pkginst(pkgname=pkgname, pkg_desc=pkg_desc)
        # This is much faster:
        self.sqlite_conn.execute(INSERT_SQL, [pkgname, pkg_desc])
      i = count.next()
      bar.update(i)
    # Need to commit, otherwise subsequent SQLObject calls will fail.
    self.sqlite_conn.commit()
    bar.finish()

  def SetDatabaseMtime(self):
    mtime = self.GetFileMtime()
    res = m.CswConfig.select(m.CswConfig.q.option_key==CONFIG_MTIME)
    if res.count() == 0:
      logging.debug("Inserting the mtime (%s) into the database.", mtime)
      config_record = m.CswConfig(option_key=CONFIG_MTIME, float_value=mtime)
    else:
      logging.debug("Updating the mtime (%s) in the database.", mtime)
      res.getOne().float_value = mtime

  def SetDatabaseSchemaVersion(self):
    try:
      config_option = m.CswConfig.select(
          m.CswConfig.q.option_key==CONFIG_DB_SCHEMA).getOne()
      config_option.int_value = DB_SCHEMA_VERSION
    except sqlobject.main.SQLObjectNotFound, e:
      version = m.CswConfig(option_key=CONFIG_DB_SCHEMA,
                            int_value=DB_SCHEMA_VERSION)

  def GetPkgmapLineByBasename(self, filename):
    """Returns pkgmap lines by basename:
      {
        path1: line1,
        path2: line2,
      }
    """
    if filename in self.cache:
      return self.cache[filename]
    self._LazyInitializeDatabase()
    res = m.CswFile.select(m.CswFile.q.basename==filename)
    lines = {}
    for obj in res:
      lines[obj.path] = obj.line
    if len(lines) == 0:
      logging.debug("Cache doesn't contain filename %s", filename)
    self.cache[filename] = lines
    return lines

  def _InferPackagesFromPkgmapLine(self, line):
    """Given a pkgmap line, return all packages it contains."""
    line = line.strip()
    parts = re.split(c.WS_RE, line)
    pkgs = []
    if parts[1] == 'd':
      parts = parts[6:]
    while parts:
      part = parts.pop()
      if self.digits_re.match(part):
        break
      elif "none" == part:
        break
      pkgs.append(part)
    # Make the packages appear in the same order as in the install/contents
    # file.
    pkgs.reverse()
    return pkgs

  def GetPathsAndPkgnamesByBasename(self, filename):
    """Returns paths and packages by basename.

    e.g.
    {"/opt/csw/lib": ["CSWfoo", "CSWbar"],
     "/opt/csw/1/lib": ["CSWfoomore"]}
    """
    lines = self.GetPkgmapLineByBasename(filename)
    pkgs = {}
    # Infer packages
    for file_path in lines:
      pkgs[file_path] = self._InferPackagesFromPkgmapLine(lines[file_path])
    # self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
    #       "/usr/lib": (u"SUNWcsl",)})
    logging.debug("self.error_mgr_mock.GetPathsAndPkgnamesByBasename(%s).AndReturn(%s)",
                  repr(filename), pprint.pformat(pkgs))
    return pkgs

  def GetPkgByPath(self, full_path):
    if full_path not in self.pkgs_by_path_cache:
      self._LazyInitializeDatabase()
      path, basename = os.path.split(full_path)
      try:
        obj = m.CswFile.select(
            sqlobject.AND(
              m.CswFile.q.path==path,
              m.CswFile.q.basename==basename)).getOne()
        self.pkgs_by_path_cache[full_path] = self._InferPackagesFromPkgmapLine(
            obj.line)
      except sqlobject.main.SQLObjectNotFound, e:
        logging.debug("Couldn't find in the db: %s/%s", path, basename)
        logging.debug(e)
        self.pkgs_by_path_cache[full_path] = []
    logging.debug("self.error_mgr_mock.GetPkgByPath(%s).AndReturn(%s)",
                  repr(full_path), pprint.pformat(self.pkgs_by_path_cache[full_path]))
    return self.pkgs_by_path_cache[full_path]

  def GetDatabaseMtime(self):
    if not self.cache_mtime:
      res = m.CswConfig.select(m.CswConfig.q.option_key==CONFIG_MTIME)
      if res.count() == 1:
        self.cache_mtime = res.getOne().float_value
      elif res.count() < 1:
        self.cache_mtime = 1
    logging.debug("GetDatabaseMtime() --> %s", self.cache_mtime)
    return self.cache_mtime

  def GetFileMtime(self):
    if not self.file_mtime:
      stat_data = os.stat(SYSTEM_PKGMAP)
      self.file_mtime = stat_data.st_mtime
    return self.file_mtime

  def GetDatabaseSchemaVersion(self):
    schema_on_disk = 1L
    if not m.CswConfig.tableExists():
      return schema_on_disk;
    res = m.CswConfig.select(m.CswConfig.q.option_key == CONFIG_DB_SCHEMA)
    if res.count() < 1:
      logging.debug("No db schema value found, assuming %s.",
                   schema_on_disk)
    elif res.count() == 1:
      schema_on_disk = res.getOne().int_value
    return schema_on_disk

  def IsDatabaseUpToDate(self):
    f_mtime_epoch = self.GetFileMtime()
    d_mtime_epoch = self.GetDatabaseMtime()
    f_mtime = time.gmtime(int(f_mtime_epoch))
    d_mtime = time.gmtime(int(d_mtime_epoch))
    logging.debug("IsDatabaseUpToDate: f_mtime %s, d_time: %s", f_mtime, d_mtime)
    # Rounding up to integer seconds.  There is a race condition: 
    # pkgadd finishes at 100.1
    # checkpkg reads /var/sadm/install/contents at 100.2
    # new pkgadd runs and finishes at 100.3
    # subsequent checkpkg runs won't pick up the last change.
    # I don't expect pkgadd to run under 1s.
    fresh = f_mtime <= d_mtime
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    logging.debug("IsDatabaseUpToDate: good_version=%s, fresh=%s",
                  repr(good_version), repr(fresh))
    return fresh and good_version

  def ClearTablesForUpdates(self):
    for table in self.TABLES_THAT_NEED_UPDATES:
      table.clearTable()

  def PurgeDatabase(self, drop_tables=False):
    if drop_tables:
      for table in self.TABLES:
        if table.tableExists():
          table.dropTable()
    else:
      logging.debug("Truncating all tables")
      for table in self.TABLES:
        table.clearTable()

  def GetInstalledPackages(self, initialize=True):
    """Returns a dictionary of all installed packages."""
    if initialize:
      self._LazyInitializeDatabase()
    res = m.Pkginst.select()
    return dict([[str(x.pkgname), str(x.pkg_desc)] for x in res])


class LddEmulator(object):
  """A class to emulate ldd(1)

  Used primarily to resolve SONAMEs and detect package dependencies.
  """
  def __init__(self):
    self.runpath_expand_cache = {}
    self.runpath_origin_expand_cache = {}
    self.symlink_expand_cache = {}
    self.symlink64_cache = {}
    self.runpath_sanitize_cache = {}

  def ExpandRunpath(self, runpath, isalist, binary_path):
    """Expands a signle runpath element.

    Args:
      runpath: e.g. "/opt/csw/lib/$ISALIST"
      isalist: isalist elements
      binary_path: Necessary to expand $ORIGIN
    """
    key = (runpath, tuple(isalist))
    if key not in self.runpath_expand_cache:
      origin_present = False
      # Emulating $ISALIST and $ORIGIN expansion
      if '$ORIGIN' in runpath:
        origin_present = True
      if origin_present:
        key_o = (runpath, tuple(isalist), binary_path)
        if key_o in self.runpath_origin_expand_cache:
          return self.runpath_origin_expand_cache[key_o]
        else:
          if not binary_path.startswith("/"):
            binary_path = "/" + binary_path
          runpath = runpath.replace('$ORIGIN', binary_path)
      if '$ISALIST' in runpath:
        expanded_list  = [runpath.replace('/$ISALIST', '')]
        expanded_list += [runpath.replace('$ISALIST', isa) for isa in isalist]
      else:
        expanded_list = [runpath]
      expanded_list = [os.path.abspath(p) for p in expanded_list]
      if not origin_present:
        self.runpath_expand_cache[key] = expanded_list
      else:
        self.runpath_origin_expand_cache[key_o] = expanded_list
        return self.runpath_origin_expand_cache[key_o]
    return self.runpath_expand_cache[key]

  def ExpandSymlink(self, symlink, target, input_path):
    key = (symlink, target, input_path)
    if key not in self.symlink_expand_cache:
      symlink_re = re.compile(r"%s(/|$)" % symlink)
      if re.search(symlink_re, input_path):
        result = input_path.replace(symlink, target)
      else:
        result = input_path
      self.symlink_expand_cache[key] = result
    return self.symlink_expand_cache[key]

  def Emulate64BitSymlinks(self, runpath_list):
    """Need to emulate the 64 -> amd64, 64 -> sparcv9 symlink

    Since we don't know the architecture, we'll adding both amd64 and sparcv9.
    It should be safe.
    """
    key = tuple(runpath_list)
    if key not in self.symlink64_cache:
      symlinked_list = []
      for runpath in runpath_list:
        for symlink, expansion_list in SYSTEM_SYMLINKS:
          for target in expansion_list:
            expanded = self.ExpandSymlink(symlink, target, runpath)
            if expanded not in symlinked_list:
              symlinked_list.append(expanded)
      self.symlink64_cache[key] = symlinked_list
    return self.symlink64_cache[key]

  def SanitizeRunpath(self, runpath):
    if runpath not in self.runpath_sanitize_cache:
      new_runpath = runpath
      while True:
        if new_runpath.endswith("/"):
          new_runpath = new_runpath[:-1]
        elif "//" in new_runpath:
          new_runpath = new_runpath.replace("//", "/")
        else:
          break
      self.runpath_sanitize_cache[runpath] = new_runpath
    return self.runpath_sanitize_cache[runpath]


  def ResolveSoname(self, runpath_list, soname, isalist, path_list, binary_path):
    """Emulates ldd behavior, minimal implementation.

    runpath: e.g. ["/opt/csw/lib/$ISALIST", "/usr/lib"]
    soname: e.g. "libfoo.so.1"
    isalist: e.g. ["sparcv9", "sparcv8"]
    path_list: A list of paths where the soname is present, e.g.
               ["/opt/csw/lib", "/opt/csw/lib/sparcv9"]

    The function returns the one path.
    """
    # Emulating the install time symlinks, for instance, if the prototype contains
    # /opt/csw/lib/i386/foo.so.0 and /opt/csw/lib/i386 is a symlink to ".",
    # the shared library ends up in /opt/csw/lib/foo.so.0 and should be
    # findable even when RPATH does not contain $ISALIST.
    original_paths_by_expanded_paths = {}
    for p in path_list:
      expanded_p_list = self.Emulate64BitSymlinks([p])
      # We can't just expand and return; we need to return one of the paths given
      # in the path_list.
      for expanded_p in expanded_p_list:
        original_paths_by_expanded_paths[expanded_p] = p
    # logging.debug("%s: looking for %s in %s",
    #     soname, runpath_list, original_paths_by_expanded_paths.keys())
    for runpath_expanded in runpath_list:
      if runpath_expanded in original_paths_by_expanded_paths:
        # logging.debug("Found %s",
        #               original_paths_by_expanded_paths[runpath_expanded])
        return original_paths_by_expanded_paths[runpath_expanded]


def ParseDumpOutput(dump_output):
  binary_data = {RUNPATH: [],
                 NEEDED_SONAMES: []}
  runpath = []
  rpath = []
  for line in dump_output.splitlines():
    fields = re.split(c.WS_RE, line)
    if len(fields) < 3:
      continue
    if fields[1] == "NEEDED":
      binary_data[NEEDED_SONAMES].append(fields[2])
    elif fields[1] == "RUNPATH":
      runpath.extend(fields[2].split(":"))
    elif fields[1] == "RPATH":
      rpath.extend(fields[2].split(":"))
    elif fields[1] == "SONAME":
      binary_data[SONAME] = fields[2]
  if runpath:
    binary_data[RUNPATH].extend(runpath)
  elif rpath:
    binary_data[RUNPATH].extend(rpath)

  # Converting runpath to a tuple, which is a hashable data type and can act as
  # a key in a dict.
  binary_data[RUNPATH] = tuple(binary_data[RUNPATH])
  # the NEEDED list must not be modified, converting to a tuple.
  binary_data[NEEDED_SONAMES] = tuple(binary_data[NEEDED_SONAMES])
  binary_data["RUNPATH RPATH the same"] = (runpath == rpath)
  binary_data["RPATH set"] = bool(rpath)
  binary_data["RUNPATH set"] = bool(runpath)
  return binary_data


class CheckpkgManagerBase(object):
  """Common functions between the older and newer calling functions."""

  def __init__(self, name, stats_basedir, md5sum_list, debug=False):
    self.debug = debug
    self.name = name
    self.md5sum_list = md5sum_list
    self.stats_basedir = stats_basedir
    self.errors = []
    self.individual_checks = []
    self.set_checks = []
    self.packages = []

  def GetPackageStatsList(self):
    return [PackageStats(None, self.stats_basedir, x) for x in self.md5sum_list]

  def FormatReports(self, errors, messages, gar_lines):
    namespace = {
        "name": self.name,
        "errors": errors,
        "debug": self.debug,
        "textwrap": textwrap,
        "messages": messages,
        "gar_lines": gar_lines,
    }
    screen_t = Template.Template(SCREEN_ERROR_REPORT_TMPL, searchList=[namespace])
    tags_report_t = Template.Template(TAG_REPORT_TMPL, searchList=[namespace])
    return screen_t, tags_report_t

  def SetErrorsToDict(self, set_errors, a_dict):
    # These were generated by a set, but are likely to be bound to specific
    # packages. We'll try to preserve the package assignments.
    errors = copy.copy(a_dict)
    for tag in set_errors:
      if tag.pkgname:
        if not tag.pkgname in errors:
          errors[tag.pkgname] = []
        errors[tag.pkgname].append(tag)
      else:
        if "package-set" not in errors:
          errors["package-set"] = []
        errors["package-set"].append(error)
    return errors

  def GetOptimizedAllStats(self, stats_obj_list):
    logging.info("Unwrapping candies...")
    pkgs_data = []
    counter = itertools.count()
    length = len(stats_obj_list)
    bar = progressbar.ProgressBar()
    bar.maxval = length
    bar.start()
    for stats_obj in stats_obj_list:
      # pkg_data = {}
      # This bit is tightly tied to the data structures returned by
      # PackageStats.
      #
      # Python strings are already implementing the flyweight pattern. What's
      # left is lists and dictionaries.
      i = counter.next()
      # logging.debug("Loading stats for %s (%s/%s)",
      #               stats_obj.md5sum, i, length)
      raw_pkg_data = stats_obj.GetAllStats()
      pkg_data = raw_pkg_data
      pkgs_data.append(pkg_data)
      bar.update(i)
    bar.finish()
    return pkgs_data

  def Run(self):
    """Runs all the checks

    Returns a tuple of an exit code and a report.
    """
    packages_data = self.GetPackageStatsList()
    db_stat_objs_by_pkgname = {}
    obj_id_list = []
    for pkg in packages_data:
      db_obj = pkg.GetDbObject()
      db_stat_objs_by_pkgname[db_obj.pkginst.pkgname] = db_obj
      obj_id_list.append(db_obj.id)
    logging.debug("Deleting old %s errors from the database.",
                  db_obj.pkginst.pkgname)
    conn = sqlobject.sqlhub.processConnection
    # It's the maximum number of ORs in a SQL statement.
    # Slicing the long list up into s-sized segments.  1000 is too much.
    obj_id_lists = SliceList(obj_id_list, 900)
    for obj_id_list in obj_id_lists:
      # WARNING: This is raw SQL, potentially breaking during a transition to
      # another db.  It's here for efficiency.
      sql = ("DELETE FROM checkpkg_error_tag WHERE %s;"
             % " OR ".join("srv4_file_id = %s" % x for x in obj_id_list))
      conn.query(sql)
    # Need to construct the predicate by hand.  Otherwise:
    # File "/opt/csw/lib/python/site-packages/sqlobject/sqlbuilder.py",
    # line 829, in OR
    # return SQLOp("OR", op1, OR(*ops))
    # RuntimeError: maximum recursion depth exceeded while calling a Python object
    #
    # The following also tries to use recursion and fails.
    # delete_predicate = sqlobject.OR(False)
    # for pred in delete_predicate_list:
    #   delete_predicate = sqlobject.OR(delete_predicate, pred)
    # conn.query(
    #     conn.sqlrepr(sqlbuilder.Delete(m.CheckpkgErrorTag.sqlmeta.table,
    #       delete_predicate
    #     )))
      # res = m.CheckpkgErrorTag.select(m.CheckpkgErrorTag.q.srv4_file==db_obj)
      # for obj in res:
      #   obj.destroySelf()
    errors, messages, gar_lines = self.GetAllTags(packages_data)
    no_errors = len(errors) + 1
    bar = progressbar.ProgressBar()
    bar.maxval = no_errors
    count = itertools.count(1)
    logging.info("Stuffing the candies under the pillow...")
    bar.start()
    for pkgname, es in errors.iteritems():
      logging.debug("Saving %s errors to the database.", pkgname)
      for e in es:
        db_error = m.CheckpkgErrorTag(srv4_file=db_stat_objs_by_pkgname[e.pkgname],
                                      pkgname=e.pkgname,
                                      tag_name=e.tag_name,
                                      tag_info=e.tag_info,
                                      msg=e.msg)
      bar.update(count.next())
    bar.finish()
    flat_error_list = reduce(operator.add, errors.values(), [])
    screen_report, tags_report = self.FormatReports(errors, messages, gar_lines)
    exit_code = 0
    return (exit_code, screen_report, tags_report)


class CheckInterfaceBase(object):
  """Proxies interaction with checking functions.

  It wraps access to the /var/sadm/install/contents cache.
  """

  def __init__(self, system_pkgmap=None, lines_dict=None):
    self.system_pkgmap = system_pkgmap
    if not self.system_pkgmap:
      self.system_pkgmap = SystemPkgmap()
    self.common_paths = {}
    if lines_dict:
      self.lines_dict = lines_dict
    else:
      self.lines_dict = {}

  def GetPathsAndPkgnamesByBasename(self, basename):
    """Proxies calls to self.system_pkgmap."""
    return self.system_pkgmap.GetPathsAndPkgnamesByBasename(basename)

  def GetPkgByPath(self, path):
    """Proxies calls to self.system_pkgmap."""
    return self.system_pkgmap.GetPkgByPath(path)

  def GetInstalledPackages(self, initialize=True):
    return self.system_pkgmap.GetInstalledPackages(initialize)

  def _GetPathsForArch(self, arch):
    if not arch in self.lines_dict:
      file_name = os.path.join(
          os.path.dirname(__file__), "..", "..", "etc", "commondirs-%s" % arch)
      logging.debug("opening %s", file_name)
      f = open(file_name, "r")
      self.lines_dict[arch] = f.read().splitlines()
      f.close()
    return self.lines_dict[arch]

  def GetCommonPaths(self, arch):
    """Returns a list of paths for architecture, from gar/etc/commondirs*."""
    # TODO: If this was cached, it could save a significant amount of time.
    assert arch in ('i386', 'sparc', 'all'), "Wrong arch: %s" % repr(arch)
    if arch == 'all':
      archs = ('i386', 'sparc')
    else:
      archs = [arch]
    lines = []
    for arch in archs:
      lines.extend(self._GetPathsForArch(arch))
    return lines


class IndividualCheckInterface(CheckInterfaceBase):
  """To be passed to the checking functions.

  Wraps the creation of tag.CheckpkgTag objects.
  """

  def __init__(self, pkgname, system_pkgmap=None):
    super(IndividualCheckInterface, self).__init__(system_pkgmap)
    self.pkgname = pkgname
    self.errors = []

  def ReportError(self, tag_name, tag_info=None, msg=None):
    logging.debug("self.error_mgr_mock.ReportError(%s, %s, %s)",
                  repr(tag_name), repr(tag_info), repr(msg))
    checkpkg_tag = tag.CheckpkgTag(self.pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(checkpkg_tag)


class SetCheckInterface(CheckInterfaceBase):
  """To be passed to set checking functions."""

  def __init__(self, system_pkgmap=None):
    super(SetCheckInterface, self).__init__(system_pkgmap)
    self.errors = []

  def ReportError(self, pkgname, tag_name, tag_info=None, msg=None):
    logging.debug("self.error_mgr_mock.ReportError(%s, %s, %s, %s)",
                  repr(pkgname),
                  repr(tag_name), repr(tag_info), repr(msg))
    checkpkg_tag = tag.CheckpkgTag(pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(checkpkg_tag)


class CheckpkgMessenger(object):
  """Class responsible for passing messages from checks to the user."""
  def __init__(self):
    self.messages = []
    self.one_time_messages = {}
    self.gar_lines = []

  def Message(self, m):
    logging.debug("self.messenger.Message(%s)", repr(m))
    self.messages.append(m)

  def OneTimeMessage(self, key, m):
    logging.debug("self.messenger.OneTimeMessage(%s, %s)", repr(key), repr(m))
    if key not in self.one_time_messages:
      self.one_time_messages[key] = m

  def SuggestGarLine(self, m):
    logging.debug("self.messenger.SuggestGarLine(%s)", repr(m))
    self.gar_lines.append(m)


class CheckpkgManager2(CheckpkgManagerBase):
  """The second incarnation of the checkpkg manager.

  Implements the API to be used by checking functions.

  Its purpose is to reduce the amount of boilerplate code and allow for easier
  unit test writing.
  """
  def _RegisterIndividualCheck(self, function):
    self.individual_checks.append(function)

  def _RegisterSetCheck(self, function):
    self.set_checks.append(function)

  def _AutoregisterChecks(self):
    """Autodetects all defined checks."""
    logging.debug("CheckpkgManager2._AutoregisterChecks()")
    checkpkg_module = package_checks
    members = dir(checkpkg_module)
    for member_name in members:
      logging.debug("Examining module member: %s", repr(member_name))
      member = getattr(checkpkg_module, member_name)
      if callable(member):
        if member_name.startswith("Check"):
          logging.debug("Registering individual check %s", repr(member_name))
          self._RegisterIndividualCheck(member)
        elif member_name.startswith("SetCheck"):
          logging.debug("Registering set check %s", repr(member_name))
          self._RegisterSetCheck(member)

  def GetAllTags(self, stats_obj_list):
    errors = {}
    pkgmap = SystemPkgmap()
    logging.debug("Loading all package statistics.")
    pkgs_data = self.GetOptimizedAllStats(stats_obj_list)
    logging.debug("All package statistics loaded.")
    messenger = CheckpkgMessenger()
    # Individual checks
    count = itertools.count()
    bar = progressbar.ProgressBar()
    bar.maxval = len(pkgs_data) * len(self.individual_checks)
    logging.info("Tasting candies one by one...")
    bar.start()
    for pkg_data in pkgs_data:
      pkgname = pkg_data["basic_stats"]["pkgname"]
      check_interface = IndividualCheckInterface(pkgname, pkgmap)
      for function in self.individual_checks:
        logger = logging.getLogger("%s-%s" % (pkgname, function.__name__))
        logger.debug("Calling %s", function.__name__)
        function(pkg_data, check_interface, logger=logger, messenger=messenger)
        if check_interface.errors:
          errors[pkgname] = check_interface.errors
        bar.update(count.next())
    bar.finish()
    # Set checks
    logging.info("Tasting them all at once...")
    for function in self.set_checks:
      logger = logging.getLogger(function.__name__)
      check_interface = SetCheckInterface(pkgmap)
      logger.debug("Calling %s", function.__name__)
      function(pkgs_data, check_interface, logger=logger, messenger=messenger)
      if check_interface.errors:
        errors = self.SetErrorsToDict(check_interface.errors, errors)
    messages = messenger.messages + messenger.one_time_messages.values()
    return errors, messages, messenger.gar_lines

  def Run(self):
    self._AutoregisterChecks()
    return super(CheckpkgManager2, self).Run()


def GetIsalist():
  args = ["isalist"]
  isalist_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = isalist_proc.communicate()
  ret = isalist_proc.wait()
  if ret:
    logging.error("Calling isalist has failed.")
  isalist = re.split(r"\s+", stdout.strip())
  return tuple(isalist)


class PackageStats(DatabaseClient):
  """Collects stats about a package and saves it.

  TODO: Maintain a global database connection instead of creating one for each
  instantiated object.
  TODO: Store overrides in a separate table for performance.
  """

  def __init__(self, srv4_pkg, stats_basedir=None, md5sum=None, debug=False):
    super(PackageStats, self).__init__(debug=debug)
    self.srv4_pkg = srv4_pkg
    self.md5sum = md5sum
    self.dir_format_pkg = None
    self.all_stats = {}
    self.stats_basedir = stats_basedir
    self.db_pkg_stats = None
    if not self.stats_basedir:
      home = os.environ["HOME"]
      parts = [home, ".checkpkg", "stats"]
      self.stats_basedir = os.path.join(*parts)
    self.InitializeSqlobject()

  def GetPkgchkData(self):
    ret, stdout, stderr = self.srv4_pkg.GetPkgchkOutput()
    data = {
        'return_code': ret,
        'stdout_lines': stdout.splitlines(),
        'stderr_lines': stderr.splitlines(),
    }
    return data

  def GetMd5sum(self):
    if not self.md5sum:
      self.md5sum = self.srv4_pkg.GetMd5sum()
    return self.md5sum

  def GetDbObject(self):
    if not self.db_pkg_stats:
      md5_sum = self.GetMd5sum()
      res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
      if not res.count():
        # TODO: Change this bit to throw an exception if the object is not
        # found.
        return None
      else:
        self.db_pkg_stats = res.getOne()
    return self.db_pkg_stats


  def StatsExist(self):
    """Checks if statistics of a package exist.

    Returns:
      bool
    """
    pkg_stats = self.GetDbObject()
    if not pkg_stats:
      return False
    if pkg_stats.stats_version != PACKAGE_STATS_VERSION:
      pkg_stats.destroySelf()
    else:
      return True
    return False

  def GetDirFormatPkg(self):
    if not self.dir_format_pkg:
      self.dir_format_pkg = self.srv4_pkg.GetDirFormatPkg()
    return self.dir_format_pkg

  def GetMtime(self):
    return self.srv4_pkg.GetMtime()

  def _MakeDirP(self, dir_path):
    """mkdir -p equivalent.

    http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    """
    try:
      os.makedirs(dir_path)
    except OSError, e:
      if e.errno == errno.EEXIST:
        pass
      else:
        raise

  def GetBinaryDumpInfo(self):
    dir_pkg = self.GetDirFormatPkg()
    # Binaries. This could be split off to a separate function.
    # man ld.so.1 for more info on this hack
    env = copy.copy(os.environ)
    env["LD_NOAUXFLTR"] = "1"
    binaries_dump_info = []
    for binary in dir_pkg.ListBinaries():
      binary_abs_path = os.path.join(dir_pkg.directory, "root", binary)
      binary_base_name = os.path.basename(binary)
      args = [DUMP_BIN, "-Lv", binary_abs_path]
      dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE, env=env)
      stdout, stderr = dump_proc.communicate()
      ret = dump_proc.wait()
      binary_data = ParseDumpOutput(stdout)
      binary_data["path"] = binary
      binary_data["base_name"] = binary_base_name
      binaries_dump_info.append(binary_data)
    return binaries_dump_info

  def GetBasicStats(self):
    dir_pkg = self.GetDirFormatPkg()
    basic_stats = {}
    basic_stats["stats_version"] = PACKAGE_STATS_VERSION
    basic_stats["pkg_path"] = self.srv4_pkg.pkg_path
    basic_stats["pkg_basename"] = os.path.basename(self.srv4_pkg.pkg_path)
    basic_stats["parsed_basename"] = opencsw.ParsePackageFileName(
        basic_stats["pkg_basename"])
    basic_stats["pkgname"] = dir_pkg.pkgname
    basic_stats["catalogname"] = dir_pkg.GetCatalogname()
    basic_stats["md5_sum"] = self.GetMd5sum()
    return basic_stats

  def GetOverrides(self):
    dir_pkg = self.GetDirFormatPkg()
    override_list = dir_pkg.GetOverrides()
    def OverrideToDict(override):
      return {
        "pkgname":  override.pkgname,
        "tag_name":  override.tag_name,
        "tag_info":  override.tag_info,
      }
    overrides_simple = [OverrideToDict(x) for x in override_list]
    return overrides_simple

  def GetLddMinusRlines(self):
    """Returns ldd -r output."""
    dir_pkg = self.GetDirFormatPkg()
    binaries = dir_pkg.ListBinaries()
    ldd_output = {}
    for binary in binaries:
      binary_abspath = os.path.join(dir_pkg.directory, "root", binary)
      # this could be potentially moved into the DirectoryFormatPackage class.
      # ldd needs the binary to be executable
      os.chmod(binary_abspath, 0755)
      args = ["ldd", "-r", binary_abspath]
      ldd_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = ldd_proc.communicate()
      retcode = ldd_proc.wait()
      if retcode:
        logging.error("%s returned an error: %s", args, stderr)
      ldd_info = []
      for line in stdout.splitlines():
        ldd_info.append(self._ParseLddDashRline(line))
      ldd_output[binary] = ldd_info
    return ldd_output

  def GetDefinedSymbols(self):
    """Returns text symbols (i.e. defined functions) for packaged ELF objects

    To do this we parse output lines from nm similar to the following. "T"s are
    the definitions which we are after.

      0000104000 D _lib_version
      0000986980 D _libiconv_version
      0000000000 U abort
      0000097616 T aliases_lookup
    """
    dir_pkg = self.GetDirFormatPkg()
    binaries = dir_pkg.ListBinaries()
    defined_symbols = {}

    for binary in binaries:
      binary_abspath = os.path.join(dir_pkg.directory, "root", binary)
      # Get parsable, ld.so.1 relevant SHT_DYNSYM symbol information
      args = ["/usr/ccs/bin/nm", "-p", "-D", binary_abspath]
      nm_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = nm_proc.communicate()
      retcode = nm_proc.wait()
      if retcode:
        logging.error("%s returned an error: %s", args, stderr)
        continue
      nm_out = stdout.splitlines()

      defined_symbols[binary] = []
      for line in nm_out:
        sym = self._ParseNmSymLine(line)
        if not sym:
          continue
        if sym['type'] not in ("T", "D", "B"):
          continue
        defined_symbols[binary].append(sym['name'])

    return defined_symbols

  def _ParseNmSymLine(self, line):
    re_defined_symbol =  re.compile('[0-9]+ [ABDFNSTU] \S+')
    m = re_defined_symbol.match(line)
    if not m:
      return None
    fields = line.split()
    sym = { 'address': fields[0], 'type': fields[1], 'name': fields[2] }
    return sym

  def CollectStats(self, force=False):
    """Lazy stats collection."""
    if force or not self.StatsExist():
      return self._CollectStats()
    return self.ReadSavedStats()

  def _CollectStats(self):
    """The list of variables needs to be synchronized with the one
    at the top of this class.
    """
    dir_pkg = self.GetDirFormatPkg()
    logging.debug("Collecting %s package statistics.", repr(dir_pkg.pkgname))
    override_dicts = self.GetOverrides()
    pkg_stats = {
        "binaries": dir_pkg.ListBinaries(),
        "binaries_dump_info": self.GetBinaryDumpInfo(),
        "depends": dir_pkg.GetDependencies(),
        "isalist": GetIsalist(),
        "overrides": override_dicts,
        "pkgchk": self.GetPkgchkData(),
        "pkginfo": dir_pkg.GetParsedPkginfo(),
        "pkgmap": dir_pkg.GetPkgmap().entries,
        "bad_paths": dir_pkg.GetFilesContaining(BAD_CONTENT_REGEXES),
        "basic_stats": self.GetBasicStats(),
        "files_metadata": dir_pkg.GetFilesMetadata(),
        "mtime": self.GetMtime(),
    }
    pkgname = pkg_stats["basic_stats"]["pkgname"]
    # Getting sqlobject representations.
    try:
      pkginst = m.Pkginst.select(m.Pkginst.q.pkgname==pkgname).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      pkginst = m.Pkginst(pkgname=pkgname)
    try:
      res = m.Architecture.select(
          m.Architecture.q.name==pkg_stats["pkginfo"]["ARCH"])
      arch = res.getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      arch = m.Architecture(name=pkg_stats["pkginfo"]["ARCH"])
    parsed_basename = pkg_stats["basic_stats"]["parsed_basename"]
    os_rel_name = parsed_basename["osrel"]
    try:
      os_rel = m.OsRelease.select(
          m.OsRelease.q.short_name==os_rel_name).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      os_rel = m.OsRelease(short_name=os_rel_name, full_name=os_rel_name)
    try:
      maint_email = pkg_stats["pkginfo"]["EMAIL"]
      maintainer = m.Maintainer.select(
          m.Maintainer.q.email==maint_email).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      maintainer = m.Maintainer(email=maint_email)

    # If there are any previous records of the same pkginst, arch and os_rel,
    # we're marking them as not-latest.
    # This assumes that the packages are examined in a chronological order.
    res = m.Srv4FileStats.select(sqlobject.AND(
        m.Srv4FileStats.q.pkginst==pkginst,
        m.Srv4FileStats.q.arch==arch,
        m.Srv4FileStats.q.os_rel==os_rel))
    for obj in res:
      obj.latest = False

    rev=None
    if "revision_info" in parsed_basename:
      if "REV" in parsed_basename["revision_info"]:
        rev = parsed_basename["revision_info"]["REV"]
    # Creating the object in the database.
    db_pkg_stats = m.Srv4FileStats(
        md5_sum=self.GetMd5sum(),
        pkginst=pkginst,
        catalogname=pkg_stats["basic_stats"]["catalogname"],
        stats_version=PACKAGE_STATS_VERSION,
        os_rel=os_rel,
        arch=arch,
        basename=pkg_stats["basic_stats"]["pkg_basename"],
        maintainer=maintainer,
        latest=True,
        version_string=parsed_basename["full_version_string"],
        rev=rev,
        mtime=self.GetMtime(),
        data=cPickle.dumps(pkg_stats))
    # Inserting overrides as rows into the database
    for override_dict in override_dicts:
      o = m.CheckpkgOverride(srv4_file=db_pkg_stats,
                             **override_dict)

    # The ldd -r reporting breaks on bigger packages during yaml saving.
    # It might work when yaml is disabled
    # self.DumpObject(self.GetLddMinusRlines(), "ldd_dash_r")
    # This check is currently disabled, let's save time by not collecting
    # these data.
    # self.DumpObject(self.GetDefinedSymbols(), "defined_symbols")
    # This one should be last, so that if the collection is interrupted
    # in one of the previous runs, the basic_stats.pickle file is not there
    # or not updated, and the collection is started again.

    logging.debug("Statistics of %s have been collected.", repr(dir_pkg.pkgname))
    return pkg_stats

  def GetAllStats(self):
    if not self.all_stats and self.StatsExist():
      self.all_stats = self.ReadSavedStats()
    elif not self.all_stats:
      self.all_stats = self.CollectStats()
    return self.all_stats

  def GetSavedOverrides(self):
    if not self.StatsExist():
      raise PackageError("Package stats not ready.")
    pkg_stats = self.GetDbObject()
    res = m.CheckpkgOverride.select(m.CheckpkgOverride.q.srv4_file==pkg_stats)
    override_list = []
    for db_override in res:
      d = {
          'pkgname': db_override.pkgname,
          'tag_name': db_override.tag_name,
          'tag_info': db_override.tag_info,
      }
      override_list.append(overrides.Override(**d))
    return override_list

  def GetSavedErrorTags(self):
    pkg_stats = self.GetDbObject()
    res = m.CheckpkgErrorTag.select(m.CheckpkgErrorTag.q.srv4_file==pkg_stats)
    tag_list = [tag.CheckpkgTag(x.pkgname, x.tag_name, x.tag_info, x.msg)
                for x in res]
    return tag_list

  def ReadSavedStats(self):
    if not self.all_stats:
      md5_sum = self.GetMd5sum()
      res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
      self.all_stats = cPickle.loads(str(res.getOne().data))
    return self.all_stats

  def _ParseLddDashRline(self, line):
    found_re = r"^\t(?P<soname>\S+)\s+=>\s+(?P<path_found>\S+)"
    symbol_not_found_re = (r"^\tsymbol not found:\s(?P<symbol>\S+)\s+"
                           r"\((?P<path_not_found>\S+)\)")
    only_so = r"^\t(?P<path_only>\S+)$"
    version_so = (r'^\t(?P<soname_version_not_found>\S+) '
                  r'\((?P<lib_name>\S+)\) =>\t \(version not found\)')
    stv_protected = (r'^\trelocation \S+ symbol: (?P<relocation_symbol>\S+): '
                     r'file (?P<relocation_path>\S+): '
                     r'relocation bound to a symbol '
                     r'with STV_PROTECTED visibility$')
    sizes_differ = (r'^\trelocation \S+ sizes differ: '
                    r'(?P<sizes_differ_symbol>\S+)$')
    sizes_info = (r'^\t\t\(file (?P<sizediff_file1>\S+) size=(?P<size1>0x\w+); '
                  r'file (?P<sizediff_file2>\S+) size=(?P<size2>0x\w+)\)$')
    sizes_one_used = (r'^\t\t(?P<sizediffused_file>\S+) size used; '
                      r'possible insufficient data copied$')
    common_re = (r"(%s|%s|%s|%s|%s|%s|%s|%s)"
                 % (found_re, symbol_not_found_re, only_so, version_so,
                    stv_protected, sizes_differ, sizes_info, sizes_one_used))
    m = re.match(common_re, line)
    response = {}
    if m:
      d = m.groupdict()
      if "soname" in d and d["soname"]:
        # it was found
        response["state"] = "OK"
        response["soname"] = d["soname"]
        response["path"] = d["path_found"]
        response["symbol"] = None
      elif "symbol" in d and d["symbol"]:
        response["state"] = "symbol-not-found"
        response["soname"] = None
        response["path"] = d["path_not_found"]
        response["symbol"] = d["symbol"]
      elif d["path_only"]:
        response["state"] = "OK"
        response["soname"] = None
        response["path"] = d["path_only"]
        response["symbol"] = None
      elif d["soname_version_not_found"]:
        response["state"] = "version-not-found"
        response["soname"] = d["soname_version_not_found"]
        response["path"] = None
        response["symbol"] = None
      elif d["relocation_symbol"]:
        response["state"] = 'relocation-bound-to-a-symbol-with-STV_PROTECTED-visibility'
        response["soname"] = None
        response["path"] = d["relocation_path"]
        response["symbol"] = d["relocation_symbol"]
      elif d["sizes_differ_symbol"]:
        response["state"] = 'sizes-differ'
        response["soname"] = None
        response["path"] = None
        response["symbol"] = d["sizes_differ_symbol"]
      elif d["sizediff_file1"]:
        response["state"] = 'sizes-diff-info'
        response["soname"] = None
        response["path"] = "%s %s" % (d["sizediff_file1"], d["sizediff_file2"])
        response["symbol"] = None
      elif d["sizediffused_file"]:
        response["state"] = 'sizes-diff-one-used'
        response["soname"] = None
        response["path"] = "%s" % (d["sizediffused_file"])
        response["symbol"] = None
      else:
        raise StdoutSyntaxError("Could not parse %s with %s"
                                % (repr(line), common_re))
    else:
      raise StdoutSyntaxError("Could not parse %s with %s"
                              % (repr(line), common_re))
    return response


def ErrorTagsFromFile(file_name):
  fd = open(file_name)
  error_tags = []
  for line in fd:
    if line.startswith("#"):
      continue
    pkgname, tag_name, tag_info = tag.ParseTagLine(line)
    error_tags.append(tag.CheckpkgTag(pkgname, tag_name, tag_info))
  return error_tags


def StatsListFromCatalog(file_name_list, catalog_file_name=None, debug=False):
  packages = [opencsw.CswSrv4File(x, debug) for x in file_name_list]
  if catalog_file_name:
    catalog = opencsw.OpencswCatalog(catalog_file_name)
    md5s_by_basename = catalog.GetDataByBasename()
    for pkg in packages:
      basename = os.path.basename(pkg.pkg_path)
      # It might be the case that a file is present on disk, but missing from
      # the catalog file.
      if basename in md5s_by_basename:
        pkg.md5sum = md5s_by_basename[basename]["md5sum"]
  stats_list = [PackageStats(pkg) for pkg in packages]
  return stats_list

def SliceList(l, size):
  """Trasforms a list into a list of lists."""
  idxes = xrange(0, len(l), size)
  sliced = [l[i:i+size] for i in idxes]
  return sliced
