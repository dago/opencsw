#!/usr/bin/env python

import unittest
import mox
import generate_catalog_file
import rest
import __builtin__
import io

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

FAKE_CATALOG_DATA = {
    "deps": [
      ["CSWfoo", ""],
      ["CSWbar", ""],
    ],
    "i_deps": [],
    "pkginfo_name": "389_admin - The 389 LDAP server Admin Tools",
    "pkgname": "CSW389-admin-mock",
}

EXPECTED_LINE = ("389_admin 1.1.29,REV=2012.05.02 CSW389-admin-mock "
                 "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz "
                 "fdb7912713da36afcbbe52266c15cb3f 395802 CSWfoo|CSWbar "
                 "none none")

class CatalogFileGeneratorUnitTest(mox.MoxTestBase):

  def testComposeCatalogLineBasic(self):
    mock_pkgcache = self.mox.CreateMock(rest.CachedPkgstats)
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
                                                     mock_pkgcache, mock_rest)
    md5_sum = 'fdb7912713da36afcbbe52266c15cb3f'
    mock_rest.GetCatalogData(md5_sum).AndReturn(FAKE_CATALOG_DATA)
    self.mox.ReplayAll()
    self.assertEquals(EXPECTED_LINE, cfg.ComposeCatalogLine(PKG_DATA_1))

  def testGenerateCatalogAsLines(self):
    mock_pkgcache = self.mox.CreateMock(rest.CachedPkgstats)
    mock_rest = self.mox.CreateMock(rest.RestClient)
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_pkgcache, mock_rest)
    md5_sum = 'fdb7912713da36afcbbe52266c15cb3f'
    mock_rest.GetCatalog('dublin', 'sparc', 'SunOS5.10').AndReturn([PKG_DATA_1])
    mock_rest.GetCatalogData(md5_sum).AndReturn(FAKE_CATALOG_DATA)
    self.mox.ReplayAll()
    self.assertEquals([
      # Potential additional lines go here.
      EXPECTED_LINE,
    ], cfg._GenerateCatalogAsLines())

  def testGenerateCatalog(self):
    mock_pkgcache = self.mox.CreateMock(rest.CachedPkgstats)
    mock_rest = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(__builtin__, 'open')
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_pkgcache, mock_rest)
    mock_rest.GetCatalog('dublin', 'sparc', 'SunOS5.10').AndReturn([PKG_DATA_1])
    md5_sum = 'fdb7912713da36afcbbe52266c15cb3f'
    mock_rest.GetCatalogData(md5_sum).AndReturn(FAKE_CATALOG_DATA)
    fake_file = io.BytesIO();
    open('fake-dir/catalog', 'w').AndReturn(fake_file)
    self.mox.ReplayAll()
    cfg.GenerateCatalog('fake-dir')

  def testGenerateDescriptions(self):
    mock_pkgcache = self.mox.CreateMock(rest.CachedPkgstats)
    mock_rest = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(__builtin__, 'open')
    cfg = generate_catalog_file.CatalogFileGenerator("dublin",
                                                     "sparc",
                                                     "SunOS5.10",
                                                     mock_pkgcache, mock_rest)
    md5_sum = 'fdb7912713da36afcbbe52266c15cb3f'
    mock_pkgcache.GetDeps(md5_sum).AndReturn(FAKE_CATALOG_DATA)
    mock_rest.GetCatalog('dublin', 'sparc', 'SunOS5.10').AndReturn([PKG_DATA_1])
    fake_file = io.BytesIO();
    open('fake-dir/descriptions', 'w').AndReturn(fake_file)
    self.mox.ReplayAll()
    cfg.GenerateDescriptions('fake-dir')


if __name__ == '__main__':
  unittest.main()
