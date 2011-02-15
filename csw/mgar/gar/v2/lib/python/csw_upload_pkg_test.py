#!/usr/bin/env python2.6

import unittest
import csw_upload_pkg
import mox
import rest
import copy

GDB_STRUCT_9 = {
    "arch": "sparc",
    "basename": "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
    "catalogname": "gdb",
    "filename_arch": "sparc",
    "maintainer_email": "pfele...@opencsw.org",
    "maintainer_full_name": None,
    "md5_sum": "7971e31461b53638d7813407fab4765b",
    "mtime": "2011-01-24 03:09:54",
    "osrel": "SunOS5.9",
    "pkgname": "CSWgdb",
    "rev": "2011.01.21",
    "size": 7616184,
    "version_string": "7.2,REV=2011.01.21",
}
GDB_STRUCT_10 = {
    "arch": "sparc",
    "basename": "gdb-7.2,REV=2011.01.21-SunOS5.10-sparc-CSW.pkg.gz",
    "catalogname": "gdb",
    "filename_arch": "sparc",
    "maintainer_email": "pfele...@opencsw.org",
    "maintainer_full_name": None,
    "md5_sum": "09cccf8097e982dadbd717910963e378",
    "mtime": "2011-01-24 03:10:05",
    "osrel": "SunOS5.10",
    "pkgname": "CSWgdb",
    "rev": "2011.01.21",
    "size": 7617270,
    "version_string": "7.2,REV=2011.01.21",
}

class Srv4UploaderUnitTest(mox.MoxTestBase):

  def test_MatchSrv4ToCatalogsSame(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_9)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.9"),
        ("unstable", "sparc", "SunOS5.10"),
        ("unstable", "sparc", "SunOS5.11"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsDifferent(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_10)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_10)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.9"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsSameSpecificOsrel(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_9)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, os_release="SunOS5.10")
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.10"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsAbsentFromAll(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(None)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(None)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(None)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.9"),
        ("unstable", "sparc", "SunOS5.10"),
        ("unstable", "sparc", "SunOS5.11"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsSameSpecificOsrelAlreadyPresent(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_10)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_10)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, os_release="SunOS5.10")
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.10"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsNotPresent(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient().AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(None)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, os_release="SunOS5.10")
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.10"),
    )
    self.assertEquals(expected, result)


if __name__ == '__main__':
  unittest.main()
