#!opt/csw/bin/python2.6
# $Id$

import re
import unittest
import mox
import sharedlib_utils as su

class UtilitiesUnitTest(unittest.TestCase):

  def testIsLibraryLinkableTrue(self):
    p = "opt/csw/lib/libfoo.so.0.2"
    self.assertTrue(su.IsLibraryLinkable(p))

  def testIsLibraryLinkableNeonTrue(self):
    p = "opt/csw/lib/libneon.so.26.0.4"
    self.assertTrue(su.IsLibraryLinkable(p))

  def testIsLibraryLinkableSparc(self):
    p = "opt/csw/lib/sparcv9/libfoo.so.0.2"
    self.assertEqual(True, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableSparcPlusVis(self):
    p = "opt/csw/lib/sparcv9+vis/libfoo.so.0.2"
    self.assertEqual(True, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableAmd64(self):
    p = "opt/csw/lib/amd64/libfoo.so.0.2"
    self.assertTrue(su.IsLibraryLinkable(p))

  def testIsLibraryLinkablePrefix(self):
    p = "opt/csw/customprefix/lib/libfoo.so.0.2"
    self.assertTrue(su.IsLibraryLinkable(p))

  def testIsLibraryLinkableLibexecFalse(self):
    p = "opt/csw/libexec/bar"
    self.assertEqual(False, su.IsLibraryLinkable(p))

  def testIsLibraryLinkableFalse(self):
    p = "opt/csw/share/bar"
    self.assertEqual(False, su.IsLibraryLinkable(p))

  def testMakePackageNameBySonameSimple(self):
    soname = "libfoo.so.0"
    expected = (
        ["CSWlibfoo0", "CSWlibfoo-0"],
        ["libfoo0", "libfoo-0"],
    )
    self.assertEqual(expected, su.MakePackageNameBySoname(soname))

  def testMakePackageNameBySonameApr(self):
    soname = "libapr-1.so.0"
    expected = (
        ['CSWlibapr-10', 'CSWlibapr-1-0'],
        ['libapr-10', 'libapr-1-0']
    )
    self.assertEqual(expected,
                     su.MakePackageNameBySoname(soname))


if __name__ == '__main__':
  unittest.main()
