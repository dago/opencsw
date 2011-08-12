# $Id$

import copy
import re
import os.path
import common_constants


# TODO: Merge with common_constants
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
BIN_MIMETYPES = (
    'application/x-executable',
    'application/x-sharedlib',
)


class Error(Exception):
  pass


class ArchitectureError(Error):
  pass


def IsLibraryLinkable(file_path):
  arch_subdirs = (SPARCV8_PATHS + SPARCV8PLUS_PATHS + SPARCV9_PATHS
                  + INTEL_386_PATHS + AMD64_PATHS)
  # Need to escape the plus signs because of the regex usage below.
  arch_subdirs = [x.replace(r"+", r"\+") for x in arch_subdirs]
  linkable_re = re.compile(r"^opt/csw(/[a-z-_]+)?/lib(/(%s))?$"
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
    prev_type = CharType(part[-1])
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
  def AddSeparator(d, sep):
    "Adds a separator based on the neighboring of two digits."
    dc = copy.copy(d)
    if dc["version"]:
      if (dc["basename"][-1].isdigit()
          and
          dc["version"][0].isdigit()):
        dc["sep"] = sep
      else:
        dc["sep"] = ""
    else:
      dc["sep"] = ""
    return dc
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
  pkgname_list = []
  keywords_pkgname = AddSeparator(keywords_pkgname, "-")
  pkgname_list.append(
      "CSW%(basename)s%(sep)s%(version)s" % keywords_pkgname)
  keywords_catalogname = AddSeparator(keywords_catalogname, "_")
  catalogname_list = [
      "%(basename)s%(sep)s%(version)s" % keywords_catalogname,
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


def ValidateCollectionName(l):
  letters = "".join(re.findall(r"[a-zA-Z]", l))
  # Special case for libz
  if len(letters) == 1 and letters[0] == 'z': return True
  if len(letters) <= 1:
    return False
  return True


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
  if not ValidateCollectionName(lcs):
    return None
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


def IsBinary(file_info):
  """Returns True or False depending on file metadata."""
  is_a_binary = False
  if "mime_type" not in file_info:
    # This would be a problem in the data.
    return False
  if not file_info["mime_type"]:
    # This should never happen, but it seems to have happened at least once.
    # TODO: Find the affected data and figure out why.
    raise PackageError("file_info is missing mime_type:" % file_info)
  for mimetype in BIN_MIMETYPES:
    if mimetype in file_info["mime_type"]:
      is_a_binary = True
      break
  return is_a_binary


def ArchByString(s):
    if s == 'sparc':
      return common_constants.ARCH_SPARC
    elif s in ('i386', 'x86'):
      return common_constants.ARCH_i386
    elif s == 'all':
      return common_constants.ARCH_ALL
    else:
      raise ArchitectureError(
          "Cannot map architecture %s to a constant." % repr(s))


def GetIsalist(str_arch):
  arch = ArchByString(str_arch)
  return common_constants.ISALISTS_BY_ARCH[arch]


def EscapeRegex(s):
  """Needs to be improved to escape more characters."""
  s = s.replace(r'.', r'\.')
  return s
