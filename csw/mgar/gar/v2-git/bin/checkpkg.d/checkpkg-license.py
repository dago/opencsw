#!/opt/csw/bin/python2.6
# $Id$

"""Checks for the existence of the license file."""

import logging
import os.path
import sys

CHECKPKG_MODULE_NAME = "license presence"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw

LICENSE_TMPL = "/opt/csw/share/doc/%s/license"

def CheckLicenseFile(pkg_data, debug):
  """Checks for the presence of the license file."""
  errors = []
  pkgmap = pkg_data["pkgmap"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  license_path = LICENSE_TMPL % catalogname
  pkgmap_paths = [x["path"] for x in pkgmap]
  if license_path not in pkgmap_paths:
    errors.append(
        checkpkg.CheckpkgTag(
          pkg_data["basic_stats"]["pkgname"],
          "license-missing",
          msg="See http://sourceforge.net/apps/trac/gar/wiki/CopyRight"))
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
  # Registering functions defined above.
  check_manager.RegisterIndividualCheck(CheckLicenseFile)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
