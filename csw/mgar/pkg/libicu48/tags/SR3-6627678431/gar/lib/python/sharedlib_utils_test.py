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


class GetCommonVersionUnitTest(unittest.TestCase):

  def testGetCommonVersionSimple(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    self.assertEqual((True, "0"), su.GetCommonVersion(sonames))

  def testGetCommonVersionMore(self):
    sonames = ["libfoo.so.0.2.1", "libfoo_util.so.0.2.1"]
    self.assertEqual((True, "0.2.1"), su.GetCommonVersion(sonames))

  def testGetCommonVersionInvalid(self):
    sonames = ["libfoo.so.0.2.1", "libfoo_util.so.0.2.3"]
    self.assertEqual((False, None), su.GetCommonVersion(sonames))

  def testGetCommonVersionEndsWithSo(self):
    sonames = ["libfoo1.so", "libfoo1.so"]
    self.assertEqual((True, ""), su.GetCommonVersion(sonames))


class MakePackageNameBySonameCollectionUnitTest(unittest.TestCase):

  def testMakePackageNameBySonameCollectionTwo(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    expected = (
        ["CSWlibfoo0"],
        ["libfoo0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionRepeated(self):
    sonames = ["libfoo.so.0", "libfoo.so.0"]
    expected = (
        ["CSWlibfoo0"],
        ["libfoo0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionBdb(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    expected = (
        ["CSWlibfoo0"],
        ["libfoo0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionNoCommonVersion(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.1"]
    self.assertEqual(None, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionMultipleSo(self):
    sonames = ["libfoo1.so", "libfoo1.so"]
    expected = (
        ["CSWlibfoo1"],
        ["libfoo1"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionMultipleSoGlib2(self):
    sonames = [
      "libgio-2.0.so.0",
      "libglib-2.0.so.0",
      "libgmodule-2.0.so.0",
      "libgobject-2.0.so.0",
      "libgthread-2.0.so.0",
    ]
    self.assertEqual(None, su.MakePackageNameBySonameCollection(sonames))


class ValidateCollectionNameTest(unittest.TestCase):

  def testLetters(self):
    self.assertEqual(True, su.ValidateCollectionName("foo"))

  def testOneLetter(self):
    self.assertEqual(False, su.ValidateCollectionName("f"))

  def testNoLetters(self):
    self.assertEqual(False, su.ValidateCollectionName("-2.0"))


class CommomSubstringTest(unittest.TestCase):

  def testLongestCommonSubstring_1(self):
    self.assertEqual(set(["foo"]), su.LongestCommonSubstring("foo", "foo"))

  def testLongestCommonSubstring_2(self):
    self.assertEqual(set([]), su.LongestCommonSubstring("foo", "bar"))

  def testLongestCommonSubstring_3(self):
    self.assertEqual(set(["bar"]), su.LongestCommonSubstring("barfoobar", "bar"))

  def testLongestCommonSubstring_4(self):
    self.assertEqual(set(['bcd', 'hij']), su.LongestCommonSubstring("abcdefghijk", "bcdhij"))


class GetIsalistUnitTest(unittest.TestCase):

  def testGetIsalistSparc(self):
    self.assertTrue("sparcv8plus+vis" in su.GetIsalist("sparc"))


if __name__ == '__main__':
  unittest.main()
