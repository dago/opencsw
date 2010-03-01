#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import unittest
import package_checks as pc
import checkpkg
import yaml
import os.path
import mox
import logging

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")
CHECKPKG_STATS_DIR = os.path.join(TESTDATA_DIR, "stats")

class CheckpkgUnitTestHelper(object):
  """Wraps common components of checkpkg tests."""
  MD5 = "461a24f02dd5020b4aa014b76f3ec2cc"

  def setUp(self):
    # This is slow. Let's speed it up somehow.  Move away from yaml and create
    # a Python module with the data.
    self.pkg_stats = checkpkg.PackageStats(None, CHECKPKG_STATS_DIR, self.MD5)
    self.pkg_data = self.pkg_stats.GetAllStats()
    self.mocker = mox.Mox()

  def testDefault(self):
    self.logger_mock = self.mocker.CreateMock(logging.Logger)
    self.error_mgr_mock = self.mocker.CreateMock(
        checkpkg.CheckpkgManager2.IndividualErrorGatherer)
    self.CheckpkgTest()
    self.mocker.ReplayAll()
    getattr(pc, self.FUNCTION_NAME)(self.pkg_data, self.error_mgr_mock, self.logger_mock)
    self.mocker.VerifyAll()


class TestMultipleDepends(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckMultipleDepends'
  def CheckpkgTest(self):
    self.pkg_data["depends"].append(("CSWcommon", "This is surplus"))
    self.error_mgr_mock.ReportError('dependency-listed-more-than-once',
                                    'CSWcommon')

class TestDescription(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDescription'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo'
    self.error_mgr_mock.ReportError('pkginfo-description-missing')


class TestCheckCatalogname(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckCatalogname'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo-bar - This catalog name is bad'
    self.error_mgr_mock.ReportError('pkginfo-bad-catalogname')


if __name__ == '__main__':
	unittest.main()
