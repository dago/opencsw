#!/usr/bin/env python2.6

import datetime
import difflib
import hashlib
import logging
import os
import re
import shutil
import subprocess
import tempfile
import time

import configuration as c
import opencsw
import overrides
import shell
import pkgmap

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

class Error(Exception):
  pass


class PackageError(Error):
  pass

class StdoutSyntaxError(Error):
  pass

class CswSrv4File(shell.ShellMixin, object):
  """Represents a package in the srv4 format (pkg)."""

  def __init__(self, pkg_path, debug=False):
    super(CswSrv4File, self).__init__()
    logging.debug("CswSrv4File(%s, debug=%s)", repr(pkg_path), debug)
    self.pkg_path = pkg_path
    self.workdir = None
    self.gunzipped_path = None
    self.transformed = False
    self.dir_format_pkg = None
    self.debug = debug
    self.pkgname = None
    self.md5sum = None
    self.mtime = None
    self.stat = None

  def __repr__(self):
    return u"CswSrv4File(%s)" % repr(self.pkg_path)

  def GetWorkDir(self):
    if not self.workdir:
      self.workdir = tempfile.mkdtemp(prefix="pkg_")
      fd = open(os.path.join(self.workdir, "admin"), "w")
      fd.write(ADMIN_FILE_CONTENT)
      fd.close()
    return self.workdir

  def GetAdminFilePath(self):
    return os.path.join(self.GetWorkDir(), "admin")

  def GetGunzippedPath(self):
    if not self.gunzipped_path:
      gzip_suffix = ".gz"
      pkg_suffix = ".pkg"
      if self.pkg_path.endswith("%s%s" % (pkg_suffix, gzip_suffix)):
        # Causing the class to stat the .gz file.  This call throws away the
        # result, but the result will be cached as a object member.
        self.GetMtime()
        self.GetMd5sum()
        base_name_gz = os.path.split(self.pkg_path)[1]
        shutil.copy(self.pkg_path, self.GetWorkDir())
        self.pkg_path = os.path.join(self.GetWorkDir(), base_name_gz)
        args = ["gunzip", "-f", self.pkg_path]
        unused_retcode = self.ShellCommand(args)
        self.gunzipped_path = self.pkg_path[:(-len(gzip_suffix))]
      elif self.pkg_path.endswith(pkg_suffix):
        self.gunzipped_path = self.pkg_path
      else:
        raise Error("The file name should end in either "
                    "%s or %s, but it's %s."
                    % (gzip_suffix, pkg_suffix, repr(self.pkg_path)))
    return self.gunzipped_path

  def Pkgtrans(self, src_file, destdir, pkgname):
    """A proxy for the pkgtrans command.

    This requires custom-pkgtrans to be available.
    """
    if not os.path.isdir(destdir):
      raise PackageError("%s doesn't exist or is not a directory" % destdir)
    args = [os.path.join(os.path.dirname(__file__), "custom-pkgtrans"),
            src_file,
            destdir,
            pkgname ]
    pkgtrans_proc = subprocess.Popen(args,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
    stdout, stderr = pkgtrans_proc.communicate()
    ret = pkgtrans_proc.wait()
    if ret:
      logging.error(stdout)
      logging.error(stderr)
      logging.error("% has failed" % args)

  def GetPkgname(self):
    """It's necessary to figure out the pkgname from the .pkg file.
    # nawk 'NR == 2 {print $1; exit;} $f
    """
    if not self.pkgname:
      gunzipped_path = self.GetGunzippedPath()
      args = ["nawk", "NR == 2 {print $1; exit;}", gunzipped_path]
      nawk_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
      stdout, stderr = nawk_proc.communicate()
      ret_code = nawk_proc.wait()
      self.pkgname = stdout.strip()
      logging.debug("GetPkgname(): %s", repr(self.pkgname))
    return self.pkgname

  def _Stat(self):
    if not self.stat:
      self.stat = os.stat(self.pkg_path)
    return self.stat

  def GetMtime(self):
    if not self.mtime:
      s = self._Stat()
      t = time.gmtime(s.st_mtime)
      self.mtime = datetime.datetime(*t[:6])
    return self.mtime

  def GetSize(self):
    s = self._Stat()
    return s.st_size

  def TransformToDir(self):
    """Transforms the file to the directory format.

    This uses the Pkgtrans function at the top, because pkgtrans behaves
    differently on Solaris 8 and 10.  Having our own implementation helps
    achieve consistent behavior.
    """
    if not self.transformed:
      gunzipped_path = self.GetGunzippedPath()
      pkgname = self.GetPkgname()
      args = [os.path.join(os.path.dirname(__file__),
                           "..", "..", "bin", "custom-pkgtrans"),
              gunzipped_path, self.GetWorkDir(), pkgname]
      logging.debug("transforming: %s", args)
      unused_retcode = self.ShellCommand(args, quiet=(not self.debug))
      dirs = self.GetDirs()
      if len(dirs) != 1:
        raise Error("Need exactly one package in the package stream: "
                    "%s." % (dirs))
      self.dir_format_pkg = self.GetDirFormatClass()(dirs[0])
      self.transformed = True

  def GetDirFormatPkg(self):
    self.TransformToDir()
    return self.dir_format_pkg

  def GetDirs(self):
    paths = os.listdir(self.GetWorkDir())
    dirs = []
    for p in paths:
      abspath = os.path.join(self.GetWorkDir(), p)
      if os.path.isdir(abspath):
        dirs.append(abspath)
    return dirs

  def GetPkgmap(self, analyze_permissions, strip=None):
    dir_format_pkg = self.GetDirFormatPkg()
    return dir_format_pkg.GetPkgmap(analyze_permissions, strip)

  def GetMd5sum(self):
    if not self.md5sum:
      logging.debug("GetMd5sum() reading file %s", repr(self.pkg_path))
      fp = open(self.pkg_path)
      hash = hashlib.md5()
      hash.update(fp.read())
      fp.close()
      self.md5sum = hash.hexdigest()
    return self.md5sum

  def GetPkgchkOutput(self):
    """Returns: (exit code, stdout, stderr)."""
    args = ["/usr/sbin/pkgchk", "-d", self.GetGunzippedPath(), "all"]
    pkgchk_proc = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = pkgchk_proc.communicate()
    ret = pkgchk_proc.wait()
    return ret, stdout, stderr

  def __del__(self):
    if self.workdir:
      logging.debug("Removing %s", repr(self.workdir))
      shutil.rmtree(self.workdir)

  def GetDirFormatClass(self):
    # Derived classes can override this class member and use other classes for
    # the directory format package.
    return DirectoryFormatPackage


class DirectoryFormatPackage(shell.ShellMixin, object):
  """Represents a package in the directory format.

  Allows some read-write operations.
  """
  def __init__(self, directory):
    self.directory = directory
    self.pkgname = os.path.basename(directory)
    self.pkgpath = self.directory
    self.pkginfo_dict = None
    self.binaries = None
    self.file_paths = None
    self.files_metadata = None

  def __repr__(self):
    return u"<DirectoryFormatPackage directory=%s>" % repr(self.directory)

  def GetCatalogname(self):
    """Returns the catalog name of the package.

    A bit hacky.  Looks for the first word of the NAME field in the package.
    """
    pkginfo = self.GetParsedPkginfo()
    words = re.split(c.WS_RE, pkginfo["NAME"])
    return words[0]

  def GetParsedPkginfo(self):
    if not self.pkginfo_dict:
      pkginfo_fd = open(self.GetPkginfoFilename(), "r")
      self.pkginfo_dict = opencsw.ParsePkginfo(pkginfo_fd)
      pkginfo_fd.close()
    return self.pkginfo_dict

  def GetSrv4FileName(self):
    """Guesses the Srv4FileName based on the package directory contents."""
    return opencsw.PkginfoToSrv4Name(self.GetParsedPkginfo())

  def ToSrv4(self, target_dir, file_name=None):
    if not file_name:
      target_file_name = self.GetSrv4FileName()
    else:
      target_file_name = file_name
    target_path = os.path.join(target_dir, target_file_name)
    if os.path.exists(target_path):
      return target_path
    pkg_container_dir, pkg_dir = os.path.split(self.directory)
    if not os.path.isdir(target_dir):
      os.makedirs(target_dir)
    args = ["pkgtrans", "-s", pkg_container_dir, target_path, pkg_dir]
    self.ShellCommand(args, quiet=True)
    args = ["gzip", "-f", target_path]
    self.ShellCommand(args, quiet=True)
    return target_path

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

  def GetPkgmap(self, analyze_permissions=False, strip=None):
    fd = open(os.path.join(self.directory, "pkgmap"), "r")
    basedir = self.GetBasedir()
    return pkgmap.Pkgmap(fd, analyze_permissions, strip, basedir)

  def SetPkginfoEntry(self, key, value):
    pkginfo = self.GetParsedPkginfo()
    logging.debug("Setting %s to %s", repr(key), repr(value))
    pkginfo[key] = value
    self.WritePkginfo(pkginfo)
    pkgmap_path = os.path.join(self.directory, "pkgmap")
    pkgmap_fd = open(pkgmap_path, "r")
    new_pkgmap_lines = []
    pkginfo_re = re.compile("1 i pkginfo")
    ws_re = re.compile(r"\s+")
    for line in pkgmap_fd:
      if pkginfo_re.search(line):
        fields = ws_re.split(line)
        # 3: size
        # 4: sum
        pkginfo_path = os.path.join(self.directory, "pkginfo")
        args = ["cksum", pkginfo_path]
        cksum_process = subprocess.Popen(args, stdout=subprocess.PIPE)
        stdout, stderr = cksum_process.communicate()
        cksum_process.wait()
        size = ws_re.split(stdout)[1]
        args = ["sum", pkginfo_path]
        sum_process = subprocess.Popen(args, stdout=subprocess.PIPE)
        stdout, stderr = sum_process.communicate()
        sum_process.wait()
        sum_value = ws_re.split(stdout)[0]
        fields[3] = size
        fields[4] = sum_value
        logging.debug("New pkgmap line: %s", fields)
        line = " ".join(fields)
      new_pkgmap_lines.append(line.strip())
    pkgmap_fd.close()
    # Write that back
    pkgmap_path_new = pkgmap_path + ".new"
    logging.debug("Writing back to %s", pkgmap_path_new)
    pkgmap_fd = open(pkgmap_path_new, "w")
    pkgmap_fd.write("\n".join(new_pkgmap_lines))
    pkgmap_fd.close()
    shutil.move(pkgmap_path_new, pkgmap_path)

    # TODO(maciej): Need to update the relevant line on pkgmap too

  def GetPkginfoFilename(self):
    return os.path.join(self.directory, "pkginfo")

  def WritePkginfo(self, pkginfo_dict):
    # Some packages extract read-only. To be sure, change them to be
    # user-writable.
    args = ["chmod", "-R", "u+w", self.directory]
    self.ShellCommand(args)
    pkginfo_filename = self.GetPkginfoFilename()
    os.chmod(pkginfo_filename, 0644)
    pkginfo_fd = open(pkginfo_filename, "w")
    pkginfo_dict = self.GetParsedPkginfo()
    for k, v in pkginfo_dict.items():
      pkginfo_fd.write("%s=%s\n" % (k, pkginfo_dict[k]))
    pkginfo_fd.close()

  def ResetNameProperty(self):
    """Sometimes, NAME= contains useless data. This method resets them."""
    pkginfo_dict = self.GetParsedPkginfo()
    catalog_name = opencsw.PkgnameToCatName(pkginfo_dict["PKG"])
    description = pkginfo_dict["DESC"]
    pkginfo_name = "%s - %s" % (catalog_name, description)
    self.SetPkginfoEntry("NAME", pkginfo_name)

  def CheckPkgpathExists(self):
    if not os.path.isdir(self.directory):
      raise PackageError("%s does not exist or is not a directory"
                         % self.directory)

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
    overrides = []
    catalogname = self.GetCatalogname()
    override_paths = (
        [self.directory,
         "root",
         "opt/csw/share/checkpkg/overrides", catalogname],
        [self.directory,
         "install",
         "checkpkg_override"],
    )
    for override_path in override_paths:
      file_path = os.path.join(*override_path)
      stream = self._GetOverridesStream(file_path)
      if stream:
        overrides.extend(self._ParseOverridesStream(stream))
    return overrides

  def GetFileContent(self, pkg_file_path):
    if pkg_file_path.startswith("/"):
      pkg_file_path = pkg_file_path[1:]
    # TODO: Write a unit test for the right path
    file_path = os.path.join(self.directory, "root", pkg_file_path)
    try:
      fd = open(file_path, "r")
      content = fd.read()
      fd.close()
      return content
    except IOError, e:
      raise PackageError(e)

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

  def MakeAbsolutePath(self, p):
    return os.path.join(self.pkgpath, p)


class PackageComparator(object):

  def __init__(self, file_name_a, file_name_b,
               permissions=False,
               strip_a=None,
               strip_b=None):
    self.analyze_permissions = permissions
    self.pkg_a = CswSrv4File(file_name_a)
    self.pkg_b = CswSrv4File(file_name_b)
    self.strip_a = strip_a
    self.strip_b = strip_b

  def Run(self):
    pkgmap_a = self.pkg_a.GetPkgmap(self.analyze_permissions, strip=self.strip_a)
    pkgmap_b = self.pkg_b.GetPkgmap(self.analyze_permissions, strip=self.strip_b)
    diff_ab = difflib.unified_diff(sorted(pkgmap_a.paths),
                                   sorted(pkgmap_b.paths),
                                   fromfile=self.pkg_a.pkg_path,
                                   tofile=self.pkg_b.pkg_path)
    diff_text = "\n".join(x.strip() for x in diff_ab)
    if diff_text:
      less_proc = subprocess.Popen(["less"], stdin=subprocess.PIPE)
      less_stdout, less_stderr = less_proc.communicate(input=diff_text)
      less_proc.wait()
    else:
      print "No differences found."


class PackageSurgeon(shell.ShellMixin):
  """Takes an OpenCSW gzipped package and performs surgery on it.

  Sows it up, adjusts checksums, and puts it back together.
  """

  def __init__(self, pkg_path, debug):
    self.debug = debug
    self.pkg_path = pkg_path
    self.srv4 = CswSrv4File(pkg_path)
    self.dir_pkg = None
    self.exported_dir = None
    self.parsed_filename = opencsw.ParsePackageFileName(self.pkg_path)

  def Transform(self):
    if not self.dir_pkg:
      self.dir_pkg = self.srv4.GetDirFormatPkg()
      logging.debug(repr(self.dir_pkg))
      # subprocess.call(["tree", self.dir_pkg.directory])

  def Export(self, dest_dir):
    self.Transform()
    if not self.exported_dir:
      basedir, pkgname = os.path.split(self.dir_pkg.directory)
      self.exported_dir = os.path.join(dest_dir, pkgname)
      shutil.copytree(
          self.dir_pkg.directory,
          self.exported_dir)
      subprocess.call(["git", "init"], cwd=self.exported_dir)
      subprocess.call(["git", "add", "."], cwd=self.exported_dir)
      subprocess.call(["git", "commit", "-a", "-m", "Initial commit"],
                      cwd=self.exported_dir)
    else:
      logging.warn("The package was already exported to %s",
                   self.exported_dir)

  def Patch(self, patch_file):
    self.Transform()
    args = ["gpatch", "-p", "1", "-d", self.dir_pkg.directory, "-i", patch_file]
    logging.debug(args)
    subprocess.call(args)

  def ToSrv4(self, dest_dir):
    self.Transform()
    pkginfo = self.dir_pkg.GetParsedPkginfo()
    date_str = datetime.datetime.now().strftime("%Y.%m.%d")
    self.parsed_filename["revision_info"]["REV"] = date_str
    new_filename = opencsw.ComposePackageFileName(self.parsed_filename)
    # Plan:
    # - Update the version in the pkginfo
    version_string = opencsw.ComposeVersionString(
        self.parsed_filename["version"],
        self.parsed_filename["revision_info"])
    logging.debug("New version string: %s", repr(version_string))
    self.dir_pkg.SetPkginfoEntry("VERSION", version_string)
    # - Update the pkgmap file, setting the checksums
    # - Transform it back to the srv4 form
    target_dir, old_path = os.path.split(self.pkg_path)
    logging.debug("Transforming into %s", new_filename)
    self.dir_pkg.ToSrv4(target_dir, new_filename)
    # - Update the pkgmap file, setting the checksums
    # - Transform it back to the srv4 form
    target_dir, old_path = os.path.split(self.pkg_path)
    logging.debug("Transforming into %s", new_filename)
    self.dir_pkg.ToSrv4(target_dir, new_filename)
