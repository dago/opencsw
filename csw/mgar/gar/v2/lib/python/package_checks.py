# $Id$
#
# Package checking functions.  They come in two flavors:
# - individual package checks
# - set checks
#
# Individual checks need to be named "Check<something>", while set checks are named
# "SetCheck<something>".
#
# def CheckSomething(pkg_data, error_mgr, logger):
#   logger.debug("Checking something.")
#   error_mgr.ReportError("something-is-wrong")

import re
import os
import checkpkg
import opencsw
from Cheetah import Template

PATHS_ALLOWED_ONLY_IN = {
    "CSWcommon": ["/opt",
                  "/opt/csw/man",
                  "/opt/csw/doc",
                  "/opt/csw/info",
                  "/opt/csw/share/locale/locale.alias"],
    "CSWiconv": ["/opt/csw/lib/charset.alias"],
    "CSWtexinfp": ["/opt/csw/share/info/dir"],
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
}
ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")


def CatalognameLowercase(pkg_data, error_mgr, logger):
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if catalogname != catalogname.lower():
    error_mgr.ReportError("catalogname-not-lowercase")
  if not re.match(r"^[\w_]+$", catalogname):
    error_mgr.ReportError("catalogname-is-not-a-simple-word")


def CheckForbiddenPaths(pkg_data, error_mgr, logger):
  for pkgname in PATHS_ALLOWED_ONLY_IN:
    if pkgname != pkg_data["basic_stats"]["pkgname"]:
      for entry in pkg_data["pkgmap"]:
        for forbidden_path in PATHS_ALLOWED_ONLY_IN[pkgname]:
          if entry["path"] == forbidden_path:
            error_mgr.ReportError("forbidden-path", entry["path"])


def CheckDirectoryPermissions(pkg_data, error_mgr, logger):
  for entry in pkg_data["pkgmap"]:
    if entry["type"] == "d":
      if entry["mode"][1] == "6":
        error_mgr.ReportError("executable-bit-missing-on-a-directory",
                              entry["path"])


def CheckNonCswPathsDirectoryPerms(pkg_data, error_mgr, logger):
  for entry in pkg_data["pkgmap"]:
    if entry["user"] == "?" or entry["group"] == "?" or entry["mode"] == "?":
      if entry["path"].startswith("/opt/csw"):
        error_mgr.ReportError("question-mark-perms-in-opt-csw", entry["path"])


def CheckPerlLocal(pkg_data, error_mgr, logger):
  perllocal_re = re.compile(r'/perllocal.pod')
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      if re.search(perllocal_re, entry["path"]):
        error_mgr.ReportError("perllocal-pod-in-pkgmap", entry["path"])


def CheckMultipleDepends(pkg_data, error_mgr, logger):
  new_depends = set()
  for pkgname, desc in pkg_data["depends"]:
    if pkgname in new_depends:
      error_mgr.ReportError("dependency-listed-more-than-once", pkgname)
    new_depends.add(pkgname)


def CheckDescription(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  desc = checkpkg.ExtractDescription(pkginfo)
  if not desc:
    error_mgr.ReportError("pkginfo-description-missing")
  else:
    if len(desc) > MAX_DESCRIPTION_LENGTH:
      error_mgr.ReportError("pkginfo-description-too-long")
    if not desc[0].isupper():
      error_mgr.ReportError("pkginfo-description-not-starting-with-uppercase",
                            desc)


def CheckCatalogname(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  catalogname = pkginfo["NAME"].split(" ")[0]
  catalogname_re = r"^(\w+)$"
  if not re.match(catalogname_re, catalogname):
    error_mgr.ReportError("pkginfo-bad-catalogname", catalogname)


def CheckSmfIntegration(pkg_data, error_mgr, logger):
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


def SetCheckSharedLibraryConsistency(pkgs_data, error_mgr, logger):
  ws_re = re.compile(r"\s+")
  result_ok = True
  binaries = []
  binaries_by_pkgname = {}
  sonames_by_pkgname = {}
  pkg_by_any_filename = {}
  needed_sonames_by_binary = {}
  filenames_by_soname = {}
  for pkg_data in pkgs_data:
    binaries_base = [os.path.basename(x) for x in pkg_data["binaries"]]
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries_by_pkgname[pkgname] = binaries_base
    binaries.extend(pkg_data["binaries"])
    for filename in pkg_data["all_filenames"]:
      pkg_by_any_filename[filename] = pkgname
    for binary_data in pkg_data["binaries_dump_info"]:
      binary_base_name = os.path.basename(binary_data["base_name"])
      needed_sonames_by_binary[binary_base_name] = binary_data
      filenames_by_soname[binary_data[checkpkg.SONAME]] = binary_base_name

  # Making the binaries unique
  binaries = set(binaries)
  isalist = pkg_data["isalist"]

  # Building indexes by soname to simplify further processing
  # These are indexes "by soname".
  (needed_sonames,
   binaries_by_soname,
   runpath_by_needed_soname) = checkpkg.BuildIndexesBySoname(
       needed_sonames_by_binary)

  logger.debug("Determining the soname-package relationships.")
  # lines by soname is an equivalent of $EXTRACTDIR/shortcatalog
  runpath_data_by_soname = {}
  for soname in needed_sonames:
    runpath_data_by_soname[soname] = error_mgr.GetPkgmapLineByBasename(soname)
  lines_by_soname = checkpkg.GetLinesBySoname(
      runpath_data_by_soname, needed_sonames, runpath_by_needed_soname, isalist)

  # Creating a map from files to packages.
  pkgs_by_filename = {}
  for soname, line in lines_by_soname.iteritems():
    # TODO: Find all the packages, not just the last field.
    fields = re.split(ws_re, line.strip())
    # For now, we'll assume that the last field is the package.
    pkgname = fields[-1]
    pkgs_by_filename[soname] = pkgname

  # A shared object dependency/provisioning report, plus checking.
  #
  # This section is somewhat overlapping with checkpkg.AnalyzeDependencies(),
  # it has a different purpose: it reports the relationships between shared
  # libraries, binaries using them and packages providing them.  Ideally, the
  # same bit of code would do both checking and reporting.
  #
  # TODO: Rewrite this using cheetah templates
  if False and needed_sonames:
    print "Analysis of sonames needed by the package set:"
    binaries_with_missing_sonames = set([])
    for soname in needed_sonames:
      logger.debug("Analyzing: %s", soname)
      if soname in filenames_by_soname:
        print "%s is provided by the package itself" % soname
      elif soname in lines_by_soname:
        print ("%s is provided by %s and required by:" 
               % (soname,
                  pkgs_by_filename[soname]))
        filename_lines = " ".join(sorted(binaries_by_soname[soname]))
        for line in textwrap.wrap(filename_lines, 70):
          print " ", line
      else:
        print ("%s is required by %s, but we don't know what provides it."
               % (soname, binaries_by_soname[soname]))
        for binary in binaries_by_soname[soname]:
          binaries_with_missing_sonames.add(binary)
        if soname in checkpkg.ALLOWED_ORPHAN_SONAMES:
          print "However, it's a whitelisted soname."
        else:
          pass
          # The error checking needs to be unified: done in one place only.
          # errors.append(
          #     checkpkg.CheckpkgTag(
          #       "%s is required by %s, but "
          #       "we don't know what provides it."
          #       % (soname, binaries_by_soname[soname])))
    if binaries_with_missing_sonames:
      print "The following are binaries with missing sonames:"
      binary_lines = " ".join(sorted(binaries_with_missing_sonames))
      for line in textwrap.wrap(binary_lines, 70):
        print " ", line
    print

  dependent_pkgs = {}
  for checker in pkgs_data:
    pkgname = checker["basic_stats"]["pkgname"]
    declared_dependencies = dict(checker["depends"])
    missing_deps, surplus_deps, orphan_sonames = checkpkg.AnalyzeDependencies(
        pkgname,
        declared_dependencies,
        binaries_by_pkgname,
        needed_sonames_by_binary,
        pkgs_by_filename,
        filenames_by_soname,
        pkg_by_any_filename)
    namespace = {
        "pkgname": pkgname,
        "missing_deps": missing_deps,
        "surplus_deps": surplus_deps,
        "orphan_sonames": orphan_sonames,
    }
    t = Template.Template(checkpkg.REPORT_TMPL, searchList=[namespace])
    print unicode(t)
    for soname in orphan_sonames:
      error_mgr.ReportError(pkgname, "orphan-soname", soname)
    for missing_dep in missing_deps:
      error_mgr.ReportError(pkgname, "missing-dependency", missing_dep)


def SetCheckDependencies(pkgs_data, error_mgr, logger):
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

def CheckDependsOnSelf(pkg_data, error_mgr, logger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for depname, dep_desc in pkg_data["depends"]:
    if depname == pkgname:
      error_mgr.ReportError("depends-on-self")

def CheckArchitectureSanity(pkg_data, error_mgr, logger):
  basic_stats = pkg_data["basic_stats"]
  pkgname = basic_stats["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  filename = basic_stats["pkg_basename"]
  arch = pkginfo["ARCH"]
  filename_re = r"-%s-" % arch
  if not re.search(filename_re, filename):
    error_mgr.ReportError("srv4-filename-architecture-mismatch", arch)


def CheckActionClasses(pkg_data, error_mgr, logger):
  """Checks the consistency between classes in the prototype and pkginfo."""
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  pkginfo_classes = set(re.split(opencsw.WS_RE, pkginfo["CLASSES"]))
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


def CheckLicenseFile(pkg_data, error_mgr, logger):
  """Checks for the presence of the license file."""
  # TODO: Write a unit test
  pkgmap = pkg_data["pkgmap"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  license_path = LICENSE_TMPL % catalogname
  pkgmap_paths = [x["path"] for x in pkgmap]
  if license_path not in pkgmap_paths:
    error_mgr.ReportError("license-missing")
    logger.info("See http://sourceforge.net/apps/trac/gar/wiki/CopyRight")

def CheckObsoleteDeps(pkg_data, error_mgr, logger):
  """Checks for obsolete dependencies."""
  deps = set(pkg_data["depends"])
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
      logger.info(msg)


def CheckArchitectureVsContents(pkg_data, error_mgr, logger):
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
  if arch == "all":
    for tag, param, desc in reasons_to_be_arch_specific:
      error_mgr.ReportError(tag, param, desc)
  elif not reasons_to_be_arch_specific:
    logger.info("Package %s does not contain any binaries.", pkgname)
    logger.info("Consider making it ARCHALL = 1 instead of %s:", arch)
    logger.info("ARCHALL_%s = 1", pkgname)
    logger.info("However, be aware that there might be other reasons "
                "to keep it architecture-specific.")
