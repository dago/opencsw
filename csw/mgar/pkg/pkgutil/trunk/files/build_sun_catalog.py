#!/opt/csw/bin/python2.6
# coding=utf-8
"""Builds a SUNW catalog in the OpenCSW format.

$Id: build_sun_catalog.py 107 2009-12-08 18:32:37Z wahwah $
"""

__author__ = "Maciej Bliziński <blizinski@google.com>"

import os
import os.path
import logging
import opencsw
import optparse
import shutil
import subprocess
import tempfile


def main():
  parser = optparse.OptionParser()
  parser.add_option("-p", "--product", dest="product_dir",
             help="Product dir, e.g. .../Solaris_10/Product")
  parser.add_option("-c", "--catalog-dir", dest="catalog_dir",
             help="Target catalog dir")
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.DEBUG)
  options_ok = True
  if not options.product_dir:
    logging.error("--product directory is required. See --help.")
    options_ok = False
  if not options.catalog_dir:
    logging.error("--catalog-dir is required. See --help.")
    options_ok = False
  if options_ok:
    b = opencsw.OpencswCatalogBuilder(options.product_dir,
                                      options.catalog_dir)
    b.Run()


if __name__ == "__main__":
  main()
