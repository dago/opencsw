#!/opt/csw/bin/python2.6
#
# $Id$
#
# This file only creates an instance of SystemPkgmap in order to update the
# package cache (if necessary), and display the information about the update.

import checkpkg
import logging


def main():
  print "Checking if the package cache is up to date."
  logging.basicConfig(level=logging.INFO)
  test_pkgmap = checkpkg.SystemPkgmap()


if __name__ == '__main__':
	main()
