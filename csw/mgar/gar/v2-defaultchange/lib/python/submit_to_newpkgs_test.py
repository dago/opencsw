#!/opt/csw/bin/python2.6

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

if __name__ == '__main__':
	unittest.main()
