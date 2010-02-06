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

def CheckLicenseFile(pkg, debug):
  """Checks for the presence of the license file."""
  errors = []
  pkgmap = pkg.GetPkgmap()
  catalogname = pkg.GetCatalogname()
  license_path = LICENSE_TMPL % catalogname
  if license_path not in pkgmap.entries_by_path:
    errors.append(
        checkpkg.CheckpkgTag(
          "license-missing",
          msg="See http://sourceforge.net/apps/trac/gar/wiki/CopyRight"))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.extractdir,
                                           pkgnames,
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
