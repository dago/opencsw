#!/opt/csw/bin/python2.6
#
# $Id$
#
# Collects statistics about a package and saves to a directory, for later use
# by checkpkg modules.

import logging
import optparse
import os
import os.path
import subprocess
import sys

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


def main():
  debug = True
  logging.basicConfig(level=logging.DEBUG)
  parser = optparse.OptionParser()
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.INFO)
  logging.info("Collecting statistics about given package files.")
  logging.debug("args: %s", args)
  packages = [opencsw.CswSrv4File(x, debug) for x in args]
  stats_list = [checkpkg.PackageStats(pkg) for pkg in packages]
  for pkg_stats in stats_list:
  	pkg_stats.CollectStats()

if __name__ == '__main__':
	main()
