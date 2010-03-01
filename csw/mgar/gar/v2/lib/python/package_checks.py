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
import checkpkg

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


def CheckCatalogname(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  catalogname = pkginfo["NAME"].split(" ")[0]
  catalogname_re = r"^(\w+)$"
  if not re.match(catalogname_re, catalogname):
    error_mgr.ReportError("pkginfo-bad-catalogname")


def SetCheckDependencies(pkgs_data, error_mgr, logger):
  """Dependencies must be either installed in the system, or in the set."""
  pass
