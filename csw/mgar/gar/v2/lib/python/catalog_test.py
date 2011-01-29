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

class OpencswCatalogUnitTest(unittest.TestCase):

  def test_ParseCatalogLine_1(self):
    line = (
        'tmux 1.2,REV=2010.05.17 CSWtmux '
        'tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz '
        '145351cf6186fdcadcd169b66387f72f 214091 '
        'CSWcommon|CSWlibevent none none\n')
    oc = catalog.OpencswCatalog(None)
    parsed = oc._ParseCatalogLine(line)
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
    expected = {'syslog_ng': {
      'category': 'none',
      'i_deps': (),
      'pkgname': 'CSWsyslogng',
      'md5sum': 'cfe40c06e994f6e8d3b191396d0365cb',
      'version': '3.0.4,REV=2009.08.30',
      'deps': ('CSWgcc4corert', 'CSWeventlog', 'CSWosslrt', 'CSWzlib',
        'CSWpcrert', 'CSWggettextrt', 'CSWglib2', 'CSWtcpwrap',
        'CSWcswclassutils', 'CSWcommon'),
      'file_basename': 'syslog_ng-3.0.4,REV=2009.08.30-SunOS5.8-i386-CSW.pkg.gz',
      'size': '137550',
      'catalogname': 'syslog_ng'}}
    fd = StringIO(CATALOG_LINE_1)
    oc = catalog.OpencswCatalog(fd)
    self.assertEqual(expected, oc.GetDataByCatalogname())


if __name__ == '__main__':
  unittest.main()
