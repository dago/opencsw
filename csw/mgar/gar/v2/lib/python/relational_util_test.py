#!/usr/bin/env python2.6

import copy
import database
import datetime
import logging
import mox
import sqlobject
import test_base
import unittest

from lib.python import checkpkg_lib
from lib.python import configuration
from lib.python import models as m
from lib.python import opencsw
from lib.python import package_stats
from lib.python import pkgmap
from lib.python import relational_util
from lib.python import rest

from testdata.tree_stats import pkgstats as tree_stats
from testdata.neon_stats import pkgstats as neon_stats


# class DatabaseIntegrationTest(test_base.SqlObjectTestMixin,
#                               mox.MoxTestBase):
# 
#   def setUp(self):
#     super(DatabaseIntegrationTest, self).setUp()
#     self.mock_rest_client = self.mox.CreateMock(rest.RestClient)
#     self.mox.StubOutWithMock(rest, 'RestClient')
#     self.mock_config = self.mox.CreateMockAnything()
#     self.mox.StubOutWithMock(configuration, 'GetConfig')
#     # configuration.GetConfig().AndReturn(self.mock_config)
#     # mock_config.get('rest', 'base_url').AndReturn('http://baz')
# 
# 
#   class TestPackageStats(package_stats.PackageStats):
#     pass
# 
#   class TestCatalog(checkpkg_lib.Catalog):
#     pass
# 
#   def testWithoutInitialDataImport(self):
#     # configuration.GetConfig().AndReturn(self.mock_config)
#     # self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     res = m.Architecture.select(m.Architecture.q.name=='sparc')
#     self.assertRaises(sqlobject.SQLObjectNotFound, res.getOne)
# 
#   def DisabledtestInitialDataImport(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     res = m.Architecture.select(m.Architecture.q.name=='sparc')
#     self.assertEqual(u'sparc', res.getOne().name)
#     res = m.OsRelease.select(m.OsRelease.q.full_name=='SunOSSunOS5.10')
#     self.assertEqual(u'SunOS5.10', res.getOne().short_name)
# 
#   def testImportSrv4(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
#     self.assertEqual(u'1f084737549977d5508ade1701e101cc', md5_sum)
#     self.TestPackageStats.SaveStats(tree_stats[0])
#     res = m.Srv4FileStats.select()
#     foo = res.getOne()
#     self.assertEqual(md5_sum, foo.md5_sum)
#     new_pkgstats = self.TestPackageStats(
#         None, None, md5_sum)
#     new_data = new_pkgstats.GetAllStats()
#     self.assertEqual(md5_sum, new_data["basic_stats"]["md5_sum"])
# 
#   def testImportOverrides(self):
#     self.mox.ReplayAll()
#     md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
#     self.assertEqual(u'1f084737549977d5508ade1701e101cc', md5_sum)
#     new_stats = copy.deepcopy(tree_stats[0])
#     new_stats["overrides"].append(
#         {'pkgname': 'CSWtree',
#          'tag_info': None,
#          'tag_name': 'bad-rpath-entry'})
#     self.TestPackageStats.SaveStats(new_stats)
#     o = m.CheckpkgOverride.select().getOne()
#     self.assertEquals("CSWtree", o.pkgname)
#     self.assertEquals("bad-rpath-entry", o.tag_name)
# 
#   def testSaveStatsDependencies(self):
#     # configuration.GetConfig().AndReturn(self.mock_config)
#     # self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
#     self.assertEqual(u'1f084737549977d5508ade1701e101cc', md5_sum)
#     new_stats = copy.deepcopy(tree_stats[0])
#     self.TestPackageStats.SaveStats(new_stats)
#     depends = list(m.Srv4DependsOn.select())
#     # Dependencies should not be inserted into the db at that stage
#     self.assertEquals(0, len(depends))
# 
#   def testImportPkgDependencies(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
#     self.assertEqual(u'1f084737549977d5508ade1701e101cc', md5_sum)
#     new_stats = copy.deepcopy(tree_stats[0])
#     self.TestPackageStats.ImportPkg(new_stats)
#     depends = list(m.Srv4DependsOn.select())
#     # Dependencies should be inserted into the db at that stage
#     self.assertEquals(1, len(depends))
#     dep = depends[0]
#     self.assertEquals(md5_sum, dep.srv4_file.md5_sum)
#     self.assertEquals(u"CSWcommon", dep.pkginst.pkgname)
# 
#   def testImportPkgDependenciesReplace(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     md5_sum = tree_stats[0]["basic_stats"]["md5_sum"]
#     self.assertEqual(u'1f084737549977d5508ade1701e101cc', md5_sum)
#     new_stats = copy.deepcopy(tree_stats[0])
#     self.TestPackageStats.ImportPkg(new_stats)
#     self.TestPackageStats.ImportPkg(new_stats, replace=True)
#     depends = list(m.Srv4DependsOn.select())
#     # Dependencies should be inserted into the db at that stage
#     self.assertEquals(1, len(depends))
#     dep = depends[0]
#     self.assertEquals(md5_sum, dep.srv4_file.md5_sum)
#     self.assertEquals(u"CSWcommon", dep.pkginst.pkgname)
# 
#   def testImportPkg(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     package_stats.PackageStats.ImportPkg(neon_stats[0])
#     # basename=u'libneon.so.26.0.4' path=u'/opt/csw/lib'
#     res = m.CswFile.select(
#         sqlobject.AND(
#         m.CswFile.q.basename==u'libneon.so.26.0.4',
#         m.CswFile.q.path==u'/opt/csw/lib'))
#     f = res.getOne()
#     line = (u'1 f none /opt/csw/lib/libneon.so.26.0.4 '
#             u'0755 root bin 168252 181 1252917142')
#     self.assertEqual(line, f.line)
# 
#   def testImportPkgLatin1EncodedFile(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     latin1_pkgmap_entry = {
#       'class': 'none',
#       'group': 'bin',
#       'line': ('1 f none /opt/csw/lib/aspell/espa\xf1ol.alias '
#                '0644 root bin 70 6058 1030077183'),
#       'mode': '0644',
#       'path': '/opt/csw/lib/aspell/espa\xf1ol.alias',
#       'type': 'f',
#       'user': 'root'}
#     neon_stats2["pkgmap"].append(latin1_pkgmap_entry)
#     package_stats.PackageStats.ImportPkg(neon_stats2)
#     res = m.CswFile.select(
#         sqlobject.AND(
#         m.CswFile.q.basename=='espa\xc3\xb1ol.alias'.decode('utf-8'),
#         m.CswFile.q.path==u'/opt/csw/lib/aspell'))
#     f = res.getOne()
#     expected_line = (u'1 f none /opt/csw/lib/aspell/espa\xf1ol.alias 0644 '
#                      u'root bin 70 6058 1030077183')
#     self.assertEqual(expected_line, f.line)
# 
#   def testImportPkgAlreadyExisting(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     package_stats.PackageStats.SaveStats(neon_stats[0])
#     package_stats.PackageStats.ImportPkg(neon_stats[0])
# 
#   def testImportPkgIdempotence(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     package_stats.PackageStats.ImportPkg(neon_stats[0])
#     package_stats.PackageStats.ImportPkg(neon_stats[0])
#     res = m.CswFile.select(
#         sqlobject.AND(
#         m.CswFile.q.basename==u'libneon.so.26.0.4',
#         m.CswFile.q.path==u'/opt/csw/lib'))
#     self.assertEquals(1, res.count())
# 
#   def testImportPkgIdempotenceWithReplace(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     package_stats.PackageStats.ImportPkg(neon_stats[0])
#     package_stats.PackageStats.ImportPkg(neon_stats[0], replace=True)
#     res = m.CswFile.select(
#         sqlobject.AND(
#         m.CswFile.q.basename==u'libneon.so.26.0.4',
#         m.CswFile.q.path==u'/opt/csw/lib'))
#     self.assertEquals(1, res.count())
# 
#   def testRegisterTwoPkgs(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.TestPackageStats.ImportPkg(neon_stats[0])
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
#     self.TestPackageStats.ImportPkg(neon_stats2)
# 
#   def testAddSrv4ToCatalog(self):
#     self.dbc.InitialDataImport()
#     sqo_srv4 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     c = self.TestCatalog()
#     c.AddSrv4ToCatalog(sqo_srv4, 'SunOS5.9', 'i386', 'unstable')
#     sqo_osrel, sqo_arch, sqo_catrel = c.GetSqlobjectTriad(
#         'SunOS5.9', 'i386', 'unstable')
#     sqo_srv4_in_cat = m.Srv4FileInCatalog.select(
#         sqlobject.AND(
#           m.Srv4FileInCatalog.q.arch==sqo_arch,
#           m.Srv4FileInCatalog.q.osrel==sqo_osrel,
#           m.Srv4FileInCatalog.q.catrel==sqo_catrel,
#           m.Srv4FileInCatalog.q.srv4file==sqo_srv4)).getOne()
#     # If no exception was thrown, the record is there in the database.
# 
#   def testAddSrv4ToCatalogNotRegistered(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     sqo_srv4 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     sqo_srv4.registered = False
#     c = self.TestCatalog()
#     self.assertRaises(
#             checkpkg_lib.CatalogDatabaseError,
#             c.AddSrv4ToCatalog, sqo_srv4, 'SunOS5.9', 'i386', 'unstable')
# 
#   def testAssignSrv4ToCatalogArchMismatch(self):
#     self.dbc.InitialDataImport()
#     x86_stats = copy.deepcopy(neon_stats[0])
#     x86_stats["pkginfo"]["ARCH"] = "i386"
#     stats = self.TestPackageStats.ImportPkg(x86_stats)
#     c = self.TestCatalog()
#     self.assertRaises(
#             checkpkg_lib.CatalogDatabaseError,
#             c.AddSrv4ToCatalog, stats, 'SunOS5.9', 'sparc', 'unstable')
# 
#   def testAssignSrv4ToCatalogArchFromFile(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     x86_stats = copy.deepcopy(neon_stats[0])
#     x86_stats["pkginfo"]["ARCH"] = "i386"
#     x86_stats["basic_stats"]["parsed_basename"]["arch"] = "all"
#     stats = self.TestPackageStats.ImportPkg(x86_stats)
#     c = self.TestCatalog()
#     c.AddSrv4ToCatalog(stats, 'SunOS5.9', 'sparc', 'unstable')
# 
#   def testRemoveSrv4FromCatalog(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     stats = self.TestPackageStats.ImportPkg(neon_stats[0])
#     c = self.TestCatalog()
#     sqo_osrel, sqo_arch, sqo_catrel = c.GetSqlobjectTriad(
#         'SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(stats, 'SunOS5.9', 'i386', 'unstable')
#     obj = m.Srv4FileInCatalog.select(
#                 sqlobject.AND(
#                     m.Srv4FileInCatalog.q.arch==sqo_arch,
#                     m.Srv4FileInCatalog.q.osrel==sqo_osrel,
#                     m.Srv4FileInCatalog.q.catrel==sqo_catrel,
#                     m.Srv4FileInCatalog.q.srv4file==stats)).getOne()
#     # At this point, we know that the record is in the db.
#     c.RemoveSrv4(stats, 'SunOS5.9', 'i386', 'unstable')
#     # Make sure that the Srv4FileInCatalog object is now gone.
#     res = m.Srv4FileInCatalog.select(
#         sqlobject.AND(
#           m.Srv4FileInCatalog.q.arch==sqo_arch,
#           m.Srv4FileInCatalog.q.osrel==sqo_osrel,
#           m.Srv4FileInCatalog.q.catrel==sqo_catrel,
#           m.Srv4FileInCatalog.q.srv4file==stats))
#     self.assertRaises(sqlobject.SQLObjectNotFound, res.getOne)
#     # Retrieved record from the db should now not have the registered flag.
#     updated_stats = m.Srv4FileStats.select(
#         m.Srv4FileStats.q.id==stats.id).getOne()
#     self.assertTrue(updated_stats.registered)
#     # Make sure that files of this package are still in the database.
#     res = m.CswFile.select(
#         m.CswFile.q.srv4_file==updated_stats)
#     self.assertEquals(22, res.count())
# 
# 
#   def testRetrievePathsMatchCatalog(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
#     c = self.TestCatalog()
#     c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg2, 'SunOS5.9', 'i386', 'legacy')
#     expected = {
#         u'/opt/csw/lib': [u'CSWneon'],
#         u'/opt/csw/lib/sparcv9': [u'CSWneon']}
#     self.assertEqual(
#         expected,
#         c.GetPathsAndPkgnamesByBasename(
#           u'libneon.so.26.0.4', 'SunOS5.9', 'i386', 'unstable'))
# 
#   def testRetrievePathsMatchCatalogUnregisterd(self):
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     neon_stats2["basic_stats"]["pkgname"] = "CSWanother"
#     configuration.GetConfig().AndReturn(self.mock_config)
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     rest.RestClient('http://baz').AndReturn(self.mock_rest_client)
#     rest.RestClient('http://baz').AndReturn(self.mock_rest_client)
#     self.mock_rest_client.GetPkgstatsByMd5(
#         'd74a2f65ef0caff0bdde7310007764a8').AndReturn(neon_stats[0])
#     self.mock_rest_client.GetPkgstatsByMd5('another pkg').AndReturn(neon_stats2)
#     self.mox.ReplayAll()
# 
#     self.dbc.InitialDataImport()
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0]['basic_stats']['md5_sum'])
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2['basic_stats']['md5_sum'])
#     c = self.TestCatalog()
#     c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg2, 'SunOS5.9', 'i386', 'legacy')
#     sqo_pkg1.registered = False
#     expected = {}
#     self.assertEqual(
#         expected,
#         c.GetPathsAndPkgnamesByBasename(
#           u'libneon.so.26.0.4', 'SunOS5.9', 'i386', 'unstable'))
# 
#   def testGetInstalledPackages(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     c = self.TestCatalog()
#     c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
#     self.assertEqual(
#         [u'CSWneon'],
#         c.GetInstalledPackages('SunOS5.9', 'i386', 'unstable'))
# 
#   def testDuplicatePkginstPassesIfItIsTheSameOne(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.dbc.InitialDataImport()
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     # md5_sum is different
#     # pkgname stays the same on purpose
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
# 
#   def testDuplicatePkginstThrowsError(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     neon_stats2["basic_stats"]["catalogname"] = "another_pkg"
#     # md5_sum is different
#     # pkgname stays the same on purpose
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
#     self.assertRaises(
#             checkpkg_lib.CatalogDatabaseError,
#             c.AddSrv4ToCatalog,
#             sqo_pkg2, *args)
# 
#   def testDuplicateCatalognameThrowsError(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     neon_stats2["basic_stats"]["pkgname"] = "CSWanother-pkg"
#     # md5_sum is different
#     # pkgname stays the same on purpose
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
#     self.assertRaises(
#             checkpkg_lib.CatalogDatabaseError,
#             c.AddSrv4ToCatalog,
#             sqo_pkg2, *args)
# 
#   def testDuplicatePkginstDoesNotThrowErrorIfDifferentCatalog(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     neon_stats2 = copy.deepcopy(neon_stats[0])
#     neon_stats2["basic_stats"]["md5_sum"] = "another pkg"
#     # md5_sum is different
#     # pkgname stays the same on purpose
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     sqo_pkg2 = self.TestPackageStats.ImportPkg(neon_stats2)
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, 'SunOS5.10', 'i386', 'unstable')
# 
#   def testGetPkgByPath(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'unstable')
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
#     self.assertEquals(
#         frozenset([u'CSWneon']),
#         c.GetPkgByPath("/opt/csw/lib/libneon.so.27.2.0",
#                        "SunOS5.9", "i386", "unstable"))
# 
#   def testGetPkgByPathWrongCatalog(self):
#     configuration.GetConfig().AndReturn(self.mock_config)
#     self.mock_config.get('rest', 'base_url').AndReturn('http://baz')
#     self.mox.ReplayAll()
#     self.dbc.InitialDataImport()
#     sqo_pkg1 = self.TestPackageStats.ImportPkg(neon_stats[0])
#     c = self.TestCatalog()
#     args = ('SunOS5.9', 'i386', 'legacy')
#     c.AddSrv4ToCatalog(sqo_pkg1, *args)
#     self.assertEquals(
#         frozenset([]),
#         c.GetPkgByPath("/opt/csw/lib/libneon.so.27.2.0",
#                        "SunOS5.9", "i386", "unstable"))
# 
#   def disabledtestContinue(self):
#     # This line can be useful: put in a specific place can ensure that
#     # this place is reached during execution.  Two flavors are
#     # available.
#     self.fail("Great, please continue!")
#     self.fail("The test should not reach this point.")


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  # logging.basicConfig(level=logging.DEBUG)
  unittest.main()
