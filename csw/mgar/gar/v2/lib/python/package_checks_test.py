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
DEFAULT_MD5 = "461a24f02dd5020b4aa014b76f3ec2cc"

class CheckpkgUnitTest(unittest.TestCase):
  """Write a helper function using mox."""

  def setUp(self):
    self.pkg_stats = checkpkg.PackageStats(None,
                                           CHECKPKG_STATS_DIR,
                                           DEFAULT_MD5)
    self.pkg_data = self.pkg_stats.GetAllStats()
    self.mocker = mox.Mox()

  def testMultipleDepends(self):
    logger_mock = self.mocker.CreateMock(logging.Logger)
    error_mgr_mock = self.mocker.CreateMock(
        checkpkg.CheckpkgManager2.IndividualErrorGatherer)
    self.pkg_data["depends"].append(("CSWcommon", "This is surplus")) # this
    error_mgr_mock.ReportError('dependency-listed-more-than-once', 'CSWcommon') # this
    self.mocker.ReplayAll()
    pc.CheckMultipleDepends(self.pkg_data, error_mgr_mock, logger_mock) # name or variable
    self.mocker.VerifyAll()


if __name__ == '__main__':
	unittest.main()
