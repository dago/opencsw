#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy check. You can use it as a boilerplate for your own checks.

Copy it and modify.
"""

import logging
import os.path
import sys
import re

CHECKPKG_MODULE_NAME = "class action scripts / prototype integrity"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


def CheckActionClasses(pkg_data, debug):
  """Checks the consistency between classes in the prototype and pkginfo."""
  errors = []
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
    error = checkpkg.CheckpkgTag(
        pkg_data["basic_stats"]["pkgname"],
        "action-class-only-in-pkginfo",
        action_class,
        msg="This shouldn't cause any problems, but it might be not necessary.")
    errors.append(error)
  for action_class in only_in_pkgmap:
    errors.append(
        checkpkg.CheckpkgTag(pkg.pkgname, "action-class-only-in-pkgmap", action_class))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  if options.debug:
  	logging.basicConfig(level=logging.DEBUG)
  else:
  	logging.basicConfig(level=logging.INFO)
  md5sums = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.stats_basedir,
                                           md5sums,
                                           options.debug)
  # Registering functions defined above.
  check_manager.RegisterIndividualCheck(CheckActionClasses)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
