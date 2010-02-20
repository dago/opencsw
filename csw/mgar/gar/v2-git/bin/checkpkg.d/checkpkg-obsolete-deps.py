#!/opt/csw/bin/python2.6
# $Id$

"""Makes sure that obsolete packages are not added as dependencies.
"""

import logging
import os.path
import sys

CHECKPKG_MODULE_NAME = "obsolete dependencies"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
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

def CheckObsoleteDeps(pkg_data, debug):
  """Checks for obsolete dependencies."""
  errors = []
  deps = set(pkg_data["depends"])
  obsolete_pkg_deps = deps.intersection(set(OBSOLETE_DEPS))
  if obsolete_pkg_deps:
    for obsolete_pkg in obsolete_pkg_deps:
      msg = ""
      if "hint" in OBSOLETE_DEPS[obsolete_pkg]:
        msg += "Hint: %s" % OBSOLETE_DEPS[obsolete_pkg]["hint"]
      if "url" in OBSOLETE_DEPS[obsolete_pkg]:
        if msg:
          msg += ", "
        msg += "URL: %s" % OBSOLETE_DEPS[obsolete_pkg]["url"]
      if not msg:
        msg = None
      errors.append(
          checkpkg.CheckpkgTag(
    	      pkg_data["basic_stats"]["pkgname"],
            "obsolete-dependency", obsolete_pkg, msg=msg))
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
  check_manager.RegisterIndividualCheck(CheckObsoleteDeps)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
