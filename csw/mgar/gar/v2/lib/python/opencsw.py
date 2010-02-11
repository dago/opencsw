#!/opt/csw/bin/python2.6
# coding=utf-8
#
# $Id$
#
# vim:set sw=2 ts=2 sts=2 expandtab:
#
# Copyright (c) 2009 OpenCSW
# Author: Maciej Bliziński
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.

import copy
import datetime
import difflib
import logging
import os
import os.path
import re
import shutil
import subprocess
import tempfile
import urllib2
import checkpkg

ARCHITECTURES = ["i386", "sparc", "all"]
MAJOR_VERSION = "major version"
MINOR_VERSION = "minor version"
PATCHLEVEL = "patchlevel"
REVISION = "revision"
OTHER_VERSION_INFO = "other version info"
NEW_PACKAGE = "new package"
NO_VERSION_CHANGE = "no version change"
REVISION_ADDED = "revision number added"
PKG_URL_TMPL = "http://www.opencsw.org/packages/%s"
CATALOG_URL = "http://mirror.opencsw.org/opencsw/current/i386/5.10/catalog"
WS_RE = re.compile(r"\s+")

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

EMAIL_TMPL = """From: %(from)s
To: %(to)s
Cc: %(cc)s
Date: %(date)s
Subject: newpkgs %(pkgnames)s

%(body)s

-- 
$Id$
"""


class Error(Exception):
  pass


class PackageError(Error):
  pass


def ParsePackageFileName(p):
  bits = p.split("-")
  catalogname = bits[0]
  version, version_info, revision_info = ParseVersionString(bits[1])
  data = {
      'catalogname': catalogname,
      'full_version_string': bits[1],
      'version': version,
      'version_info': version_info,
      'revision_info': revision_info,
  }
  return data

def ParseVersionString(s):
  version_bits = re.split("_|,", s)
  version_str = version_bits[0]
  revision_bits = version_bits[1:]
  revision_info = {}
  version_info = {}
  version_number_bits = version_str.split(".")
  version_info[MAJOR_VERSION] = version_number_bits[0]
  if len(version_number_bits) >= 2:
    version_info[MINOR_VERSION] = version_number_bits[1]
  if len(version_number_bits) >= 3:
    version_info[PATCHLEVEL] = version_number_bits[2]
  for version_bit in revision_bits:
    if "=" in version_bit:
      (var_name, var_value) = version_bit.split("=")
      revision_info[var_name] = var_value
    else:
      if not "extra_strings" in revision_info:
        revision_info["extra_strings"] = []
      revision_info["extra_strings"].append(version_bit)
  return version_str, version_info, revision_info


def IndexDictsBy(list_of_dicts, field_key):
  """Creates an index of list of dictionaries by a field name.

  Returns a dictionary of lists.
  """
  index = {}
  for d in list_of_dicts:
    if d[field_key] not in index:
      index[d[field_key]] = []
    index[d[field_key]].append(d)
  return index


class CatalogBasedOpencswPackage(object):

  catalog_downloaded = False

  def __init__(self, catalogname):
    self.catalogname = catalogname

  def IsOnTheWeb(self):
    url = PKG_URL_TMPL % self.catalogname
    logging.debug("Opening %s", repr(url))
    package_page = urllib2.urlopen(url)
    html = package_page.read()
    # Since beautifulsoup is not installed on the buildfarm yet, a quirk in
    # package page display is going to be used.
    package_not_in_mantis_pattern = u"cannot find maintainer"
    return html.find(package_not_in_mantis_pattern) >= 0

  def IsNew(self):
    return not self.IsOnTheWeb()

  def UpgradeType(self, new_version_string):
    """What kind of upgrade would it be if the new version was X.

    This function contains ugly logic.  It has many unit tests to prove that it
    does the right thing.

    Args:
      New (candidate) version string

    Returns:
      Revision type, message, (old_data, new_data)
    """
    (new_version,
     new_version_info,
     new_revision_info) = ParseVersionString(new_version_string)
    catalog_data = self.GetCatalogPkgData()
    if not catalog_data:
      return (NEW_PACKAGE,
              "/dev/null -> %s" % new_version_string,
              (None, new_version_string))
    cat_version_info = catalog_data["version_info"]
    levels = (MAJOR_VERSION, MINOR_VERSION, PATCHLEVEL)
    for level in levels:
      if level in cat_version_info and level in new_version_info:
        if (cat_version_info[level] != new_version_info[level]):
          versions = (catalog_data["full_version_string"], new_version_string)
          msg = "%s --> %s" % versions
          return level, msg, versions
    cat_rev_info = catalog_data["revision_info"]
    for rev_kw in new_revision_info:
      if rev_kw in cat_rev_info:
        if cat_rev_info[rev_kw] != new_revision_info[rev_kw]:
          msg = "%s: %s --> %s" % (rev_kw,
                                   cat_rev_info[rev_kw],
                                   new_revision_info[rev_kw])
          versions = cat_rev_info[rev_kw], new_revision_info[rev_kw]
          return REVISION, msg, versions
      else:
        # This revision info is missing from the old package
        msg = "new tag %s: %s" % (repr(rev_kw),
                                  new_revision_info[rev_kw])
        return REVISION_ADDED, msg, (None, new_revision_info[rev_kw])
    if (catalog_data["version"] == new_version
            and
        catalog_data["revision_info"] == new_revision_info):
      return NO_VERSION_CHANGE, "no", (new_version, new_version)
    return OTHER_VERSION_INFO, "other", (None, None)

  @classmethod
  def LazyDownloadCatalogData(cls, catalog_source=None):
    if not cls.catalog_downloaded:
      cls.DownloadCatalogData(catalog_source)
      cls.catalog_downloaded = True

  @classmethod
  def DownloadCatalogData(cls, catalog_source):
    """Downloads catalog data."""
    logging.debug("Downloading catalog data from %s.", repr(CATALOG_URL))
    if not catalog_source:
      catalog_source = urllib2.urlopen(CATALOG_URL)
    cls.catalog = {}
    for line in catalog_source:
      # Working around the GPG signature
      if line.startswith("#"): continue
      if "BEGIN PGP SIGNED MESSAGE" in line: continue 
      if line.startswith("Hash:"): continue
      if len(line.strip()) <= 0: continue 
      if "BEGIN PGP SIGNATURE" in line: break
      fields = re.split(r"\s+", line)
      try:
        cls.catalog[fields[0]] = ParsePackageFileName(fields[3])
      except IndexError, e:
        print repr(line)
        print fields
        print e
        raise

  @classmethod
  def _GetCatalogPkgData(cls, catalogname):
    cls.LazyDownloadCatalogData()
    if catalogname in cls.catalog:
      return cls.catalog[catalogname]
    else:
      return None

  def GetCatalogPkgData(self):
    """A wrapper for the classmethod _GetCatalogPkgData, supplying the catalogname."""
    return self._GetCatalogPkgData(self.catalogname)


class StagingDir(object):
  """Represents a staging directory."""

  def __init__(self, dir_path):
    self.dir_path = dir_path

  def GetLatest(self, software, architectures=ARCHITECTURES):
    files = os.listdir(self.dir_path)
    package_files = []
    for a in architectures:
      relevant_pkgs = sorted(shutil.fnmatch.filter(files,
                                                   "*-%s-*.pkg.gz" % a))
      relevant_pkgs = sorted(shutil.fnmatch.filter(relevant_pkgs,
                                                   "%s-*.pkg.gz" % software))
      if relevant_pkgs:
        package_files.append(relevant_pkgs[-1])
    if not package_files:
      raise PackageError("Could not find %s in %s" % (software, self.dir_path))
    logging.debug("The latest packages %s in %s are %s",
                  repr(software),
                  repr(self.dir_path),
                  repr(package_files))
    return [os.path.join(self.dir_path, x) for x in package_files]


class NewpkgMailer(object):

  def __init__(self, pkgnames, paths,
               release_mgr_name,
               release_mgr_email,
               sender_name,
               sender_email,
               release_cc):
    self.sender = u"%s <%s>" % (sender_name, sender_email)
    self.pkgnames = pkgnames
    self.paths = paths
    self.release_mgr = u"%s <%s>" % (release_mgr_name, release_mgr_email)
    self.release_cc = u"%s" % release_cc

  def FormatMail(self):
    body_list = ["The following package files are ready to be released:"]
    body_list.append("")
    # Gathering package information, grouping packages that are upgraded
    # together.
    pkgs_data = {}
    for p in self.paths:
      base_file_name = os.path.split(p)[1]
      catalogname = base_file_name.split("-")[0]
      pkg = CatalogBasedOpencswPackage(catalogname)
      new_data = ParsePackageFileName(base_file_name)
      new_version_str = new_data["full_version_string"]
      catalog_data = pkg.GetCatalogPkgData()
      if catalog_data:
        catalog_version_str = catalog_data["full_version_string"]
      else:
        catalog_version_str = "package not in the catalog"
      upgrade_type, upgrade_msg, versions = pkg.UpgradeType(new_version_str)
      pkgs_data_key = (upgrade_type, upgrade_msg, versions)
      if pkgs_data_key not in pkgs_data:
        pkgs_data[pkgs_data_key] = []
      pkg.srv4path = p
      pkg.cat_version_str = catalog_version_str
      pkg.new_version_str = new_version_str
      pkgs_data[pkgs_data_key].append(pkg)
    # Formatting grouped packages:
    for upgrade_type, upgrade_msg, versions in pkgs_data:
      msg = []
      pkgs = pkgs_data[(upgrade_type, upgrade_msg, versions)]
      group_name = CatalogNameGroupName([pkg.catalogname for pkg in pkgs])
      if upgrade_type == NEW_PACKAGE:
        msg.append("* %s: %s" % (upgrade_type, group_name))
      elif upgrade_type == NO_VERSION_CHANGE:
        msg.append("* WARNING: no version change of %s" % group_name)
      else:
        msg.append("* %s: %s upgrade" % (group_name, upgrade_type))
        msg.append("  - from: %s" % versions[0])
        msg.append("  -   to: %s" % versions[1])
      for pkg in pkgs:
        msg.append("  + %s" % os.path.split(pkg.srv4path)[1])
      body_list.extend(msg)
    body_list.append("")
    body = "\n".join(body_list)
    d = {
        'from': self.sender,
        'to': self.release_mgr,
        'cc': self.release_cc,
        'pkgnames': ", ".join(self.pkgnames),
        'body': body,
        'date': datetime.datetime.now(),
    }
    mail_text = EMAIL_TMPL % d
    return mail_text

  def GetEditorName(self, env):
    editor = "/opt/csw/bin/vim"
    if "EDITOR" in env:
      editor = env["EDITOR"]
    if "VISUAL" in env:
      editor = env["VISUAL"]
    return editor


class ShellMixin(object):

  def ShellCommand(self, args, quiet=False):
    logging.debug("Calling: %s", repr(args))
    if quiet:
      sub_stdout = subprocess.PIPE
      sub_stderr = subprocess.PIPE
    else:
      sub_stdout = None
      sub_stderr = None
    retcode = subprocess.call(args,
                              stdout=sub_stdout,
                              stderr=sub_stderr)
    if retcode:
      raise Error("Running %s has failed." % repr(args))
    return retcode


class CswSrv4File(ShellMixin, object):
  """Represents a package in the srv4 format (pkg)."""

  def __init__(self, pkg_path):
    self.pkg_path = pkg_path
    self.workdir = None
    self.gunzipped_path = None
    self.transformed = False
    self.dir_format_pkg = None

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
    gzip_suffix = ".gz"
    pkg_suffix = ".pkg"
    if not self.gunzipped_path:
      if self.pkg_path.endswith("%s%s" % (pkg_suffix, gzip_suffix)):
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
                    "%s or %s." % (gzip_suffix, pkg_suffix))
    return self.gunzipped_path

  def TransformToDir(self):
    if not self.transformed:
      args = ["pkgtrans", "-a", self.GetAdminFilePath(),
              self.GetGunzippedPath(), self.GetWorkDir(), "all"]
      unused_retcode = self.ShellCommand(args, quiet=True)
      dirs = self.GetDirs()
      if len(dirs) != 1:
        raise Error("Need exactly one package in the package stream: "
                    "%s." % (dirs))
      self.dir_format_pkg = DirectoryFormatPackage(dirs[0])
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

  def __del__(self):
    if self.workdir:
      logging.debug("Removing %s", repr(self.workdir))
      shutil.rmtree(self.workdir)


def ParsePkginfo(lines):
  """Parses a pkginfo data."""
  d = {}
  for line in lines:
    try:
      # Can't use split, because there might be multiple '=' characters.
      line = line.strip()
      # Skip empty and commented lines
      if not line: continue
      if line.startswith("#"): continue
      var_name, var_value = line.split("=", 1)
      d[var_name] = var_value
    except ValueError, e:
      raise PackageError("Can't parse %s: %s" % (repr(line), e))
  return d


def PkgnameToCatName(pkgname):
  """Creates a catalog name based on the pkgname.

  SUNWbash  --> sunw_bash
  SUNWbashS --> sunw_bash_s
  SUNWPython --> sunw_python

  Incomprehensible, but unit tested!
  """
  known_prefixes = ["SUNW", "FJSV", "CSW"]
  for prefix in known_prefixes:
    if pkgname.startswith(prefix):
      unused, tmp_prefix, the_rest = pkgname.partition(prefix)
      pkgname = tmp_prefix + "_" + the_rest
  return "_".join(SplitByCase(pkgname))


def SplitByCase(s):
  def CharType(c):
    if c.isalnum():
      if c.isupper():
        return 1
      else:
        return 2
    else:
      return 3
  chartype_list = [CharType(x) for x in s]
  neighbors = zip(chartype_list, chartype_list[1:])
  casechange = [False] + [x != y for x, y in neighbors]
  str_list = [(cc * "_") + l.lower() for l, cc in zip(s, casechange)]
  s2 = "".join(str_list)
  return re.findall(r"[a-z]+", s2)


def CatalogNameGroupName(catalogname_list):
  """Uses heuristics to guess the common name of a group of packages."""
  catalogname_list = copy.copy(catalogname_list)
  if len(catalogname_list) == 1:
    return catalogname_list[0]
  current_substring = catalogname_list.pop()
  while catalogname_list and current_substring:
    substring_set = LongestCommonSubstring(current_substring,
                                           catalogname_list.pop())
    if substring_set:
      current_substring = list(substring_set)[0]
  if len(current_substring) >= 2:
    return current_substring
  return "various packages"


def LongestCommonSubstring(S, T):
  """Stolen from Wikibooks

  http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python"""
  m = len(S); n = len(T)
  L = [[0] * (n+1) for i in xrange(m+1)]
  LCS = set()
  longest = 0
  for i in xrange(m):
    for j in xrange(n):
      if S[i] == T[j]:
        v = L[i][j] + 1
        L[i+1][j+1] = v
        if v > longest:
          longest = v
          LCS = set()
        if v == longest:
          LCS.add(S[i-v+1:i+1])
  return LCS


def PkginfoToSrv4Name(pkginfo_dict):
  SRV4_FN_TMPL = "%(catalog_name)s-%(version)s-%(osver)s-%(arch)s-%(tag)s.pkg"
  fn_data = {}
  fn_data["catalog_name"] = PkgnameToCatName(pkginfo_dict["PKG"])
  fn_data["version"] = pkginfo_dict["VERSION"]
  # os_version = pkginfo_dict["SUNW_PRODVERS"].split("/", 1)[0]
  # fn_data["osver"] = pkginfo_dict["SUNW_PRODNAME"] + os_version
  fn_data["osver"] = "SunOS5.10" # Hardcoded, because the original data contains
                                 # trash.
  fn_data["arch"] = pkginfo_dict["ARCH"]
  fn_data["tag"] = "SUNW"
  return SRV4_FN_TMPL % fn_data


class DirectoryFormatPackage(ShellMixin, object):

  def __init__(self, directory):
    self.directory = directory
    self.pkgname = os.path.split(directory)[1]
    self.pkgpath = self.directory
    self.pkginfo_dict = None

  def GetCatalogname(self):
    """Returns the catalog name of the package.

    A bit hacky.  Looks for the first word of the NAME field in the package.
    """
    pkginfo = self.GetParsedPkginfo()
    words = re.split(WS_RE, pkginfo["NAME"])
    return words[0]

  def GetParsedPkginfo(self):
    if not self.pkginfo_dict:
      pkginfo_fd = open(self.GetPkginfoFilename(), "r")
      self.pkginfo_dict = ParsePkginfo(pkginfo_fd)
      pkginfo_fd.close()
    return self.pkginfo_dict

  def GetSrv4FileName(self):
    """Guesses the Srv4FileName based on the package directory contents."""
    return PkginfoToSrv4Name(self.GetParsedPkginfo())

  def ToSrv4(self, target_dir):
    target_file_name = self.GetSrv4FileName()
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

  def GetPkgmap(self, analyze_permissions=False, strip=None):
    fd = open(os.path.join(self.directory, "pkgmap"), "r")
    return Pkgmap(fd, analyze_permissions, strip)

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
    catalog_name = PkgnameToCatName(pkginfo_dict["PKG"])
    description = pkginfo_dict["DESC"]
    pkginfo_name = "%s - %s" % (catalog_name, description)
    self.SetPkginfoEntry("NAME", pkginfo_name)

  def GetDependencies(self):
    fd = open(os.path.join(self.directory, "install", "depend"), "r")
    depends = {}
    for line in fd:
      fields = re.split(WS_RE, line)
      if fields[0] == "P":
        depends[fields[1]] = " ".join(fields[1:])
    fd.close()
    return depends

  def CheckPkgpathExists(self):
    if not os.path.isdir(self.directory):
      raise PackageError("%s does not exist or is not a directory"
                         % self.directory)

  def ListBinaries(self):
    """Shells out to list all the binaries from a given package.

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
    """
    self.CheckPkgpathExists()
    find_tmpl = "find '%s' -print | xargs file | grep ELF | nawk -F: '{print $1}'"
    find_proc = subprocess.Popen(find_tmpl % self.directory,
                                 shell=True,
                                 stdout=subprocess.PIPE)
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

  def _GetOverridesStream(self):
    catalogname = self.GetCatalogname()
    file_path = os.path.join(self.directory,
                             "root",
                             "opt/csw/share/checkpkg/overrides",
                             catalogname)
    # This might potentially cause a file descriptor leak, but I'm not going to
    # worry about that at this stage.
    logging.debug("Trying to open %s", repr(file_path))
    if os.path.isfile(file_path):
    	return open(file_path, "r")
    else:
    	return None

  def _ParseOverridesStream(self, stream):
    overrides = []
    for line in stream:
      if line.startswith("#"):
      	continue
      overrides.append(checkpkg.ParseOverrideLine(line))
    return overrides

  def GetOverrides(self):
    """Returns overrides, a list of checkpkg.Override instances."""
    stream = self._GetOverridesStream()
    if stream:
    	return self._ParseOverridesStream(stream)
    else:
    	return list()

  def GetFileContent(self, pkg_file_path):
    if pkg_file_path.startswith("/"):
      pkg_file_path = pkg_file_path[1:]
    file_path = os.path.join(self.directory, "root", pkg_file_path)
    fd = open(file_path, "r")
    content = fd.read()
    fd.close()
    return content


class Pkgmap(object):
  """Represents the pkgmap of the package.

  The plan:

    entries = [
      {
        'path': ...,
        'class': ...,
        (more fields?)
      }, ...
    ]

  + indexes
  """
  ENTRY_TYPES = {
      "1": "header (?)",
      "d": "directory",
      "f": "file",
      "s": "symlink",
      "l": "link",
      "i": "script",
  }

  def __init__(self, input, permissions=False,
               strip=None):
    self.paths = set()
    self.analyze_permissions = permissions
    self.entries = []
    self.classes = None
    for line in input:
      fields = re.split(r'\s+', line)
      if strip:
        strip_re = re.compile(r"^%s" % strip)
        fields = [re.sub(strip_re, "", x) for x in fields]
      logging.debug(fields)
      line_to_add = None
      installed_path = None
      prototype_class = None
      line_type = fields[1]
      mode = None
      user = None
      group = None
      if len(fields) < 2:
        continue
      elif line_type in ('f', 'd'):
        # Files and directories
        line_to_add = fields[3]
        installed_path = fields[3]
        prototype_class = fields[2]
        if self.analyze_permissions:
          line_to_add += " %s" % fields[4]
        mode, user, group = fields[4:7]
      elif line_type in ('s', 'l'):
        # soft- and hardlinks
        link_from, link_to = fields[3].split("=")
        installed_path = link_from
        line_to_add = "%s --> %s" % (link_from, link_to)
        prototype_class = fields[2]
      if line_to_add:
        self.paths.add(line_to_add)
      entry = {
          "line": line,
          "type": line_type,
      }
      entry["path"] = installed_path
      entry["class"] = prototype_class
      entry["mode"] = mode
      entry["user"] = user
      entry["group"] = group
      self.entries.append(entry)
    self.entries_by_line = IndexDictsBy(self.entries, "line")
    self.entries_by_type = IndexDictsBy(self.entries, "type")
    self.entries_by_class = IndexDictsBy(self.entries, "class")
    self.entries_by_path = IndexDictsBy(self.entries, "path")

  def GetClasses(self):
    """The assumtion is that the set of classes never changes."""
    if not self.classes:
      self.classes = set()
      for entry in self.entries:
        if entry["class"]:  # might be None
          self.classes.add(entry["class"])
    return self.classes


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
    diff_text = "\n".join(diff_ab)
    if diff_text:
      less_proc = subprocess.Popen(["less"], stdin=subprocess.PIPE)
      less_stdout, less_stderr = less_proc.communicate(input=diff_text)
      less_proc.wait()
    else:
      print "No differences found."


class OpencswCatalogBuilder(object):

  def __init__(self, product_dir, catalog_dir):
    self.product_dir = product_dir
    self.catalog_dir = catalog_dir

  def Run(self):
    pkg_dirs = os.listdir(self.product_dir)
    for pkg_dir in pkg_dirs:
      pkg_path = os.path.join(self.product_dir, pkg_dir)
      pkginfo_path = os.path.join(pkg_path, "pkginfo")
      if (os.path.isdir(pkg_path)
            and
          os.path.exists(pkginfo_path)):
        if not self.Srv4Exists(pkg_path):
          pkg = None
          tmpdir = None
          try:
            tmpdir = tempfile.mkdtemp(prefix="sunw-pkg-")
            logging.debug("Copying %s to %s", repr(pkg_path), repr(tmpdir))
            tmp_pkg_dir = os.path.join(tmpdir, pkg_dir)
            shutil.copytree(pkg_path, tmp_pkg_dir, symlinks=True)
            pkg = DirectoryFormatPackage(tmp_pkg_dir)
            # Replacing NAME= in the pkginfo, setting it to the catalog name.
            pkg.ResetNameProperty()
            pkg.ToSrv4(self.catalog_dir)
          except IOError, e:
            logging.warn("%s has failed: %s", pkg_path, e)
          finally:
            if pkg:
              del(pkg)
            if os.path.exists(tmpdir):
              shutil.rmtree(tmpdir)
        else:
          logging.warn("srv4 file for %s already exists, skipping", pkg_path)
      else:
        logging.warn("%s is not a directory.", pkg_path)

  def Srv4Exists(self, pkg_dir):
    pkg = DirectoryFormatPackage(pkg_dir)
    srv4_name = pkg.GetSrv4FileName()
    srv4_name += ".gz"
    srv4_path = os.path.join(self.catalog_dir, srv4_name)
    result = os.path.exists(srv4_path)
    logging.debug("Srv4Exists(%s) => %s, %s", pkg_dir, repr(srv4_path), result)
    return result
