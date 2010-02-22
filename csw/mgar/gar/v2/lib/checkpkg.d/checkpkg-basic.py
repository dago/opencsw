#!/opt/csw/bin/python2.6
# $Id: checkpkg-you-can-write-your-own.py 8571 2010-02-16 09:05:51Z wahwah $

"""This is a dummy module. You can use it as a boilerplate for your own modules.

Copy it and modify.
"""

import os.path
import sys

CHECKPKG_MODULE_NAME = "basic checks ported from Korn shell"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import package_checks

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
  check_manager.RegisterIndividualCheck(package_checks.CatalognameLowercase)
  check_manager.RegisterIndividualCheck(package_checks.FileNameSanity)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
