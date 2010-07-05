#!/opt/csw/bin/python2.6

import os
import sys
import unittest
import mox
import checkpkg_collect_stats as ccs

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw


class PackageStatsUnitTest(unittest.TestCase):

  def setUp(self):
    self.mocker = mox.Mox()

  def testGetStatsPath(self):
    mock_pkg = self.mocker.CreateMock(opencsw.CswSrv4File)
    mock_pkg.GetMd5sum().AndReturn("abcdef")
    self.mocker.ReplayAll()
    sc = ccs.PackageStats(mock_pkg)
    expected = "/home/joe/.checkpkg/stats/ab/abcdef"
    self.assertEqual(expected, sc.GetStatsPath("/home/joe"))
    self.mocker.VerifyAll()


if __name__ == '__main__':
	unittest.main()
