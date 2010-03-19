#!/opt/csw/bin/python2.6
#
# $Id$
#
# Collects statistics about a package and saves to a directory, for later use
# by checkpkg modules.

import itertools
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
  parser = optparse.OptionParser()
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  logging.debug("Collecting statistics about given package files.")
  logging.debug("calling: %s, please be patient", args)
  packages = [opencsw.CswSrv4File(x, options.debug) for x in args]
  stats_list = [checkpkg.PackageStats(pkg) for pkg in packages]
  del(packages)
  stats_list.reverse()
  total_packages = len(stats_list)
  counter = itertools.count(1)
  while stats_list:
    # This way objects will get garbage collected as soon as they are removed
    # from the list by pop().  The destructor (__del__()) of the srv4 class
    # removes the temporary directory from the disk.  This allows to process
    # the whole catalog.
    stats_list.pop().CollectStats()
    logging.debug("Collected stats %s of %s.", counter.next(), total_packages)

if __name__ == '__main__':
  main()
