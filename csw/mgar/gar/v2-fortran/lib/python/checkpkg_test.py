#!/usr/bin/env python2.6
# $Id$

import copy
import re
import unittest
import mox
import difflib
import checkpkg
import checkpkg_lib
import database
import models as m
import tag
import package_stats
import sqlite3
import sqlobject
import test_base
import common_constants

from testdata.tree_stats import pkgstats as tree_stats
from testdata.neon_stats import pkgstats as neon_stats

"""A set of unit tests for the library checking code.

A bunch of lines to test in the interactive Python shell.

import sys
sys.path.append("lib/python")
import checkpkg

sqlite3 ~/.checkpkg/var-sadm-install-contents-cache-build8x
SELECT * FROM systempkgmap WHERE basename = 'libncursesw.so.5';
"""

class ExtractorsUnitTest(unittest.TestCase):

  def testExtractDescriptionFromGoodData(self):
    data = {"NAME": "nspr_devel - Netscape Portable Runtime header files"}
    result = "Netscape Portable Runtime header files"
    self.assertEqual(result, checkpkg.ExtractDescription(data))

  def testExtractDescriptionWithBadCatalogname(self):
    data = {"NAME": "foo-bar - Bad catalogname shouldn't break this function"}
    result = "Bad catalogname shouldn't break this function"
    self.assertEqual(result, checkpkg.ExtractDescription(data))

  def testExtractMaintainerName(self):
    data = {"VENDOR": "https://ftp.mozilla.org/pub/mozilla.org/"
                      "nspr/releases/v4.8/src/ packaged for CSW by "
                      "Maciej Blizinski"}
    result = "Maciej Blizinski"
    self.assertEqual(result, checkpkg.ExtractMaintainerName(data))

  def testPstampRegex(self):
    pstamp = "hson@solaris9s-csw-20100313144445"
    expected = {
        'username': 'hson',
        'timestamp': '20100313144445',
        'hostname': 'solaris9s-csw'
    }
    self.assertEqual(expected, re.match(common_constants.PSTAMP_RE, pstamp).groupdict())


class SliceListUnitTest(unittest.TestCase):

  def testOne(self):
    l = [1, 2, 3, 4, 5]
    s = 1
    expected = [[1], [2], [3], [4], [5]]
    self.assertTrue(expected, checkpkg_lib.SliceList(l, s))

  def testTwo(self):
    l = [1, 2, 3, 4, 5]
    s = 2
    expected = [[1, 2], [3, 4], [5]]
    self.assertTrue(expected, checkpkg_lib.SliceList(l, s))


class SqliteUnitTest(unittest.TestCase):

  "Makes sure that we can lose state between tests."

  def setUp(self):
    self.conn = sqlite3.connect(":memory:")
    self.c = self.conn.cursor()

  def tearDown(self):
    self.conn = None

  def testCannotCreateTwoTables(self):
    self.c.execute("CREATE TABLE foo (INT bar);")
    self.assertRaises(
        sqlite3.OperationalError,
        self.c.execute, "CREATE TABLE foo (INT bar);")

  def testOne(self):
    self.c.execute("CREATE TABLE foo (INT bar);")

  def testTwo(self):
    self.c.execute("CREATE TABLE foo (INT bar);")


class SqlobjectUnitTest(test_base.SqlObjectTestMixin, unittest.TestCase):

  "Makes sure that we can lose state between methods."

  class TestModel(sqlobject.SQLObject):
    name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

  # This does not work. Why?
  # def testCannotCreateTwoTables(self):
  #   self.TestModel.createTable()
  #   self.assertRaises(
  #       sqlite3.OperationalError,
  #       self.TestModel.createTable)

  def testOne(self):
    self.TestModel.createTable()

  def testTwo(self):
    self.TestModel.createTable()


if __name__ == '__main__':
  # import logging
  # logging.basicConfig(level=logging.DEBUG)
  unittest.main()
