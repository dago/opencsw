#!/usr/bin/env python2.6
# $Id$

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

  def testIsLibraryLinkablePrefix(self):
    self.assertFalse(
        su.IsLibraryLinkable("opt/csw/customprefix/lib/libfoo.so.0.2"))

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
    self.assertEqual(False, su.IsLibraryLinkable(
      "opt/csw/lib/erlang/lib/megaco-3.6.0.1/priv/lib"
      "/megaco_flex_scanner_drv_mt.so"))

  def testIsLibraryLinkableInShared(self):
    self.assertEqual(False, su.IsLibraryLinkable(
      "opt/csw/share/Adobe/Reader8/Reader/sparcsolaris/lib"
      "/libcrypto.so.0.9.6"))

  def testMakePackageNameBySonameSimple(self):
    soname = "libfoo.so.0"
    expected = (
        ["CSWlibfoo0", "CSWlibfoo-0"],
        ["libfoo0", "libfoo_0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameMinorVersion(self):
    soname = "libfoo.so.0.1"
    expected = (
        ["CSWlibfoo0-1", "CSWlibfoo-0-1"],
        ["libfoo0_1", "libfoo_0_1"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameApr(self):
    soname = "libapr-1.so.0"
    expected = (
        ['CSWlibapr-10', 'CSWlibapr-1-0'],
        ['libapr_10', 'libapr_1_0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameDot(self):
    soname = "libbabl-0.1.so.0"
    expected = (
        ['CSWlibbabl-0-10', 'CSWlibbabl-0-1-0'],
        ['libbabl_0_10', 'libbabl_0_1_0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameMoreDot(self):
    soname = "libgettextlib-0.14.1.so"
    expected = (
        ['CSWlibgettextlib-0-14-1'],
        ['libgettextlib_0_14_1'],
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
       ['CSWlibstdc++6', 'CSWlibstdc++-6'],
       ['libstdc++6', 'libstdc++_6']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonamePlus(self):
    soname = "libdnet.1"
    expected = (
       ['CSWlibdnet1', 'CSWlibdnet-1'],
       ['libdnet1', 'libdnet_1']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testMakePackageNameUppercase(self):
    soname = "libUpperCase.so.1"
    expected = (
       ['CSWlibuppercase1', 'CSWlibuppercase-1'],
       ['libuppercase1', 'libuppercase_1']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))

  def testSanitizeWithChar(self):
    self.assertEqual("foo_0", su.SanitizeWithChar("foo-0", "_"))


class GetCommonVersionUnitTest(unittest.TestCase):

  def testGetCommonVersionSimple(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    self.assertEqual("0", su.GetCommonVersion(sonames))

  def testGetCommonVersionMore(self):
    sonames = ["libfoo.so.0.2.1", "libfoo_util.so.0.2.1"]
    self.assertEqual("0.2.1", su.GetCommonVersion(sonames))

  def testGetCommonVersionInvalid(self):
    sonames = ["libfoo.so.0.2.1", "libfoo_util.so.0.2.3"]
    self.assertEqual(None, su.GetCommonVersion(sonames))


class MakePackageNameBySonameCollectionUnitTest(unittest.TestCase):

  def testMakePackageNameBySonameCollectionTwo(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    expected = (
        ["CSWlibfoo0", "CSWlibfoo-0"],
        ["libfoo0", "libfoo_0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionBdb(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.0"]
    expected = (
        ["CSWlibfoo0", "CSWlibfoo-0"],
        ["libfoo0", "libfoo_0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySonameCollection(sonames))

  def testMakePackageNameBySonameCollectionNoCommonVersion(self):
    sonames = ["libfoo.so.0", "libfoo_util.so.1"]
    self.assertEqual(None, su.MakePackageNameBySonameCollection(sonames))


class CommomSubstringTest(unittest.TestCase):

  def testLongestCommonSubstring_1(self):
    self.assertEqual(set(["foo"]), su.LongestCommonSubstring("foo", "foo"))

  def testLongestCommonSubstring_2(self):
    self.assertEqual(set([]), su.LongestCommonSubstring("foo", "bar"))

  def testLongestCommonSubstring_3(self):
    self.assertEqual(set(["bar"]), su.LongestCommonSubstring("barfoobar", "bar"))

  def testLongestCommonSubstring_4(self):
    self.assertEqual(set(['bcd', 'hij']), su.LongestCommonSubstring("abcdefghijk", "bcdhij"))


if __name__ == '__main__':
  unittest.main()
