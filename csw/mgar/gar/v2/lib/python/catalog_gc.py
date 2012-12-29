#!/opt/csw/bin/python2.6

"""Garbage-collecting for the catalog tree.

The allpkgs directory may contain unused files.  They should be deleted.
"""

import logging
import optparse
import os
import pipes
import re
import common_constants
import rest

USAGE = """%prog --catalog-tree /home/mirror/opencsw-official --dest_dir /home/mirror/gc > gc_01.sh
less gc_01.sh

# Looks good?

bash gc_01.sh

If everything is fine (catalog still generates, no files are missing that are
necessary), you can remove files from /home/mirror/gc.
"""

class Error(Exception):
  """Base error."""

class UsageError(Error):
  """Wrong usage."""


class CatalogGarbageCollector(object):

  ADDITIONAL_CATALOGS = ("legacy",)

  def __init__(self, d, dest_dir):
    logging.debug("CatalogGarbageCollector(%s)", repr(d))
    self.catalog_dir = d
    self.dest_dir = dest_dir

  def GarbageCollect(self):
    allpkgs_path = os.path.join(self.catalog_dir, "allpkgs")
    allpkgs = set()
    files_in_catalogs = set()
    catalogs_by_files = {}
    for p in os.listdir(allpkgs_path):
      allpkgs.add(p)
    catalogs_to_check = tuple(common_constants.DEFAULT_CATALOG_RELEASES)
    catalogs_to_check += self.ADDITIONAL_CATALOGS
    rest_client = rest.RestClient()
    catalog_triplet_list = rest_client.GetCatalogList()
    catalogs_to_check += tuple(set([x[2] for x in catalog_triplet_list]))
    catalogs_to_check = tuple(set(catalogs_to_check))
    logging.info("Collecting packages from catalogs: %s",
                 catalogs_to_check)
    file_sizes = {}
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
              full_path = os.path.join(catalog_path, p)
              files_in_catalogs.add(p)
              l = catalogs_by_files.setdefault(p, [])
              l.append((catrel, arch, osrel_short))
              if full_path not in file_sizes:
                s = os.stat(full_path)
                file_sizes[full_path] = s.st_size
      logging.info(
          "Collected from %r, found references to %d files (out of %d in allpkgs)",
          catrel, len(files_in_catalogs), len(allpkgs))
    to_remove = allpkgs.difference(files_in_catalogs)
    logging.debug("Collecting file sizes.")
    total_size = sum(os.stat(os.path.join(allpkgs_path, x)).st_size
                     for x in to_remove)
    logging.info("Found %d packages to remove, total size: %.1fMB.",
                 len(to_remove), float(total_size) / 1024 ** 2)
    for p in to_remove:
      full_path = os.path.join(allpkgs_path, p)
      print "mv", pipes.quote(full_path), pipes.quote(self.dest_dir)


def main():
  parser = optparse.OptionParser()
  parser.add_option("--catalog-tree",
      dest="catalog_tree",
      help=("Path to the catalog tree, that is the directory "
            "containing subdirectories unstable, testing, etc."))
  parser.add_option("--dest-dir",
      dest="dest_dir",
      help=("Move files out to this catalog."))
  options, args = parser.parse_args()
  logging.basicConfig(level=logging.DEBUG)
  if not options.catalog_tree or not options.dest_dir:
    parser.print_usage()
    raise UsageError("Missing the catalog tree option, see --help.")
  gcg = CatalogGarbageCollector(options.catalog_tree, options.dest_dir)
  gcg.GarbageCollect()


if __name__ == '__main__':
  main()
