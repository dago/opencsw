#!/usr/bin/env python2.6
# $Id$

"""Tests for the shared library utilities."""

__author__ = "Maciej Blizinski <maciej@opencsw.org>"

import re
import unittest
import mox
import sharedlib_utils as su

class UtilitiesUnitTest(unittest.TestCase):

  def testIsLibraryLinkableTrue(self):
    self.assertTrue(su.IsLibraryLinkable("opt/csw/lib/libfoo.so.0.2"))

  def testIsLibraryLinkableNeonTrue(self):
    p = "opt/csw/lib/libneon.so.26.0.4"
    self.assertTrue(su.IsLibraryLinkable(p))

  def testIsLibraryLinkableSparc(self):
    p = "opt/csw/lib/sparcv9/libfoo.so.0.2"
    self.assertEqual(True, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableSparcPlusVis(self):
    p = "opt/csw/lib/sparcv8plus+vis/libfoo.so.0.2"
    self.assertEqual(True, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableAmd64(self):
    self.assertTrue(su.IsLibraryLinkable("opt/csw/lib/amd64/libfoo.so.0.2"))

  def testIsLibraryLinkableLibexecFalse(self):
    p = "opt/csw/libexec/bar"
    self.assertEqual(False, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableFalse(self):
    p = "opt/csw/share/bar"
    self.assertEqual(False, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableSubdir(self):
    p = "opt/csw/lib/gnucash/libgncmod-stylesheets.so.0.0.0"
    self.assertEqual(False, su.IsLibraryLinkable(p))

  def testIsLibraryLinkablePrivateLib(self):
    self.assertFalse(su.IsLibraryLinkable(
      "opt/csw/lib/erlang/lib/megaco-3.6.0.1/priv/lib"
      "/megaco_flex_scanner_drv_mt.so"))

  def testIsLibraryLinkableInShared(self):
    self.assertFalse(su.IsLibraryLinkable(
      "opt/csw/share/Adobe/Reader8/Reader/sparcsolaris/lib"
      "/libcrypto.so.0.9.6"))

  def testIsLibraryLinkablePrefix(self):
    self.assertTrue(
        su.IsLibraryLinkable("opt/csw/customprefix/lib/libfoo.so.0.2"))

  def testIsLibraryLinkableInPrefix(self):
    """This could be considered linkable.

    Reason: It has the form of "/opt/csw/foo/lib/libfoo.so.1"."""
    self.assertTrue(su.IsLibraryLinkable(
      "opt/csw/boost-gcc/lib"
      "/libboost_wserialization.so.1.44.0"))

  def testIsLibraryLinkableWithPrefix(self):
    self.assertTrue(
        su.IsLibraryLinkable("opt/csw/bdb48/lib/libdb-4.8.so"))


class MakePackageNameBySonameUnitTest(unittest.TestCase):

  def testMakePackageNameBySonameSimple(self):
    soname = "libfoo.so.0"
    expected = (
        ["CSWlibfoo0"],
        ["libfoo0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameMinorVersion(self):
    soname = "libfoo.so.0.1"
    expected = (
        ["CSWlibfoo0-1"],
        ["libfoo0_1"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameApr(self):
    soname = "libapr-1.so.0"
    expected = (
        ['CSWlibapr1-0'],
        ['libapr1_0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameDot(self):
    soname = "libbabl-0.1.so.0"
    expected = (
        ['CSWlibbabl0-1-0'],
        ['libbabl0_1_0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameMoreDot(self):
    soname = "libgettextlib-0.14.1.so"
    expected = (
        ['CSWlibgettextlib0-14-1'],
        ['libgettextlib0_14_1'],
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameComplexApr(self):
    soname = "libapr-1.so.10"
    expected = (
       ['CSWlibapr-110', 'CSWlibapr-1-10'],
       ['libapr_110', 'libapr_1_10']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonamePlus(self):
    soname = "libstdc++.so.6"
    expected = (
       ['CSWlibstdc++6'],
       ['libstdc++6']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameNoVersion(self):
    soname = "libdnet.1"
    expected = (
       ['CSWlibdnet1'],
       ['libdnet1']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameUppercase(self):
    soname = "libUpperCase.so.1"
    expected = (
       ['CSWlibuppercase1'],
       ['libuppercase1']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameDashesNoDashes(self):
    soname = "libpyglib-2.0-python.so.0"
    expected = (
       ['CSWlibpyglib2-0python0'],
       ['libpyglib2_0python0'],
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameDashesNoDashesPython(self):
    soname = "libpython3.1.so.1.0"
    expected = (
       ['CSWlibpython3-1-1-0'],
       ['libpython3_1_1_0'],
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameComplexApr(self):
    soname = "libapr-1.so.10.0.0"
    expected = (
       ['CSWlibapr1-10-0-0'],
       ['libapr1_10_0_0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameWithPath(self):
    soname = "libfoo.so.0"
    path = "/opt/csw/gxx/lib"
    expected = (
        ["CSWlibfoo0-gxx"],
        ["libfoo0-gxx"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname, path))

  def testMakePackageNameBySonameWithPathSparcv9(self):
    soname = "libfoo.so.0"
    path = "/opt/csw/gxx/lib/sparcv9"
    expected = (
        ["CSWlibfoo0-gxx"],
        ["libfoo0-gxx"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname, path))


class ParseLibPathTest(unittest.TestCase):

  def testSimple(self):
    self.assertEquals({"prefix": None}, su.ParseLibPath("/opt/csw/lib"))

  def testPrefix(self):
    self.assertEquals({"prefix": "gxx"}, su.ParseLibPath("/opt/csw/gxx/lib"))

  def testWithArch(self):
    self.assertEquals({"prefix": "gxx"}, su.ParseLibPath("/opt/csw/gxx/lib/amd64"))


class SanitizationUnitTest(unittest.TestCase):

  def testSanitizeWithChar(self):
    self.assertEqual("foo_0", su.SanitizeWithChar("foo-0", "_"))

  def testSanitizeWithChar(self):
    self.assertEqual("foo_0", su.SanitizeWithChar("foo-0", "_"))

  def testSonameToStringWithCharAlphaDigit(self):
    self.assertEqual("foo0", su.SonameToStringWithChar("foo-0", "_"))

  def testSonameToStringWithCharDigitDigit(self):
    self.assertEqual("foo0_0", su.SonameToStringWithChar("foo-0-0", "_"))

  def testSonameToStringWithCharDigitDigit(self):
    self.assertEqual("foo_bar0_0", su.SonameToStringWithChar("foo-bar-0-0", "_"))

  def testSonameToStringWithCharPython(self):
    self.assertEqual("libpython3_1_1_0", su.SonameToStringWithChar("libpython3.1.so.1.0", "_"))


class GetIsalistUnitTest(unittest.TestCase):

  def testGetIsalistSparc(self):
    self.assertTrue("sparcv8plus+vis" in su.GetIsalist("sparc"))


class ExtractPrefixTest(unittest.TestCase):

  def testNoPrefix(self):
    self.assertEquals(None, su.ExtractPrefix("/opt/csw/lib"))

  def testSimple(self):
    self.assertEquals("gxx", su.ExtractPrefix("/opt/csw/gxx/lib"))

  def testWithArch(self):
    self.assertEquals("gxx", su.ExtractPrefix("/opt/csw/gxx/lib/sparcv9"))


if __name__ == '__main__':
  unittest.main()
