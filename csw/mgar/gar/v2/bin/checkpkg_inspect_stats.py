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
  filenames = []
  md5s = []
  md5_re = re.compile(r"^[0123456789abcdef]{32}$")
  for arg in args:
    if md5_re.match(arg):
      md5s.append(arg)
    else:
      filenames.append(arg)
  srv4_pkgs = [opencsw.CswSrv4File(x) for x in filenames]
  pkgstat_objs = []
  bar = progressbar.ProgressBar()
  bar.maxval = len(md5s) + len(srv4_pkgs)
  bar.start()
  counter = itertools.count()
  for pkg in srv4_pkgs:
    pkgstat_objs.append(checkpkg.PackageStats(pkg, debug=options.debug))
    bar.update(counter.next())
  for md5 in md5s:
    pkgstat_objs.append(checkpkg.PackageStats(None, md5sum=md5, debug=options.debug))
    bar.update(counter.next())
  bar.finish()
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
