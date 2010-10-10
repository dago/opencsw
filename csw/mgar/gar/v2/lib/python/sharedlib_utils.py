# $Id$

import re
import os.path

SPARCV8_PATHS = ('sparcv8', 'sparcv8-fsmuld',
                 'sparcv7', 'sparc')
SPARCV8PLUS_PATHS = ('sparcv8plus+vis2', 'sparcv8plus+vis', 'sparcv8plus')
SPARCV9_PATHS = ('sparcv9+vis2', 'sparcv9+vis', 'sparcv9')
INTEL_386_PATHS = ('pentium_pro+mmx', 'pentium_pro',
                   'pentium+mmx', 'pentium',
                   'i486', 'i386', 'i86')
AMD64_PATHS = ('amd64',)
LEGIT_CHAR_RE = re.compile(r"[a-zA-Z0-9\+]+")

class SonameParsingException(Exception):
  pass

def IsLibraryLinkable(file_path):
  arch_subdirs = (SPARCV8_PATHS + SPARCV8PLUS_PATHS + SPARCV9_PATHS
                  + INTEL_386_PATHS + AMD64_PATHS)
  # Need to escape the plus signs because of the regex usage below.
  arch_subdirs = [x.replace(r"+", r"\+") for x in arch_subdirs]
  linkable_re = re.compile(r"^opt/csw(/([^\/]+(?!lib)))*/lib(/(%s))?$"
                           % "|".join(arch_subdirs))
  file_dir, file_basename = os.path.split(file_path)
  return bool(linkable_re.match(file_dir))


def SanitizeWithChar(s, c):
  parts = LEGIT_CHAR_RE.findall(s)
  if "so" in parts:
    parts.remove("so")
  return c.join(parts).lower()


def MakePackageNameBySoname(soname):
  """Find the package name based on the soname.

  Returns a pair of pkgname, catalogname.
  """
  soname_re = re.compile(r"(?P<basename>[\w\+]+([\.\-]+[\w\+]+)*)"
                         r"\.so"
                         r"(\.(?P<version>\d+)(\..*)?)?"
                         r"$")
  m = soname_re.match(soname)
  if not m:
    # There was no ".so" component, so it's hardo to figure out which one is
    # the name, but we'll try to figure out the numeric part of the soname.
    digits = "".join(re.findall(r"[0-9]+", soname))
    alnum = "".join(re.findall(r"[a-zA-Z]+", soname))
    parsed = {
        "basename": alnum,
        "version": digits,
    }
  else:
    parsed = m.groupdict()
  keywords_pkgname = {}
  keywords_catalogname = {}
  for key in parsed:
    if parsed[key]:
      keywords_pkgname[key] = SanitizeWithChar(parsed[key], "-")
      keywords_catalogname[key] = SanitizeWithChar(parsed[key], "_")
    else:
      keywords_pkgname[key] = ""
      keywords_catalogname[key] = ""
  pkgname_list = [
      "CSW%(basename)s%(version)s" % keywords_pkgname,
  ]
  catalogname_list = [
      "%(basename)s%(version)s" % keywords_catalogname,
  ]
  if keywords_pkgname["version"]:
    catalogname_list.append(
      "%(basename)s_%(version)s" % keywords_catalogname)
    pkgname_list.append(
      "CSW%(basename)s-%(version)s" % keywords_pkgname)
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
