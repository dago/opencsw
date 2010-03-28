#!/opt/csw/bin/python2.6
# $Id$

"""This script runs all the checks written in Python."""

import logging
import os.path
import sys
import re

CHECKPKG_MODULE_NAME = "Second checkpkg API version"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


def main():
  options, args = checkpkg.GetOptions()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  md5sums = args
  # CheckpkgManager2 class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager2(CHECKPKG_MODULE_NAME,
                                            options.stats_basedir,
                                            md5sums,
                                            options.debug)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  if screen_report:
    sys.stdout.write(screen_report)
  else:
    logging.debug("No screen report.")
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
