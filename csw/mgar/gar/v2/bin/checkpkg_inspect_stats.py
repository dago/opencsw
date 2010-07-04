#!/opt/csw/bin/python2.6
# coding=utf-8

import code
import logging
import optparse
import os
import pprint
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
  filenames = args
  srv4_pkgs = [opencsw.CswSrv4File(x) for x in filenames]
  pkgstats = [checkpkg.PackageStats(x) for x in srv4_pkgs]
  pkgstats = [x.GetAllStats() for x in pkgstats]
  code.interact(local=locals())

if __name__ == '__main__':
	main()
