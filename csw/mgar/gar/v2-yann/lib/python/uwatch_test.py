#!/usr/bin/env python2.6

import unittest
import uwatch
import re

class UpstreamWatchCommandUnitTest(unittest.TestCase):

  V1 = "1.8.1,REV=2010.07.13"
  V2 = "1.8.2,REV=2011.01.17"

  def testCompareVersionAndGetNewest(self):
    uwc = uwatch.UpstreamWatchCommand("fake name")
    self.assertEquals(
        self.V2,
        uwc.CompareVersionAndGetNewest(self.V1, self.V2))


class UwatchRegexGeneratorUnitTest(unittest.TestCase):

  def setUp(self):
    self.urg = uwatch.UwatchRegexGenerator()

  def test_ChooseDistfile(self):
    data = uwatch.UwatchRegexGenerator.WS_RE.split(
        u'amavisd-new-2.6.4.tar.gz '
        u'CSWamavisdnew.cswusergroup CSWamavisdnew.postinstall '
        u'CSWamavisdnew.preinstall ')
    self.assertEquals(u'amavisd-new-2.6.4.tar.gz',
        self.urg._ChooseDistfile(data))

  def testDigitSplit(self):
    self.assertEqual(
        ['-', '.tar.gz'],
        uwatch.UwatchRegexGenerator.DIGIT_REMOVAL_RE.split("-4.13b.tar.gz"))

  def ExpandBaseRegex(self, expected_regex):
    expected = [
        expected_regex % {"letter": "[a-z]?"},
        expected_regex % {"letter": ""},
    ]
    return expected

  def test_SeparateArchiveName(self):
    filename = "Crypt-DES_EDE3-0.01.tar.gz"
    expected = ('Crypt-DES_EDE3-0.01', '.tar.gz')
    self.assertEqual(expected, self.urg._SeparateArchiveName(filename))

  def test_SeparateArchiveName(self):
    filename = "Crypt-DES_EDE3-0.01.tar.bz2"
    expected = ('Crypt-DES_EDE3-0.01', '.tar.bz2')
    self.assertEqual(expected, self.urg._SeparateArchiveName(filename))

  def test_SeparateSoftwareName(self):
    filename = "Crypt-DES_EDE3-0.01.tar.gz"
    expected = ('Crypt-DES_EDE3', '-0.01.tar.gz')
    self.assertEqual(
        expected,
        self.urg._SeparateSoftwareName("pm_crypt_des_ede3", filename))

  def testSimple(self):
    distfiles = "foo-0.01.tar.gz"
    regex = self.urg.GenerateRegex("foo", distfiles)[0]
    self.assertEqual(["0.01"], re.findall(regex, distfiles))

  def testDash(self):
    distfiles = "foo-0.01.tar.gz"
    new_file = "foo-0.01-2.tar.gz"
    regex = self.urg.GenerateRegex("foo", distfiles)[0]
    self.assertEqual(["0.01-2"], re.findall(regex, new_file))

  def testDigitInName(self):
    distfiles = "Crypt-DES_EDE3-0.01.tar.gz"
    regex = self.urg.GenerateRegex("foo", distfiles)[0]
    self.assertEqual(["0.01"], re.findall(regex, distfiles))



if __name__ == '__main__':
	unittest.main()
