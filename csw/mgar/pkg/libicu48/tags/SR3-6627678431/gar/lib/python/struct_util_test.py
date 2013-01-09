#!/usr/bin/env python2.6

import unittest
import struct_util

class IndexByUnitTest(unittest.TestCase):

  def testIndexDictsBy_1(self):
    list_of_dicts = [
        {"a": 1},
        {"a": 2},
        {"a": 3},
    ]
    expected = {
        1: [{'a': 1}],
        2: [{'a': 2}],
        3: [{'a': 3}],
    }
    self.assertEquals(expected, struct_util.IndexDictsBy(list_of_dicts, "a"))

  def testIndexDictsBy_2(self):
    list_of_dicts = [
        {"a": 1, "b": 1},
        {"a": 1, "b": 2},
        {"a": 1, "b": 3},
    ]
    expected = {
        1: [
          {'a': 1, 'b': 1},
          {'a': 1, 'b': 2},
          {'a': 1, 'b': 3},
        ]
    }
    self.assertEquals(expected, struct_util.IndexDictsBy(list_of_dicts, "a"))


class ResolveSymlinkUnitTest(unittest.TestCase):

  def testRelative(self):
    self.assertEquals(
        "/opt/csw/libexec/foo-exec",
        struct_util.ResolveSymlink("/opt/csw/bin/foo", "../libexec/foo-exec"))

  def testAsolute(self):
    self.assertEquals(
        "/libexec/foo-exec",
        struct_util.ResolveSymlink("/opt/csw/bin/foo", "/libexec/foo-exec"))


class OsReleaseToLongTest(unittest.TestCase):

  def testLong(self):
    self.assertEqual("SunOS5.9", struct_util.OsReleaseToLong("SunOS5.9"))

  def testShort(self):
    self.assertEqual("SunOS5.9", struct_util.OsReleaseToLong("5.9"))


class MakeCatalognameByPkgnameTest(unittest.TestCase):

  def testSimple(self):
    self.assertEqual("foo", struct_util.MakeCatalognameByPkgname("CSWfoo"))

  def testWithDash(self):
    self.assertEqual("foo_bar", struct_util.MakeCatalognameByPkgname("CSWfoo-bar"))

  def testCollapseSeparators(self):
    self.assertEqual("foo_bar", struct_util.MakeCatalognameByPkgname("CSWfoo--bar"))

  def testWithDigits(self):
    # This shouldn't be a typical case.
    self.assertEqual("libfoo1_1", struct_util.MakeCatalognameByPkgname("CSWlibfoo1-1"))

  def testPluses(self):
    # Pluses?  Plusen?  Plusi?
    self.assertEqual("libnetcdf_c++5", struct_util.MakeCatalognameByPkgname("CSWlibnetcdf-c++5"))

  def testWithDigits(self):
    self.assertEqual("libfoo1_1", struct_util.MakeCatalognameByPkgname("CSWlibfoo1-1"))


if __name__ == '__main__':
	unittest.main()
