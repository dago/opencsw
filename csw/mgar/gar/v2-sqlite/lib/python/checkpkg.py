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
DB_SCHEMA_VERSION = 4L
PACKAGE_STATS_VERSION = 6L
SYSTEM_PKGMAP = "/var/sadm/install/contents"
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"
SONAME = "soname"
CONFIG_MTIME = "mtime"
CONFIG_DB_SCHEMA = "db_schema_version"
WRITE_YAML = False
DO_NOT_REPORT_SURPLUS = set([u"CSWcommon", u"CSWcswclassutils", u"CSWisaexec"])
DO_NOT_REPORT_MISSING = set([])
DO_NOT_REPORT_MISSING_RE = [r"SUNW.*", r"\*SUNW.*"]
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


# This shared library is present on Solaris 10 on amd64, but it's missing on
# Solaris 8 on i386.  It's okay if it's missing.
ALLOWED_ORPHAN_SONAMES = set([u"libm.so.2"])
DEPENDENCY_FILENAME_REGEXES = (
    (r".*\.pl$", u"CSWperl"),
    (r".*\.pm$", u"CSWperl"),
    (r".*\.py$", u"CSWpython"),
    (r".*\.rb$", u"CSWruby"),
    (r".*\.el$", u"CSWemacscommon"),
    (r".*\.elc$", u"CSWemacscommon"),
)

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
  parser.add_option("-b", dest="stats_basedir",
                    help=("The base directory with package statistics "
                          "in yaml format, e.g. ~/.checkpkg/stats"))
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-o", "--output", dest="output",
                    help="Output error tag file")
  (options, args) = parser.parse_args()
  if not options.stats_basedir:
    raise ConfigurationError("ERROR: the -b option is missing.")
  if not options.output:
    raise ConfigurationError("ERROR: the -o option is missing.")
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
  if m:
    return m.group("username")
  else:
    return None


class DatabaseClient(object):

  CHECKPKG_DIR = ".checkpkg"
  SQLITE3_DBNAME_TMPL = "var-sadm-install-contents-cache-%s"
  TABLES = (m.CswConfig,
            m.CswFile,
            m.CswPackage,
            m.Srv4FileStats)

  def __init__(self, debug=False):
    self.fqdn = socket.getfqdn()
    self.checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    self.db_path = os.path.join(self.checkpkg_dir,
                                self.SQLITE3_DBNAME_TMPL % self.fqdn)
    self.debug = debug

  def InitializeSqlobject(self):
    logging.debug("Connecting to the %s database.", self.db_path)
    self.sqo_conn = sqlobject.connectionForURI(
        'sqlite:%s' % self.db_path, debug=(self.debug and False))
    sqlobject.sqlhub.processConnection = self.sqo_conn

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
    self.file_mtime = None
    self.cache_mtime = None
    self.initialized = False
    if not system_pkgmap_files:
      self.system_pkgmap_files = [SYSTEM_PKGMAP]
    else:
      self.system_pkgmap_files = system_pkgmap_files

  def _LazyInitializeDatabase(self):
    if not self.initialized:
      self.InitializeDatabase()

  def InitializeRawDb(self):
    """It's necessary for low level operations."""
    if True:
      logging.debug("Connecting to sqlite")
      self.sqlite_conn = sqlite3.connect(self.db_path)

  def InitializeDatabase(self):
    """Refactor this class to first create CswFile with no primary key and no indexes.
    """
    need_to_create_tables = False
    if not os.path.exists(self.db_path):
      print "Building a cache of %s." % self.system_pkgmap_files
      print "The cache will be kept in %s." % self.db_path
      if not os.path.exists(self.checkpkg_dir):
        logging.debug("Creating %s", self.checkpkg_dir)
        os.mkdir(self.checkpkg_dir)
      need_to_create_tables = True
    self.InitializeRawDb()
    self.InitializeSqlobject()
    if not self.IsDatabaseGoodSchema():
      logging.info("Old database schema detected.")
      self.PurgeDatabase(drop_tables=True)
      need_to_create_tables = True
    if need_to_create_tables:
      self.CreateTables()
    if not self.IsDatabaseUpToDate():
      logging.info("Rebuilding the package cache, can take a few minutes.")
      self.PurgeDatabase()
      self.PopulateDatabase()
    self.initialized = True

  def PopulateDatabase(self):
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
    # The progressbar library doesn't like to handle large numbers, and it
    # displays up to 99% if we feed it a maxval in the range of hundreds of
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
    print "Processing %s" % pkgmap_path
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
      # pkgmap_entry = m.CswFile(basename=pkgmap_entry_base_name, path=pkgmap_entry_dir, line=line.strip())
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
    logging.info("All lines of %s were processed.", pkgmap_path)

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
    INSERT INTO csw_package (pkgname, pkg_desc)
    VALUES (?, ?);
    """
    for line in stdout.splitlines():
      pkgname, pkg_desc = self._ParsePkginfoLine(line)
      # This is slow:
      # pkg = m.CswPackage(pkgname=pkgname, pkg_desc=pkg_desc)
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
    res = m.CswConfig.select(m.CswConfig.q.option_key==CONFIG_DB_SCHEMA)
    if res.count() == 0:
      version = m.CswConfig(option_key=CONFIG_DB_SCHEMA,
                            int_value=DB_SCHEMA_VERSION)
    else:
      config_option = res.getOne()
      config_option.int_value = DB_SCHEMA_VERSION

  def GetPkgmapLineByBasename(self, filename):
    """Returns pkgmap lines by basename:
      {
        path1: line1,
        path2: line2,
      }
    """
    self._LazyInitializeDatabase()
    if filename in self.cache:
      return self.cache[filename]
    # sql = "SELECT path, line FROM systempkgmap WHERE basename = ?;"
    # c = self.conn.cursor()
    # c.execute(sql, [filename])
    res = m.CswFile.select(m.CswFile.q.basename==filename)
    lines = {}
    for obj in res:
      lines[obj.path] = obj.line
    if len(lines) == 0:
      logging.debug("Cache doesn't contain filename %s", filename)
    self.cache[filename] = lines
    logging.debug("GetPkgmapLineByBasename(%s) --> %s",
                  filename, lines)
    return lines

  def _InferPackagesFromPkgmapLine(self, line):
    """A stub of a function, to be enhanced."""
    line = line.strip()
    parts = re.split(c.WS_RE, line)
    return [parts[-1]]

  def GetPathsAndPkgnamesByBasename(self, filename):
    """Returns paths and packages by basename.

    e.g.
    {"/opt/csw/lib": ["CSWfoo", "CSWbar"],
     "/opt/csw/1/lib": ["CSWfoomore"]}
    """
    lines = self.GetPkgmapLineByBasename(filename)
    # Infer packages
    for file_path in lines:
      lines[file_path] = self._InferPackagesFromPkgmapLine(lines[file_path])
    return lines

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
      logging.info("No db schema value found, assuming %s.",
                   schema_on_disk)
    elif res.count() == 1:
      schema_on_disk = res.getOne().int_value
    return schema_on_disk

  def IsDatabaseUpToDate(self):
    f_mtime = self.GetFileMtime()
    d_mtime = self.GetDatabaseMtime()
    logging.debug("IsDatabaseUpToDate: f_mtime %s, d_time: %s", f_mtime, d_mtime)
    # Rounding up to integer seconds.  There is a race condition: 
    # pkgadd finishes at 100.1
    # checkpkg reads /var/sadm/install/contents at 100.2
    # new pkgadd runs and finishes at 100.3
    # subsequent checkpkg runs won't pick up the last change.
    # I don't expect pkgadd to run under 1s.
    fresh = int(f_mtime) <= int(d_mtime)
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    logging.debug("IsDatabaseUpToDate: good_version=%s, fresh=%s",
                  repr(good_version), repr(fresh))
    return fresh and good_version

  def PurgeDatabase(self, drop_tables=False):
    if drop_tables:
      for table in self.TABLES:
        if table.tableExists():
          table.dropTable()
    else:
      logging.info("Truncating all tables")
      for table in self.TABLES:
        table.clearTable()

  def GetInstalledPackages(self):
    """Returns a dictionary of all installed packages."""
    self._LazyInitializeDatabase()
    res = m.CswPackage.select()
    return dict([[str(x.pkgname), str(x.pkg_desc)] for x in res])


def ExpandRunpath(runpath, isalist):
  # Emulating $ISALIST expansion
  if '$ISALIST' in runpath:
    expanded_list = [runpath.replace('$ISALIST', isa) for isa in isalist]
  else:
    expanded_list = [runpath]
  return expanded_list

def ExpandSymlink(symlink, target, input_path):
  symlink_re = re.compile(r"%s(/|$)" % symlink)
  if re.search(symlink_re, input_path):
    result = input_path.replace(symlink, target)
  else:
    result = input_path
  return result

def Emulate64BitSymlinks(runpath_list):
  """Need to emulate the 64 -> amd64, 64 -> sparcv9 symlink

  Since we don't know the architecture, we'll adding both amd64 and sparcv9.
  It should be safe.
  """
  symlinked_list = []
  for runpath in runpath_list:
    for symlink, expansion_list in SYSTEM_SYMLINKS:
      for target in expansion_list:
        expanded = ExpandSymlink(symlink, target, runpath)
        if expanded not in symlinked_list:
          symlinked_list.append(expanded)
  return symlinked_list


def SanitizeRunpath(runpath):
  while True:
    if runpath.endswith("/"):
      runpath = runpath[:-1]
    elif "//" in runpath:
      runpath = runpath.replace("//", "/")
    else:
      break
  return runpath


def ResolveSoname(runpath, soname, isalist, path_list):
  """Emulates ldd behavior, minimal implementation.

  runpath: e.g. ["/opt/csw/lib/$ISALIST", "/usr/lib"]
  soname: e.g. "libfoo.so.1"
  isalist: e.g. ["sparcv9", "sparcv8"]
  path_list: A list of paths where the soname is present, e.g.
             ["/opt/csw/lib", "/opt/csw/lib/sparcv9"]

  The function returns the one path.
  """
  runpath = SanitizeRunpath(runpath)
  runpath_list = ExpandRunpath(runpath, isalist)
  runpath_list = Emulate64BitSymlinks(runpath_list)
  # Emulating the install time symlinks, for instance, if the prototype contains
  # /opt/csw/lib/i386/foo.so.0 and /opt/csw/lib/i386 is a symlink to ".",
  # the shared library ends up in /opt/csw/lib/foo.so.0 and should be
  # findable even when RPATH does not contain $ISALIST.
  original_paths_by_expanded_paths = {}
  for p in path_list:
    expanded_p_list = Emulate64BitSymlinks([p])
    # We can't just expand and return; we need to return one of the paths given
    # in the path_list.
    for expanded_p in expanded_p_list:
      original_paths_by_expanded_paths[expanded_p] = p
  logging.debug("%s: looking for %s in %s",
      soname, runpath_list, original_paths_by_expanded_paths.keys())
  for runpath_expanded in runpath_list:
    if runpath_expanded in original_paths_by_expanded_paths:
      logging.debug("Found %s",
                    original_paths_by_expanded_paths[runpath_expanded])
      return original_paths_by_expanded_paths[runpath_expanded]


def ParseDumpOutput(dump_output):
  binary_data = {RUNPATH: [],
                 NEEDED_SONAMES: []}
  runpath = []
  rpath = []
  for line in dump_output.splitlines():
    fields = re.split(c.WS_RE, line)
    # TODO: Make it a unit test
    # logging.debug("%s says: %s", DUMP_BIN, fields)
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
    stats_list = []
    for md5sum in self.md5sum_list:
      stats_list.append(PackageStats(None, self.stats_basedir, md5sum))
    return stats_list

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
    screen_report = unicode(screen_t)
    tags_report = unicode(tags_report_t)
    return screen_report, tags_report

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
    pkgs_data = []
    counter = itertools.count()
    length = len(stats_obj_list)
    for stats_obj in stats_obj_list:
      # pkg_data = {}
      # This bit is tightly tied to the data structures returned by
      # PackageStats.
      #
      # Python strings are already implementing the flyweight pattern. What's
      # left is lists and dictionaries.
      i = counter.next()
      logging.debug("Loading stats for %s (%s/%s)",
                    stats_obj.md5sum, i, length)
      raw_pkg_data = stats_obj.GetAllStats()
      pkg_data = raw_pkg_data
      pkgs_data.append(pkg_data)
    return pkgs_data

  def Run(self):
    """Runs all the checks

    Returns a tuple of an exit code and a report.
    """
    packages_data = self.GetPackageStatsList()
    errors, messages, gar_lines = self.GetAllTags(packages_data)
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

  def GetPkgmapLineByBasename(self, basename):
    """Proxies calls to self.system_pkgmap."""
    logging.warning("GetPkgmapLineByBasename(%s): deprecated function",
                    basename)
    return self.system_pkgmap.GetPkgmapLineByBasename(basename)

  def GetPathsAndPkgnamesByBasename(self, basename):
    """Proxies calls to self.system_pkgmap."""
    return self.system_pkgmap.GetPathsAndPkgnamesByBasename(basename)

  def GetInstalledPackages(self):
    return self.system_pkgmap.GetInstalledPackages()

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
    # TODO: If this was cached, it would save a significant amount of time.
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
    checkpkg_tag = tag.CheckpkgTag(self.pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(checkpkg_tag)


class SetCheckInterface(CheckInterfaceBase):
  """To be passed to set checking functions."""

  def __init__(self, system_pkgmap=None):
    super(SetCheckInterface, self).__init__(system_pkgmap)
    self.errors = []

  def ReportError(self, pkgname, tag_name, tag_info=None, msg=None):
    checkpkg_tag = tag.CheckpkgTag(pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(checkpkg_tag)


class CheckpkgMessenger(object):
  """Class responsible for passing messages from checks to the user."""
  def __init__(self):
    self.messages = []
    self.gar_lines = []

  def Message(self, m):
    self.messages.append(m)

  def SuggestGarLine(self, m):
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
    for pkg_data in pkgs_data:
      pkgname = pkg_data["basic_stats"]["pkgname"]
      check_interface = IndividualCheckInterface(pkgname, pkgmap)
      for function in self.individual_checks:
        logger = logging.getLogger("%s-%s" % (pkgname, function.__name__))
        logger.debug("Calling %s", function.__name__)
        function(pkg_data, check_interface, logger=logger, messenger=messenger)
        if check_interface.errors:
          errors[pkgname] = check_interface.errors
    # Set checks
    for function in self.set_checks:
      logger = logging.getLogger(function.__name__)
      check_interface = SetCheckInterface(pkgmap)
      logger.debug("Calling %s", function.__name__)
      function(pkgs_data, check_interface, logger=logger, messenger=messenger)
      if check_interface.errors:
        errors = self.SetErrorsToDict(check_interface.errors, errors)
    return errors, messenger.messages, messenger.gar_lines

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
  return isalist


class PackageStats(DatabaseClient):
  """Collects stats about a package and saves it.

  TODO: Maintain a global database connection instead of creating one for each
  instantiated object.
  TODO: Store overrides in a separate table for performance.
  """
  # This list needs to be synchronized with the CollectStats() method.
  STAT_FILES = [
      "bad_paths",
      "binaries",
      "binaries_dump_info",
      # "defined_symbols",
      "depends",
      "isalist",
      # "ldd_dash_r",
      "overrides",
      "pkgchk",
      "pkginfo",
      "pkgmap",
      # This entry needs to be last because of the assumption in the
      # CollectStats() function.
      "basic_stats",
      "files_metadata",
  ]

  def __init__(self, srv4_pkg, stats_basedir=None, md5sum=None, debug=False):
    super(PackageStats, self).__init__(debug=debug)
    self.srv4_pkg = srv4_pkg
    self.md5sum = md5sum
    self.dir_format_pkg = None
    self.stats_path = None
    self.all_stats = {}
    self.stats_basedir = stats_basedir
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

  def GetStatsPath(self):
    if not self.stats_path:
      md5sum = self.GetMd5sum()
      two_chars = md5sum[0:2]
      parts = [self.stats_basedir, two_chars, md5sum]
      self.stats_path = os.path.join(*parts)
    return self.stats_path

  def StatsExist(self):
    """Checks if statistics of a package exist.

    Returns:
      bool
    """
    # More checks can be added in the future.
    md5_sum = self.GetMd5sum()
    logging.debug("StatsExist() md5_sum=%s", md5_sum)
    res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
    if not res.count():
      logging.debug("%s are not in the db", md5_sum)
      return False
    else:
      logging.debug("%s are in the db", md5_sum)
      pkg_stats = res.getOne()
      return pkg_stats.stats_version == PACKAGE_STATS_VERSION

  def GetDirFormatPkg(self):
    if not self.dir_format_pkg:
      self.dir_format_pkg = self.srv4_pkg.GetDirFormatPkg()
    return self.dir_format_pkg

  def MakeStatsDir(self):
    stats_path = self.GetStatsPath()
    self._MakeDirP(stats_path)

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
      binary_data["soname_guessed"] = False
      binary_data["base_name"] = binary_base_name
      if SONAME not in binary_data:
        # The binary doesn't tell its SONAME.  We're guessing it's the
        # same as the base file name.
        binary_data[SONAME] = binary_base_name
        binary_data["soname_guessed"] = True
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
    return basic_stats

  def GetOverrides(self):
    dir_pkg = self.GetDirFormatPkg()
    overrides = dir_pkg.GetOverrides()
    def OverrideToDict(override):
      d = {}
      d["pkgname"] = override.pkgname
      d["tag_name"] = override.tag_name
      d["tag_info"] = override.tag_info
      return d
    overrides_simple = [OverrideToDict(x) for x in overrides]
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
    if force:
      return self._CollectStats()
    if not self.StatsExist():
      return self._CollectStats()
    return self.ReadSavedStats()

  def _CollectStats(self):
    """The list of variables needs to be synchronized with the one
    at the top of this class.

    TODO:
    - Run pkgchk against the package file.
    - Grep all the files for bad paths.
    """
    stats_path = self.GetStatsPath()
    self.MakeStatsDir()
    dir_pkg = self.GetDirFormatPkg()
    logging.info("Collecting %s package statistics.", repr(dir_pkg.pkgname))
    pkg_stats = {
        "binaries": dir_pkg.ListBinaries(),
        "binaries_dump_info": self.GetBinaryDumpInfo(),
        "depends": dir_pkg.GetDependencies(),
        "isalist": GetIsalist(),
        "overrides": self.GetOverrides(),
        "pkgchk": self.GetPkgchkData(),
        "pkginfo": dir_pkg.GetParsedPkginfo(),
        "pkgmap": dir_pkg.GetPkgmap().entries,
        "bad_paths": dir_pkg.GetFilesContaining(BAD_CONTENT_REGEXES),
        "basic_stats": self.GetBasicStats(),
        "files_metadata": dir_pkg.GetFilesMetadata(),
    }
    db_pkg_stats = m.Srv4FileStats(md5_sum=self.GetMd5sum(),
                                   pkgname=pkg_stats["basic_stats"]["pkgname"],
                                   stats_version=PACKAGE_STATS_VERSION,
                                   data=cPickle.dumps(pkg_stats))
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
    logging.debug("GetAllStats()")
    if not self.all_stats and self.StatsExist():
      self.all_stats = self.ReadSavedStats()
    elif not self.all_stats:
      self.all_stats = self.CollectStats()
    return self.all_stats

  def GetSavedOverrides(self):
    if not self.StatsExist():
      raise PackageError("Package stats not ready.")
    override_stats = self.GetAllStats()["overrides"]
    override_list = [overrides.Override(**x) for x in override_stats]
    return override_list

  def DumpObject(self, obj, name):
    """Saves an object."""
    stats_path = self.GetStatsPath()
    # yaml
    if WRITE_YAML:
      out_file_name = os.path.join(stats_path, "%s.yml" % name)
      logging.debug("DumpObject(): writing %s", repr(out_file_name))
      f = open(out_file_name, "w")
      f.write(yaml.safe_dump(obj))
      f.close()
    # pickle
    out_file_name_pickle = os.path.join(stats_path, "%s.pickle" % name)
    logging.debug("DumpObject(): writing %s", repr(out_file_name_pickle))
    f = open(out_file_name_pickle, "wb")
    cPickle.dump(obj, f)
    f.close()
    self.all_stats[name] = obj

  def ReadSavedStats(self):
    md5_sum = self.GetMd5sum()
    res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
    return cPickle.loads(str(res.getOne().data))

  def _ParseLddDashRline(self, line):
    found_re = r"^\t(?P<soname>\S+)\s+=>\s+(?P<path_found>\S+)"
    symbol_not_found_re = (r"^\tsymbol not found:\s(?P<symbol>\S+)\s+"
                           r"\((?P<path_not_found>\S+)\)")
    only_so = r"^\t(?P<path_only>\S+)$"
    version_so = (r'^\t(?P<soname_version_not_found>\S+) '
                  r'\((?P<lib_name>\S+)\) =>\t \(version not found\)')
    stv_protected = (r'^\trelocation \S+ symbol: (?P<relocation_symbol>\S+): '
                     r'file (?P<relocation_path>\S+): '
                     r'relocation bound to a symbol with STV_PROTECTED visibility$')
    sizes_differ = (r'^\trelocation \S+ sizes differ: (?P<sizes_differ_symbol>\S+)$')
    sizes_info = (r'^\t\t\(file (?P<sizediff_file1>\S+) size=(?P<size1>0x\w+); '
                  r'file (?P<sizediff_file2>\S+) size=(?P<size2>0x\w+)\)$')
    sizes_one_used = (
        r'^\t\t(?P<sizediffused_file>\S+) size used; '
        'possible insufficient data copied$')
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
