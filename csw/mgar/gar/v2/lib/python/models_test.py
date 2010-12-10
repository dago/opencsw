import unittest
import models

class CheckpkgErrorTagUnitTest(unittest.TestCase):

  class TestErrorTag(models.CheckpkgErrorTagMixin):

    def __init__(self, pkgname, tag_name, tag_info=None):
      self.pkgname = pkgname
      self.tag_name = tag_name
      self.tag_info = tag_info

  def testToGarSyntaxNoParam(self):
    t = self.TestErrorTag("CSWfoo", "bar")
    self.assertEquals(u'CHECKPKG_OVERRIDES_CSWfoo += bar', t.ToGarSyntax())

  def testToGarSyntaxWithParam(self):
    t = self.TestErrorTag("CSWfoo", "bar", "parameter")
    self.assertEquals(u'CHECKPKG_OVERRIDES_CSWfoo += bar|parameter', t.ToGarSyntax())

  def testToGarSyntaxWithParamWithSpacees(self):
    t = self.TestErrorTag("CSWfoo", "bar", "a b c")
    self.assertEquals(u'CHECKPKG_OVERRIDES_CSWfoo += bar|a|b|c', t.ToGarSyntax())

  def testComparison(self):
    t1 = self.TestErrorTag("CSWfoo", "bar", "a b c")
    t2 = self.TestErrorTag("CSWfoo", "bar", "a b c")
    self.assertEquals(t1, t2)


if __name__ == '__main__':
  unittest.main()

