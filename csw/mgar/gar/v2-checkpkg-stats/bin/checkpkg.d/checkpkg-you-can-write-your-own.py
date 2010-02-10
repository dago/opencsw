#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy module. You can use it as a boilerplate for your own modules.

Copy it and modify.
"""

import os.path
import sys

CHECKPKG_MODULE_NAME = "a template of a checkpkg module"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

# Defining the checking functions.  They come in two flavors: individual
# package checks and set checks.

def MyCheckForAsinglePackage(pkg, debug):
  """Checks an individual package.
  
  Gets a DirctoryFormatPackage as an argument, and returns a list of errors.

  Errors should be a list of checkpkg.CheckpkgTag objects:
  errors.append(checkpkg.CheckpkgTag(pkg.pkgname, "tag-name"))

  You can also add a parameter:
  errors.append(checkpkg.CheckpkgTag(pkg.pkgname, "tag-name", "/opt/csw/bin/problem"))
  """
  errors = []
  # Checking code for an individual package goes here.  See the
  # DirectoryFormatPackage class in lib/python/opencsw.py for the available
  # APIs.

  # Here's how to report an error:
  something_is_wrong = False
  if something_is_wrong:
    errors.append(checkpkg.CheckpkgTag(pkg.pkgname, "example-problem", "thing"))
  return errors


def MyCheckForAsetOfPackages(pkgs, debug):
  """Checks a set of packages.

  Sometimes individual checks aren't enough. If you need to write code which
  needs to examine multiple packages at the same time, use this function.

  Gets a list of packages, returns a list of errors.
  """
  errors = []
  # Checking code goes here.
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.extractdir,
                                           pkgnames,
                                           options.debug)
  # Registering functions defined above.
  check_manager.RegisterIndividualCheck(MyCheckForAsinglePackage)
  check_manager.RegisterSetCheck(MyCheckForAsetOfPackages)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
