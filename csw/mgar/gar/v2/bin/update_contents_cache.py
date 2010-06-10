#!/opt/csw/bin/python2.6
#
# $Id$
#
# This file only creates an instance of SystemPkgmap in order to update the
# package cache (if necessary), and display the information about the update.

import os
import os.path
import sys
import logging

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

def main():
  logging.basicConfig(level=logging.INFO)
  test_pkgmap = checkpkg.SystemPkgmap()
  test_pkgmap.InitializeDatabase()


if __name__ == '__main__':
  main()
