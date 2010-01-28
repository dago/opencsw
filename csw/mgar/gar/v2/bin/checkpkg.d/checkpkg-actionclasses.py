#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy check. You can use it as a boilerplate for your own checks.

Copy it and modify.
"""

import logging
import os.path
import sys
import re

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


def CheckActionClasses(pkg):
  """Checks the consistency between classes in the prototype and pkginfo."""
  errors = []
  pkginfo = pkg.GetParsedPkginfo()
  pkgmap = pkg.GetPkgmap()
  pkginfo_classes = set(re.split(opencsw.WS_RE, pkginfo["CLASSES"]))
  pkgmap_classes = pkgmap.GetClasses()
  only_in_pkginfo = pkginfo_classes.difference(pkgmap_classes)
  only_in_pkgmap = pkgmap_classes.difference(pkginfo_classes)
  for cls in only_in_pkginfo:
  	errors.append(
  	    opencsw.PackageError("Class %s is only in pkginfo" % repr(cls)))
  for cls in only_in_pkgmap:
  	errors.append(
  	    opencsw.PackageError("Class %s is only in pkgmap" % repr(cls)))
  if only_in_pkginfo or only_in_pkgmap:
  	errors.append(
        opencsw.PackageError(
            "pkginfo_classes: %s, pkgmap classes: %s" % (
                pkginfo_classes, pkgmap_classes)))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  check_manager = checkpkg.CheckpkgManager(
      "class action scripts / prototype integrity",
      options.extractdir,
      pkgnames,
      options.debug)
  check_manager.RegisterIndividualCheck(CheckActionClasses)
  exit_code, report = check_manager.Run()
  print report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
