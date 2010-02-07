#!/opt/csw/bin/python2.6
#
# $Id$

"""Verifies the architecture of the package."""

import os.path
import sys

CHECKPKG_MODULE_NAME = "architecture check"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

def CheckArchitectureVsContents(pkg, debug):
  """Verifies the relationship between package contents and architecture."""
  errors = []
  binaries = pkg.ListBinaries()
  pkginfo = pkg.GetParsedPkginfo()
  arch = pkginfo["ARCH"]
  if binaries and arch == "all":
    for binary in binaries:
    	errors.append(checkpkg.CheckpkgTag(pkg.pkgname, "archall-with-binaries"), binary)
  elif not binaries and arch != "all":
    # This is not a clean way of handling messages for the user, but there's
    # not better way at the moment.
    print "Package %s does not contain any binaries." % pkg.pkgname
    print "Consider making it ARCHALL = 1 instead of %s:" % arch
    print "ARCHALL_%s = 1" % pkg.pkgname
    print ("However, be aware that there might be other reasons "
           "to keep it architecture-specific.")
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.extractdir,
                                           pkgnames,
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
