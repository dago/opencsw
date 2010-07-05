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


def main():
  parser = optparse.OptionParser()
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-c", "--catalog", dest="catalog_file",
                    help="Catalog file")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  logging.debug("Collecting statistics about given package files.")
  args_display = args
  if len(args_display) > 5:
    args_display = args_display[:5] + ["...more..."]
  logging.debug("Processing: %s, please be patient", args_display)
  packages = [opencsw.CswSrv4File(x, options.debug) for x in args]
  if options.catalog_file:
    # Using cached md5sums to save time: injecting md5sums
    # from the catalog.
    catalog = opencsw.OpencswCatalog(options.catalog_file)
    md5s_by_basename = catalog.GetDataByBasename()
    for pkg in packages:
      basename = os.path.basename(pkg.pkg_path)
      # It might be the case that a file is present on disk, but missing from
      # the catalog file.
      if basename in md5s_by_basename:
        pkg.md5sum = md5s_by_basename[basename]["md5sum"]
  stats_list = [checkpkg.PackageStats(pkg) for pkg in packages]
  md5s_by_basename = None # To free memory
  catalog = None          # To free memory
  del(packages)
  stats_list.reverse()
  total_packages = len(stats_list)
  counter = itertools.count(1)
  bar = progressbar.ProgressBar()
  bar.maxval = total_packages
  bar.start()
  logging.debug("Making sure package statistics are collected.")
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
