#!/opt/csw/bin/python2.6

import cjson
import copy
import datetime
import hashlib
import logging
import optparse
import os
import re
import shutil
import sys
import tempfile
import time

from lib.python import common_constants
from lib.python import configuration
from lib.python import opencsw
from lib.python import overrides
from lib.python import pkgmap
from lib.python import rest
from lib.python import sharedlib_utils
from lib.python import shell
from lib.python import util
from lib.python import representations

ADMIN_FILE_CONTENT = """
basedir=default
runlevel=nocheck
conflict=nocheck
setuid=nocheck
action=nocheck
partial=nocheck
instance=unique
idepend=quit
rdepend=quit
space=quit
authentication=nocheck
networktimeout=10
networkretries=5
keystore=/var/sadm/security
proxy=
"""

BAD_CONTENT_REGEXES = (
    # Slightly obfuscating these by using the default concatenation of
    # strings.
    r'/export' r'/home',
    r'/export' r'/medusa',
    r'/opt' r'/build',
    r'/usr' r'/local',
    r'/usr' r'/share',
)


class Error(Exception):
  """Generic error."""


class ShellCommandError(Error):
  """A problem with running a binary."""


class Unpacker(object):
  """Responsible for unpacking the package and extracting data.

  The functionality of this class used to be split among 3 classes in the old
  code base: Package, InspectivePackage and PackageStats.
  """
  STATS_VERSION = 13L
  
  def __init__(self, pkg_path, debug):
    self.debug = debug
    self.pkg_path = pkg_path
    self._work_dir = None
    self._admin_file = None
    self._gunzipped_path = None
    self._md5_sum = None
    self._stat = None
    self._mtime = None
    self._transformed = False
    self._pkgname = None
    self._pkginfo_dict = None
    self._dir_format_base_dir = None
    self._files_metadata = None
    self._binaries = None
    self._file_paths = None
    self.config = configuration.GetConfig()
    self.rest_client = rest.RestClient(
        pkgdb_url=self.config.get('rest', 'pkgdb'),
        releases_url=self.config.get('rest', 'releases'))

  def __del__(self):
    self.Cleanup()

  def __repr__(self):
    return u"Unpacker(%s)" % repr(self.pkg_path)

  def Cleanup(self):
    if self._work_dir and shutil:
      logging.debug("Removing %r", self._work_dir)
      shutil.rmtree(self._work_dir)
      self._work_dir = None

  @property
  def work_dir(self):
    if not self._work_dir:
      self._work_dir = tempfile.mkdtemp(prefix="pkg_", dir="/var/tmp")
    return self._work_dir

  @property
  def admin_file_path(self):
    if self._admin_file is None:
      self._admin_file = os.path.join(self.work_dir, "admin")
      with open(self._admin_file, "w") as fd:
        fd.write(ADMIN_FILE_CONTENT)
    return self._admin_file

  @property
  def md5_sum(self):
    if self._md5_sum is None:
      logging.debug("md5_sum: reading file %r", self.pkg_path)
      md5_hash = hashlib.md5()
      with open(self.pkg_path) as fp:
        # Chunking the data reads to avoid reading huge packages into memory at
        # once.
        chunk_size = 2 * 1024 * 1024
        data = fp.read(chunk_size)
        while data:
          md5_hash.update(data)
          data = fp.read(chunk_size)
      self._md5_sum = md5_hash.hexdigest()
    return self._md5_sum

  @property
  def stat(self):
    if self._stat is None:
      self._stat = os.stat(self.pkg_path)
    return self._stat

  @property
  def size(self):
    return self.stat.st_size

  @property
  def mtime(self):
    """The mtime of the svr4 file.

    Returns: a datetime.datetime object (not encodable with json!).
    """
    if self._mtime is None:
      s = self.stat
      t = time.gmtime(s.st_mtime)
      self._mtime = datetime.datetime(*t[:6])
    return self._mtime

  def _Gunzip(self):
    """Gunzipping the package."""
    gzip_suffix = ".gz"
    pkg_suffix = ".pkg"
    if self.pkg_path.endswith("%s%s" % (pkg_suffix, gzip_suffix)):
      # Causing the class to stat the .gz file.  This call throws away the
      # result, but the result will be cached as a object member.
      self.mtime
      self.md5_sum
      base_name = os.path.split(self.pkg_path)[1][:(-len(gzip_suffix))]
      self._gunzipped_path = os.path.join(self.work_dir, base_name)
      with open(self._gunzipped_path, 'w') as gunzipped_file:
        args = ["gunzip", "-f", "-c", self.pkg_path]
        unused_ret_code, _, _ = shell.ShellCommand(args, stdout=gunzipped_file)
    elif self.pkg_path.endswith(pkg_suffix):
      self._gunzipped_path = self.pkg_path
    else:
      raise Error("The file name should end in either "
                  "%s or %s, but it's %s."
                  % (gzip_suffix, pkg_suffix, repr(self.pkg_path)))

  @property
  def gunzipped_path(self):
    if self._gunzipped_path is None:
      self._Gunzip()
    return self._gunzipped_path

  @property
  def pkgname(self):
    """It's necessary to figure out the pkgname from the .pkg file.
    # nawk 'NR == 2 {print $1; exit;} $f
    """
    if self._pkgname is None:
      gunzipped_path = self.gunzipped_path
      args = ["nawk", "NR == 2 {print $1; exit;}", gunzipped_path]
      ret_code, stdout, stderr = shell.ShellCommand(args)
      self._pkgname = stdout.strip()
      logging.debug("GetPkgname(): %s", repr(self.pkgname))
    return self._pkgname

  def DirsInWorkdir(self):
    """Directories present in self.work_dir."""
    paths = os.listdir(self.work_dir)
    dirs = []
    for p in paths:
      abspath = os.path.join(self.work_dir, p)
      if os.path.isdir(abspath):
        dirs.append(abspath)
    return dirs

  def _TransformToDir(self):
    """Transforms the file to the directory format.

    This uses the Pkgtrans function at the top, because pkgtrans behaves
    differently on Solaris 8 and 10.  Having our own implementation helps
    achieve consistent behavior.
    """
    if not self._transformed:
      gunzipped_path = self.gunzipped_path
      pkgname = self.pkgname
      args = [os.path.join(os.path.dirname(__file__),
                           "..", "..", "bin", "custom-pkgtrans"),
              gunzipped_path, self.work_dir, pkgname]
      shell.ShellCommand(args, allow_error=False)
      dirs = self.DirsInWorkdir()
      if len(dirs) != 1:
        raise Error("Exactly one package in the package stream is expected; actual: "
                    "%s." % (dirs))
      self._transformed = True
      self._dir_format_base_dir = os.path.join(self.work_dir, pkgname)

  def GetPkginfoFilename(self):
    return os.path.join(self._dir_format_base_dir, "pkginfo")

  def GetParsedPkginfo(self):
    if self._pkginfo_dict is None:
      with open(self.GetPkginfoFilename(), "r") as pkginfo_fd:
        self._pkginfo_dict = opencsw.ParsePkginfo(pkginfo_fd)
    return self._pkginfo_dict

  def GetBasedir(self):
    basedir_id = "BASEDIR"
    pkginfo = self.GetParsedPkginfo()
    if basedir_id in pkginfo:
      basedir = pkginfo[basedir_id]
    else:
      basedir = ""
    # The convention in checkpkg is to not include the leading slash in paths.
    basedir = basedir.lstrip("/")
    return basedir

  def GetCatalogname(self):
    """Returns the catalog name of the package.

    A bit hacky.  Looks for the first word of the NAME field in the package.
    """
    pkginfo = self.GetParsedPkginfo()
    words = re.split(configuration.WS_RE, pkginfo["NAME"])
    return words[0]

  def GetBasicStats(self):
    basic_stats = {}
    basic_stats["stats_version"] = self.STATS_VERSION
    basic_stats["pkg_path"] = self.pkg_path
    basic_stats["pkg_basename"] = os.path.basename(self.pkg_path)
    basic_stats["parsed_basename"] = opencsw.ParsePackageFileName(
        basic_stats["pkg_basename"])
    basic_stats["pkgname"] = self.pkgname
    basic_stats["catalogname"] = self.GetCatalogname()
    basic_stats["md5_sum"] = self.md5_sum
    basic_stats["size"] = self.size
    return basic_stats

  def _GetOverridesStream(self, file_path):
    # This might potentially cause a file descriptor leak, but I'm not going to
    # worry about that at this stage.
    # NB, the whole catalog run doesn't seem to be suffering. (~2500 packages)
    #
    # There is a race condition here, but it's executing sequentially, I don't
    # expect any concurrency problems.
    if os.path.isfile(file_path):
      logging.debug("Opening %s override file." % repr(file_path))
      return open(file_path, "r")
    else:
      logging.debug("Override file %s not found." % repr(file_path))
      return None

  def _ParseOverridesStream(self, stream):
    override_list = []
    for line in stream:
      if line.startswith("#"):
        continue
      override_list.append(overrides.ParseOverrideLine(line))
    return override_list

  def GetOverrides(self):
    """Returns overrides, a list of overrides.Override instances."""
    override_list = []
    catalogname = self.GetCatalogname()
    override_paths = (
        [self._dir_format_base_dir,
         "root",
         "opt/csw/share/checkpkg/overrides", catalogname],
        [self._dir_format_base_dir,
         "install",
         "checkpkg_override"],
    )
    for override_path in override_paths:
      file_path = os.path.join(*override_path)
      try:
        with open(file_path, "r") as stream:
          override_list.extend(self._ParseOverridesStream(stream))
      except IOError as e:
        logging.debug('Could not open %r: %s' % (file_path, e))
    """Simple data structure with overrides."""
    def OverrideToDict(override):
      return {
        "pkgname":  override.pkgname,
        "tag_name":  override.tag_name,
        "tag_info":  override.tag_info,
      }
    overrides_simple = [OverrideToDict(x) for x in override_list]
    return overrides_simple

  def GetDependencies(self):
    """Gets dependencies information.

    Returns:
      A tuple of (list, list) of depends and i_depends.
    """
    # The collection of dependencies needs to be a list (as opposed to
    # a set) because there might be duplicates and it's necessary to
    # carry that information.
    depends = []
    i_depends = []
    depend_file_path = os.path.join(self._dir_format_base_dir, "install", "depend")
    try:
      with open(depend_file_path, "r") as fd:
        for line in fd:
          fields = re.split(configuration.WS_RE, line)
          if len(fields) < 2:
            logging.warning("Bad depends line: %r", line)
          if fields[0] == "P":
            pkgname = fields[1]
            pkg_desc = " ".join(fields[1:])
            depends.append((pkgname, pkg_desc))
          if fields[0] == "I":
            pkgname = fields[1]
            i_depends.append(pkgname)
    except IOError as e:
      logging.debug('Could not open %r: %s' % (depend_file_path, e))
    return depends, i_depends

  def CheckPkgpathExists(self):
    if not os.path.isdir(self._dir_format_base_dir):
      raise PackageError("%s does not exist or is not a directory"
                         % self._dir_format_base_dir)

  def GetPathsInSubdir(self, remove_prefix, subdir):
    file_paths = []
    for root, dirs, files in os.walk(os.path.join(self._dir_format_base_dir, subdir)):
      full_paths = [os.path.join(root, f) for f in files]
      file_paths.extend([f.replace(remove_prefix, "") for f in full_paths])
    return file_paths

  def GetAllFilePaths(self):
    """Returns a list of all paths from the package."""
    if self._file_paths is None:
      # Support for relocatable packages
      basedir = self.GetBasedir()
      self.CheckPkgpathExists()
      remove_prefix = "%s/" % self._dir_format_base_dir
      self._file_paths = self.GetPathsInSubdir(remove_prefix, "root")
      if self.RelocPresent():
        self._file_paths += self.GetPathsInSubdir(remove_prefix, "reloc")
    return self._file_paths

  def GetFilesMetadata(self):
    """Returns a data structure with all the files plus their metadata.

    [
      {
        "path": ...,
        "mime_type": ...,
      },
    ]
    """
    if not self._files_metadata:
      self.CheckPkgpathExists()
      self._files_metadata = []
      files_root = self.GetFilesDir()
      all_files = self.GetAllFilePaths()
      file_magic = util.FileMagic()
      basedir = self.GetBasedir()
      for file_path in all_files:
        full_path = unicode(self.MakeAbsolutePath(file_path))
        file_info = util.GetFileMetadata(file_magic, self._dir_format_base_dir, full_path)
        # To prevent files from containing the full temporary path.
        file_info_dict = file_info._asdict()
        file_info_dict["path"] = util.StripRe(file_path, util.ROOT_RE)
        file_info = representations.FileMetadata(**file_info_dict)
        self._files_metadata.append(file_info)
      file_magic.Close()
    return self._files_metadata

  def RelocPresent(self):
    return os.path.exists(os.path.join(self._dir_format_base_dir, "reloc"))

  def GetFilesDir(self):
    """Returns the subdirectory in which files, are either "reloc" or "root"."""
    if self.RelocPresent():
      return "reloc"
    else:
      return "root"

  def MakeAbsolutePath(self, p):
    return os.path.join(self._dir_format_base_dir, p)

  def ListBinaries(self):
    """Lists all the binaries from a given package.

    Original checkpkg code:

    #########################################
    # find all executables and dynamic libs,and list their filenames.
    listbinaries() {
      if [ ! -d $1 ] ; then
        print errmsg $1 not a directory
        rm -rf $EXTRACTDIR
        exit 1
      fi
      find $1 -print | xargs file |grep ELF |nawk -F: '{print $1}'
    }

    Returns a list of absolute paths.

    Now that there are files_metadata, this function can safely go away, once
    all its callers are modified to use files_metadata instead.
    """
    if self._binaries is None:
      self.CheckPkgpathExists()
      files_metadata = self.GetFilesMetadata()
      self._binaries = []
      # The nested for-loop looks inefficient.
      for file_info in files_metadata:
        if sharedlib_utils.IsBinary(file_info._asdict()):
          self._binaries.append(file_info.path)
      self._binaries.sort()
    return self._binaries

  def GetBinaryDumpInfo(self):
    # Binaries. This could be split off to a separate function.
    # man ld.so.1 for more info on this hack
    basedir = self.GetBasedir()
    binaries_dump_info = []
    for binary in self.ListBinaries():
      binary_abs_path = os.path.join(
          self._dir_format_base_dir, self.GetFilesDir(), binary)
      if basedir:
        binary = os.path.join(basedir, binary)
      
      binaries_dump_info.append(util.GetBinaryDumpInfo(binary_abs_path, binary))

    return binaries_dump_info

  def GetObsoletedBy(self):
    """Collects obsolescence information from the package if it exists

    Documentation:
    http://wiki.opencsw.org/obsoleting-packages

    Returns:

    A dictionary of "has_obsolete_info", "syntax_ok" and
    "obsoleted_by" where obsoleted_by is a list of (pkgname,
    catalogname) tuples and has_obsolete_info and syntax_ok are
    booleans.

    If the package has not been obsoleted or the package predates the
    implementation of this mechanism, obsoleted_by is an empty list
    and has_obsolete_info will be False.

    If the package provides obsolescence information but the format of
    the information is invalid, syntax_ok will be False and the list
    may be empty.  It will always contain the valid entries.
    """

    has_obsolete_info = False
    obsoleted_syntax_ok = True
    obsoleted_by = []
    obsoleted_by_path = os.path.join(self._dir_format_base_dir, "install", "obsolete")

    if os.path.exists(obsoleted_by_path):
      has_obsolete_info = True
      with open(obsoleted_by_path, "r") as fd:
        for line in fd:
          fields = re.split(configuration.WS_RE, line)
          if len(fields) < 2:
            obsoleted_syntax_ok = False
            logging.warning("Bad line in obsolete file: %s", repr(line))
            continue
          pkgname, catalogname = fields[0:2]
          obsoleted_by.append((pkgname, catalogname))

    return {
        "syntax_ok": obsoleted_syntax_ok,
        "obsoleted_by": obsoleted_by,
        "has_obsolete_info": has_obsolete_info,
    }

  def GetPkgmap(self, analyze_permissions=False, strip=None):
    fd = open(os.path.join(self._dir_format_base_dir, "pkgmap"), "r")
    basedir = self.GetBasedir()
    return pkgmap.Pkgmap(fd, analyze_permissions, strip, basedir)

  def GetPkgchkOutput(self):
    """Returns: (exit code, stdout, stderr)."""
    if not self._transformed:
        self._TransformToDir()
    args = ["/usr/sbin/pkgchk", "-d", self.work_dir, self.pkgname]
    return shell.ShellCommand(args)

  def GetPkgchkData(self):
    ret, stdout, stderr = self.GetPkgchkOutput()
    data = {
        'return_code': ret,
        'stdout_lines': stdout.splitlines(),
        'stderr_lines': stderr.splitlines(),
    }
    return data

  def GetFilesContaining(self, regex_list):
    full_paths = self.GetAllFilePaths()
    files_by_pattern = {}
    for full_path in full_paths:
      content = open(self.MakeAbsolutePath(full_path), "rb").read()
      for regex in regex_list:
        if re.search(regex, content):
          if regex not in files_by_pattern:
            files_by_pattern[regex] = []
          files_by_pattern[regex].append(full_path)
    return files_by_pattern

  def GetMainStatsStruct(self, binary_md5_sums):
    basic_stats = self.GetBasicStats()
    depends, i_depends = self.GetDependencies()
    arch = basic_stats["parsed_basename"]["arch"]
    pkg_stats = {
        "basic_stats": basic_stats,
        "depends": depends,
        "i_depends": i_depends,
        "overrides": self.GetOverrides(),
        "pkginfo": self.GetParsedPkginfo(),
        # GetIsaList returns a frozenset, but we need a list because of
        # serializing to JSON.
        "isalist": list(sharedlib_utils.GetIsalist(arch)),
        # Data in json must be stored using simple structures such as numbers
        # or strings. We cannot store a datetime.datetime object, we must
        # convert it into a string.
        "mtime": self.mtime.isoformat(),
        "files_metadata": self.GetFilesMetadata(),
        "binaries": self.ListBinaries(),
        "binaries_dump_info": self.GetBinaryDumpInfo(),
        "obsoleteness_info": self.GetObsoletedBy(),
        "pkgmap": self.GetPkgmap().entries,
        "pkgchk": self.GetPkgchkData(),
        "bad_paths": self.GetFilesContaining(BAD_CONTENT_REGEXES),
        "binary_md5_sums": binary_md5_sums,
    }
    return pkg_stats

  def _CollectElfdumpData(self):
    logging.debug("Elfdump data.")
    binary_md5_sums = []
    for binary in self.ListBinaries():
      binary_abs_path = os.path.join(
          self._dir_format_base_dir, self.GetFilesDir(), binary)
      args = [os.path.join(os.path.dirname(__file__),
                           'collect_binary_elfinfo.py'),
              '--input', binary_abs_path]
      se = None
      if self.debug:
        args.append('--debug')
        se = sys.stderr
      ret_code, stdout, stderr = shell.ShellCommand(args, stderr=se)
      if ret_code:
        raise ShellCommandError(stderr)
      binary_data = cjson.decode(stdout)
      binary_md5_sums.append((binary, binary_data['md5_sum']))
    return binary_md5_sums


  def CollectStats(self, force_unpack):
    if force_unpack or not self.rest_client.BlobExists('pkgstats',
                                                       self.md5_sum):
      self._Gunzip()
      self._TransformToDir()
      binary_md5_sums = self._CollectElfdumpData()
      main_struct = self.GetMainStatsStruct(binary_md5_sums)
      self.rest_client.SaveBlob('pkgstats', self.md5_sum, main_struct)
      return True
    return False


if __name__ == '__main__':
  parser = optparse.OptionParser()
  parser.add_option("-i", "--input", dest="input_file",
                    help="Input file")
  parser.add_option("--force-unpack", dest="force_unpack",
                    action="store_true", default=False)
  parser.add_option("--debug", dest="debug",
                    action="store_true", default=False)
  options, args = parser.parse_args()
  if not options.input_file:
    sys.stdout.write("Please provide an input file name. See --help\n")
    sys.exit(1)
  logging.basicConfig(level=logging.DEBUG)
  unpacker = Unpacker(options.input_file, debug=options.debug)
  unpacked = unpacker.CollectStats(force_unpack=options.force_unpack)
  unpacker.Cleanup()
  data_back = {
      "md5_sum": unpacker.md5_sum,
      "unpacked": bool(unpacked),
  }
  # Returning data to the master process.
  print(cjson.encode(data_back))
