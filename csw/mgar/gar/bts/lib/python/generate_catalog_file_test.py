#!/usr/bin/env python

import unittest
import mox
import generate_catalog_file
import rest

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
    cfg = generate_catalog_file.CatalogFileGenerator("dublin", "sparc", "SunOS5.10", mock_pkgcache, mock_rest)
    mock_pkgcache.GetDeps('fdb7912713da36afcbbe52266c15cb3f').AndReturn(
        {
          "pkgname": "CSW389-admin-mock",
          "deps": [
            ["CSWfoo", ""],
            ["CSWbar", ""],
          ]
        }
    )
    mock_pkgcache.GetPkgstats('fdb7912713da36afcbbe52266c15cb3f').AndReturn(
        # {"i_depends": ["CSWincompatible", "CSWzorg"]}
        {"i_depends": []}
    )
    self.mox.ReplayAll()
    self.assertEquals(
        "389_admin "
        "1.1.29,REV=2012.05.02 "
        "CSW389-admin-mock "
        "389_admin-1.1.29,REV=2012.05.02-SunOS5.10-sparc-CSW.pkg.gz "
        "fdb7912713da36afcbbe52266c15cb3f "
        "395802 "
        "CSWfoo|CSWbar "
        "none none",
        cfg.ComposeCatalogLine(PKG_DATA_1))


if __name__ == '__main__':
  unittest.main()
