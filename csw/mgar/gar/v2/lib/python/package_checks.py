# $Id$
#
# Package checking functions.  They come in two flavors:
# - individual package checks
# - set checks
#
# Some ideas for the future development of the checks.  Here's what a check
# could look like:
#
# class FooCheck(checkpkg.IndividualCheck):
#   """Simplest check for an individual package."""
#   
#   def CheckExampleOne(self):
#     """First idea, with an ReportError method."""
#     if self.catalogname != self.catalogname.lower():
#       self.ReportError("catalogname-not-lowercase")
#
#   def CheckExampleTwo(self):
#     """Second idea, more similar to a unit test."""
#     self.checkEqual(self.catalogname,
#                     self.catalogname.lower(),
#                     "catalogname-not-lowercase")
#
# What would be needed to do that:
#
#  - Have a class that looks for classes derived from checkpkg.IndividualCheck,
#    run SetUp on them (which sets things such as self.catalogname) and then
#    Check().
#  - Read all the data and set appropriate member names.
#     
# Set checks would be slightly more complicated.
#
# class BarCheck(checkpkg.SetCheck):
#   """More complex check for multiple packages.
#
#   We cannot have package data as class members any more, we have to use
#   a class member with a list of objects containing packages' data.
#
#   In this class, checkEqual() methods needs one more parameter, denoting
#   the package to assign the error to.
#   """
#
#   def Check(self):
#     for pkg in self.pkgs:
#       self.checkEqual(pkg.catalogname,
#                       pkg.catalogname.lower(),
#                       pkg,
#                       "catalogname-not-lowercase")
#     
# Alternately, a function-based approach is possible:
#
# def IndividualCheckCatalogname(pkg_data, checkpkg_mgr):
#   catalogdata = pkg_data["basic_stats"]["catalogname"]
#   if catalogdata != catalogdata.lower():
#     checkpkg_mgr.ReportError("catalogname-not-lowercase")

import checkpkg
import re

ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")

def CatalognameLowercase(pkg_data, debug):
  errors = []
  # Here's how to report an error:
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if catalogname != catalogname.lower():
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "catalogname-not-lowercase"))
  if not re.match(r"^\w+$", catalogname):
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "catalogname-is-not-a-simple-word"))
  return errors


def FileNameSanity(pkg_data, debug):
  errors = []
  # Here's how to report an error:
  basic_stats = pkg_data["basic_stats"]
  revision_info = basic_stats["parsed_basename"]["revision_info"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if "REV" not in revision_info:
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "rev-tag-missing-in-filename"))
  return errors


def CheckArchitectureVsContents(pkg_data, debug):
  """Verifies the relationship between package contents and architecture."""
  errors = []
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
      errors.append(checkpkg.CheckpkgTag(pkgname, tag, param))
  elif not reasons_to_be_arch_specific:
    # This is not a clean way of handling messages for the user, but there's
    # not better way at the moment.
    print "Package %s does not contain any binaries." % pkgname
    print "Consider making it ARCHALL = 1 instead of %s:" % arch
    print "ARCHALL_%s = 1" % pkgname
    print ("However, be aware that there might be other reasons "
           "to keep it architecture-specific.")
  return errors



