#!/usr/bin/env python

import __builtin__
import datetime
import io
import mox
import rest
import unittest2 as unittest

from lib.python import generate_catalog_file

PKG_DATA_1 = [
        ["389_admin", "1.1.29,REV=2012.05.02",
         "CSW389-admin-mock",
         "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz",
         "fdb7912713da36afcbbe52266c15cb3f",
         "395802", "CSWfoo|CSWbar", "none", "none",
         "389_admin - The 389 LDAP server Admin Tools"],
]

EXPECTED_LINE = ("389_admin 1.1.29,REV=2012.05.02 CSW389-admin-mock "
                 "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz "
                 "fdb7912713da36afcbbe52266c15cb3f 395802 CSWfoo|CSWbar "
                 "none none")

class CatalogFileGeneratorUnitTest(mox.MoxTestBase, unittest.TestCase):

  def testComposeCatalogLineBasic(self):
    mock_rest = self.mox.CreateMock(rest.RestClient)
    # Catalog format:
    #   http://wiki.opencsw.org/catalog-format
    #   common version package file md5 size dependencies category i-dependencies
    # For example:
    #   bind 9.4.2,REV=2008.07.09_rev=p1 CSWbind
    #   bind-9.4.2,REV=2008.07.09_rev=p1-SunOS5.8-sparc-CSW.pkg.gz
    #   f68df57fcf54bfd37304b79d6f7eeacc 2954112 CSWcommon|CSWosslrt net none
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_rest)
    self.mox.ReplayAll()
    self.assertEquals(EXPECTED_LINE, cfg.ComposeCatalogLine(PKG_DATA_1[0]))

  def testGenerateCatalogEmpty(self):
    mock_rest = self.mox.CreateMock(rest.RestClient)
    fake_datetime = datetime.datetime(year=2013, month=4, day=1,
                                      hour=11, minute=11, second=11)
    self.mox.StubOutWithMock(datetime, 'datetime')
    datetime.datetime.utcnow().AndReturn(fake_datetime)
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_rest)
    mock_rest.GetCatalogForGeneration('dublin', 'sparc', 'SunOS5.10').AndReturn([])
    self.mox.ReplayAll()
    catalog_lines, descriptions = cfg._GenerateCatalogAsLines()
    expected_lines = [
      "# CREATIONDATE 2013-04-01T11:11:11Z",
    ]
    self.assertEquals(expected_lines, catalog_lines)
    self.assertEquals([], descriptions)

  def testGenerateCatalogAsLines(self):
    mock_rest = self.mox.CreateMock(rest.RestClient)
    fake_datetime = datetime.datetime(year=2013, month=4, day=1,
                                      hour=11, minute=11, second=11)
    self.mox.StubOutWithMock(datetime, 'datetime')
    datetime.datetime.utcnow().AndReturn(fake_datetime)
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_rest)
    mock_rest.GetCatalogForGeneration('dublin', 'sparc', 'SunOS5.10').AndReturn(PKG_DATA_1)
    self.mox.ReplayAll()
    catalog_lines, descriptions = cfg._GenerateCatalogAsLines()
    expected_lines = [
      "# CREATIONDATE 2013-04-01T11:11:11Z",
      EXPECTED_LINE,
    ]
    self.assertEquals(expected_lines, catalog_lines)
    self.assertEquals(['389_admin - The 389 LDAP server Admin Tools'], descriptions)

  def testGenerateCatalog(self):
    mock_rest = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(__builtin__, 'open')
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_rest)
    mock_rest.GetCatalogForGeneration('dublin', 'sparc', 'SunOS5.10').AndReturn(PKG_DATA_1)
    fake_file = io.BytesIO()
    fake_desc_file = io.BytesIO()
    open('fake-dir/catalog', 'w').AndReturn(fake_file)
    open('fake-dir/descriptions', 'w').AndReturn(fake_desc_file)
    self.mox.ReplayAll()
    cfg.GenerateCatalog('fake-dir')


if __name__ == '__main__':
  unittest.main()
