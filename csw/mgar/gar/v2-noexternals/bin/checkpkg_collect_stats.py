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
import progressbar

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw
import package_stats

def main():
  parser = optparse.OptionParser()
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-c", "--catalog", dest="catalog",
                    help="Catalog file")
  parser.add_option("-p", "--profile", dest="profile",
                    default=False, action="store_true",
                    help="A disabled option")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  logging.debug("Collecting statistics about given package files.")
  args_display = args
  if len(args_display) > 5:
    args_display = args_display[:5] + ["...more..."]
  file_list = args
  logging.debug("Processing: %s, please be patient", args_display)
  stats_list = package_stats.StatsListFromCatalog(
      file_list, options.catalog, options.debug)
  # Reversing the item order in the list, so that the pop() method can be used
  # to get packages, and the order of processing still matches the one in the
  # catalog file.
  stats_list.reverse()
  total_packages = len(stats_list)
  counter = itertools.count(1)
  logging.info("Juicing the srv4 package stream files...")
  bar = progressbar.ProgressBar()
  bar.maxval = total_packages
  bar.start()
  while stats_list:
    # This way objects will get garbage collected as soon as they are removed
    # from the list by pop().  The destructor (__del__()) of the srv4 class
    # removes the temporary directory from the disk.  This allows to process
    # the whole catalog.
    stats_list.pop().CollectStats()
    bar.update(counter.next())
  bar.finish()

if __name__ == '__main__':
  main()
