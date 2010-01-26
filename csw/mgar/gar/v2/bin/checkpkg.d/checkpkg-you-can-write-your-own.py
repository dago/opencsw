#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy check. You can use it as a boilerplate for your own checks.

Copy it and modify.
"""

import logging
import os.path
import sys

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

# Defining checking functions.

def CheckIndividualPackage(pkg):
  """Checks an individual package.
  
  Gets a DirctoryFormatPackage as an argument, and returns a list of errors.

  Errors should be a list of checkpkg.PackageError objects:

  errors.append(checkpkg.PackageError("There's something wrong."))
  """
  errors = []
  # Checking code for an individual package goes here.
  return errors


def CheckAsetOfPackages(pkgs):
  """Checks a set of packages.

  Sometimes individual checks aren't enough. If you need to write code which
  needs to examine multiple packages at the same time, use this function.

  Gets a list of packages.
  """
  errors = []
  # Checking code goes here.
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager("a template of a checkpkg module",
                                           options.extractdir,
                                           pkgnames,
                                           options.debug)
  # Registering previously defined checks.
  check_manager.RegisterIndividualCheck(CheckIndividualPackage)
  check_manager.RegisterSetCheck(CheckAsetOfPackages)
  # Running the checks, reporting and exiting.
  exit_code, report = check_manager.Run()
  print report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
