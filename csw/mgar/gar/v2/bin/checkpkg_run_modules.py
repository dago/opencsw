#!/opt/csw/bin/python2.6
# $Id$

"""This script runs all the checks written in Python."""

import datetime
import logging
import os
import os.path
import sys
import re
import cProfile

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
  screen_report = unicode(screen_report)
  if not options.quiet and screen_report:
    sys.stdout.write(screen_report)
  else:
    logging.debug("No screen report.")
  sys.exit(exit_code)


if __name__ == '__main__':
  if "--profile" in sys.argv:
    t_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    home = os.environ["HOME"]
    cprof_file_name = os.path.join(
        home, ".checkpkg", "run-modules-%s.cprof" % t_str)
    cProfile.run("main()", sort=1, filename=cprof_file_name)
  else:
    main()
