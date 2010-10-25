# $Id$

import copy
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
SONAME_VERSION_RE = re.compile("^(?P<name>.*)\.so\.(?P<version>[\d\.]+)$")


class SonameParsingException(Exception):
  pass


def IsLibraryLinkable(file_path):
  arch_subdirs = (SPARCV8_PATHS + SPARCV8PLUS_PATHS + SPARCV9_PATHS
                  + INTEL_386_PATHS + AMD64_PATHS)
  # Need to escape the plus signs because of the regex usage below.
  arch_subdirs = [x.replace(r"+", r"\+") for x in arch_subdirs]
  linkable_re = re.compile(r"^opt/csw/lib(/(%s))?$"
                           % "|".join(arch_subdirs))
  blacklist = [
      # If it has two lib components, it's a private lib.
      re.compile(r"^opt/csw/.*lib.*lib.*"),
      re.compile(r"^opt/csw/share.*lib.*"),
  ]
  file_dir, file_basename = os.path.split(file_path)
  if linkable_re.match(file_dir):
    for regex in blacklist:
      if regex.match(file_dir):
        return False
    return True
  return False


def SonameToStringWithChar(s, c):
  """Sanitization function tailored at package names.

  It only inserts separators where digits of letters would be jammed
  togeher.  For example, foo-0 becomes foo0, but foo-0-0 becomes foo0-0."""
  def CharType(mychar):
    if mychar.isalpha():
      return "alpha"
    elif mychar.isdigit():
      return "digit"
    else:
      return "unknown"
  parts = LEGIT_CHAR_RE.findall(s)
  if "so" in parts:
    parts.remove("so")
  prev_type = "unknown"
  new_parts = []
  for part in parts:
    first_type = CharType(part[0])
    need_sep = False
    if (first_type == prev_type
        and
        (prev_type == "digit" or prev_type == "alpha")):
      need_sep = True
    if need_sep:
      new_parts.append(c)
    new_parts.append(part)
    prev_type = first_type
  return "".join(new_parts).lower()


def SanitizeWithChar(s, c):
  """Generic string sanitization function."""
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
                         r"(\.(?P<version>[\d\.]+))?"
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
      keywords_pkgname[key] = SonameToStringWithChar(parsed[key], "-")
      keywords_catalogname[key] = SonameToStringWithChar(parsed[key], "_")
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


def GetCommonVersion(sonames):
  versions = []
  for soname in sonames:
    m = SONAME_VERSION_RE.search(soname)
    if m:
      versions.append(m.groupdict()["version"])
    else:
      versions.append("")
  versions_set = set(versions)
  if len(versions_set) > 1 or not versions_set:
    return (False, None)
  else:
    return (True, versions_set.pop())


def MakePackageNameBySonameCollection(sonames):
  """Finds a name for a collection of sonames.

  Try to find the largest common prefix in the sonames, and establish
  whether there is a common version to them.
  """
  common_version_exists, common_version = GetCommonVersion(sonames)
  if not common_version_exists:
    # If the sonames don't have a common version, they shouldn't be together
    # in one package.
    return None
  common_substring_candidates = []
  for soname in sonames:
    candidate = soname
    # We always want such package to start with the prefix "lib".  Therefore,
    # we're stripping the prefix "lib" if it exists, and we're adding it back
    # to the pkgname and soname at the end of the function.
    if candidate.startswith("lib"):
      candidate = candidate[3:]
    m = re.search("\.so", candidate)
    candidate = re.sub("\.so.*$", "", candidate)
    common_substring_candidates.append(candidate)
  lcs = CollectionLongestCommonSubstring(copy.copy(common_substring_candidates))
  pkgnames = [
      "CSW" + SonameToStringWithChar("lib%s%s" % (lcs, common_version), "-"),
  ]
  dashed = "CSW" + SonameToStringWithChar("lib%s-%s" % (lcs, common_version), "-")
  if dashed not in pkgnames:
    pkgnames.append(dashed)
  catalognames = [
      SonameToStringWithChar("lib%s%s" % (lcs, common_version), "_"),
  ]
  underscored = SonameToStringWithChar("lib%s_%s" % (lcs, common_version), "_")
  if underscored not in catalognames:
    catalognames.append(underscored)
  return pkgnames, catalognames


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


def CollectionLongestCommonSubstring(collection):
  current_substring = collection.pop()
  while collection and current_substring:
    substring_set = LongestCommonSubstring(current_substring,
                                           collection.pop())
    if substring_set:
      current_substring = list(substring_set)[0]
  return current_substring
