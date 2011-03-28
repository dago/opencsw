#!/usr/bin/env python2.6

import unittest2 as unittest
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
GDB_STRUCT_11 = {
    "arch": "sparc",
    "basename": "gdb-7.2,REV=2011.01.21-SunOS5.11-sparc-CSW.pkg.gz",
    "catalogname": "gdb",
    "filename_arch": "sparc",
    "maintainer_email": "pfele...@opencsw.org",
    "maintainer_full_name": None,
    "md5_sum": "09cccf8097e982dadbd717910963e378",
    "mtime": "2011-01-24 03:10:05",
    "osrel": "SunOS5.11",
    "pkgname": "CSWgdb",
    "rev": "2011.01.21",
    "size": 7617270,
    "version_string": "7.2,REV=2011.01.21",
}
TEST_PLANNED_MODIFICATIONS_1 = [
 ('foo.pkg',
  '58f564d11d6419592dcca3915bfabc55',
  u'all',
  u'SunOS5.9',
  'sparc',
  u'SunOS5.9'),
 ('foo.pkg',
  '58f564d11d6419592dcca3915bfabc55',
  u'all',
  u'SunOS5.9',
  'sparc',
  u'SunOS5.10'),
 ('bar.pkg',
  '84b409eb7c2faf87e22ee0423e55b888',
  u'sparc',
  u'SunOS5.9',
  u'sparc',
  u'SunOS5.9'),
]


class Srv4UploaderUnitTest(mox.MoxTestBase):

  def test_MatchSrv4ToCatalogsSame(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_9)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None)
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
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_10)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_10)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.9"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsNewerPackage(self):
    # A scenario in which a 5.9 package exists in the catalog, and we're
    # uploading a 5.10 package.
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_9)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.10-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.10",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.10"),
        ("unstable", "sparc", "SunOS5.11"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsSameSpecificOsrel(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_9)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None, os_release="SunOS5.10")
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
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(None)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(None)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(None)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None)
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
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_10)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_10)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None, os_release="SunOS5.10")
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
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_9)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(None)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None, os_release="SunOS5.10")
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.10"),
    )
    self.assertEquals(expected, result)

  def test_MatchSrv4ToCatalogsFirstNotPresent(self):
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient(None).AndReturn(rest_client_mock)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.9', 'gdb').AndReturn(None)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.10', 'gdb').AndReturn(GDB_STRUCT_10)
    rest_client_mock.Srv4ByCatalogAndCatalogname(
        'unstable', 'sparc', u'SunOS5.11', 'gdb').AndReturn(GDB_STRUCT_10)
    self.mox.ReplayAll()
    su = csw_upload_pkg.Srv4Uploader(None, None)
    result = su._MatchSrv4ToCatalogs(
        "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz",
        "unstable", "sparc", "SunOS5.9",
        "deadbeef61b53638d7813407fab4765b")
    expected = (
        ("unstable", "sparc", "SunOS5.9"),
    )
    self.assertEquals(expected, result)


class Srv4UploaderDataDrivenUnitTest(mox.MoxTestBase):
  """A unit test doing an search over multiple combinations.

  It generalizes the unit test above, and is more data-driven.

  It could be rewriten in a way which generates separate test functions for
  each data row, but for now, we'll just loop over the data set in one test.
  """

  DATA = (
      # in_catalog, pkg, specified, expected_insertions
      ((None, None, None),  9, None, (9, 10, 11)),
      ((None, None,    9),  9, None, (9, 10, 11)),
      ((None,    9,    9),  9, None, (9, 10, 11)),
      ((   9,    9,    9),  9, None, (9, 10, 11)),
      ((None,    9,   10),  9, None, (9, 10)),
      ((   9,    9,   10),  9, None, (9, 10)),
      ((   9,   10,   10),  9, None, (9,)),
      ((   9,   10,   10),  9,    9, (9,)),
      ((   9,   10,   10),  9,   10, (10,)),
      ((   9,    9,   10),  9,   10, (10,)),
      ((   9,    9,   10),  9,   11, (11,)),
      ((      None, None), 10, None, (10, 11)),
      ((      None,   10), 10, None, (10, 11)),
      ((        10,   10), 10, None, (10, 11)),
      ((        10,   11), 10, None, (10,)),
      ((      None,   10), 10, None, (10, 11,)),
  )
  BASENAME = "gdb-7.2,REV=2011.01.21-SunOS5.9-sparc-CSW.pkg.gz"
  MD5_SUM = "deadbeef61b53638d7813407fab4765b"

  def testAllPossibilities(self):
    for (in_catalog,
         pkg_osrel, osrel_spec,
         expected_rels) in self.DATA:
      self.DataPointTest(in_catalog, pkg_osrel, osrel_spec, expected_rels)

  def DataPointTest(self, in_catalog, pkg_osrel, osrel_spec, expected_rels):
    pkg_struct_map = {
        None: None,
        9: GDB_STRUCT_9,
        10: GDB_STRUCT_10,
        11: GDB_STRUCT_11,
    }
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    self.mox.StubOutWithMock(rest, "RestClient")
    rest.RestClient(None).AndReturn(rest_client_mock)
    for i, os_n in enumerate(in_catalog, 3 - len(in_catalog)):
      pkg_struct = pkg_struct_map[os_n]
      rest_client_mock.Srv4ByCatalogAndCatalogname(
          'unstable',
          'sparc',
          u'SunOS5.%s' % (i + 9), 'gdb').AndReturn(pkg_struct)
    self.mox.ReplayAll()
    os_release_to_specify = "SunOS5.%s" % osrel_spec if osrel_spec else None
    su = csw_upload_pkg.Srv4Uploader(None, None, os_release=os_release_to_specify)
    result = su._MatchSrv4ToCatalogs(
        self.BASENAME,
        "unstable", "sparc", "SunOS5.%s" % pkg_osrel,
        self.MD5_SUM)
    expected = []
    for n in expected_rels:
      expected.append(("unstable", "sparc", "SunOS5.%s" % n))
    expected = tuple(expected)
    self.assertEquals(expected, result)
    self.mox.ResetAll()
    self.mox.UnsetStubs()

  def test_CheckpkgSets(self):
    su = csw_upload_pkg.Srv4Uploader(None, None)
    expected = {
        ('sparc', u'SunOS5.10'):
          [('foo.pkg', '58f564d11d6419592dcca3915bfabc55')],
        ('sparc', u'SunOS5.9'):
          [('foo.pkg', '58f564d11d6419592dcca3915bfabc55'),
           ('bar.pkg', '84b409eb7c2faf87e22ee0423e55b888')]}
    self.assertEqual(expected, su._CheckpkgSets(TEST_PLANNED_MODIFICATIONS_1))


if __name__ == '__main__':
  unittest.main()
