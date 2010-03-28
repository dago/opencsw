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
import socket
import sqlite3
import subprocess
import textwrap
import yaml
from Cheetah import Template
import opencsw
import package_checks

DB_SCHEMA_VERSION = 2L
PACKAGE_STATS_VERSION = 5L
SYSTEM_PKGMAP = "/var/sadm/install/contents"
WS_RE = re.compile(r"\s+")
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"
SONAME = "soname"
CONFIG_MTIME = "mtime"
DO_NOT_REPORT_SURPLUS = set([u"CSWcommon", u"CSWcswclassutils", u"CSWisaexec"])
DO_NOT_REPORT_MISSING = set([])
DO_NOT_REPORT_MISSING_RE = [r"SUNW.*", r"\*SUNW.*"]
DUMP_BIN = "/usr/ccs/bin/dump"
PSTAMP_RE = r"(?P<username>\w+)@(?P<hostname>[\w\.-]+)-(?P<timestamp>\d+)"
DESCRIPTION_RE = r"^([\S]+) - (.*)$"
BAD_CONTENT_REGEXES = (
    # No need to encode / obfuscate these, as overrides can be used.
    r'/export/medusa',
    r'/opt/build',
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
)

REPORT_TMPL = u"""#if $missing_deps or $surplus_deps or $orphan_sonames
Missing dependencies of $pkgname:
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
$textwrap.fill($msg, 78, initial_indent="# ", subsequent_indent="# ")
#end for
#end if
#if $gar_lines

# Checkpkg suggests adding the following lines to the GAR recipe,
# see above for details:
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


class SystemPkgmap(object):
  """A class to hold and manipulate the /var/sadm/install/contents file.

  TODO: Implement timestamp checking and refreshing the cache.
  """

  STOP_PKGS = ["SUNWbcp", "SUNWowbcp", "SUNWucb"]
  CHECKPKG_DIR = ".checkpkg"
  SQLITE3_DBNAME_TMPL = "var-sadm-install-contents-cache-%s"

  def __init__(self):
    """There is no need to re-parse it each time.

    Read it slowly the first time and cache it for later."""
    self.cache = {}
    self.checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    self.fqdn = socket.getfqdn()
    self.db_path = os.path.join(self.checkpkg_dir,
                                self.SQLITE3_DBNAME_TMPL % self.fqdn)
    self.file_mtime = None
    self.cache_mtime = None
    self.initialized = False

  def _LazyInitializeDatabase(self):
    if not self.initialized:
      self.InitializeDatabase()

  def InitializeDatabase(self):
    if os.path.exists(self.db_path):
      logging.debug("Connecting to the %s database.", self.db_path)
      self.conn = sqlite3.connect(self.db_path)
      if not self.IsDatabaseGoodSchema():
        logging.warning("Old database schema detected. Dropping tables.")
        self.PurgeDatabase(drop_tables=True)
        self.CreateTables()
      if not self.IsDatabaseUpToDate():
        logging.warning("Rebuilding the package cache, can take a few minutes.")
        self.PurgeDatabase()
        self.PopulateDatabase()
    else:
      print "Building a cache of %s." % SYSTEM_PKGMAP
      print "The cache will be kept in %s." % self.db_path
      if not os.path.exists(self.checkpkg_dir):
        logging.debug("Creating %s", self.checkpkg_dir)
        os.mkdir(self.checkpkg_dir)
      self.conn = sqlite3.connect(self.db_path)
      self.CreateTables()
      self.PopulateDatabase()
    self.initialized = True

  def CreateTables(self):
      c = self.conn.cursor()
      c.execute("""
          CREATE TABLE systempkgmap (
            id INTEGER PRIMARY KEY,
            basename TEXT,
            path TEXT,
            line TEXT
          );
      """)
      logging.debug("Creating the config table.")
      c.execute("""
          CREATE TABLE config (
            key VARCHAR(255) PRIMARY KEY,
            float_value FLOAT,
            int_value INTEGER,
            str_value VARCHAR(255)
          );
      """)
      c.execute("""
          CREATE TABLE packages (
            pkgname VARCHAR(255) PRIMARY KEY,
            pkg_desc VARCHAR(255)
          );
      """)

  def PopulateDatabase(self):
    """Imports data into the database.

    Original bit of code from checkpkg:
    egrep -v 'SUNWbcp|SUNWowbcp|SUNWucb' /var/sadm/install/contents |
        fgrep -f $EXTRACTDIR/liblist >$EXTRACTDIR/shortcatalog
    """
    contents_length = os.stat(SYSTEM_PKGMAP).st_size
    estimated_lines = contents_length / INSTALL_CONTENTS_AVG_LINE_LENGTH
    system_pkgmap_fd = open(SYSTEM_PKGMAP, "r")
    stop_re = re.compile("(%s)" % "|".join(self.STOP_PKGS))
    # Creating a data structure:
    # soname - {<path1>: <line1>, <path2>: <line2>, ...}
    logging.debug("Building sqlite3 cache db of the %s file",
                  SYSTEM_PKGMAP)
    print "Processing %s" % SYSTEM_PKGMAP
    c = self.conn.cursor()
    count = itertools.count()
    sql = "INSERT INTO systempkgmap (basename, path, line) VALUES (?, ?, ?);"
    for line in system_pkgmap_fd:
      i = count.next()
      if not i % 1000:
        print "\r~%3.1f%%" % (100.0 * i / estimated_lines,),
      if stop_re.search(line):
        continue
      if line.startswith("#"):
        continue
      fields = re.split(WS_RE, line)
      pkgmap_entry_path = fields[0].split("=")[0]
      pkgmap_entry_dir, pkgmap_entry_base_name = os.path.split(pkgmap_entry_path)
      c.execute(sql, (pkgmap_entry_base_name, pkgmap_entry_dir, line.strip()))
    print "\rAll lines of %s were processed." % SYSTEM_PKGMAP
    print "Creating the main database index."
    sql = "CREATE INDEX basename_idx ON systempkgmap(basename);"
    c.execute(sql)
    self.PopulatePackagesTable()
    self.SetDatabaseMtime()
    self.SetDatabaseSchemaVersion()
    self.conn.commit()

  def _ParsePkginfoLine(self, line):
    fields = re.split(WS_RE, line)
    pkgname = fields[1]
    pkg_desc = u" ".join(fields[2:])
    return pkgname, pkg_desc

  def PopulatePackagesTable(self):
    args = ["pkginfo"]
    pkginfo_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = pkginfo_proc.communicate()
    ret = pkginfo_proc.wait()
    c = self.conn.cursor()
    sql = """
    INSERT INTO packages (pkgname, pkg_desc)
    VALUES (?, ?);
    """
    for line in stdout.splitlines():
      pkgname, pkg_desc = self._ParsePkginfoLine(line)
      try:
        c.execute(sql, [pkgname, pkg_desc])
      except sqlite3.IntegrityError, e:
        logging.warn("pkgname %s throws an sqlite3.IntegrityError: %s",
                     repr(pkgname), e)

  def SetDatabaseMtime(self):
    c = self.conn.cursor()
    sql = "DELETE FROM config WHERE key = ?;"
    c.execute(sql, [CONFIG_MTIME])
    mtime = self.GetFileMtime()
    logging.debug("Inserting the mtime (%s) into the database.", mtime)
    sql = """
    INSERT INTO config (key, float_value)
    VALUES (?, ?);
    """
    c.execute(sql, [CONFIG_MTIME, mtime])

  def SetDatabaseSchemaVersion(self):
    sql = """
    INSERT INTO config (key, int_value)
    VALUES (?, ?);
    """
    c = self.conn.cursor()
    c.execute(sql, ["db_schema_version", DB_SCHEMA_VERSION])
    logging.debug("Setting db_schema_version to %s", DB_SCHEMA_VERSION)

  def GetPkgmapLineByBasename(self, filename):
    self._LazyInitializeDatabase()
    if filename in self.cache:
      return self.cache[filename]
    sql = "SELECT path, line FROM systempkgmap WHERE basename = ?;"
    c = self.conn.cursor()
    c.execute(sql, [filename])
    lines = {}
    for row in c:
      lines[row[0]] = row[1]
    if len(lines) == 0:
      logging.debug("Cache doesn't contain filename %s", filename)
    self.cache[filename] = lines
    return lines

  def _InferPackagesFromPkgmapLine(self, line):
    """A stub of a function, to be enhanced."""
    line = line.strip()
    parts = re.split(WS_RE, line)
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
      sql = """
      SELECT float_value FROM config
      WHERE key = ?;
      """
      c = self.conn.cursor()
      c.execute(sql, [CONFIG_MTIME])
      row = c.fetchone()
      if not row:
        # raise ConfigurationError("Could not find the mtime setting")
        self.cache_mtime = 1
      else:
        self.cache_mtime = row[0]
    return self.cache_mtime

  def GetFileMtime(self):
    if not self.file_mtime:
      stat_data = os.stat(SYSTEM_PKGMAP)
      self.file_mtime = stat_data.st_mtime
    return self.file_mtime

  def GetDatabaseSchemaVersion(self):
    sql = """
    SELECT int_value FROM config
    WHERE key = ?;
    """
    c = self.conn.cursor()
    schema_on_disk = 1L
    try:
      c.execute(sql, ["db_schema_version"])
      for row in c:
        schema_on_disk = row[0]
    except sqlite3.OperationalError, e:
      # : no such column: int_value
      # The first versions of the database did not
      # have the int_value field.
      if re.search(r"int_value", str(e)):
        # We assume it's the first schema version.
        logging.debug("sqlite3.OperationalError, %s: guessing it's 1.", e)
      else:
        raise
    return schema_on_disk

  def IsDatabaseGoodSchema(self):
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    return good_version

  def IsDatabaseUpToDate(self):
    f_mtime = self.GetFileMtime()
    d_mtime = self.GetDatabaseMtime()
    logging.debug("f_mtime %s, d_time: %s", f_mtime, d_mtime)
    fresh = self.GetFileMtime() <= self.GetDatabaseMtime()
    good_version = self.GetDatabaseSchemaVersion() >= DB_SCHEMA_VERSION
    return fresh and good_version

  def SoftDropTable(self, tablename):
    c = self.conn.cursor()
    try:
      # This doesn't accept placeholders.
      c.execute("DROP TABLE %s;" % tablename)
    except sqlite3.OperationalError, e:
      logging.warn("sqlite3.OperationalError: %s", e)

  def PurgeDatabase(self, drop_tables=False):
    c = self.conn.cursor()
    if drop_tables:
      for table_name in ("config", "systempkgmap", "packages"):
        self.SoftDropTable(table_name)
    else:
      logging.info("Dropping the index.")
      sql = "DROP INDEX basename_idx;"
      try:
        c.execute(sql)
      except sqlite3.OperationalError, e:
        logging.warn(e)
      logging.info("Deleting all rows from the cache database")
      for table in ("config", "systempkgmap", "packages"):
        try:
          c.execute("DELETE FROM %s;" % table)
        except sqlite3.OperationalError, e:
          logging.warn("sqlite3.OperationalError: %s", e)

  def GetInstalledPackages(self):
    """Returns a dictioary of all installed packages."""
    self._LazyInitializeDatabase()
    c = self.conn.cursor()
    sql = "SELECT pkgname, pkg_desc FROM packages;"
    c.execute(sql)
    return dict(x[0:2] for x in c)


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
    fields = re.split(WS_RE, line)
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


class CheckpkgTag(object):
  """Represents a tag to be written to the checkpkg tag file."""

  def __init__(self, pkgname, tag_name, tag_info=None, severity=None, msg=None):
    self.pkgname = pkgname
    self.tag_name = tag_name
    self.tag_info = tag_info
    self.severity = severity
    self.msg = msg

  def __repr__(self):
    return (u"CheckpkgTag(%s, %s, %s)"
            % (repr(self.pkgname),
               repr(self.tag_name),
               repr(self.tag_info)))

  def ToGarSyntax(self):
    msg_lines = []
    if self.msg:
      msg_lines.extend(textwrap(self.msg, 70,
                                initial_indent="# ",
                                subsequent_indent="# "))
    if self.tag_info:
      tag_postfix = "|%s" % self.tag_info.replace(" ", "|")
    else:
      tag_postfix = ""
    msg_lines.append(u"CHECKPKG_OVERRIDES_%s += %s%s"
                     % (self.pkgname, self.tag_name, tag_postfix))
    return "\n".join(msg_lines)


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
    for stats_obj in stats_obj_list:
      # pkg_data = {}
      # This bit is tightly tied to the data structures returned by
      # PackageStats.
      #
      # Python strings are already implementing the flyweight pattern. What's
      # left is lists and dictionaries.
      logging.debug("Loading stats for %s", stats_obj.md5sum)
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

  def __init__(self, system_pkgmap=None):
    self.system_pkgmap = system_pkgmap
    if not self.system_pkgmap:
      self.system_pkgmap = SystemPkgmap()
    self.common_paths = {}

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

  def GetCommonPaths(self, arch):
    """Returns a list of paths for architecture, from gar/etc/commondirs*."""
    assert arch in ('i386', 'sparc', 'all'), "Wrong arch: %s" % repr(arch)
    if arch == 'all':
      archs = ('i386', 'sparc')
    else:
      archs = [arch]
    lines = []
    for arch in archs:
      file_name = os.path.join(
          os.path.dirname(__file__), "..", "..", "etc", "commondirs-%s" % arch)
      logging.debug("opening %s", file_name)
      f = open(file_name, "r")
      lines.extend(f.read().splitlines())
      f.close()
    return lines


class IndividualCheckInterface(CheckInterfaceBase):
  """To be passed to the checking functions.

  Wraps the creation of CheckpkgTag objects.
  """

  def __init__(self, pkgname, system_pkgmap=None):
    super(IndividualCheckInterface, self).__init__(system_pkgmap)
    self.pkgname = pkgname
    self.errors = []

  def ReportError(self, tag_name, tag_info=None, msg=None):
    tag = CheckpkgTag(self.pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(tag)


class SetCheckInterface(CheckInterfaceBase):
  """To be passed to set checking functions."""

  def __init__(self, system_pkgmap=None):
    super(SetCheckInterface, self).__init__(system_pkgmap)
    self.errors = []

  def ReportError(self, pkgname, tag_name, tag_info=None, msg=None):
    tag = CheckpkgTag(pkgname, tag_name, tag_info, msg=msg)
    self.errors.append(tag)


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


def ParseTagLine(line):
  """Parses a line from the tag.${module} file.

  Returns a triplet of pkgname, tagname, tag_info.
  """
  level_1 = line.strip().split(":")
  if len(level_1) > 1:
    data_1 = ":".join(level_1[1:])
    pkgname = level_1[0]
  else:
    data_1 = level_1[0]
    pkgname = None
  level_2 = re.split(WS_RE, data_1.strip())
  tag_name = level_2[0]
  if len(level_2) > 1:
    tag_info = " ".join(level_2[1:])
  else:
    tag_info = None
  return (pkgname, tag_name, tag_info)


class Override(object):
  """Represents an override of a certain checkpkg tag.

  It's similar to checkpkg.CheckpkgTag, but serves a different purpose.
  """

  def __init__(self, pkgname, tag_name, tag_info):
    self.pkgname = pkgname
    self.tag_name = tag_name
    self.tag_info = tag_info

  def __repr__(self):
    return (u"Override(%s, %s, %s)"
            % (repr(self.pkgname), repr(self.tag_name), repr(self.tag_info)))

  def DoesApply(self, tag):
    """Figures out if this override applies to the given tag."""
    basket_a = {}
    basket_b = {}
    if self.pkgname:
      basket_a["pkgname"] = self.pkgname
      basket_b["pkgname"] = tag.pkgname
    if self.tag_info:
      basket_a["tag_info"] = self.tag_info
      basket_b["tag_info"] = tag.tag_info
    basket_a["tag_name"] = self.tag_name
    basket_b["tag_name"] = tag.tag_name
    return basket_a == basket_b


def ParseOverrideLine(line):
  level_1 = line.split(":")
  if len(level_1) > 1:
    pkgname = level_1[0]
    data_1 = level_1[1]
  else:
    pkgname = None
    data_1 = level_1[0]
  level_2 = re.split(WS_RE, data_1.strip())
  if len(level_2) > 1:
    tag_name = level_2[0]
    tag_info = " ".join(level_2[1:])
  else:
    tag_name = level_2[0]
    tag_info = None
  return Override(pkgname, tag_name, tag_info)


def ApplyOverrides(error_tags, overrides):
  """Filters out all the error tags that overrides apply to.

  O(N * M), but N and M are always small.
  """
  tags_after_overrides = []
  applied_overrides = set([])
  provided_overrides = set(copy.copy(overrides))
  for tag in error_tags:
    override_applies = False
    for override in overrides:
      if override.DoesApply(tag):
        override_applies = True
        applied_overrides.add(override)
    if not override_applies:
      tags_after_overrides.append(tag)
  unapplied_overrides = provided_overrides.difference(applied_overrides)
  return tags_after_overrides, unapplied_overrides


def GetIsalist():
  args = ["isalist"]
  isalist_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = isalist_proc.communicate()
  ret = isalist_proc.wait()
  if ret:
    logging.error("Calling isalist has failed.")
  isalist = re.split(r"\s+", stdout.strip())
  return isalist


class PackageStats(object):
  """Collects stats about a package and saves it."""
  # This list needs to be synchronized with the CollectStats() method.
  STAT_FILES = [
      "all_filenames",
      "bad_paths",
      "basic_stats",
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
  ]

  def __init__(self, srv4_pkg, stats_basedir=None, md5sum=None):
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
    if not self.StatsDirExists():
      return False
    # More checks can be added in the future.
    return True

  def StatsDirExists(self):
    return os.path.isdir(self.GetStatsPath())

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
        logging.debug("The %s binary doesn't provide a SONAME. "
                      "(It might be an executable)",
                     binary_base_name)
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
    if not self.StatsDirExists() or force:
      self._CollectStats()
      return
    basic_stats_file = in_file_name_pickle = os.path.join(
        self.GetStatsPath(), "basic_stats.pickle")
    f = open(basic_stats_file, "r")
    obj = cPickle.load(f)
    f.close()
    saved_version = obj["stats_version"]
    if saved_version < PACKAGE_STATS_VERSION:
      self._CollectStats()

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
    self.DumpObject(dir_pkg.GetAllFilenames(), "all_filenames")
    self.DumpObject(dir_pkg.ListBinaries(), "binaries")
    self.DumpObject(self.GetBinaryDumpInfo(), "binaries_dump_info")
    self.DumpObject(dir_pkg.GetDependencies(), "depends")
    self.DumpObject(GetIsalist(), "isalist")
    self.DumpObject(self.GetOverrides(), "overrides")
    self.DumpObject(self.GetPkgchkData(), "pkgchk")
    self.DumpObject(dir_pkg.GetParsedPkginfo(), "pkginfo")
    self.DumpObject(dir_pkg.GetPkgmap().entries, "pkgmap")
    # The ldd -r reporting breaks on bigger packages during yaml saving.
    # self.DumpObject(self.GetLddMinusRlines(), "ldd_dash_r")
    # This check is currently disabled, let's save time by not collecting
    # these data.
    # self.DumpObject(self.GetDefinedSymbols(), "defined_symbols")
    self.DumpObject(dir_pkg.GetFilesContaining(BAD_CONTENT_REGEXES), "bad_paths")
    # This one should be last, so that if the collection is interrupted
    # in one of the previous runs, the basic_stats.pickle file is not there
    # or not updated, and the collection is started again.
    self.DumpObject(self.GetBasicStats(), "basic_stats")
    logging.debug("Statistics of %s have been collected.", repr(dir_pkg.pkgname))

  def GetAllStats(self):
    if self.StatsExist():
      self.all_stats = self.ReadSavedStats()
    else:
      self.CollectStats()
    return self.all_stats

  def GetSavedOverrides(self):
    if not self.StatsExist():
      raise PackageError("Package stats not ready.")
    override_stats = self.ReadObject("overrides")
    overrides = [Override(**x) for x in override_stats]
    return overrides

  def DumpObject(self, obj, name):
    """Saves an object."""
    stats_path = self.GetStatsPath()
    # yaml
    out_file_name = os.path.join(stats_path, "%s.yml" % name)
    logging.debug("DumpObject(): writing %s", repr(out_file_name))
    f = open(out_file_name, "w")
    f.write(yaml.safe_dump(obj))
    f.close()
    # pickle
    out_file_name_pickle = os.path.join(stats_path, "%s.pickle" % name)
    f = open(out_file_name_pickle, "wb")
    cPickle.dump(obj, f)
    f.close()
    self.all_stats[name] = obj

  def ReadObject(self, name):
    """Reads an object."""
    stats_path = self.GetStatsPath()
    in_file_name = os.path.join(stats_path, "%s.yml" % name)
    in_file_name_pickle = os.path.join(stats_path, "%s.pickle" % name)
    if os.path.exists(in_file_name_pickle):
      f = open(in_file_name_pickle, "r")
      obj = cPickle.load(f)
      f.close()
    else:
      f = open(in_file_name, "r")
      obj = yaml.safe_load(f)
      f.close()
    return obj

  def ReadSavedStats(self):
    all_stats = {}
    for name in self.STAT_FILES:
      all_stats[name] = self.ReadObject(name)
    return all_stats

  def _ParseLddDashRline(self, line):
    found_re = r"^\t(?P<soname>\S+)\s+=>\s+(?P<path_found>\S+)"
    symbol_not_found_re = r"^\tsymbol not found:\s(?P<symbol>\S+)\s+\((?P<path_not_found>\S+)\)"
    only_so = r"^\t(?P<path_only>\S+)$"
    version_so = r'^\t(?P<soname_version_not_found>\S+) \((?P<lib_name>\S+)\) =>\t \(version not found\)'
    stv_protected = (r'^\trelocation \S+ symbol: (?P<relocation_symbol>\S+): '
                     r'file (?P<relocation_path>\S+): '
                     r'relocation bound to a symbol with STV_PROTECTED visibility$')
    common_re = (r"(%s|%s|%s|%s|%s)"
                 % (found_re, symbol_not_found_re, only_so, version_so,
                    stv_protected))
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
    pkgname, tag_name, tag_info = ParseTagLine(line)
    error_tags.append(CheckpkgTag(pkgname, tag_name, tag_info))
  return error_tags
