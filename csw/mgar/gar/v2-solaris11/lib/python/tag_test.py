#!/opt/csw/bin/python2.6
# $Id$
# coding=utf-8

import unittest
import tag

class ParseTagLineUnitTest(unittest.TestCase):

  def testParseTagLine1(self):
    line = "foo-tag"
    self.assertEquals((None, "foo-tag", None), tag.ParseTagLine(line))

  def testParseTagLine2(self):
    line = "CSWfoo: foo-tag"
    self.assertEquals(("CSWfoo", "foo-tag", None), tag.ParseTagLine(line))

  def testParseTagLine3(self):
    line = "CSWfoo: foo-tag foo-info"
    self.assertEquals(("CSWfoo", "foo-tag", "foo-info"),
                      tag.ParseTagLine(line))

  def testParseTagLine4(self):
    line = "CSWfoo: foo-tag foo-info1 foo-info2"
    self.assertEquals(("CSWfoo", "foo-tag", "foo-info1 foo-info2"),
                      tag.ParseTagLine(line))

  def testParseTagLine_WithUrl(self):
    line = "CSWfoo: tag-with-an-url http://www.example.com/"
    self.assertEquals(("CSWfoo", "tag-with-an-url", "http://www.example.com/"),
                      tag.ParseTagLine(line))


if __name__ == '__main__':
  unittest.main()
