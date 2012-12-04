#!/opt/csw/bin/python2.6
# coding=utf-8

import code
import itertools
import logging
import optparse
import os
import pprint
import sys
import re
import progressbar

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw
import configuration

def main():
  usage = "Usage: %prog [ options ] file | md5 [ file | md5 [ ... ] ]"
  parser = optparse.OptionParser(usage)
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-p", "--print_stats", dest="print_stats",
                    default=False, action="store_true")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  logging.debug("Collecting statistics about given package files.")
  configuration.SetUpSqlobjectConnection()
  pkgstat_objs = checkpkg.GetPackageStatsByFilenamesOrMd5s(
      args,
      options.debug)
  bar = progressbar.ProgressBar()
  bar.maxval = len(pkgstat_objs)
  bar.start()
  counter = itertools.count()
  pkgstats = []
  for pkgstat in pkgstat_objs:
    pkgstats.append(pkgstat.GetAllStats())
    bar.update(counter.next())
  bar.finish()
  if options.print_stats:
    print "import datetime"
    print "pkgstat_objs = ",
    pprint.pprint(pkgstats)
  else:
    code.interact(local=locals())

if __name__ == '__main__':
  main()
