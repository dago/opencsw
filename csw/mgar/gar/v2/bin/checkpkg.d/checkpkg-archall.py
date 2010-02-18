#!/opt/csw/bin/python2.6
#
# $Id$

"""Verifies the architecture of the package."""

import os.path
import re
import sys

CHECKPKG_MODULE_NAME = "architecture check"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")

def CheckArchitectureVsContents(pkg_data, debug):
  """Verifies the relationship between package contents and architecture."""
  errors = []
  binaries = pkg_data["binaries"]
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg.GetPkgmap()
  arch = pkginfo["ARCH"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  reasons_to_be_arch_specific = []
  for pkgmap_path in pkgmap.entries_by_path:
    # print "pkgmap_path", repr(pkgmap_path), type(pkgmap_path)
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


def main():
  options, args = checkpkg.GetOptions()
  md5sums = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.stats_basedir,
                                           md5sums,
                                           options.debug)

  check_manager.RegisterIndividualCheck(CheckArchitectureVsContents)

  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()

# vim:set sw=2 ts=2 sts=2 expandtab:
