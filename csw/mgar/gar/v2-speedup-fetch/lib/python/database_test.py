#!/usr/bin/env python2.6

import unittest
import database
import mox
import models


class DatabaseManagerUnitTest(mox.MoxTestBase):

  def testNoSystemFiles(self):
    # This test shows that stubbing out sqlite classes is quite laborious.
    saved_s = database.m.Srv4FileStats
    srv4_file_stats_mock_factory = self.mox.CreateMockAnything()
    database.m.Srv4FileStats = srv4_file_stats_mock_factory
    q_mock = self.mox.CreateMockAnything()
    q_mock.use_to_generate_catalogs = self.mox.CreateMockAnything()
    database.m.Srv4FileStats.q = q_mock
    # We would prefer to use self.mox.CreateMock(models.OsRelease).  The
    # reason why it doesn't work, is that mox tries to inspect the class, and
    # sqlobject overrides the __get__ method of that class, where it tries to
    # verify that a connection to a database exists.  In our tests we don't
    # have a connection, and sqlobject throws an exception.
    osrel_mock = self.mox.CreateMockAnything()
    arch_mock = self.mox.CreateMockAnything()
    osrel_mock.short_name = 'AlienOS5.3'
    arch_mock.name = 'amd65'
    dm = database.DatabaseManager()
    result_mock = self.mox.CreateMockAnything()
    srv4_file_stats_mock_factory.select(0).AndReturn(result_mock)
    # This is where we return the number of system files (0)
    result_mock.count().AndReturn(0)
    self.mox.ReplayAll()
    self.assertRaises(
        database.DatabaseError,
        dm.VerifyContents, osrel_mock, arch_mock)
    database.m.Srv4FileStats = saved_s


if __name__ == '__main__':
  unittest.main()
