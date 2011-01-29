#!/usr/bin/env python2.6

import unittest
import catalog

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


if __name__ == '__main__':
  unittest.main()
