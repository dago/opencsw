#!/usr/bin/env python2.6

import copy
import unittest
import package_stats
import checkpkg_lib
import database
import sqlobject
import models as m
import test_base
import logging
import mox
import inspective_package
import opencsw
import datetime
import pkgmap

from testdata.tree_stats import pkgstats as tree_stats
from testdata.neon_stats import pkgstats as neon_stats


class PackageStatsWithDbUnitTest(test_base.SqlObjectTestMixin,
                           unittest.TestCase):

  def setUp(self):
    super(PackageStatsWithDbUnitTest, self).setUp()
    self.mox = mox.Mox()

  def test_CollectStats(self):
    """Test if it's possible to collect stats.

    It's a real showdown of a part of code I didn't want to unit test
    earlier.  It's possible to see how the law of Demeter was violated,
    leading to a confusing API.
    """
    mock_srv4 = self.mox.CreateMock(
        inspective_package.InspectiveCswSrv4File)
    mock_dirpkg = self.mox.CreateMock(
        inspective_package.InspectivePackage)
    mock_pkgmap = self.mox.CreateMock(
        pkgmap.Pkgmap)
    mock_srv4.GetInspectivePkg().AndReturn(mock_dirpkg)
    mock_srv4.pkg_path = "/tmp/foo-1.2,REV=1234.12.11-SunOS5.8-sparc-CSW.pkg.gz"
    mock_dirpkg.pkgname = "MOCKpkgname"
    mock_dirpkg.GetOverrides().AndReturn([])
    mock_dirpkg.GetCatalogname().AndReturn("mock_catalogname")
    mock_srv4.GetMd5sum().AndReturn("mock md5sum")
    mock_srv4.GetSize().AndReturn(42)
    mock_dirpkg.GetDependencies().AndReturn(([], []))
    mock_dirpkg.ListBinaries().AndReturn([])
    mock_dirpkg.GetBinaryDumpInfo().AndReturn([])
    mock_srv4.GetPkgchkOutput().AndReturn((0, "", ""))
    mock_dirpkg.GetObsoletedBy().AndReturn(([], []))
    mock_dirpkg.GetParsedPkginfo().AndReturn({
      "ARCH": "sparc",
      "EMAIL": "maintainer@example.com",
      })
    mock_dirpkg.GetPkgmap().AndReturn(mock_pkgmap)
    mock_pkgmap.entries = []
    mock_dirpkg.GetFilesContaining(mox.IsA(tuple)).AndReturn([])
    mock_dirpkg.GetFilesMetadata().AndReturn([])
    mock_srv4.GetMtime().AndReturn(datetime.datetime(2010, 12, 8, 7, 52, 54))
    mock_dirpkg.GetLddMinusRlines().AndReturn({})
    mock_dirpkg.GetBinaryElfInfo().AndReturn({})
    pkgstats = package_stats.PackageStats(mock_srv4)
    self.mox.ReplayAll()
    data_structure = pkgstats._CollectStats(True)
    self.mox.VerifyAll()
    self.assertEqual(
        "1234.12.11",
        data_structure["basic_stats"]["parsed_basename"]["revision_info"]["REV"])
    self.assertEqual(datetime.datetime(2010, 12, 8, 7, 52, 54),
                     data_structure["mtime"])


class DatabaseIntegrationTest(test_base.SqlObjectTestMixin,
                              unittest.TestCase):

  class TestPackageStats(package_stats.PackageStatsMixin):
    pass

  class TestCatalog(checkpkg_lib.CatalogMixin):
    pass

  def testWithoutInitialDataImport(self):
    res = m.Architecture.select(m.Architecture.q.name=='sparc')
    self.assertRaises(sqlobject.SQLObjectNotFound, res.getOne)

  def DisabledtestInitialDataImport(self):
    self.dbc.InitialDataImport()
    res = m.Architecture.select(m.Architecture.q.name=='sparc')
    self.assertEqual(u'sparc', res.getOne().name)
    res = m.OsRelease.select(m.OsRelease.q.full_name=='SunOSSunOS5.10')
    self.assertEqual(u'SunOS5.10', res.getOne().short_name)

  def testImportSrv4(self):
    md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
    self.assertEqual(u'1e43fa1c7e637b25d9356ad516ae0403', md5_sum)
    self.TestPackageStats.SaveStats(tree_stats[0])
    res = m.Srv4FileStats.select()
    foo = res.getOne()
    self.assertEqual(md5_sum, foo.md5_sum)
    new_pkgstats = self.TestPackageStats(
        None, None, md5_sum)
    new_data = new_pkgstats.GetAllStats()
    self.assertEqual(md5_sum, new_data["basic_stats"]["md5_sum"])

  def testImportOverrides(self):
    md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
    self.assertEqual(u'1e43fa1c7e637b25d9356ad516ae0403', md5_sum)
    new_stats = copy.deepcopy(tree_stats[0])
    new_stats["overrides"].append(
        {'pkgname': 'CSWtree',
         'tag_info': None,
         'tag_name': 'bad-rpath-entry'})
    self.TestPackageStats.SaveStats(new_stats)
    o = m.CheckpkgOverride.select().getOne()
    self.assertEquals("CSWtree", o.pkgname)
    self.assertEquals("bad-rpath-entry", o.tag_name)

  def testSaveStatsDependencies(self):
    md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
    self.assertEqual(u'1e43fa1c7e637b25d9356ad516ae0403', md5_sum)
    new_stats = copy.deepcopy(tree_stats[0])
    self.TestPackageStats.SaveStats(new_stats)
    depends = list(m.Srv4DependsOn.select())
    # Dependencies should not be inserted into the db at that stage
    self.assertEquals(0, len(depends))

  def testImportPkgDependencies(self):
    md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
    self.assertEqual(u'1e43fa1c7e637b25d9356ad516ae0403', md5_sum)
    new_stats = copy.deepcopy(tree_stats[0])
    self.TestPackageStats.ImportPkg(new_stats)
    depends = list(m.Srv4DependsOn.select())
    # Dependencies should be inserted into the db at that stage
    self.assertEquals(1, len(depends))
    dep = depends[0]
    self.assertEquals(md5_sum, dep.srv4_file.md5_sum)
    self.assertEquals(u"CSWcommon", dep.pkginst.pkgname)

  def testImportPkgDependenciesReplace(self):
    """Make sure deps are not imported twice."""
    md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
    self.assertEqual(u'1e43fa1c7e637b25d9356ad516ae0403', md5_sum)
    new_stats = copy.deepcopy(tree_stats[0])
    self.TestPackageStats.ImportPkg(new_stats)
    self.TestPackageStats.ImportPkg(new_stats, replace=True)
    depends = list(m.Srv4DependsOn.select())
    # Dependencies should be inserted into the db at that stage
    self.assertEquals(1, len(depends))
    dep = depends[0]
    self.assertEquals(md5_sum, dep.srv4_file.md5_sum)
    self.assertEquals(u"CSWcommon", dep.pkginst.pkgname)

  def testImportPkg(self):
    """Registers the package in the database."""
    package_stats.PackageStats.ImportPkg(neon_stats[0])
    # basename=u'libneon.so.26.0.4' path=u'/opt/csw/lib' 
    res = m.CswFile.select(
        sqlobject.AND(
        m.CswFile.q.basename==u'libneon.so.26.0.4',
        m.CswFile.q.path==u'/opt/csw/lib'))
    f = res.getOne()
    line = (u'1 f none /opt/csw/lib/libneon.so.26.0.4 '
            u'0755 root bin 168252 181 1252917142')
    self.assertEqual(line, f.line)

  def testImportPkgLatin1EncodedFile(self):
    """Registers the package in the database."""
    neon_stats2 = copy.deepcopy(neon_stats[0])
    latin1_pkgmap_entry = {
      'class': 'none',
      'group': 'bin',
      'line': ('1 f none /opt/csw/lib/aspell/espa\xf1ol.alias '
               '0644 root bin 70 6058 1030077183'),
      'mode': '0644',
      'path': '/opt/csw/lib/aspell/espa\xf1ol.alias',
      'type': 'f',
      'user': 'root'}
    neon_stats2["pkgmap"].append(latin1_pkgmap_entry)
    package_stats.PackageStats.ImportPkg(neon_stats2)
    res = m.CswFile.select(
        sqlobject.AND(
        m.CswFile.q.basename=='espa\xc3\xb1ol.alias'.decode('utf-8'),
        m.CswFile.q.path==u'/opt/csw/lib/aspell'))
    f = res.getOne()
    expected_line = (u'1 f none /opt/csw/lib/aspell/espa\xf1ol.alias 0644 '
                     u'root bin 70 6058 1030077183')
    self.assertEqual(expected_line, f.line)

  def testImportPkgAlreadyExisting(self):
    """Registers an already saved package in the database."""
    package_stats.PackageStats.SaveStats(neon_stats[0])
    package_stats.PackageStats.ImportPkg(neon_stats[0])

  def testImportPkgIdempotence(self):
    """Files shouldn't be imported twice for one package."""
    package_stats.PackageStats.ImportPkg(neon_stats[0])
    package_stats.PackageStats.ImportPkg(neon_stats[0])
    res = m.CswFile.select(
        sqlobject.AND(
        m.CswFile.q.basename==u'libneon.so.26.0.4',
        m.CswFile.q.path==u'/opt/csw/lib'))
    self.assertEquals(1, res.count())

  def testImportPkgIdempotenceWithReplace(self):
    """Files shouldn't be imported twice for one package."""
    package_stats.PackageStats.ImportPkg(neon_stats[0])
    package_stats.PackageStats.ImportPkg(neon_stats[0], replace=True)
    res = m.CswFile.select(
        sqlobject.AND(
        m.CswFile.q.basename==u'libneon.so.26.0.4',
        m.CswFile.q.path==u'/opt/csw/lib'))
    self.assertEquals(1, res.count())

  def testRegisterTwoPkgs(self):
    self.TestPackageStats.ImportPkg(neon_stats[0])
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
    self.TestPackageStats.ImportPkg(neon_stats2)

  def testAddSrv4ToCatalog(self):
    self.dbc.InitialDataImport()
    sqo_srv4 = self.TestPackageStats.ImportPkg(neon_stats[0])
    c = self.TestCatalog()
    c.AddSrv4ToCatalog(sqo_srv4, 'SunOS5.9', 'i386', 'unstable')
    sqo_osrel, sqo_arch, sqo_catrel = c.GetSqlobjectTriad(
        'SunOS5.9', 'i386', 'unstable')
    sqo_srv4_in_cat = m.Srv4FileInCatalog.select(
        sqlobject.AND(
          m.Srv4FileInCatalog.q.arch==sqo_arch,
          m.Srv4FileInCatalog.q.osrel==sqo_osrel,
          m.Srv4FileInCatalog.q.catrel==sqo_catrel,
          m.Srv4FileInCatalog.q.srv4file==sqo_srv4)).getOne()
    # If no exception was thrown, the record is there in the database.

  def testAddSrv4ToCatalogNotRegistered(self):
    """Unregistered package should not be added to any catalogs."""
    self.dbc.InitialDataImport()
    sqo_srv4 = self.TestPackageStats.ImportPkg(neon_stats[0])
    sqo_srv4.registered = False
    c = self.TestCatalog()
    self.assertRaises(
            checkpkg_lib.CatalogDatabaseError,
            c.AddSrv4ToCatalog, sqo_srv4, 'SunOS5.9', 'i386', 'unstable')

  def testAssignSrv4ToCatalogArchMismatch(self):
    self.dbc.InitialDataImport()
    x86_stats = copy.deepcopy(neon_stats[0])
    x86_stats["pkginfo"]["ARCH"] = "i386"
    stats = self.TestPackageStats.ImportPkg(x86_stats)
    c = self.TestCatalog()
    self.assertRaises(
            checkpkg_lib.CatalogDatabaseError,
            c.AddSrv4ToCatalog, stats, 'SunOS5.9', 'sparc', 'unstable')

  def testAssignSrv4ToCatalogArchFromFile(self):
    """If a package has 'all' in the filename, import it to all catalogs."""
    self.dbc.InitialDataImport()
    x86_stats = copy.deepcopy(neon_stats[0])
    x86_stats["pkginfo"]["ARCH"] = "i386"
    x86_stats["basic_stats"]["parsed_basename"]["arch"] = "all"
    stats = self.TestPackageStats.ImportPkg(x86_stats)
    c = self.TestCatalog()
    c.AddSrv4ToCatalog(stats, 'SunOS5.9', 'sparc', 'unstable')

  def testRemoveSrv4FromCatalog(self):
    self.dbc.InitialDataImport()
    stats = self.TestPackageStats.ImportPkg(neon_stats[0])
    c = self.TestCatalog()
    sqo_osrel, sqo_arch, sqo_catrel = c.GetSqlobjectTriad(
        'SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(stats, 'SunOS5.9', 'i386', 'unstable')
    obj = m.Srv4FileInCatalog.select(
                sqlobject.AND(
                    m.Srv4FileInCatalog.q.arch==sqo_arch,
                    m.Srv4FileInCatalog.q.osrel==sqo_osrel,
                    m.Srv4FileInCatalog.q.catrel==sqo_catrel,
                    m.Srv4FileInCatalog.q.srv4file==stats)).getOne()
    # At this point, we know that the record is in the db.
    c.RemoveSrv4(stats, 'SunOS5.9', 'i386', 'unstable')
    # Make sure that the Srv4FileInCatalog object is now gone.
    res = m.Srv4FileInCatalog.select(
        sqlobject.AND(
          m.Srv4FileInCatalog.q.arch==sqo_arch,
          m.Srv4FileInCatalog.q.osrel==sqo_osrel,
          m.Srv4FileInCatalog.q.catrel==sqo_catrel,
          m.Srv4FileInCatalog.q.srv4file==stats))
    self.assertRaises(sqlobject.SQLObjectNotFound, res.getOne)
    # Retrieved record from the db should now not have the registered flag.
    updated_stats = m.Srv4FileStats.select(
        m.Srv4FileStats.q.id==stats.id).getOne()
    self.assertTrue(updated_stats.registered)
    # Make sure that files of this package are still in the database.
    res = m.CswFile.select(
        m.CswFile.q.srv4_file==updated_stats)
    self.assertEquals(22, res.count())


  def testRetrievePathsMatchCatalog(self):
    """Make sure that returned paths match the right catalog."""
    self.dbc.InitialDataImport()
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg2, 'SunOS5.9', 'i386', 'legacy')
    expected = {
        u'/opt/csw/lib': [u'CSWneon'],
        u'/opt/csw/lib/sparcv9': [u'CSWneon']}
    self.assertEqual(
        expected,
        c.GetPathsAndPkgnamesByBasename(
          u'libneon.so.26.0.4', 'SunOS5.9', 'i386', 'unstable'))

  def testRetrievePathsMatchCatalogUnregisterd(self):
    """Make sure we're returning files for registered packages only."""
    self.dbc.InitialDataImport()
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg2, 'SunOS5.9', 'i386', 'legacy')
    sqo_pkg1.registered = False
    expected = {}
    self.assertEqual(
        expected,
        c.GetPathsAndPkgnamesByBasename(
          u'libneon.so.26.0.4', 'SunOS5.9', 'i386', 'unstable'))

  def testGetInstalledPackages(self):
    self.dbc.InitialDataImport()
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    c = self.TestCatalog()
    c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
    self.assertEqual(
        [u'CSWneon'],
        c.GetInstalledPackages('SunOS5.9', 'i386', 'unstable'))

  def testDuplicatePkginstPassesIfItIsTheSameOne(self):
    self.dbc.InitialDataImport()
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    # md5_sum is different
    # pkgname stays the same on purpose
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, *args)
    c.AddSrv4ToCatalog(sqo_pkg1, *args)

  def testDuplicatePkginstThrowsError(self):
    self.dbc.InitialDataImport()
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    neon_stats2["basic_stats"]["catalogname"] = "another_pkg"
    # md5_sum is different
    # pkgname stays the same on purpose
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, *args)
    self.assertRaises(
            checkpkg_lib.CatalogDatabaseError,
            c.AddSrv4ToCatalog,
            sqo_pkg2, *args)

  def testDuplicateCatalognameThrowsError(self):
    self.dbc.InitialDataImport()
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    neon_stats2["basic_stats"]["pkgname"] = "CSWanother-pkg"
    # md5_sum is different
    # pkgname stays the same on purpose
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, *args)
    self.assertRaises(
            checkpkg_lib.CatalogDatabaseError,
            c.AddSrv4ToCatalog,
            sqo_pkg2, *args)

  def testDuplicatePkginstDoesNotThrowErrorIfDifferentCatalog(self):
    self.dbc.InitialDataImport()
    neon_stats2 = copy.deepcopy(neon_stats[0])
    neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
    # md5_sum is different
    # pkgname stays the same on purpose
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.10', 'i386', 'unstable')

  def testGetPkgByPath(self):
    self.dbc.InitialDataImport()
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'unstable')
    c.AddSrv4ToCatalog(sqo_pkg1, *args)
    self.assertEquals(
        frozenset([u'CSWneon']),
        c.GetPkgByPath("/opt/csw/lib/libneon.so.27.2.0",
                       "SunOS5.9", "i386", "unstable"))

  def testGetPkgByPathWrongCatalog(self):
    """Makes sure packages from wrong catalogs are not returned."""
    self.dbc.InitialDataImport()
    sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
    c = self.TestCatalog()
    args = ('SunOS5.9', 'i386', 'legacy')
    c.AddSrv4ToCatalog(sqo_pkg1, *args)
    self.assertEquals(
        frozenset([]),
        c.GetPkgByPath("/opt/csw/lib/libneon.so.27.2.0",
                       "SunOS5.9", "i386", "unstable"))

  def disabledtestContinue(self):
    # This line can be useful: put in a specific place can ensure that
    # this place is reached during execution.  Two flavors are
    # available.
    self.fail("Great, please continue!")
    self.fail("The test should not reach this point.")


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  unittest.main()
