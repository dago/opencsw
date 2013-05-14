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
import datetime
import representations


class Error(Exception):
  """A general error."""

class CatalogFileGenerator(object):

  def __init__(self, catrel, arch, osrel,
               rest_client=None):
    self.catrel = catrel
    self.arch = arch
    self.osrel = osrel
    home_dir = os.environ['HOME']
    self.rest_client = rest_client or rest.RestClient()
    self._catalog = None

  @property
  def catalog(self):
    if not self._catalog:
      self._catalog = self.rest_client.GetCatalogForGeneration(self.catrel,
                                                               self.arch,
                                                               self.osrel)
      try:
        self._catalog = [representations.CatalogEntry._make(x)
                         for x in self._catalog]
      except TypeError:
        print self._catalog
        raise
    return self._catalog

  def ComposeCatalogLine(self, catalog_entry):
    items = tuple(catalog_entry)[:9]
    return " ".join(items)

  def GenerateCatalog(self, out_dir):
    out_catalog = os.path.join(out_dir, CATALOG_FN)
    out_desc = os.path.join(out_dir, DESC_FN)
    if os.path.exists(out_catalog):
      raise Error("File %s already exists." % out_catalog)
    if os.path.exists(out_desc):
      raise Error("File %s already exists." % out_desc)
    lines, descriptions = self._GenerateCatalogAsLines()
    with open(out_catalog, "w") as fd:
      fd.write("\n".join(lines).encode('utf-8'))
    with open(out_desc, "w") as fd:
      fd.write("\n".join(descriptions).encode('utf-8'))

  def _GenerateCatalogAsLines(self):
    """Return the complete catalog as a list of lines."""
    lines = []
    descriptions = []
    date_iso = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
    lines.append("# CREATIONDATE %sZ" % date_iso)

    # Potential additional lines might go here.
    # lines.append("...")
    if self.catalog:  # the catalog might be None
      for catalog_entry in self.catalog:
        lines.append(self.ComposeCatalogLine(catalog_entry))
        descriptions.append(catalog_entry.desc)
    return lines, descriptions


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


if __name__ == '__main__':
  main()
