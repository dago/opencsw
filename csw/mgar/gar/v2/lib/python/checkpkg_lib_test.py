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

from testdata.neon_stats import pkgstats as neon_stats


class CheckpkgManager2UnitTest(unittest.TestCase):

  def setUp(self):
    super(CheckpkgManager2UnitTest, self).setUp()
    self.mox = mox.Mox()

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


if __name__ == '__main__':
  unittest.main()
