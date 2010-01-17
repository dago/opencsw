# $Id$
#
# This is the checkpkg library, common for all checkpkg tests written in
# Python.

import itertools
import logging
import optparse
import os
import os.path
import re
import socket
import sqlite3
import subprocess
import StringIO
from Cheetah import Template

SYSTEM_PKGMAP = "/var/sadm/install/contents"
WS_RE = re.compile(r"\s+")
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"
SONAME = "soname"
CONFIG_MTIME = "mtime"
DO_NOT_REPORT_SURPLUS = set([u"CSWcommon", u"CSWcswclassutils", u"CSWisaexec"])
DO_NOT_REPORT_MISSING = set([u"SUNWlibC", u"SUNWcsl", u"SUNWlibms",
                             u"*SUNWcslr", u"*SUNWlibC", u"*SUNWlibms"])

# This shared library is present on Solaris 10 on amd64, but it's missing on
# Solaris 8 on i386.  It's okay if it's missing.
ALLOWED_ORPHAN_SONAMES = set([u"libm.so.2"])
DEPENDENCY_FILENAME_REGEXES = (
    (r".*\.pl", u"CSWperl"),
    (r".*\.pm", u"CSWperl"),
    (r".*\.py", u"CSWpython"),
    (r".*\.rb", u"CSWruby"),
)

REPORT_TMPL = u"""$pkgname:
#if $missing_deps
SUGGESTION: you may want to add some or all of the following as depends:
   (Feel free to ignore SUNW or SPRO packages)
#for $pkg in $sorted($missing_deps)
> $pkg
#end for
#end if
#if $surplus_deps
The following packages might be unnecessary dependencies:
#for $pkg in $sorted($surplus_deps)
? $pkg
#end for
#end if
#if $orphan_sonames
The following sonames don't belong to any package:
#for $soname in $sorted($orphan_sonames)
! $soname
#end for
#end if
#if not $missing_deps and not $surplus_deps and not $orphan_sonames
+ Dependencies of $pkgname look good.
#end if
"""

class Error(Exception):
  pass


class ConfigurationError(Error):
  pass


class PackageError(Error):
  pass


def GetOptions():
  parser = optparse.OptionParser()
  parser.add_option("-e", dest="extractdir",
                    help="The directory into which the package has been extracted")
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  (options, args) = parser.parse_args()
  if not options.extractdir:
    raise ConfigurationError("ERROR: -e option is missing.")
  # Using set() to make the arguments unique.
  return options, set(args)


class CheckpkgBase(object):
  """This class has functionality overlapping with DirectoryFormatPackage
  from the opencsw.py library. The classes should be merged.
  """

  def __init__(self, extractdir, pkgname):
    self.extractdir = extractdir
    self.pkgname = pkgname
    self.pkgpath = os.path.join(self.extractdir, self.pkgname)

  def CheckPkgpathExists(self):
    if not os.path.isdir(self.pkgpath):
      raise PackageError("%s does not exist or is not a directory"
                         % self.pkgpath)

  def ListBinaries(self):
    """Shells out to list all the binaries from a given package.

    Original checkpkg code:

    # #########################################
    # # find all executables and dynamic libs,and list their filenames.
    # listbinaries() {
    #   if [ ! -d $1 ] ; then
    #     print errmsg $1 not a directory
    #     rm -rf $EXTRACTDIR
    #     exit 1
    #   fi
    # 
    #   find $1 -print | xargs file |grep ELF |nawk -F: '{print $1}'
    # }
    """
    self.CheckPkgpathExists()
    find_tmpl = "find %s -print | xargs file | grep ELF | nawk -F: '{print $1}'"
    find_proc = subprocess.Popen(find_tmpl % self.pkgpath,
                                 shell=True, stdout=subprocess.PIPE)
    stdout, stderr = find_proc.communicate()
    ret = find_proc.wait()
    if ret:
      logging.error("The find command returned an error.")
    return stdout.splitlines()

  def GetAllFilenames(self):
    self.CheckPkgpathExists()
    file_basenames = []
    for root, dirs, files in os.walk(self.pkgpath):
      file_basenames.extend(files)
    return file_basenames

  def GetDependencies(self):
    fd = open(os.path.join(self.pkgpath, "install", "depend"), "r")
    depends = {}
    for line in fd:
      fields = re.split(WS_RE, line)
      if fields[0] == "P":
        depends[fields[1]] = " ".join(fields[1:])
    fd.close()
    return depends

  def FormatDepsReport(self, missing_deps, surplus_deps, orphan_sonames):
    """A intermediate version in which StringIO is used."""
    namespace = {
        "pkgname": self.pkgname,
        "missing_deps": missing_deps,
        "surplus_deps": surplus_deps,
        "orphan_sonames": orphan_sonames,
    }
    t = Template.Template(REPORT_TMPL, searchList=[namespace])
    return unicode(t)


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
    if os.path.exists(self.db_path):
      logging.debug("Connecting to the %s database.", self.db_path)
      self.conn = sqlite3.connect(self.db_path)
      if not self.IsDatabaseUpToDate():
        self.PurgeDatabase()
        self.PopulateDatabase()
    else:
      print "Building a cache of /var/sadm/install/contents."
      print "The cache will be kept in %s." % self.db_path
      if not os.path.exists(self.checkpkg_dir):
        logging.debug("Creating %s", self.checkpkg_dir)
        os.mkdir(self.checkpkg_dir)
      self.conn = sqlite3.connect(self.db_path)
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
            str_value VARCHAR(255)
          );
      """)
      self.PopulateDatabase()

  def PopulateDatabase(self):
    """Imports data into the database.

    Original bit of code from checkpkg:
    
    egrep -v 'SUNWbcp|SUNWowbcp|SUNWucb' /var/sadm/install/contents |
        fgrep -f $EXTRACTDIR/liblist >$EXTRACTDIR/shortcatalog
    """

    system_pkgmap_fd = open(SYSTEM_PKGMAP, "r")
    stop_re = re.compile("(%s)" % "|".join(self.STOP_PKGS))
    # Creating a data structure:
    # soname - {<path1>: <line1>, <path2>: <line2>, ...}
    logging.debug("Building sqlite3 cache db of the %s file",
                  SYSTEM_PKGMAP)
    c = self.conn.cursor()
    count = itertools.count()
    for line in system_pkgmap_fd:
      i = count.next()
      if not i % 1000:
        print "\r%s" % i,
      if stop_re.search(line):
        continue
      fields = re.split(WS_RE, line)
      pkgmap_entry_path = fields[0].split("=")[0]
      pkgmap_entry_dir, pkgmap_entry_base_name = os.path.split(pkgmap_entry_path)
      sql = "INSERT INTO systempkgmap (basename, path, line) VALUES (?, ?, ?);"
      c.execute(sql, (pkgmap_entry_base_name, pkgmap_entry_dir, line.strip()))
    print
    print "Creating the main database index."
    sql = "CREATE INDEX basename_idx ON systempkgmap(basename);"
    c.execute(sql)
    self.SetDatabaseMtime()
    self.conn.commit()

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

  def GetPkgmapLineByBasename(self, filename):
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

  def IsDatabaseUpToDate(self):
    f_mtime = self.GetFileMtime()
    d_mtime = self.GetDatabaseMtime()
    logging.debug("f_mtime", f_mtime, "d_time", d_mtime)
    return self.GetFileMtime() <= self.GetDatabaseMtime()

  def PurgeDatabase(self):
    c = self.conn.cursor()
    sql = "DELETE FROM config;"
    c.execute(sql)
    sql = "DELETE FROM systempkgmap;"
    c.execute(sql)
    sql = "DROP INDEX basename_idx;"
    try:
      c.execute(sql)
    except sqlite3.OperationalError, e:
      logging.warn(e)

def SharedObjectDependencies(pkgname,
                             binaries_by_pkgname,
                             needed_sonames_by_binary,
                             pkgs_by_soname,
                             filenames_by_soname,
                             pkg_by_any_filename):
  """This is one of the more obscure and more important pieces of code.

  I tried to make it simpler, but given that the operations here involve
  whole sets of packages, it's not easy.
  """
  so_dependencies = set()
  orphan_sonames = set()
  self_provided = set()
  for binary in binaries_by_pkgname[pkgname]:
    needed_sonames = needed_sonames_by_binary[binary][NEEDED_SONAMES]
    for soname in needed_sonames:
      if soname in filenames_by_soname:
        filename = filenames_by_soname[soname]
        pkg = pkg_by_any_filename[filename]
        self_provided.add(soname)
        so_dependencies.add(pkg)
      elif soname in pkgs_by_soname:
        so_dependencies.add(pkgs_by_soname[soname])
      else:
        orphan_sonames.add(soname)
  return so_dependencies, self_provided, orphan_sonames


def GuessDepsByFilename(pkgname, pkg_by_any_filename):
  """Guesses dependencies based on filename regexes."""
  guessed_deps = set()
  for pattern, dep_pkgname in DEPENDENCY_FILENAME_REGEXES:
    # If any file name matches, add the dep, go to the next pattern/pkg
    # combination.
    pattern_re = re.compile("^%s$" % pattern)
    for filename in pkg_by_any_filename:
      if (re.match(pattern_re, filename)
            and
          pkgname == pkg_by_any_filename[filename]):
        guessed_deps.add(dep_pkgname)
        break
  return guessed_deps


def GuessDepsByPkgname(pkgname, pkg_by_any_filename):
  # More guessed dependencies: If one package is a substring of another, it
  # might be a hint. For example, CSWmysql51test should depend on CSWmysql51.
  # However, the rt (runtime) packages should not want to depend on the main
  # package.
  guessed_deps = set()
  all_other_pkgs = set(pkg_by_any_filename.values())
  for other_pkg in all_other_pkgs:
    other_pkg = unicode(other_pkg)
    if pkgname == other_pkg:
      continue
    if pkgname.startswith(other_pkg):
      endings = ["devel", "test", "bench", "dev"]
      for ending in endings:
        if pkgname.endswith(ending):
          guessed_deps.add(other_pkg)
  return guessed_deps


def AnalyzeDependencies(pkgname,
                        declared_dependencies,
                        binaries_by_pkgname,
                        needed_sonames_by_binary,
                        pkgs_by_soname,
                        filenames_by_soname,
                        pkg_by_any_filename):
  """Gathers and merges dependency results from other functions.

  declared_dependencies: Dependencies that the package in question claims to
                         have.

  binaries_by_pkgname: A dictionary mapping pkgnames (CSWfoo) to binary names
                       (without paths)

  needed_sonames_by_binary: A dictionary mapping binary file name to
                            a dictionary containing: "needed sonames",
                            "soname", "rpath". Based on examining the binary
                            files within the packages.

  pkgs_by_soname: A dictionary mapping sonames to pkgnames, based on the
                  contents of the system wide pkgmap
                  (/var/sadm/install/contents)

  filenames_by_soname: A dictionary mapping shared library sonames to filenames,
                       based on files within packages

  pkg_by_any_filename: Mapping from file names to packages names, based on the
                       contents of the packages under examination.
  """
  declared_dependencies_set = set(declared_dependencies)

  so_dependencies, self_provided, orphan_sonames = SharedObjectDependencies(
      pkgname,
      binaries_by_pkgname,
      needed_sonames_by_binary,
      pkgs_by_soname,
      filenames_by_soname,
      pkg_by_any_filename)
  auto_dependencies = reduce(lambda x, y: x.union(y),
      [
        so_dependencies,
        GuessDepsByFilename(pkgname, pkg_by_any_filename),
        GuessDepsByPkgname(pkgname, pkg_by_any_filename),
      ])
  missing_deps = auto_dependencies.difference(declared_dependencies_set)
  # Don't report itself as a suggested dependency.
  missing_deps = missing_deps.difference(set([pkgname]))
  missing_deps = missing_deps.difference(set(DO_NOT_REPORT_MISSING))
  surplus_deps = declared_dependencies_set.difference(auto_dependencies)
  surplus_deps = surplus_deps.difference(DO_NOT_REPORT_SURPLUS)
  orphan_sonames = orphan_sonames.difference(ALLOWED_ORPHAN_SONAMES)
  return missing_deps, surplus_deps, orphan_sonames


def ExpandRunpath(runpath, isalist):
  # Emulating $ISALIST expansion
  if '$ISALIST' in runpath:
    expanded_list = [runpath.replace('$ISALIST', isa) for isa in isalist]
  else:
    expanded_list = [runpath]
  return expanded_list

def Emulate64BitSymlinks(runpath_list):
  """Need to emulate the 64 -> amd64, 64 -> sparcv9 symlink

  Since we don't know the architecture, we'll adding both amd64 and sparcv9.
  It should be safe.
  """
  symlinks = (
      ("/opt/csw/bdb4", ["/opt/csw/bdb42"]),
      ("/64", ["/amd64", "/sparcv9"]),
  )
  symlinked_list = []
  for runpath in runpath_list:
    for symlink, expansion_list in symlinks:
      symlink_re = re.compile(r"%s(/|$)" % symlink)
      if re.search(symlink_re, runpath):
        for expansion in expansion_list:
          symlinked_list.append(runpath.replace(symlink, expansion))
      else:
        symlinked_list.append(runpath)
  return symlinked_list


def SanitizeRunpath(runpath):
  ok = False
  while True:
    if runpath.endswith("/"):
      runpath = runpath[:-1]
    elif "//" in runpath:
      runpath = runpath.replace("//", "/")
    else:
      break
  return runpath


def GetLinesBySoname(pkgmap, needed_sonames, runpath_by_needed_soname, isalist):
  """Works out which system pkgmap lines correspond to given sonames."""
  lines_by_soname = {}
  for soname in needed_sonames:
    # This is the critical part of the algorithm: it iterates over the
    # runpath and finds the first matching one.
    runpath_found = False
    for runpath in runpath_by_needed_soname[soname]:
      runpath = SanitizeRunpath(runpath)
      runpath_list = ExpandRunpath(runpath, isalist)
      runpath_list = Emulate64BitSymlinks(runpath_list)
      soname_runpath_data = pkgmap.GetPkgmapLineByBasename(soname)
      logging.debug("%s: will be looking for %s in %s" %
                    (soname, runpath_list, soname_runpath_data.keys()))
      for runpath_expanded in runpath_list:
        if runpath_expanded in soname_runpath_data:
          lines_by_soname[soname] = soname_runpath_data[runpath_expanded]
          runpath_found = True
          # This break only goes out of the inner loop,
          # need another one below to finish the outer loop.
          break
      if runpath_found:
        break
  return lines_by_soname


def BuildIndexesBySoname(needed_sonames_by_binary):
  """Builds data structures indexed by soname.

  Building indexes
  {"foo.so": ["/opt/csw/lib/gcc4", "/opt/csw/lib", ...],
   ...
  }
  """
  needed_sonames = set()
  binaries_by_soname = {}
  runpath_by_needed_soname = {}
  for binary_name, data in needed_sonames_by_binary.iteritems():
    for soname in data[NEEDED_SONAMES]:
      needed_sonames.add(soname)
      if soname not in runpath_by_needed_soname:
        runpath_by_needed_soname[soname] = []
      runpath_by_needed_soname[soname].extend(data[RUNPATH])
      if soname not in binaries_by_soname:
        binaries_by_soname[soname] = set()
      binaries_by_soname[soname].add(binary_name)
  return needed_sonames, binaries_by_soname, runpath_by_needed_soname


def ParseDumpOutput(dump_output):
  binary_data = {RUNPATH: [],
                 NEEDED_SONAMES: []}
  for line in dump_output.splitlines():
    fields = re.split(WS_RE, line)
    # TODO: Make it a unit test
    # logging.debug("%s says: %s", DUMP_BIN, fields)
    if len(fields) < 3:
      continue
    if fields[1] == "NEEDED":
      binary_data[NEEDED_SONAMES].append(fields[2])
    elif fields[1] == "RUNPATH":
      binary_data[RUNPATH].extend(fields[2].split(":"))
    elif fields[1] == "SONAME":
      binary_data[SONAME] = fields[2]
  # Adding the default runtime path search option.
  binary_data[RUNPATH].append("/usr/lib/$ISALIST")
  binary_data[RUNPATH].append("/usr/lib")
  binary_data[RUNPATH].append("/lib/$ISALIST")
  binary_data[RUNPATH].append("/lib")
  return binary_data
