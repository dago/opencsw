# $Id$
# coding=utf-8

import unittest
import overrides
import re
import tag

class ParseOverrideLineUnitTest(unittest.TestCase):

  def setUp(self):
    line1 = "CSWfoo: foo-override"
    line2 = "CSWfoo: foo-override foo-info"
    line3 = "CSWfoo: foo-override foo-info-1 foo-info-2"
    line4 = ("CSWpmcommonsense: "
             "pkginfo-description-not-starting-with-uppercase "
             "common-sense: Some sane defaults for Perl programs")
    self.o1 = overrides.ParseOverrideLine(line1)
    self.o2 = overrides.ParseOverrideLine(line2)
    self.o3 = overrides.ParseOverrideLine(line3)
    self.o4 = overrides.ParseOverrideLine(line4)

  def test_ParseOverridesLine1(self):
    self.assertEqual("CSWfoo", self.o1.pkgname)

  def test_ParseOverridesLine2(self):
    self.assertEqual("foo-override", self.o1.tag_name)

  def test_ParseOverridesLine3(self):
    self.assertEqual(None, self.o1.tag_info)

  def test_ParseOverridesLine4(self):
    self.assertEqual("foo-info", self.o2.tag_info)

  def test_ParseOverridesLine5(self):
    self.assertEqual("CSWfoo", self.o3.pkgname)

  def test_ParseOverridesLine6(self):
    self.assertEqual("foo-override", self.o3.tag_name)

  def test_ParseOverridesLine7(self):
    self.assertEqual("foo-info-1 foo-info-2", self.o3.tag_info)

  def test_ParseOverridesLine_4_1(self):
    self.assertEqual("CSWpmcommonsense", self.o4.pkgname)

  def test_ParseOverridesLine_4_2(self):
    self.assertEqual(
        "pkginfo-description-not-starting-with-uppercase",
        self.o4.tag_name)

  def test_ParseOverridesLine_4_3(self):
    self.assertEqual(
        "common-sense: Some sane defaults for Perl programs",
        self.o4.tag_info)


class ApplyOverridesUnitTest(unittest.TestCase):

  # This would be better, more terse. But requires metaclasses.
  DATA_1 = (
      (None, 'tag1', 'info1', None, 'tag1', 'info1', None),
  )

  def test_1a(self):
    """One tag, no overrides."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag")]
    oo = []
    self.assertEqual((tags, set([])), overrides.ApplyOverrides(tags, oo))

  def test_1b(self):
    """One override, matching by tag name only."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag")]
    oo = [overrides.Override(None, "foo-tag", None)]
    self.assertEqual(([], set([])), overrides.ApplyOverrides(tags, oo))

  def test_1c(self):
    """One override, matching by tag name only, no pkgname."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag")]
    oo = [overrides.Override(None, "foo-tag", None)]
    self.assertEqual(([], set([])), overrides.ApplyOverrides(tags, oo))

  def test_2(self):
    """One override, matching by tag name and tag info, no pkgname."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag")]
    oo = [overrides.Override(None, "foo-tag", None)]
    self.assertEqual(([], set([])), overrides.ApplyOverrides(tags, oo))

  def test_3(self):
    """One override, matching by tag name, mismatching tag info, no pkgname."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag", "tag-info-1")]
    oo = [overrides.Override(None, "foo-tag", "tag-info-2")]
    self.assertEqual((tags, set(oo)), overrides.ApplyOverrides(tags, oo))

  def test_4(self):
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag", "tag-info-1")]
    oo = [overrides.Override(None, "foo-tag", "tag-info-1")]
    self.assertEqual(([], set([])), overrides.ApplyOverrides(tags, oo))

  def test_5(self):
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag", "tag-info-1")]
    oo = [overrides.Override("CSWfoo", "foo-tag", "tag-info-1")]
    self.assertEqual(([], set([])), overrides.ApplyOverrides(tags, oo))

  def test_6(self):
    """Pkgname mismatch."""
    tags = [tag.CheckpkgTag("CSWfoo", "foo-tag", "tag-info-1")]
    oo = [overrides.Override("CSWbar", "foo-tag", "tag-info-1")]
    self.assertEqual((tags, set(oo)), overrides.ApplyOverrides(tags, oo))


if __name__ == '__main__':
  unittest.main()
