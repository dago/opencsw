#!/opt/csw/bin/python2.6

"""Garbage-collecting for the catalog tree.

The allpkgs directory may contain unused files.  They should be deleted.
"""

import logging
import optparse
import os.path
import pipes
import re
import common_constants

USAGE = """%prog --catalog-tree /home/mirror/opencsw-official > gc_01.sh
less gc_01.sh

# Looks good?

bash gc_01.sh
"""

class Error(Exception):
  """Base error."""

class UsageError(Error):
  """Wrong usage."""


class CatalogGarbageCollector(object):

  ADDITIONAL_CATALOGS = ("legacy",)

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
      print "rm", pipes.quote(os.path.join(allpkgs_path, p))


def main():
  parser = optparse.OptionParser()
  parser.add_option("--catalog-tree",
      dest="catalog_tree",
      help=("Path to the catalog tree, that is the directory "
            "containing subdirectories unstable, testing, etc."))
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.DEBUG)
  if not options.catalog_tree:
    parser.print_usage()
    raise UsageError("Missing the catalog tree option, see --help.")
  gcg = CatalogGarbageCollector(options.catalog_tree)
  gcg.GarbageCollect()


if __name__ == '__main__':
  main()
