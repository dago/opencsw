#!/opt/csw/bin/python2.6

"""Garbage-collecting for a catalog.

The allpkgs directory may contain unused files.  They should be deleted.
"""

import optparse
import logging
import os.path
import re
import common_constants

class Error(Exception):
  """Base error."""

class UsageError(Error):
  """Wrong usage."""


class CatalogGarbageCollector(object):

  ADDITIONAL_CATALOGS = ("legacy")

  def __init__(self, d):
    logging.debug("CatalogGarbageCollector(%s)", repr(d))
    self.catalog_dir = d

  def GarbageCollect(self):
    allpkgs_path = os.path.join(self.catalog_dir, "allpkgs")
    allpkgs = set()
    files_in_catalogs = set()
    catalogs_by_files = {}
    for p in os.listdir(allpkgs_path):
      allpkgs.add(p)
    catalogs_to_check = (
        tuple(common_constants.DEFAULT_CATALOG_RELEASES)
        + self.ADDITIONAL_CATALOGS)
    for catrel in catalogs_to_check:
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        for osrel_long in common_constants.OS_RELS:
          osrel_short = re.sub(r"^SunOS", r"", osrel_long)
          catalog_path = os.path.join(
              self.catalog_dir, catrel, arch, osrel_short)
          if not os.path.exists(catalog_path):
            logging.debug("%s does not exist", catalog_path)
            continue
          pkg_re = re.compile(r"\.pkg(\.gz)?$")
          for p in os.listdir(catalog_path):
            if pkg_re.search(p):
              # It's a package
              files_in_catalogs.add(p)
              l = catalogs_by_files.setdefault(p, [])
              l.append((catrel, arch, osrel_short))
    for p in allpkgs.difference(files_in_catalogs):
      logging.debug("File %s is not used by any catalogs.", p)
      print "rm %s/%s" % (allpkgs_path, p)


def main():
  parser = optparse.OptionParser()
  parser.add_option("-c", "--catalog",
      dest="catalog",
      help="Catalog path")
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.DEBUG)
  if not options.catalog:
    parser.print_usage()
    raise UsageError("Missing catalog option, see --help.")
  gcg = CatalogGarbageCollector(options.catalog)
  gcg.GarbageCollect()


if __name__ == '__main__':
  main()
