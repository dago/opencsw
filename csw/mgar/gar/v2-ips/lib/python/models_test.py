#!/usr/bin/env python2.6

import unittest
import mox
import test_base
import models
import sqlobject
import datetime

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


class Srv4FileStatsUnitTest(test_base.SqlObjectTestMixin, mox.MoxTestBase):

  def setUp(self):
    super(Srv4FileStatsUnitTest, self).setUp()
    self.dbc.InitialDataImport()
    self.sqo_arch = models.Architecture.selectBy(id=1).getOne()
    self.sqo_osrel = models.OsRelease.selectBy(id=1).getOne()
    self.sqo_catrel = models.CatalogRelease.selectBy(id=1).getOne()
    self.pkginst = models.Pkginst(pkgname="CSWfoo")
    self.maintainer = models.Maintainer(
        email='joe@example.com',
        full_name='Joe Bloggs')
    self.p = models.Srv4FileStats(
        arch=self.sqo_arch,
        basename="foo.pkg",
        catalogname="foo",
        data_obj=None,
        filename_arch=self.sqo_arch,
        latest=True,
        maintainer=self.maintainer,
        md5_sum="not a real one",
        size=1L,
        mtime=datetime.datetime.now(),
        os_rel=self.sqo_osrel,
        pkginst=self.pkginst,
        registered=True,
        use_to_generate_catalogs=True,
        rev="2011.01.01",
        stats_version=0,
        version_string="1.0,REV=2011.01.01",
    )

  def testRemoveCheckpkgResults(self):
    error_tag = models.CheckpkgErrorTag(
        tag_name="foo",
        tag_info="foo_info",
        srv4_file=self.p,
        os_rel=self.sqo_osrel,
        arch=self.sqo_arch,
        catrel=self.sqo_catrel,
    )
    self.assertEqual(1, models.CheckpkgErrorTag.select().count())
    self.p.RemoveCheckpkgResults(self.sqo_osrel, self.sqo_arch, self.sqo_catrel)
    self.assertEqual(0, models.CheckpkgErrorTag.select().count())


if __name__ == '__main__':
  unittest.main()

