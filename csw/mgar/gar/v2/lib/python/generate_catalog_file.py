#!/usr/bin/env python

"""Generates a catalog file from the REST interface.

Does not require a database connection.

PKG_DATA_1 = {
        "basename": "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz",
        "catalogname": "389_admin",
        "file_basename": "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz",
        "md5_sum": "fdb7912713da36afcbbe52266c15cb3f",
        "mtime": "2012-05-02 12:06:38",
        "rev": "2012.05.02",
        "size": 395802,
        "version": "1.1.29,REV=2012.05.02",
        "version_string": "1.1.29,REV=2012.05.02"
}

"""

CATALOG_FN = "catalog"
DESC_FN = "descriptions"

import rest
import os
import optparse
import logging
import sys


class Error(Exception):
  """A general error."""

class CatalogFileGenerator(object):

  def __init__(self, catrel, arch, osrel,
               pkgcache=None, rest_client=None):
    self.catrel = catrel
    self.arch = arch
    self.osrel = osrel
    home_dir = os.environ['HOME']
    self.pkgcache = pkgcache or rest.CachedPkgstats(os.path.join(home_dir, "pkgstats"))
    self.rest_client = rest_client or rest.RestClient()
    self._catalog = None

  @property
  def catalog(self):
    if not self._catalog:
      self._catalog = self.rest_client.GetCatalog(self.catrel, self.arch, self.osrel)
    return self._catalog

  def ComposeCatalogLine(self, pkg_data):
    catalog_data = self.rest_client.GetCatalogData(pkg_data["md5_sum"])
    i_deps = catalog_data["i_deps"]
    if i_deps:
      i_deps = "|".join(i_deps)
    else:
      i_deps = "none"
    deps = []
    for dep, _ in catalog_data["deps"]:
      if "CSW" in dep:
        deps.append(dep)
    if deps:
      deps = "|".join(deps)
    else:
      deps = "none"
    items = [
        pkg_data["catalogname"],
        pkg_data["version_string"],
        catalog_data["pkgname"],
        pkg_data["basename"],
        pkg_data["md5_sum"],
        unicode(pkg_data["size"]),
        deps,
        "none",
        i_deps]
    return " ".join(items)

  def GenerateCatalog(self, out_dir):
    out_file = os.path.join(out_dir, CATALOG_FN)
    if os.path.exists(out_file):
      raise Error("File %s already exists." % out_file)
    lines = self._GenerateCatalogAsLines()
    with open(out_file, "w") as fd:
      fd.write("\n".join(lines).encode('utf-8'))

  def _GenerateCatalogAsLines(self):
    """Return the complete catalog as a list of lines."""
    lines = []
    # Potential additional lines might go here.
    # liens.append("...")
    if self.catalog:  # the catalog might be None
      for pkg_data in self.catalog:
        lines.append(self.ComposeCatalogLine(pkg_data))
    return lines

  def GenerateDescriptions(self, out_dir):
    out_file = os.path.join(out_dir, DESC_FN)
    if os.path.exists(out_file):
      raise Error("File %s already exists." % out_file)
    lines = []
    if self.catalog:
      for pkg_data in self.catalog:
        catalog_data = self.pkgcache.GetDeps(pkg_data["md5_sum"])
        lines.append(catalog_data['pkginfo_name'])
    with open(out_file, "w") as fd:
      fd.write("\n".join(lines).encode('utf-8'))


def main():
  logging.basicConfig(level=logging.DEBUG)
  parser = optparse.OptionParser()
  parser.add_option("--out-dir", dest="out_dir")
  parser.add_option("--catalog-release", dest="catrel")
  parser.add_option("--arch", dest="arch")
  parser.add_option("--os-release", dest="osrel")
  options, args = parser.parse_args()
  cfg = CatalogFileGenerator(options.catrel, options.arch, options.osrel)
  cfg.GenerateCatalog(options.out_dir)
  cfg.GenerateDescriptions(options.out_dir)


if __name__ == '__main__':
  main()
