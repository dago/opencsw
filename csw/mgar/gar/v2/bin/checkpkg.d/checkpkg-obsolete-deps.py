#!/opt/csw/bin/python2.6
# $Id$

"""Makes sure that obsolete packages are not added as dependencies.
"""

import logging
import os.path
import sys

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.getcwd(),
             os.path.split(sys.argv[0])[0],
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

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

def CheckObsoleteDeps(pkg):
  """Checks for obsolete dependencies."""
  errors = []
  deps = set(pkg.GetDependencies())
  obsolete_pkg_deps = deps.intersection(set(OBSOLETE_DEPS))
  if obsolete_pkg_deps:
    for obsolete_pkg in obsolete_pkg_deps:
      errors.append(
          checkpkg.PackageError(
            "Package %s should not depend on %s."
             % (pkg.pkgname, obsolete_pkg)))
      if "hint" in OBSOLETE_DEPS[obsolete_pkg]:
        errors.append(
            checkpkg.PackageError("Hint: %s" % OBSOLETE_DEPS[obsolete_pkg]["hint"]))
      if "url" in OBSOLETE_DEPS[obsolete_pkg]:
      	errors.append(
      	    checkpkg.PackageError("URL: %s" % OBSOLETE_DEPS[obsolete_pkg]["url"]))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  check_manager = checkpkg.CheckpkgManager("obsolete dependencies",
                                           options.extractdir,
                                           pkgnames,
                                           options.debug)
  check_manager.RegisterIndividualCheck(CheckObsoleteDeps)
  exit_code, report = check_manager.Run()
  print report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
