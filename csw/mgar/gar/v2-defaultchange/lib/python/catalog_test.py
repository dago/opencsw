#!/usr/bin/env python2.6

import unittest
import catalog
import os.path
from StringIO import StringIO

CATALOG_LINE_1 = (
    "syslog_ng 3.0.4,REV=2009.08.30 "
    "CSWsyslogng "
    "syslog_ng-3.0.4,REV=2009.08.30-SunOS5.8-i386-CSW.pkg.gz "
    "cfe40c06e994f6e8d3b191396d0365cb 137550 "
    "CSWgcc4corert|CSWeventlog|CSWosslrt|CSWzlib|CSWpcrert|CSWggettextrt|"
    "CSWglib2|CSWtcpwrap|CSWcswclassutils|CSWcommon none")
CATALOG_LINE_2 = (
    "syslog_ng 3.0.4,REV=2009.10.12 "
    "CSWsyslogng "
    "syslog_ng-3.0.4,REV=2009.10.12-SunOS5.8-i386-CSW.pkg.gz "
    "a1e9747ac3aa04c0497d2a3a23885995 137367 "
    "CSWcswclassutils|CSWgcc4corert|CSWeventlog|CSWosslrt|CSWzlib|CSWpcrert|"
    "CSWggettextrt|CSWglib2|CSWtcpwrap|CSWcswclassutils|CSWcommon none")
CATALOG_LINE_3 = (
        'tmux 1.2,REV=2010.05.17 CSWtmux '
        'tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz '
        '145351cf6186fdcadcd169b66387f72f 214091 '
        'CSWcommon|CSWlibevent none none\n')

# Package as returned by the catalog file parser
PKG_STRUCT_1 = {
    'catalogname': 'syslog_ng',
    'category': 'none',
    'deps': (
        # Dependencies need to be ordered that way, because they're
        # listed that way in the package.
        'CSWgcc4corert',
        'CSWeventlog',
        'CSWosslrt',
        'CSWzlib',
        'CSWpcrert',
        'CSWggettextrt',
        'CSWglib2',
        'CSWtcpwrap',
        'CSWcswclassutils',
        'CSWcommon',
    ),
    'file_basename': 'syslog_ng-3.0.4,REV=2009.08.30-SunOS5.8-i386-CSW.pkg.gz',
    'i_deps': (),
    'md5sum': 'cfe40c06e994f6e8d3b191396d0365cb',
    'pkgname': 'CSWsyslogng',
    'size': '137550',
    'version': '3.0.4,REV=2009.08.30',
}


class OpencswCatalogUnitTest(unittest.TestCase):

  def test_ParseCatalogLine_1(self):
    oc = catalog.OpencswCatalog(None)
    parsed = oc._ParseCatalogLine(CATALOG_LINE_3)
    expected = {'catalogname': 'tmux',
                'deps': ('CSWcommon', 'CSWlibevent'),
                'file_basename': 'tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz',
                'md5sum': '145351cf6186fdcadcd169b66387f72f',
                'category': 'none',
                'i_deps': (),
                'pkgname': 'CSWtmux',
                'size': '214091',
                'version': '1.2,REV=2010.05.17'}
    self.assertEquals(expected, parsed)

  def testGetDataByCatalogname(self):
    fd = StringIO(CATALOG_LINE_1)
    oc = catalog.OpencswCatalog(fd)
    expected = {"syslog_ng": PKG_STRUCT_1}
    self.assertEqual(expected, oc.GetDataByCatalogname())


class CatalogComparatorUnitTest(unittest.TestCase):

  def testUpdateOnly(self):
    oc1 = catalog.OpencswCatalog(StringIO(CATALOG_LINE_1))
    oc2 = catalog.OpencswCatalog(StringIO(CATALOG_LINE_2))
    c = catalog.CatalogComparator()
    new_pkgs, removed_pkgs, updated_pkgs = c.GetCatalogDiff(oc1, oc2)
    self.assertFalse(new_pkgs)
    self.assertFalse(removed_pkgs)
    self.assertTrue("from" in updated_pkgs[0])

  def testAddition(self):
    oc1 = catalog.OpencswCatalog(StringIO(CATALOG_LINE_1))
    oc2 = catalog.OpencswCatalog(
        StringIO(CATALOG_LINE_1 + "\n" + CATALOG_LINE_3))
    c = catalog.CatalogComparator()
    new_pkgs, removed_pkgs, updated_pkgs = c.GetCatalogDiff(oc1, oc2)
    self.assertFalse(removed_pkgs)
    self.assertFalse(updated_pkgs)
    self.assertEqual(1, len(new_pkgs))

  def testRemoval(self):
    oc1 = catalog.OpencswCatalog(
        StringIO(CATALOG_LINE_1 + "\n" + CATALOG_LINE_3))
    oc2 = catalog.OpencswCatalog(StringIO(CATALOG_LINE_1))
    c = catalog.CatalogComparator()
    new_pkgs, removed_pkgs, updated_pkgs = c.GetCatalogDiff(oc1, oc2)
    self.assertFalse(new_pkgs)
    self.assertFalse(updated_pkgs)
    self.assertEqual(1, len(removed_pkgs))


if __name__ == '__main__':
  unittest.main()
