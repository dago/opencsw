#!/usr/bin/env python2.6

import unittest
import pkgdb

class CatalogImporterUnitTest(unittest.TestCase):

  def testComposeCatalogFilePath(self):
    ci = pkgdb.CatalogImporter()
    self.assertEquals(
        "/home/mirror/opencsw/current/sparc/5.9/catalog",
        ci.ComposeCatalogFilePath("/home/mirror/opencsw/current", "SunOS5.9", "sparc"))


if __name__ == '__main__':
  unittest.main()
