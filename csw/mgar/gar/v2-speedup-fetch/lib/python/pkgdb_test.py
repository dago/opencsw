#!/usr/bin/env python2.6

import unittest
import pkgdb
import logging

class CatalogImporterUnitTest(unittest.TestCase):

  def testComposeCatalogFilePath(self):
    ci = pkgdb.CatalogImporter()
    self.assertEquals(
        "/home/mirror/opencsw/current/sparc/5.9/catalog",
        ci.ComposeCatalogFilePath("/home/mirror/opencsw/current", "SunOS5.9", "sparc"))


class FunctionUnitTest(unittest.TestCase):

  def testNormalizeIdentifier(self):
    self.assertEqual("baz", pkgdb.NormalizeId("/foo/bar/baz"))


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  unittest.main()
