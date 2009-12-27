# $Id$
#
# This is the checkpkg library, common for all checkpkg tests written in
# Python.

import optparse
import os
import os.path
import logging
import subprocess
import cPickle
import re
import sqlite3

SYSTEM_PKGMAP = "/var/sadm/install/contents"
WS_RE = re.compile(r"\s+")
NEEDED_SONAMES = "needed sonames"
# Don't report these as unnecessary.
TYPICAL_DEPENDENCIES = set(["CSWcommon", "CSWcswclassutils", "CSWisaexec"])

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



class SystemPkgmap(object):
  """A class to hold and manipulate the /var/sadm/install/contents file."""
  
  STOP_PKGS = ["SUNWbcp", "SUNWowbcp", "SUNWucb"] 
  CHECKPKG_DIR = ".checkpkg"
  SQLITE3_DBNAME = "var-sadm-install-contents-cache"

  def __init__(self):
    """There is no need to re-parse it each time.

    Read it slowly the first time and cache it for later."""
    self.checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    self.db_path = os.path.join(self.checkpkg_dir, self.SQLITE3_DBNAME)
    if os.path.exists(self.db_path):
      logging.debug("Connecting to the %s database.", self.db_path)
      self.conn = sqlite3.connect(self.db_path)
    else:
      logging.info("Building a cache of /var/sadm/install/contents.")
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

      # egrep -v 'SUNWbcp|SUNWowbcp|SUNWucb' /var/sadm/install/contents |
      #     fgrep -f $EXTRACTDIR/liblist >$EXTRACTDIR/shortcatalog

      system_pkgmap_fd = open(SYSTEM_PKGMAP, "r")

      stop_re = re.compile("(%s)" % "|".join(self.STOP_PKGS))

      # Creating a data structure:
      # soname - {<path1>: <line1>, <path2>: <line2>, ...}
      logging.debug("Building in-memory data structure for the %s file",
                    SYSTEM_PKGMAP)
      for line in system_pkgmap_fd:
        if stop_re.search(line):
          continue
        fields = re.split(WS_RE, line)
        pkgmap_entry_path = fields[0].split("=")[0]
        pkgmap_entry_dir, pkgmap_entry_base_name = os.path.split(pkgmap_entry_path)
        sql = "INSERT INTO systempkgmap (basename, path, line) VALUES (?, ?, ?);"
        c.execute(sql, (pkgmap_entry_base_name, pkgmap_entry_dir, line))
      logging.info("Creating an index.")
      sql = "CREATE INDEX basename_idx ON systempkgmap(basename);"
      self.conn.execute(sql)

  def GetPkgmapLineByBasename(self, filename):
    sql = "SELECT path, line FROM systempkgmap WHERE basename = ?;"
    c = self.conn.cursor()
    c.execute(sql, [filename])
    lines = {}
    for row in c:
      lines[row[0]] = row[1]
    return lines

def SharedObjectDependencies(pkgname,
                             binaries_by_pkgname,
                             needed_sonames_by_binary,
                             pkgs_by_soname,
                             filenames_by_soname,
                             pkg_by_any_filename):
  so_dependencies = set()
  orphan_sonames = set()
  self_provided = set()
  for binary in binaries_by_pkgname[pkgname]:
    if binary in needed_sonames_by_binary:
      for soname in needed_sonames_by_binary[binary][NEEDED_SONAMES]:
        if soname in filenames_by_soname:
          filename = filenames_by_soname[soname]
          pkg = pkg_by_any_filename[filename]
          self_provided.add(soname)
          so_dependencies.add(pkg)
        elif soname in pkgs_by_soname:
          so_dependencies.add(pkgs_by_soname[soname])
        else:
          orphan_sonames.add(soname)
    else:
      logging.warn("%s not found in needed_sonames_by_binary (%s)",
                   binary, needed_sonames_by_binary.keys())
  return so_dependencies, self_provided, orphan_sonames


def AnalyzeDependencies(pkgname,
                        declared_dependencies,
                        binaries_by_pkgname,
                        needed_sonames_by_binary,
                        pkgs_by_soname,
                        filenames_by_soname,
                        pkg_by_any_filename):
    """
    missing_deps, surplus_deps, orphan_sonames = checkpkg.AnalyzeDependencies(...)
    """
    so_dependencies, self_provided, orphan_sonames = SharedObjectDependencies(
        pkgname,
        binaries_by_pkgname,
        needed_sonames_by_binary,
        pkgs_by_soname,
        filenames_by_soname,
        pkg_by_any_filename)
    guessed_deps = set()
    patterns = (
        (r".*\.py", u"CSWpython"),
        (r".*\.pl", u"CSWperl"),
        (r".*\.rb", u"CSWruby"),
    )
    for pattern, dep_pkgname in patterns:
      # If any file name matches, add the dep, go to the next pattern/pkg
      # combination.
      tmp_re = re.compile("^%s$" % pattern)
      for f in pkg_by_any_filename:
        if re.match(tmp_re, f):
          if pkgname == pkg_by_any_filename[f]:
            guessed_deps.add(dep_pkgname)
            break
    auto_dependencies = so_dependencies.union(guessed_deps)
    declared_dependencies_set = set(declared_dependencies)
    missing_deps = auto_dependencies.difference(declared_dependencies_set)
    surplus_deps = declared_dependencies_set.difference(auto_dependencies)
    surplus_deps = surplus_deps.difference(TYPICAL_DEPENDENCIES)
    return missing_deps, surplus_deps, orphan_sonames
