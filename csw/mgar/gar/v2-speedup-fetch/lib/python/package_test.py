#!/usr/bin/env python2.6

import unittest
import package
import mox
import os
import posix
import datetime

class CswSrv4FileUnitTest(mox.MoxTestBase):

  def testGetMtime(self):
    p = package.CswSrv4File("/fake/path")
    self.mox.StubOutWithMock(os, 'stat')
    stat_result_mock = self.mox.CreateMock(posix.stat_result)
    stat_result_mock.st_mtime = 1292318507.0
    os.stat("/fake/path").AndReturn(stat_result_mock)
    self.mox.ReplayAll()
    self.assertEquals(
        datetime.datetime(2010, 12, 14, 9, 21, 47),
        p.GetMtime())


if __name__ == '__main__':
  unittest.main()
