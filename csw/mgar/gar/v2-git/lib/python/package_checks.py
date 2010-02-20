# Defining the checking functions.  They come in two flavors: individual
# package checks and set checks.

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



