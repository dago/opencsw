# $Id$

import re
import os.path

def IsLibraryLinkable(file_path):
  linkable_re = re.compile(r"^opt/csw(/[\w\.]+)*/lib(/[\w\+]+)?$")
  file_dir, file_basename = os.path.split(file_path)
  return bool(linkable_re.match(file_dir))

def MakePackageNameBySoname(soname):
  """Find the package name based on the soname.

  Returns a pair of pkgname, catalogname.
  """
  soname_re = re.compile(r"(?P<basename>[\w-]+)\.so\.(?P<version>\d+)(\..*)?$")
  m = soname_re.match(soname)
  keywords = m.groupdict()
  pkgname_list = [
      "CSW%(basename)s%(version)s" % keywords,
      "CSW%(basename)s-%(version)s" % keywords,
  ]
  catalogname_list = [
      "%(basename)s%(version)s" % keywords,
      "%(basename)s-%(version)s" % keywords,
  ]
  return pkgname_list, catalogname_list


def GetSharedLibs(pkg_data):
  # Finding all shared libraries
  shared_libs = []
  for metadata in pkg_data["files_metadata"]:
    if "mime_type" in metadata and metadata["mime_type"]:
      # TODO: Find out where mime_type is missing and why
      if "sharedlib" in metadata["mime_type"]:
        shared_libs.append(metadata["path"])
  return shared_libs
