#!/usr/bin/env python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
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

  def testMissingArchitecture(self):
    fc = stn.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'i386-SunOS5.9-missing', 'libnspr4')]
    self.assertEqual(expected, fc.CheckFiles(SAMPLE_FILES))

  def testMissingArchitectureWithOsrel(self):
    files = [
        'foo-1.0,REV=2011.03.30-SunOS5.9-i386-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.9-sparc-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.10-i386-CSW.pkg.gz',
        # Intentionally missing
        # 'foo-1.0,REV=2011.03.30-SunOS5.10-sparc-CSW.pkg.gz',
    ]
    fc = stn.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'sparc-SunOS5.10-missing', 'foo')]
    self.assertEqual(expected, fc.CheckFiles(files))

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
