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


class Error(Exception):
  """A general error."""

class CatalogFileGenerator(object):

  def __init__(self, catrel, arch, osrel,
               pkgcache=None, rest_client=None):
    self.catrel = catrel
    self.arch = arch
    self.osrel = osrel
    self.pkgcache = pkgcache or rest.CachedPkgstats("/home/web/pkgstats")
    self.rest_client = rest_client or rest.RestClient()
    self._catalog = None

  @property
  def catalog(self):
    if not self._catalog:
      self._catalog = self.rest_client.GetCatalog(self.catrel, self.arch, self.osrel)
    return self._catalog

  def ComposeCatalogLine(self, pkg_data):
    deps_data = self.pkgcache.GetDeps(pkg_data["md5_sum"])
    pkg_stats = self.pkgcache.GetPkgstats(pkg_data["md5_sum"])
    i_deps = pkg_stats["i_depends"]
    if i_deps:
      i_deps = "|".join(i_deps)
    else:
      i_deps = "none"
    deps = []
    for dep, _ in deps_data["deps"]:
      if "CSW" in dep:
        deps.append(dep)
    if deps:
      deps = "|".join(deps)
    else:
      deps = "none"
    items = [
        pkg_data["catalogname"],
        pkg_data["version_string"],
        deps_data["pkgname"],
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
    lines = []
    for pkg_data in self.catalog:
      lines.append(self.ComposeCatalogLine(pkg_data))
    with open(out_file, "w") as fd:
      fd.write("\n".join(lines))

  def GenerateDescriptions(self, out_dir):
    out_file = os.path.join(out_dir, DESC_FN)
    if os.path.exists(out_file):
      raise Error("File %s already exists." % out_file)
    lines = []
    for pkg_data in self.catalog:
      pkg_stats = self.pkgcache.GetPkgstats(pkg_data["md5_sum"])
      lines.append(pkg_stats["pkginfo"]["NAME"])
    with open(out_file, "w") as fd:
      fd.write("\n".join(lines))


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
