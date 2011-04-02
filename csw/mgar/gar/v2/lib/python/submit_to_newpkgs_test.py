#!/usr/bin/env python2.6

import unittest
import submit_to_newpkgs as stn
import tag

SAMPLE_FILES = [
  # This file intentionally missing.
  # '/home/experimental/maciej/libnspr4-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/libnspr4_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
  '/home/experimental/maciej/nspr-4.8.6,REV=2010.10.16-SunOS5.9-all-CSW.pkg.gz',
  '/home/experimental/maciej/nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-CSW.pkg.gz',
  '/home/experimental/maciej/nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-CSW.pkg.gz',
]

class FileSetCheckerUnitTest(unittest.TestCase):

  def testNsprFiles(self):
    fc = stn.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'i386-arch-missing', 'libnspr4')]
    self.assertEqual(expected, fc.CheckFiles(SAMPLE_FILES))

  def testUncommitted(self):
    fc = stn.FileSetChecker()
    expected = [
        tag.CheckpkgTag(None, 'bad-vendor-tag', 'nspr_devel expected=CSW actual=UNCOMMITTED'),
        tag.CheckpkgTag(None, 'bad-vendor-tag', 'nspr_devel expected=CSW actual=UNCOMMITTED'),
    ]
    files = ['/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-UNCOMMITTED.pkg.gz',
             '/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-UNCOMMITTED.pkg.gz']
    self.assertEqual(expected, fc.CheckFiles(files))


if __name__ == '__main__':
	unittest.main()
