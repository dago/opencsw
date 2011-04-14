#!/usr/bin/env python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:
#
# Copyright (c) 2009 Maciej Bliziński
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.

"""Compares the contents of two svr4 packages.

The needed opencsw.py library is now at:
https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/python/

$Id: compare_pkgs.py 124 2010-02-18 07:28:10Z wahwah $
"""

import logging
import optparse
import opencsw
import package

USAGE = """Compares two packages with the same catalogname.

To use, place packages (say, foo-1.0,REV=1898.09.25-SunOS5.9-sparc-CSW.pkg.gz
and foo-1.0.1,REV=2010.09.25-SunOS5.9-sparc-CSW.pkg.gz) in two directories
(say, /a and /b), and issue:

  comparepkg --package-dir-a /a --package-dir-b /b --catalog-name foo
"""

def main():
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true")
  parser.add_option("-a", "--package-dir-a", dest="package_dir_a",
                    help="Package directory A")
  parser.add_option("-b", "--package-dir-b", dest="package_dir_b",
                    help="Package directory B")
  parser.add_option("-c", "--catalog-name", dest="catalog_name",
                    help="Catalog name, for example 'cups'")
  parser.add_option("-p", "--permissions", dest="permissions",
                    help="Whether to analyze permission bits",
                    default=False, action="store_true")
  parser.add_option("", "--strip-a", dest="strip_a",
                    help="Strip from paths in a")
  parser.add_option("", "--strip-b", dest="strip_b",
                    help="Strip from paths in b")
  (options, args) = parser.parse_args()
  if options.debug:
    current_logging_level = logging.DEBUG
  else:
    current_logging_level = logging.INFO
  logging.basicConfig(level=current_logging_level)
  pkg_dir_a = opencsw.StagingDir(options.package_dir_a)
  pkg_dir_b = opencsw.StagingDir(options.package_dir_b)
  pkg_path_a = pkg_dir_a.GetLatest(options.catalog_name)[-1]
  pkg_path_b = pkg_dir_b.GetLatest(options.catalog_name)[-1]
  pc = package.PackageComparator(
                         pkg_path_a,
                         pkg_path_b,
                         permissions=options.permissions,
                         strip_a=options.strip_a,
                         strip_b=options.strip_b)
  pc.Run()


if __name__ == '__main__':
  main()
