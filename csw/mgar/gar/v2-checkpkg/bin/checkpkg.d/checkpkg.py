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

SYSTEM_PKGMAP = "/var/sadm/install/contents"
WS_RE = re.compile(r"\s+")

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
    find_tmpl = "find %s -print | xargs file | grep ELF | nawk -F: '{print $1}'"
    if not os.path.isdir(self.pkgpath):
      raise PackageError("%s does not exist or is not a directory"
                         % self.pkgpath)
    find_proc = subprocess.Popen(find_tmpl % self.pkgpath,
                                 shell=True, stdout=subprocess.PIPE)
    stdout, stderr = find_proc.communicate()
    ret = find_proc.wait()
    if ret:
      logging.error("The find command returned an error.")
    return stdout.splitlines()

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
  
  PICKLE_NAME = "var-sadm-install-contents.pickle"
  STOP_PKGS = ["SUNWbcp", "SUNWowbcp", "SUNWucb"] 
  CHECKPKG_DIR = ".checkpkg"

  def __init__(self):
    """There is no need to re-parse it each time.

    Read it slowly the first time and cache it for later."""
    self.checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    self.pickle_path = os.path.join(self.checkpkg_dir, self.PICKLE_NAME)
    if os.path.exists(self.pickle_path):
      logging.info("Unpickling %s, this can take up to 30s.", self.pickle_path)
      pickle_fd = open(self.pickle_path, "r")
      self.pkmap_lines_by_basename = cPickle.load(pickle_fd)
      pickle_fd.close()
    else:
      # The original checkpkg code to port is in the comments.
      #
      # egrep -v 'SUNWbcp|SUNWowbcp|SUNWucb' /var/sadm/install/contents |
      #     fgrep -f $EXTRACTDIR/liblist >$EXTRACTDIR/shortcatalog
      system_pkgmap_fd = open(SYSTEM_PKGMAP, "r")

      stop_re = re.compile("(%s)" % "|".join(self.STOP_PKGS))

      # Creating a data structure:
      # soname - {<path1>: <line1>, <path2>: <line2>, ...}
      logging.debug("Building in-memory data structure for the %s file",
                    SYSTEM_PKGMAP)
      pkmap_lines_by_basename = {}
      for line in system_pkgmap_fd:
        if stop_re.search(line):
          continue
        fields = re.split(WS_RE, line)
        pkgmap_entry_path = fields[0].split("=")[0]
        pkgmap_entry_dir, pkgmap_entry_base_name = os.path.split(pkgmap_entry_path)
        if pkgmap_entry_base_name not in pkmap_lines_by_basename:
          pkmap_lines_by_basename[pkgmap_entry_base_name] = {}
        pkmap_lines_by_basename[pkgmap_entry_base_name][pkgmap_entry_dir] = line
      logging.debug("The data structure contains %s files",
                    len(pkmap_lines_by_basename))
      self.pkmap_lines_by_basename = pkmap_lines_by_basename
      if not os.path.exists(self.checkpkg_dir):
        logging.debug("Creating %s", self.checkpkg_dir)
        os.mkdir(self.checkpkg_dir)
      logging.debug("Pickling to %s", self.pickle_path)
      pickle_fd = open(self.pickle_path, "w")
      cPickle.dump(self.pkmap_lines_by_basename, pickle_fd)
      pickle_fd.close()

  def GetPkgmapLineByBasename(self, filename):
    if filename in self.pkmap_lines_by_basename:
      return self.pkmap_lines_by_basename[filename]
    else:
      raise KeyError, "%s not found in self.pkmap_lines_by_basename" % filename
