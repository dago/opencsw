#!/usr/bin/env python2.6

import copy
import unittest
import checkpkg_lib
import tag
import package_stats
import database
import sqlobject
import models
import package_stats
import inspective_package
import mox
import test_base
import cPickle

from testdata.neon_stats import pkgstats as neon_stats


class CheckpkgManager2UnitTest(mox.MoxTestBase):

  def testSingleTag(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = u'# Tags reported by testname module\nCSWfoo: foo-tag foo-info\n'
    self.assertEqual(expected, unicode(tags_report))

  def testThreeTags(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
          tag.CheckpkgTag("CSWfoo", "bar-tag", "bar-info"),
          tag.CheckpkgTag("CSWfoo", "baz-tag"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = (u'# Tags reported by testname module\n'
                u'CSWfoo: foo-tag foo-info\n'
                u'CSWfoo: bar-tag bar-info\n'
                u'CSWfoo: baz-tag\n')
    self.assertEqual(expected, unicode(tags_report))

  def testGetAllTags(self):
    # Does not run any checks, because they are unregistered.
    self.mox.StubOutWithMock(checkpkg_lib, 'IndividualCheckInterface',
        use_mock_anything=True)
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # checkpkg_interface_mock = self.mox.CreateMock(
    #     checkpkg_lib.IndividualCheckInterface)
    # Throws:
    # UnknownMethodCallError: Method called is not a member of the
    # object: GetPkgByPath
    checkpkg_interface_mock = self.mox.CreateMockAnything()
    checkpkg_interface_mock.needed_files = [
        checkpkg_lib.NeededFile("CSWfoo", "/opt/csw/bin/foo", "Because!"),
    ]
    checkpkg_interface_mock.GetPkgByPath("/opt/csw/bin/foo").AndReturn(
        ["CSWbar", "CSWbaz"])
    self.mox.StubOutWithMock(checkpkg_lib, 'Catalog',
        use_mock_anything=True)
    checkpkg_lib.Catalog().AndReturn(catalog_mock)
    checkpkg_lib.IndividualCheckInterface(
        'CSWneon', '5.9', 'sparc', 'unstable', catalog_mock).AndReturn(
            checkpkg_interface_mock)
    stat_obj = self.mox.CreateMockAnything()
    data_obj = self.mox.CreateMockAnything()
    stat_obj.data_obj = data_obj
    pkg_stats = copy.deepcopy(neon_stats[0])
    # Resetting the dependencies so that it doesn't report surplus deps.
    pkg_stats["depends"] = []
    data_obj.pickle = cPickle.dumps(pkg_stats)
    checkpkg_interface_mock.ReportErrorForPkgname(
        'CSWfoo', 'missing-dependency', 'CSWbar or CSWbaz')
    self.mox.ReplayAll()
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    # m._AutoregisterChecks()
    self.assertEquals(({}, [], []), m.GetAllTags([stat_obj]))


class CheckpkgManager2DatabaseIntegrationTest(
    test_base.SqlObjectTestMixin, unittest.TestCase):

  def setUp(self):
    super(CheckpkgManager2DatabaseIntegrationTest, self).setUp()
    self.mox = mox.Mox()

  def testInsertNeon(self):
    self.dbc.InitialDataImport()
    sqo_pkg = package_stats.PackageStats.SaveStats(neon_stats[0], True)
    cm = checkpkg_lib.CheckpkgManager2(
        "testname", [sqo_pkg], "SunOS5.9", "sparc", "unstable",
        show_progress=False)
    cm.Run()
    # Verifying that there are some reported error tags.
    self.assertTrue(list(models.CheckpkgErrorTag.select()))


class IndividualCheckInterfaceUnitTest(mox.MoxTestBase):
  
  def testNeededFile(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    self.mox.StubOutWithMock(checkpkg_lib, 'Catalog', use_mock_anything=True)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    checkpkg_lib.Catalog().AndReturn(catalog_mock)
    self.mox.ReplayAll()
    ici = checkpkg_lib.IndividualCheckInterface(
        'CSWfoo', 'AlienOS5.1', 'amd65', 'calcified')
    ici.NeedFile("/opt/csw/bin/foo", "Because.")
    # This might look like encapsulation violation, but I think this is
    # a reasonable interface to that class.
    self.assertEqual(1, len(ici.needed_files))
    needed_file = ici.needed_files[0]
    self.assertEqual("CSWfoo", needed_file.pkgname)
    self.assertEqual("/opt/csw/bin/foo", needed_file.full_path)
    self.assertEqual("Because.", needed_file.reason)


class SetCheckInterfaceUnitTest(mox.MoxTestBase):
  
  def testNeededFile(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    self.mox.StubOutWithMock(checkpkg_lib, 'Catalog', use_mock_anything=True)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    checkpkg_lib.Catalog().AndReturn(catalog_mock)
    self.mox.ReplayAll()
    sci = checkpkg_lib.SetCheckInterface(
        'AlienOS5.1', 'amd65', 'calcified')
    sci.NeedFile("CSWfoo", "/opt/csw/bin/foo", "Because.")
    # This might look like encapsulation violation, but I think this is
    # a reasonable interface to that class.
    self.assertEqual(1, len(sci.needed_files))
    needed_file = sci.needed_files[0]
    self.assertEqual("CSWfoo", needed_file.pkgname)
    self.assertEqual("/opt/csw/bin/foo", needed_file.full_path)
    self.assertEqual("Because.", needed_file.reason)


if __name__ == '__main__':
  unittest.main()
