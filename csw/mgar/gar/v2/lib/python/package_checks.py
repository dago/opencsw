# $Id$
#
# Package checking functions.  They come in two flavors:
# - individual package checks
# - set checks
#
# Individual checks need to be named "Check<something>", while set checks are named
# "SetCheck<something>".
#
# def CheckSomething(pkg_data, error_mgr, logger, messenger):
#   logger.debug("Checking something.")
#   error_mgr.ReportError("something-is-wrong")
#
# TODO(maciej): In general, the development package should depend on all the libraries.
# TODO(maciej): If foo.so links to foo.so.1, the devel package should depend on
#               the library package.

import copy
import re
import operator
import os
import checkpkg
import opencsw
import pprint
import textwrap
import dependency_checks as depchecks
import configuration as c
import sharedlib_utils as su
import struct_util
from Cheetah import Template
import common_constants
import logging

PATHS_ALLOWED_ONLY_IN = {
    # Leading slash must be removed.
    # Using strings where possible for performance.
    "CSWcommon":  {"string": [
                       r"opt",
                       r"opt/csw/man",
                       r"opt/csw/doc",
                       r"opt/csw/info",
                       r"opt/csw/share/locale/locale.alias",
                   ],
                   "regex": [r"opt/csw/man/.*"]},
    "CSWiconv":   {"string": [r"opt/csw/lib/charset.alias"]},
    "CSWtexinfo": {"string": [r"opt/csw/share/info/dir"]},
}
MAX_DESCRIPTION_LENGTH = 100
LICENSE_TMPL = "/opt/csw/share/doc/%s/license"
OBSOLETE_DEPS = {
    # "CSWfoo": {
    #   "hint": "Do this...",
    #   "url": "http://www.opencsw.org/bugtrack/view.php?id=..."
    # },
    "CSWpython-rt": {
      "hint": "CSWpython-rt is deprecated, use CSWpython instead.",
      "url": "http://www.opencsw.org/bugtrack/view.php?id=4031"
    },
    "CSWlibcups": {
      "hint": "CSWlibcups is deprecated, please depend on specific "
              "shared library packages.",
      "url": "http://wiki.opencsw.org/packaging-shared-libraries",
    },
    "CSWcswclassutils": {
      "hint": "CSWcswclassutils is deprecated, please depend on specific "
              "CSWcas-* packages.",
              "url": ("http://lists.opencsw.org/pipermail/maintainers/"
                      "2010-October/012862.html"),
    },
}
ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")
EMAIL_RE = re.compile(r"^.*@opencsw.org$")
MAX_CATALOGNAME_LENGTH = 29
MAX_PKGNAME_LENGTH = 32
ARCH_LIST = common_constants.ARCHITECTURES
VERSION_RE = r".*,REV=(20[01][0-9]\.[0-9][0-9]\.[0-9][0-9]).*"
# Pkgnames matching these regexes must not be ARCHALL = 1
ARCH_SPECIFIC_PKGNAMES_RE_LIST = [
    re.compile(r".*dev(el)?$"),
]

DISCOURAGED_FILE_PATTERNS = (
    (r"\.py[co]$", ("Python compiled files are supposed to be compiled using"
                    "the cswpycompile class action script. For more "
                    "information, see "
                    "http://wiki.opencsw.org/cswclassutils-package")),
    (r"/lib\w+\.l?a$", "Static libraries aren't necessary on Solaris."),
    (r"opt/csw/var($|/)", ("The /opt/csw/var directory is not writable on "
                            "sparse non-global zones.  "
                            "Please use /var/opt/csw instead.")),
    (r"\.git", ("Git files in most cases shouldn't be included in "
                "a package.")),
    (r"\.CVS", ("CVS files in most cases shouldn't be included in "
                "a package.")),
)
RPATH_PARTS = {
    'prefix': r"(?P<prefix>/opt/csw)",
    'prefix_extra': r"(?P<prefix_extra>(/(?!lib)[\w-]+)*)",
    'subdirs': r"(?P<subdirs>(/(?!-R)[\w\-\.]+)*)",
    'isalist': r"(?P<isalist>/(\$ISALIST|64))",
    'subdir2': r"(?P<subdir2>/[\w\-\.]+)",
}
RPATH_WHITELIST = [
    (r"^"
     r"%(prefix)s"
     r"%(prefix_extra)s"
     r"/(lib|libexec)"
     r"%(subdirs)s"
     r"%(isalist)s?"
     r"%(subdir2)s?"
     r"$") % RPATH_PARTS,
    r"^\$ORIGIN$",
    r"^\$ORIGIN/..$",
    r"^/usr(/(ccs|dt|openwin))?/lib(/(sparcv9|amd64|64))?$",
]
# Check ldd -r only for Perl modules
SYMBOLS_CHECK_ONLY_FOR = r"^CSWpm.*$"

# Valid URLs in the VENDOR field in pkginfo
VENDORURL_RE = r"^(http|ftp)s?\://.+\..+$"

# Settings for binary placements: which architectures can live in which
# directories.
BASE_BINARY_PATHS = ('bin', 'sbin', 'lib', 'libexec', 'cgi-bin')
HACHOIR_MACHINES = {
    # id: (name, allowed_paths, disallowed_paths)
    -1: {"name": "Unknown",
         "allowed": {
           common_constants.OS_REL_58: (),
           common_constants.OS_REL_59: (),
           common_constants.OS_REL_510: (),
           common_constants.OS_REL_511: (),
         }, "disallowed": (),
         "type": "unknown"},
     2: {"name": "sparcv8",
         "type": common_constants.ARCH_SPARC,
         "allowed": {
           common_constants.OS_REL_58: BASE_BINARY_PATHS + su.SPARCV8_PATHS,
           common_constants.OS_REL_59: BASE_BINARY_PATHS + su.SPARCV8_PATHS,
           common_constants.OS_REL_510: BASE_BINARY_PATHS + su.SPARCV8_PATHS,
           common_constants.OS_REL_511: BASE_BINARY_PATHS + su.SPARCV8_PATHS,
         },
         "disallowed": su.SPARCV9_PATHS + su.INTEL_386_PATHS + su.AMD64_PATHS,
        },
     # pentium_pro binaries are also identified as 3.
     3: {"name": "i386",
         "type": common_constants.ARCH_i386,
         "allowed": {
           common_constants.OS_REL_58: BASE_BINARY_PATHS + su.INTEL_386_PATHS,
           common_constants.OS_REL_59: BASE_BINARY_PATHS + su.INTEL_386_PATHS,
           common_constants.OS_REL_510: BASE_BINARY_PATHS + su.INTEL_386_PATHS,
           common_constants.OS_REL_511: BASE_BINARY_PATHS + su.INTEL_386_PATHS,
         },
         "disallowed": su.SPARCV8_PATHS + su.SPARCV8PLUS_PATHS +
                       su.SPARCV9_PATHS + su.AMD64_PATHS,
        },
     6: {"name": "i486",
         "type": common_constants.ARCH_i386,
         "allowed": {
           common_constants.OS_REL_58: su.INTEL_386_PATHS,
           common_constants.OS_REL_59: su.INTEL_386_PATHS,
           common_constants.OS_REL_510: su.INTEL_386_PATHS,
           common_constants.OS_REL_511: su.INTEL_386_PATHS,
         },
         "disallowed": su.SPARCV8_PATHS + su.SPARCV8PLUS_PATHS +
                       su.SPARCV9_PATHS + su.AMD64_PATHS,
         },
    18: {"name": "sparcv8+",
         "type": common_constants.ARCH_SPARC,
         "allowed": {
           common_constants.OS_REL_58: su.SPARCV8PLUS_PATHS,
           common_constants.OS_REL_59: su.SPARCV8PLUS_PATHS,
           # We allow sparcv8+ as the base architecture on Solaris 10+.
           common_constants.OS_REL_510: BASE_BINARY_PATHS + su.SPARCV8PLUS_PATHS,
           common_constants.OS_REL_511: BASE_BINARY_PATHS + su.SPARCV8PLUS_PATHS,
         },
         "disallowed": su.SPARCV8_PATHS + su.SPARCV9_PATHS +
                       su.AMD64_PATHS + su.INTEL_386_PATHS,
        },
    43: {"name": "sparcv9",
         "type": common_constants.ARCH_SPARC,
         "allowed": {
           common_constants.OS_REL_58: su.SPARCV9_PATHS,
           common_constants.OS_REL_59: su.SPARCV9_PATHS,
           common_constants.OS_REL_510: su.SPARCV9_PATHS,
           common_constants.OS_REL_511: su.SPARCV9_PATHS,
         },
         "disallowed": su.INTEL_386_PATHS + su.AMD64_PATHS,
        },
    62: {"name": "amd64",
         "type": common_constants.ARCH_i386,
         "allowed": {
           common_constants.OS_REL_58: su.AMD64_PATHS,
           common_constants.OS_REL_59: su.AMD64_PATHS,
           common_constants.OS_REL_510: su.AMD64_PATHS,
           common_constants.OS_REL_511: su.AMD64_PATHS,
         },
         "disallowed": su.SPARCV8_PATHS + su.SPARCV8PLUS_PATHS +
                       su.SPARCV9_PATHS,
        },
}


ALLOWED_STARTING_PATHS = frozenset([
  "/opt/csw",
  "/etc/opt/csw",
  "/var/opt/csw",
])


def RemovePackagesUnderInstallation(paths_and_pkgs_by_soname,
                                    pkgs_to_be_installed):
  """Emulates uninstallation of packages prior to installation
  of the new ones.
  {'libfoo.so.1': {u'/opt/csw/lib': [u'CSWlibfoo']}}
  """
  # for brevity
  ptbi = set(pkgs_to_be_installed)
  ppbs = paths_and_pkgs_by_soname
  new_ppbs = {}
  for soname in ppbs:
    if soname not in new_ppbs:
      new_ppbs[soname] = {}
    for binary_path in ppbs[soname]:
      for pkgname in ppbs[soname][binary_path]:
        if pkgname not in ptbi:
          if binary_path not in new_ppbs[soname]:
            new_ppbs[soname][binary_path] = []
          new_ppbs[soname][binary_path].append(pkgname)
  return new_ppbs


def CheckDirectoryPermissions(pkg_data, error_mgr, logger, messenger):
  for entry in pkg_data["pkgmap"]:
    if (entry["type"] == "d"
          and
        entry["mode"] != "?"
          and
        entry["mode"][1] == "6"):
      error_mgr.ReportError("executable-bit-missing-on-a-directory",
                            entry["path"])


def CheckNonCswPathsDirectoryPerms(pkg_data, error_mgr, logger, messenger):
  for entry in pkg_data["pkgmap"]:
    if entry["user"] == "?" or entry["group"] == "?" or entry["mode"] == "?":
      if entry["path"].startswith("/opt/csw"):
        error_mgr.ReportError("pkgmap-question-mark-perms-in-opt-csw", entry["path"])


def CheckPerlLocal(pkg_data, error_mgr, logger, messenger):
  perllocal_re = re.compile(r'/perllocal.pod')
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      if re.search(perllocal_re, entry["path"]):
        error_mgr.ReportError("perllocal-pod-in-pkgmap", entry["path"])

def CheckGzippedManpages(pkg_data, error_mgr, logger, messenger):
  gzipman_re = re.compile(r'share/man/man.*/.*\.gz$')
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      if re.search(gzipman_re, entry["path"]):
        error_mgr.ReportError(
          'gzipped-manpage-in-pkgmap', entry["path"],
          "Solaris' man cannot automatically inflate man pages. "
          "Solution: man page should be gunzipped.")

def CheckMultipleDepends(pkg_data, error_mgr, logger, messenger):
  new_depends = set()
  for pkgname, desc in pkg_data["depends"]:
    if pkgname in new_depends:
      error_mgr.ReportError("dependency-listed-more-than-once", pkgname)
    new_depends.add(pkgname)


def CheckDescription(pkg_data, error_mgr, logger, messenger):
  pkginfo = pkg_data["pkginfo"]
  desc = checkpkg.ExtractDescription(pkginfo)
  if not desc:
    error_mgr.ReportError("pkginfo-description-missing")
  else:
    if len(desc) > MAX_DESCRIPTION_LENGTH:
      error_mgr.ReportError("pkginfo-description-too-long", "length=%s" % len(desc))
    if not desc[0].isupper():
      error_mgr.ReportError("pkginfo-description-not-starting-with-uppercase",
                            desc)


def CheckVendorURL(pkg_data, error_mgr, logger, messenger):
  vendorurl = c.WS_RE.split(pkg_data["pkginfo"]["VENDOR"])[0]
  if not re.match(VENDORURL_RE, vendorurl):
    error_mgr.ReportError("pkginfo-bad-vendorurl", vendorurl,
                          "Solution: add VENDOR_URL to GAR Recipe")


def CheckCatalogname(pkg_data, error_mgr, logger, messenger):
  pkginfo = pkg_data["pkginfo"]
  catalogname = pkginfo["NAME"].split(" ")[0]
  catalogname_2 = pkg_data["basic_stats"]["catalogname"]
  if catalogname != catalogname_2:
    error_mgr.ReportError("pkginfo-catalogname-disagreement pkginfo=%s filename=%s"
        % (catalogname, catalogname_2))
  catalogname_re = r"^([\w\+]+)$"
  if not re.match(catalogname_re, catalogname):
    error_mgr.ReportError("pkginfo-bad-catalogname", catalogname)
  if catalogname != catalogname.lower():
    error_mgr.ReportError("catalogname-not-lowercase")


def CheckSmfIntegration(pkg_data, error_mgr, logger, messenger):
  init_re = re.compile(r"/init\.d/")
  for entry in pkg_data["pkgmap"]:
    if not entry["path"]:
      continue
    if not re.search(init_re, entry["path"]):
      continue
    if entry["class"] != "cswinitsmf":
      error_mgr.ReportError(
          "init-file-missing-cswinitsmf-class",
          "%s class=%s" % (entry["path"], entry["class"]))
      messenger.Message(
          "The init file %s in the package has the %s class, while it "
          "should have the cswinitsmf class, which takes advantage of "
          "the SMF integration automation from cswclassutils."
          % (entry["path"], entry["class"]))
      messenger.SuggestGarLine("INITSMF = %s" % entry["path"])

    # This is not an error, in fact, putting files into
    # /opt/csw/etc/init.d breaks packages.

    if "/opt/csw/etc/init.d" in entry["path"]:
      messenger.Message("Init files under /opt result in broken packages, "
                        "see http://lists.opencsw.org/pipermail/maintainers/"
                        "2010-June/012145.html")
      error_mgr.ReportError(
          "init-file-wrong-location",
          entry["path"])


def SetCheckLibraries(pkgs_data, error_mgr, logger, messenger):
  """Second version of the library checking code.

  1. Collect all the needed data from the FS:
     {"<basename>": {"/path/1": ["CSWfoo1"], "/path/2": ["CSWfoo2"]}}
     1.1. find all needed sonames
     1.2. get all the data for needed sonames
  2. Construct an overlay by applying data from the package set
  3. For each binary
     3.1. Resolve all NEEDED sonames
  """
  needed_sonames = []
  pkgs_to_be_installed = [x["basic_stats"]["pkgname"] for x in pkgs_data]
  paths_to_verify = set()
  pkg_by_path = {}
  logger.debug("Building needed_sonames, paths_to_verify and pkg_by_path...")
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    for binary_info in pkg_data["binaries_dump_info"]:
      needed_sonames.extend(binary_info["needed sonames"])
    # Creating an index of packages by path
    for pkgmap_entry in pkg_data["pkgmap"]:
      if "path" in pkgmap_entry and pkgmap_entry["path"]:
        base_dir, basename = os.path.split(pkgmap_entry["path"])
        paths_to_verify.add(base_dir)
        paths_to_verify.add(pkgmap_entry["path"])
        if pkgmap_entry["path"] not in pkg_by_path:
          pkg_by_path[pkgmap_entry["path"]] = []
        pkg_by_path[pkgmap_entry["path"]].append(pkgname)
  needed_sonames = sorted(set(needed_sonames))
  # Finding candidate libraries from the filesystem (/var/sadm/install/contents)
  path_and_pkg_by_basename = depchecks.GetPathAndPkgByBasename(
      error_mgr, logger, needed_sonames)
  # Removing files from packages that are to be installed.
  path_and_pkg_by_basename = RemovePackagesUnderInstallation(
      path_and_pkg_by_basename, pkgs_to_be_installed)
  # Populating the mapping using data from the local packages.  The call to
  # GetPkgByFullPath will complete the mapping using data from the filesystem.
  pkg_by_path = depchecks.GetPkgByFullPath(
      error_mgr, logger, paths_to_verify, pkg_by_path)
  # Adding overlay based on the given package set
  # Considering files from the set under examination.
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    # Processing the whole pkgmap.  There yet no verification whether the files
    # that are put in here are actually shared libraries, or symlinks to shared
    # libraries.  Implementing symlink resolution would be a nice bonus.
    for pkgmap_entry in pkg_data["pkgmap"]:
      if "path" not in pkgmap_entry: continue
      if not pkgmap_entry["path"]: continue
      binary_path, basename = os.path.split(pkgmap_entry["path"])
      if not binary_path.startswith('/'):
        binary_path = "/" + binary_path
      path_and_pkg_by_basename.setdefault(basename, {})
      path_and_pkg_by_basename[basename][binary_path] = [pkgname]
  # Resolving sonames for each binary
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    declared_deps = frozenset(x[0] for x in pkg_data["depends"])
    check_args = (pkg_data, error_mgr, logger, messenger,
                  path_and_pkg_by_basename, pkg_by_path)
    depchecks.Libraries(*check_args)
    depchecks.ByFilename(*check_args)
    # This test needs more work, or potentially, architectural changes.
    # by_directory_reasons = ByDirectory(*check_args)
    # req_pkgs_reasons.extend(by_directory_reasons)


def SetCheckDependencies(pkgs_data, error_mgr, logger, messenger):
  """Dependencies must be either installed in the system, or in the set."""
  known_pkgs = set(error_mgr.GetInstalledPackages())
  pkgs_under_check = [x["basic_stats"]["pkgname"] for x in pkgs_data]
  for pkgname in pkgs_under_check:
    known_pkgs.add(pkgname)
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    for depname, dep_desc in pkg_data["depends"]:
      if depname not in known_pkgs:
        error_mgr.ReportError(pkgname, "unidentified-dependency", depname)


def CheckDependsOnSelf(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for depname, dep_desc in pkg_data["depends"]:
    if depname == pkgname:
      error_mgr.ReportError("depends-on-self")


def CheckArchitectureSanity(pkg_data, error_mgr, logger, messenger):
  basic_stats = pkg_data["basic_stats"]
  pkgname = basic_stats["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  filename = basic_stats["pkg_basename"]
  arch = pkginfo["ARCH"]
  filename_re = r"-%s-" % arch
  if not re.search(filename_re, filename):
    error_mgr.ReportError("srv4-filename-architecture-mismatch",
                          "pkginfo=%s filename=%s" % (arch, filename))


def CheckActionClasses(pkg_data, error_mgr, logger, messenger):
  """Checks the consistency between classes in the prototype and pkginfo."""
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  if "CLASSES" not in pkginfo:
    return
  pkginfo_classes = set(re.split(c.WS_RE, pkginfo["CLASSES"]))
  pkgmap_classes = set()
  for entry in pkgmap:
    if entry["class"]:  # might be None
      pkgmap_classes.add(entry["class"])
  only_in_pkginfo = pkginfo_classes.difference(pkgmap_classes)
  only_in_pkgmap = pkgmap_classes.difference(pkginfo_classes)
  for action_class in only_in_pkginfo:
    error_mgr.ReportError("action-class-only-in-pkginfo", action_class)
  for action_class in only_in_pkgmap:
    error_mgr.ReportError("action-class-only-in-pkgmap", action_class)


def CheckLicenseFile(pkg_data, error_mgr, logger, messenger):
  """Checks for the presence of the license file."""
  # TODO: Write a unit test
  pkgmap = pkg_data["pkgmap"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  license_path = LICENSE_TMPL % catalogname
  pkgmap_paths = [x["path"] for x in pkgmap]
  if license_path not in pkgmap_paths:
    messenger.Message("The license file needs to be placed "
                      "at %s. Also see "
                      "http://sourceforge.net/apps/trac/gar/wiki/CopyRight"
                      % license_path)
    error_mgr.ReportError(
        "license-missing", license_path,
        "See http://sourceforge.net/apps/trac/gar/wiki/CopyRight")


def CheckObsoleteDeps(pkg_data, error_mgr, logger, messenger):
  """Checks for obsolete dependencies."""
  deps = frozenset([x for x, y in pkg_data["depends"]])
  obsolete_pkg_deps = deps.intersection(set(OBSOLETE_DEPS))
  if obsolete_pkg_deps:
    for obsolete_pkg in obsolete_pkg_deps:
      error_mgr.ReportError("obsolete-dependency", obsolete_pkg)
      msg = ""
      if "hint" in OBSOLETE_DEPS[obsolete_pkg]:
        msg += "Hint: %s" % OBSOLETE_DEPS[obsolete_pkg]["hint"]
      if "url" in OBSOLETE_DEPS[obsolete_pkg]:
        if msg:
          msg += ", "
        msg += "URL: %s" % OBSOLETE_DEPS[obsolete_pkg]["url"]
      if not msg:
        msg = None
      messenger.Message(msg)


def CheckArchitectureVsContents(pkg_data, error_mgr, logger, messenger):
  """Verifies the relationship between package contents and architecture."""
  binaries = pkg_data["binaries"]
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  arch = pkginfo["ARCH"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  reasons_to_be_arch_specific = []
  pkgmap_paths = [x["path"] for x in pkgmap]
  for pkgmap_path in pkgmap_paths:
    if re.search(ARCH_RE, str(pkgmap_path)):
      reasons_to_be_arch_specific.append((
          "archall-with-arch-paths",
          pkgmap_path,
          "path %s looks arch-specific" % pkgmap_path))
  for binary in binaries:
    reasons_to_be_arch_specific.append((
        "archall-with-binaries",
        binary,
        "package contains binary %s" % binary))
  for pkgname_re in ARCH_SPECIFIC_PKGNAMES_RE_LIST:
    if pkgname_re.match(pkgname):
      reasons_to_be_arch_specific.append((
          "archall-devel-package", None, None))
  if arch == "all":
    for tag, param, desc in reasons_to_be_arch_specific:
      error_mgr.ReportError(tag, param, desc)
  elif not reasons_to_be_arch_specific:
    messenger.Message("Package %s does not contain any binaries. "
                      "Consider making it ARCHALL = 1 instead of %s. "
                      "However, be aware that there might be other reasons "
                      "to keep it architecture-specific."
                      % (pkgname, arch))
    messenger.SuggestGarLine("ARCHALL_%s = 1" % pkgname)


# TODO: Verify that architecture type of binaries matches the actual binaries.
# Correlate architecture type from files_metadata and HACHOIR_MACHINES with
# pkginfo.


def CheckFileNameSanity(pkg_data, error_mgr, logger, messenger):
  basic_stats = pkg_data["basic_stats"]
  revision_info = basic_stats["parsed_basename"]["revision_info"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  if "REV" not in revision_info:
    error_mgr.ReportError("rev-tag-missing-in-filename")
  if len(catalogname) > MAX_CATALOGNAME_LENGTH:
    error_mgr.ReportError("catalogname-too-long")
  if len(pkgname) > MAX_PKGNAME_LENGTH:
    error_mgr.ReportError("pkgname-too-long")
  if basic_stats["parsed_basename"]["osrel"] == "unspecified":
    error_mgr.ReportError("osrel-tag-not-specified")


def CheckPkginfoSanity(pkg_data, error_mgr, logger, messenger):
  """pkginfo sanity checks.

if [ "$maintname" = "" ] ; then
  # the old format, in the DESC field
  maintname=`sed -n 's/^DESC=.*for CSW by //p' $TMPFILE`

  # Since the DESC field has been coopted, take
  # description from second half of NAME field now.
  desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
else
  if [ "$desc" = "" ] ; then
    desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
  fi
fi

software=`sed -n 's/^NAME=\([^ -]*\) -.*$/\1/p' $TMPFILE`
version=`sed -n 's/^VERSION=//p' $TMPFILE`
desc=`sed -n 's/^DESC=//p' $TMPFILE`
email=`sed -n 's/^EMAIL=//p' $TMPFILE`
maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
hotline=`sed -n 's/^HOTLINE=//p' $TMPFILE`
basedir=`sed -n 's/^BASEDIR=//p' $TMPFILE`
pkgarch=`sed -n 's/^ARCH=//p' $TMPFILE|head -1`

if [ "$software" = "" ] ; then errmsg $f: software field not set properly in NAME ; fi
if [ "$pkgname" = "" ] ; then errmsg $f: pkgname field blank ; fi
if [ "$desc" = "" ] ; then errmsg $f: no description in either NAME or DESC field ; fi
if [ ${#desc} -gt 100 ] ; then errmsg $f: description greater than 100 chars ; fi
if [ "$version" = "" ] ; then errmsg $f: VERSION field blank ;  fi
if [ "$maintname" = "" ] ; then errmsg $f: maintainer name not detected. Fill out VENDOR field properly ; fi
if [ "$email" = "" ] ; then errmsg $f: EMAIL field blank ; fi
if [ "$hotline" = "" ] ; then errmsg $f: HOTLINE field blank ; fi
  """
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  # PKG, NAME, ARCH, VERSION and CATEGORY
  for parameter in ("PKG", "NAME", "ARCH", "VERSION", "CATEGORY"):
    if parameter not in pkginfo:
      error_mgr.ReportError("pkginfo-missing-parameter", parameter)
  if not catalogname:
    error_mgr.ReportError("pkginfo-empty-catalogname")
  if not pkgname:
    error_mgr.ReportError("pkginfo-empty-pkgname")
  if not "VERSION" in pkginfo or not pkginfo["VERSION"]:
    error_mgr.ReportError("pkginfo-version-field-missing")
  # maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
  maintname = checkpkg.ExtractMaintainerName(pkginfo)
  if not maintname:
    error_mgr.ReportError("pkginfo-maintainer-name-not-set")
  # email
  if not pkginfo["EMAIL"]:
    error_mgr.ReportError("pkginfo-email-blank")
  # hotline
  if not pkginfo["HOTLINE"]:
    error_mgr.ReportError("pkginfo-hotline-blank")
  pkginfo_version = pkg_data["basic_stats"]["parsed_basename"]["full_version_string"]
  if pkginfo_version != pkginfo["VERSION"]:
    error_mgr.ReportError("filename-version-does-not-match-pkginfo-version",
                          "filename=%s pkginfo=%s"
                          % (pkginfo_version, pkginfo["VERSION"]))
  if re.search(r"-", pkginfo["VERSION"]):
    error_mgr.ReportError("pkginfo-minus-in-version", pkginfo["VERSION"])
  if not re.match(VERSION_RE, pkginfo["VERSION"]):
    msg = "Should match %s" % VERSION_RE
    error_mgr.ReportError("pkginfo-version-wrong-format",
                          pkginfo["VERSION"],
                          msg)
  if pkginfo["ARCH"] not in ARCH_LIST:
    error_mgr.ReportError(
        "pkginfo-nonstandard-architecture",
        pkginfo["ARCH"],
        "known architectures: %s" % ARCH_LIST)


def CheckEmail(pkg_data, error_mgr, logger, messenger):
  """Checks the e-mail address."""
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  if not re.match(EMAIL_RE, pkginfo["EMAIL"]):
    error_mgr.ReportError("pkginfo-email-not-opencsw-org",
                          "email=%s" % pkginfo["EMAIL"])


def CheckPstamp(pkg_data, error_mgr, logger, messenger):
  pkginfo = pkg_data["pkginfo"]
  if "PSTAMP" in pkginfo:
    if not re.match(common_constants.PSTAMP_RE, pkginfo["PSTAMP"]):
      msg=("It should be 'username@hostname-timestamp', "
           "but it's %s." % repr(pkginfo["PSTAMP"]))
      error_mgr.ReportError("pkginfo-pstamp-in-wrong-format", pkginfo["PSTAMP"], msg)
  else:
    error_mgr.ReportError("pkginfo-pstamp-missing")


def DisabledCheckMissingSymbols(pkgs_data, error_mgr, logger, messenger):
  """Analyzes missing symbols reported by ldd -r.

  1. Collect triplets: pkgname, binary, missing symbol
  2. If there are any missing symbols, collect all the symbols that are provided
     by the set of packages.
  3. From the list of missing symbols, remove all symbols that are provided
     by the set of packages.
  4. Report any remaining symbols as errors.

  What indexes do we need?

  symbol -> (pkgname, binary)
  set(allsymbols)
  """
  missing_symbols = []
  all_symbols = set()
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries = pkg_data["binaries"]
    for binary in binaries:
      for ldd_elem in pkg_data["ldd_dash_r"][binary]:
        if ldd_elem["state"] == "symbol-not-found":
          missing_symbols.append((pkgname,
                                  binary,
                                  ldd_elem["symbol"]))
      for symbol in pkg_data["defined_symbols"][binary]:
        all_symbols.add(symbol)
  # Remove symbols defined elsewhere.
  while missing_symbols:
    ms_pkgname, ms_binary, ms_symbol = missing_symbols.pop()
    if ms_symbol not in all_symbols:
      error_mgr.ReportError("symbol-not-found", "%s %s" % (ms_binary, ms_symbol))


def CheckBuildingUser(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  username = checkpkg.ExtractBuildUsername(pkg_data["pkginfo"])
  for entry in pkg_data["pkgmap"]:
    if entry["user"] and entry["user"] == username:
      error_mgr.ReportError("file-owned-by-building-user"
                            "%s, %s" % (entry["path"], entry["user"]))


def CheckDisallowedPaths(pkg_data, error_mgr, logger, messenger):
  """Checks for disallowed paths, such as common paths."""
  arch = pkg_data["pkginfo"]["ARCH"]
  # Common paths read from the file are absolute, e.g. /opt/csw/lib
  # while paths in pkginfo are relative, e.g. opt/csw/lib.
  common_paths = []
  for common_path in error_mgr.GetCommonPaths(arch):
    if common_path.startswith("/"):
      common_path = common_path[1:]
    common_paths.append(common_path)
  paths_only_allowed_in = copy.copy(PATHS_ALLOWED_ONLY_IN)
  ss = paths_only_allowed_in["CSWcommon"]["string"]
  paths_only_allowed_in["CSWcommon"]["string"] = set(ss).union(common_paths)
  # Compile all the regex expressions ahead of time.
  for pkgname in paths_only_allowed_in:
    if "regex" in paths_only_allowed_in[pkgname]:
      regexes = paths_only_allowed_in[pkgname]["regex"]
      paths_only_allowed_in[pkgname]["regex"] = map(re.compile, regexes)
    if "string" in paths_only_allowed_in[pkgname]:
      paths_only_allowed_in[pkgname]["string"] = set(
          paths_only_allowed_in[pkgname]["string"])
  paths_in_pkg = set()
  for entry in pkg_data["pkgmap"]:
    entry_path = entry["path"]
    if not entry_path:
      continue
    if entry_path.startswith("/"):
      entry_path = entry_path[1:]
    paths_in_pkg.add(entry_path)
  for pkgname in paths_only_allowed_in:
    if pkgname != pkg_data["basic_stats"]["pkgname"]:
      if "string" in paths_only_allowed_in[pkgname]:
        ss = paths_only_allowed_in[pkgname]["string"]
        intersection =  ss.intersection(paths_in_pkg)
        for path_in_pkg in intersection:
          error_mgr.ReportError(
              "disallowed-path", path_in_pkg,
              "This path is already provided by %s "
              "or is not allowed for other reasons." % pkgname)
      if "regex" in paths_only_allowed_in[pkgname]:
        rr = paths_only_allowed_in[pkgname]["regex"]
        for disallowed_re in rr:
          badpaths = filter(disallowed_re.match, paths_in_pkg)
          for path_in_pkg in badpaths:
              error_mgr.ReportError(
                  "disallowed-path", path_in_pkg,
                  "This path is already provided by %s "
                  "or is not allowed for other reasons." % pkgname)


def CheckLinkingAgainstSunX11(pkg_data, error_mgr, logger, messenger):
  shared_libs = set(su.GetSharedLibs(pkg_data))
  for binary_info in pkg_data["binaries_dump_info"]:
    for soname in binary_info["needed sonames"]:
      if (binary_info["path"] in shared_libs
          and
          soname in common_constants.DO_NOT_LINK_AGAINST_THESE_SONAMES):
        error_mgr.ReportError("linked-against-discouraged-library",
                              "%s %s" % (binary_info["base_name"], soname))


def CheckDiscouragedFileNamePatterns(pkg_data, error_mgr, logger, messenger):
  patterns = [(x, re.compile(x), y) for x, y in DISCOURAGED_FILE_PATTERNS]
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      for pattern, pattern_re, msg in patterns:
        if pattern_re.search(entry["path"]):
          error_mgr.ReportError("discouraged-path-in-pkgmap",
                                entry["path"])
          messenger.OneTimeMessage(
              "discouraged-path-in-pkgmap-%s" % pattern, msg)


def CheckBadContent(pkg_data, error_mgr, logger, messenger):
  for regex in pkg_data["bad_paths"]:
    for file_name in pkg_data["bad_paths"][regex]:
      messenger.Message(
          "File %s contains bad content: %s. "
          "If it's a legacy file you can't modify, "
          "or if you investigated the issue and the string does not pose "
          "a real issue, you can override this error. "
          % (file_name, repr(regex)))
      error_mgr.ReportError("file-with-bad-content", "%s %s" % (regex, file_name))


def CheckPkgchk(pkg_data, error_mgr, logger, messenger):
  if pkg_data["pkgchk"]["return_code"] != 0:
    error_mgr.ReportError("pkgchk-failed-with-code", pkg_data["pkgchk"]["return_code"])
    for line in pkg_data["pkgchk"]["stderr_lines"]:
      logger.warn(line)

def CheckRpath(pkg_data, error_mgr, logger, messenger):
  regex_whitelist = [re.compile(x) for x in RPATH_WHITELIST]
  for binary_info in pkg_data["binaries_dump_info"]:
    actual_rpaths = binary_info["runpath"]
    matching = []
    not_matching = []
    for rpath in actual_rpaths:
      matched = False
      for white_re in regex_whitelist:
        m = white_re.match(rpath)
        if m:
          matching.append((rpath, m.groupdict()))
          matched = True
          break
      if matched:
        matching.append(rpath)
      else:
        not_matching.append(rpath)

    for bad in sorted(not_matching):
      logger.debug("Bad rpath: %s", bad)
      error_mgr.ReportError(
          "bad-rpath-entry",
          "%s %s" % (bad, binary_info["path"]))


def DisabledCheckForMissingSymbols(pkgs_data, debug):
  """Analyzes missing symbols reported by ldd -r.

  1. Collect triplets: pkgname, binary, missing symbol
  2. If there are any missing symbols, collect all the symbols that are provided
     by the set of packages.
  3. From the list of missing symbols, remove all symbols that are provided
     by the set of packages.
  4. Report any remaining symbols as errors.

  What indexes do we need?

  symbol -> (pkgname, binary)
  set(allsymbols)
  """
  errors = []
  missing_symbols = []
  all_symbols = set()
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries = pkg_data["binaries"]
    for binary in binaries:
      for ldd_elem in pkg_data["ldd_dash_r"][binary]:
        if ldd_elem["state"] == "symbol-not-found":
          missing_symbols.append((pkgname,
                                  binary,
                                  ldd_elem["symbol"]))
      for symbol in pkg_data["defined_symbols"][binary]:
        all_symbols.add(symbol)
  # Remove symbols defined elsewhere.
  while missing_symbols:
    ms_pkgname, ms_binary, ms_symbol = missing_symbols.pop()
    if ms_symbol not in all_symbols:
      errors.append(checkpkg.CheckpkgTag(
        ms_pkgname, "symbol-not-found", "%s %s" % (ms_binary, ms_symbol)))
  return errors


def DisabledCheckForMissingSymbolsDumb(pkg_data, error_mgr, logger, messenger):
  """Analyzes missing symbols reported by ldd -r.

  So far only made sense for perl modules.  Disables because it falls over on
  big KDE packages.  During pickling (serialization), Python runs out of memory.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  if not re.match(SYMBOLS_CHECK_ONLY_FOR, pkgname):
    return
  symbol_not_found_was_seen = False
  relocation_was_seen = False
  for binary_info in pkg_data["binaries_dump_info"]:
    for ldd_elem in pkg_data["ldd_dash_r"][binary_info["path"]]:
      if not symbol_not_found_was_seen and ldd_elem["state"] == "symbol-not-found":
        error_mgr.ReportError("symbol-not-found",
                              "e.g. %s misses %s" % (binary_info["path"], ldd_elem["symbol"]))
        symbol_not_found_was_seen = True
      if (not relocation_was_seen
            and
          ldd_elem["state"] == 'relocation-bound-to-a-symbol-with-STV_PROTECTED-visibility'):
        error_mgr.ReportError(ldd_elem["state"],
            "e.g. symbol: %s file: %s "
            "relocation bound to a symbol with STV_PROTECTED visibility"
            % (ldd_elem["symbol"], ldd_elem["path"]))


def SetCheckFileCollisions(pkgs_data, error_mgr, logger, messenger):
  """Throw an error if two packages contain the same file.

  Directories don't count.  The strategy is to create an in-memory index of
  packages by filename.
  """
  pkgs_by_path = {}
  # File types are described at:
  # http://docs.sun.com/app/docs/doc/816-5174/pkgmap-4?l=en&n=1&a=view
  skip_file_types = set(["d"])
  pkgnames = set(x["basic_stats"]["pkgname"] for x in pkgs_data)
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    for pkgmap_entry in pkg_data["pkgmap"]:
      if pkgmap_entry["path"] and pkgmap_entry["type"] not in skip_file_types:
        if pkgmap_entry["path"] not in pkgs_by_path:
          pkgs_by_path[pkgmap_entry["path"]] = set()
        pkgs_by_path[pkgmap_entry["path"]].add(pkgname)
        pkgs_in_db = error_mgr.GetPkgByPath(pkgmap_entry["path"])

        # We need to simulate package removal before next install.  We want to
        # throw an error if two new packages have a conflict; however, we
        # don't want to throw an error in the following scenario:
        #
        # db:
        # CSWfoo with /opt/csw/bin/foo
        #
        # new:
        # CSWfoo - empty
        # CSWfoo-utils with /opt/csw/bin/foo
        #
        # Here, CSWfoo-utils conflicts with CSWfoo from the database; but we
        # don't need to check against CSWfoo in the database, but with with
        # one in the package set under examination instead.
        pkgs_in_db = pkgs_in_db.difference(pkgnames)

        pkgs_by_path[pkgmap_entry["path"]].update(pkgs_in_db)
  # Traversing the data structure
  for file_path in pkgs_by_path:
    if len(pkgs_by_path[file_path]) > 1:
      pkgnames = sorted(pkgs_by_path[file_path])
      for pkgname in pkgnames:
        error_mgr.ReportError(
            pkgname,
            'file-collision',
            '%s %s' % (file_path, " ".join(pkgnames)))


def CheckPythonPackageName(pkg_data, error_mgr, logger, messenger):
  """Checks for CSWpy-* and py_* package names."""
  pyfile_re = re.compile(r"/opt/csw/lib/python.*/.*")
  pkgname = pkg_data["basic_stats"]["pkgname"]
  has_py_files = False
  example_py_file = ""
  for pkgmap_entry in pkg_data["pkgmap"]:
    if not pkgmap_entry["path"]:
      continue
    if pyfile_re.match(pkgmap_entry["path"]):
      has_py_files = True
      example_py_file = pkgmap_entry["path"]
      break
  if has_py_files and not pkgname.startswith("CSWpy-"):
    error_mgr.ReportError("pkgname-does-not-start-with-CSWpy-")
    messenger.Message("The package "
                      "installs files into /opt/csw/lib/python. For example, %s. "
                      "However, the pkgname doesn't start with 'CSWpy-'."
                      % repr(example_py_file))
  if has_py_files and not pkg_data["basic_stats"]["catalogname"].startswith("py_"):
    error_mgr.ReportError("catalogname-does-not-start-with-py_")
    messenger.Message("The package installs files into /opt/csw/lib/python. "
        "For example, %s. "
        "However, the catalogname doesn't start with 'py_'."
        % repr(example_py_file))


def CheckArchitecture(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for metadata in pkg_data["files_metadata"]:
    if "machine_id" not in metadata:
      continue
    logger.debug("CheckArchitecture(): %s", metadata)
    machine_id = metadata["machine_id"]
    if machine_id not in HACHOIR_MACHINES:
      error_mgr.ReportError(
          "binary-architecture-unknown",
          "file=%s arch_id=%s" % (
            metadata["path"],
            metadata["machine_id"]))
      continue
    machine_data = HACHOIR_MACHINES[machine_id]
    cpu_type = machine_data["name"]
    # allowed_paths needs to depend on the OS release. The OS release is
    # only available from the file name.
    os_release = pkg_data["basic_stats"]["parsed_basename"]["osrel"]
    if os_release not in machine_data["allowed"]:
      raise checkpkg.InternalDataError(
          "%s not found in machine_data" % os_release)
    allowed_paths = set(machine_data["allowed"][os_release])
    disallowed_paths = set(machine_data["disallowed"])
    path_parts = set(metadata["path"].split(os.path.sep))
    if not path_parts.intersection(allowed_paths):
      error_mgr.ReportError(
          "binary-architecture-does-not-match-placement",
          "file=%s arch_id=%s arch_name=%s" % (
            metadata["path"],
            machine_id,
            cpu_type))
      messenger.OneTimeMessage(
          "binary-placement",
          "Files compiled for specific architectures must be placed in "
          "subdirectories that match the architecture.  "
          "For example, a sparcv8+ binary must not be placed under "
          "/opt/csw/lib, but under /opt/csw/lib/sparcv8plus.  "
          "Typically, the case is that sparcv8+ binaries end up under bin/ "
          "or under lib/ because of ignored CFLAGS.  "
          "For more information about the OpenCSW binary placement policy, "
          "visit "
          "http://www.opencsw.org/extend-it/contribute-packages/"
          "build-standards/"
          "architecture-optimization-using-isaexec-and-isalist/")
    else:
      for bad_path in path_parts.intersection(disallowed_paths):
        error_mgr.ReportError(
          "binary-disallowed-placement",
          "file=%s arch_id=%s arch_name=%s bad_path=%s" % (
            metadata["path"],
            machine_id,
            cpu_type,
            bad_path))
        messenger.Message(
            "The %s binary is placed in a disallowed path.  "
            "For example, a sparcv8+ binary must not be placed "
            "under a directory named sparcv9.  "
            "For more information, visit "
            "http://www.opencsw.org/extend-it/contribute-packages/"
            "build-standards/"
            "architecture-optimization-using-isaexec-and-isalist/")


def CheckWrongArchitecture(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  filename_arch = pkg_data["basic_stats"]["parsed_basename"]["arch"]
  pkginfo_arch = pkg_data["pkginfo"]["ARCH"]
  files_metadata = pkg_data["files_metadata"]
  for file_metadata in files_metadata:
    if su.IsBinary(file_metadata):
      machine = HACHOIR_MACHINES[file_metadata["machine_id"]]
      if machine["type"] != pkginfo_arch:
        error_mgr.ReportError(
            "binary-wrong-architecture",
            "file=%s pkginfo-says=%s actual-binary=%s" % (
              file_metadata["path"],
              pkginfo_arch,
              machine["type"]))


def CheckSharedLibraryNamingPolicy(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  shared_libs = set(su.GetSharedLibs(pkg_data))
  linkable_shared_libs = []
  for binary_info in pkg_data["binaries_dump_info"]:
    if binary_info["path"] in shared_libs:
      if su.IsLibraryLinkable(binary_info["path"]):
        # It is a shared library and other projects might link to it.
        # Some libraries don't declare a soname; compile time linker defaults
        # to their file name.
        if "soname" in binary_info and binary_info["soname"]:
          soname = binary_info["soname"]
        else:
          soname = os.path.split(binary_info["path"])[1]
        linkable_shared_libs.append((soname, binary_info))
      else:
        logging.debug("%r is not linkable", binary_info["path"])
  logging.debug("CheckSharedLibraryNamingPolicy(): "
                "linkable shared libs of %s: %s"
                % (pkgname, linkable_shared_libs))
  for soname, binary_info in linkable_shared_libs:
    path = os.path.split(binary_info["path"])[0]
    tmp = su.MakePackageNameBySoname(soname, path)
    policy_pkgname_list, policy_catalogname_list = tmp
    if pkgname not in policy_pkgname_list:
      error_mgr.ReportError(
          "shared-lib-pkgname-mismatch",
          "file=%s "
          "soname=%s "
          "pkgname=%s "
          "expected=%s"
          % (binary_info["path"],
             soname, pkgname,
             ",".join(policy_pkgname_list)))

      suggested_pkgname = policy_pkgname_list[0]
      lib_path, lib_basename = os.path.split(binary_info["path"])
      pkginfo = pkg_data["pkginfo"]
      description = " ".join(pkginfo["NAME"].split(" ")[2:])
      depchecks.SuggestLibraryPackage(error_mgr, messenger,
        suggested_pkgname,
        policy_catalogname_list[0],
        description,
        lib_path, lib_basename, soname,
        pkgname)

      messenger.OneTimeMessage(
          soname,
          "This shared library (%s) is in a directory indicating that it "
          "is likely to be linked to by other programs.  If this is the "
          "case, the library is best packaged separately, in a package "
          "with a library-specific name.  Examples of such names include: "
          "%s. If this library is not meant to be linked to by other "
          "packages, it's best moved to a 'private' directory.  "
          "For example, instead of /opt/csw/lib/foo.so, "
          "try /opt/csw/lib/projectname/foo.so. "
          "More information: http://wiki.opencsw.org/checkpkg-error-tags"
          % (binary_info["path"], policy_pkgname_list))


def CheckSharedLibraryPkgDoesNotHaveTheSoFile(pkg_data, error_mgr, logger, messenger):
  """If it's a package with shared libraries, it should not contain the .so file.

  For example, libfoo.so.1 should not be in the same package as libfoo.so,
  because the latter is used for linking during compilation, and the former is
  a shared object that needs to be phased out at some point.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  shared_libs = set(su.GetSharedLibs(pkg_data))
  shared_libs = filter(su.IsLibraryLinkable, shared_libs)
  if shared_libs:
    # If the package contains shared libraries, it must not contain
    # corrersponding .so files, which are used during linking.
    for entry in pkg_data["pkgmap"]:
      if entry["path"]:
        if entry["path"].endswith(".so") and entry["type"] == "s":
          error_mgr.ReportError(
              "shared-lib-package-contains-so-symlink",
              "file=%s" % entry["path"])
          messenger.SuggestGarLine("# (If %s-dev doesn't exist yet)" % pkgname)
          messenger.SuggestGarLine("PACKAGES += %s-dev" % pkgname)
          messenger.SuggestGarLine(
              "CATALOGNAME_%s-dev = %s_dev"
              % (pkgname, pkg_data["basic_stats"]["catalogname"]))
          messenger.SuggestGarLine(
              "SPKG_DESC_%s-dev += $(DESCRIPTION), development files" % pkgname)
          messenger.SuggestGarLine(
              "PKGFILES_%s-dev += %s" % (pkgname, entry["path"]))
          messenger.SuggestGarLine("# Maybe also the generic:")
          messenger.SuggestGarLine(
              "# PKGFILES_%s-dev += $(PKGFILES_DEVEL)" % (pkgname))
          messenger.Message(
              "The package contains shared libraries together with the "
              "symlink of the form libfoo.so -> libfoo.so.1.  "
              "In this case: %s.  "
              "This kind of symlink should not be together with the shared "
              "libraries; it is only used during compiling and linking.  "
              "The best practice "
              "is to put the shared libraries into a separate package, and "
              "the .so file together with the header files in the devel "
              "package." % entry["path"])

def CheckPackagesWithHeaderFilesMustContainTheSoFile(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  shared_libs = set(su.GetSharedLibs(pkg_data))
  shared_libs = filter(su.IsLibraryLinkable, shared_libs)
  if shared_libs:
    # If the package contains shared libraries, it must not contain
    # corrersponding .so files, which are used during linking.
    for entry in pkg_data["pkgmap"]:
      if entry["path"]:
        if entry["path"].endswith(".so") and entry["type"] == "s":
          error_mgr.ReportError(
              "shared-lib-package-contains-so-symlink",
              "file=%s" % entry["path"])
          messenger.Message(
              "The package contains shared libraries together with the "
              "symlink of the form libfoo.so -> libfoo.so.1.  "
              "In this case: %s.  "
              "This kind of symlink should not be together with the shared "
              "libraries; it is only used during compiling and linking.  "
              "The best practice "
              "is to put the shared libraries into a separate package, and "
              "the .so file together with the header files in the devel "
              "package." % entry["path"])


def CheckSharedLibraryNameMustBeAsubstringOfSoname(
    pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for binary_info in pkg_data["binaries_dump_info"]:
    if "soname" in binary_info:
      if binary_info["soname"] not in binary_info["base_name"]:
        error_mgr.ReportError(
            "soname-not-part-of-filename",
            "soname=%s "
            "filename=%s"
            % (binary_info["soname"], binary_info["base_name"]))


def CheckLicenseFilePlacement(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  docpath_re = re.compile(r"/opt/csw/share/doc/(?P<docname>[^/]+)/license$")
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" not in pkgmap_entry: continue
    if not pkgmap_entry["path"]: continue
    m = docpath_re.match(pkgmap_entry["path"])
    if m:
      if m.groupdict()["docname"] != pkg_data["basic_stats"]["catalogname"]:
        msg = ("The package contains a docdir which doesn't match its "
               "catalog name.  To fix, repeat the merge state (mgar remerge "
               "repackage).")
        messenger.Message(msg)
        error_mgr.ReportError(
            "wrong-docdir",
            "expected=/opt/csw/shared/doc/%s/... "
            "in-package=%s"
            % (pkg_data["basic_stats"]["catalogname"],
               pkgmap_entry["path"]))


def CheckBaseDirs(pkg_data, error_mgr, logger, messenger):
  """Symlinks and nonstandard class files need base directories

  This cannot be made a general check, because there would be too many false
  positives.  However, symlinks and nonstandard class files are so prone to
  this problem that it makes sense to throw errors if they miss base
  directories.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" not in pkgmap_entry: continue
    if not pkgmap_entry["path"]: continue
    if pkgmap_entry["type"] == "s" or pkgmap_entry["class"] != "none":
      base_dir = os.path.dirname(pkgmap_entry["path"])
      error_mgr.NeedFile(
          base_dir,
          "%s contains %s which needs a base directory: %s."
          % (pkgname, repr(pkgmap_entry["path"]), repr(base_dir)))


def CheckDanglingSymlinks(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" not in pkgmap_entry: continue
    if not pkgmap_entry["path"]: continue
    if pkgmap_entry["type"] in ("s", "l"):
      link_type = "symlink"
      if pkgmap_entry["type"] == "l":
        link_type = "hardlink"
      error_mgr.NeedFile(
          pkgmap_entry["target"],
          "%s contains a %s (%s) which needs the target file: %s."
          % (link_type, pkgname, repr(pkgmap_entry["path"]), repr(pkgmap_entry["target"])))


def CheckPrefixDirs(pkg_data, error_mgr, logger, messenger):
  """Files are allowed to be in /opt/csw, /etc/opt/csw and /var/opt/csw."""
  pkgname = pkg_data["basic_stats"]["pkgname"]
  paths_with_slashes = [(x, x + "/") for x in ALLOWED_STARTING_PATHS]
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" not in pkgmap_entry: continue
    if not pkgmap_entry["path"]: continue
    allowed_found = False
    for p, pslash in paths_with_slashes:
      # We need to handle /opt/csw as an allowed path
      if pkgmap_entry["path"] == p:
        allowed_found = True
        break
      if pkgmap_entry["path"].startswith(pslash):
        allowed_found = True
        break
    if not allowed_found:
      error_mgr.ReportError(
          "bad-location-of-file",
          "file=%s" % pkgmap_entry["path"])


def CheckCatalognameMatchesPkgname(pkg_data, error_mgr, logger, messenger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  std_catalogname = struct_util.MakeCatalognameByPkgname(pkgname)
  if catalogname != std_catalogname:
    msg = (
        "The catalogname should match the pkgname. "
        "For more information, see "
        "http://www.opencsw.org/extend-it/contribute-packages/"
        "build-standards/package-creation/")
    error_mgr.ReportError(
        'catalogname-does-not-match-pkgname',
        'pkgname=%s catalogname=%s expected-catalogname=%s'
        % (pkgname, catalogname, std_catalogname))


def CheckSonameMustNotBeEqualToFileNameIfFilenameEndsWithSo(
    pkg_data, error_mgr, logger, messenger):
  shared_libs = set(su.GetSharedLibs(pkg_data))
  for binary_info in pkg_data["binaries_dump_info"]:
    if binary_info["path"] not in shared_libs:
      continue
    if not su.IsLibraryLinkable(binary_info["path"]):
      continue
    base_name = binary_info["base_name"]
    if "soname" in binary_info:
      soname = binary_info["soname"]
    else:
      soname = base_name
    if (base_name.endswith(".so")
        and soname == base_name):
      msg = ("File /%s is a shared library.  Its SONAME is equal to its "
             "filename, and the filename ends with .so. "
             "This is a serious problem. "
             "If such shared library is released and any programs link "
             "to it, it is very hard to do any subsequent updates to "
             "that shared library.  This problem has occurred with relation "
             "to libnet. "
             "For information how to update such library, please see: "
             "http://wiki.opencsw.org/project-libnet" %
             binary_info["path"])
      messenger.Message(msg)
      error_mgr.ReportError(
          "soname-equals-filename",
          "file=/%s" % binary_info["path"])


def CheckLinkableSoFileMustBeAsymlink(
    pkg_data, error_mgr, logger, messenger):
  pass


def CheckPkginfoOpencswRepository(
    pkg_data, error_mgr, logger, messenger):
  repotag = "OPENCSW_REPOSITORY"
  pkginfo = pkg_data["pkginfo"]
  if repotag not in pkginfo:
    error_mgr.ReportError("pkginfo-opencsw-repository-missing")
    return
  if "UNCOMMITTED" in pkginfo[repotag]:
    error_mgr.ReportError("pkginfo-opencsw-repository-uncommitted")

def CheckAlternativesDependency(
    pkg_data, error_mgr, logger, messenger):

  need_alternatives = False
  for entry in pkg_data["pkgmap"]:
    if not entry["path"]:
      continue
    if entry["class"] == "cswalternatives":
      need_alternatives = True
      break
  if need_alternatives:
    error_mgr.NeedFile(
        "/opt/csw/sbin/alternatives",
        "The alternatives subsystem is used")


def CheckSharedLibrarySoExtension(pkg_data, error_mgr, logger, messenger):
  shared_libs = set(su.GetSharedLibs(pkg_data))
  for shared_lib in shared_libs:
    if ".so" not in shared_lib:
      error_mgr.ReportError(
          "shared-library-missing-dot-so",
          "file=%s" % shared_lib)
