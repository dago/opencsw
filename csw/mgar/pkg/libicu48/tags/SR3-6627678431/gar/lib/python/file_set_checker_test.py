#!/usr/bin/env python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import file_set_checker
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
    fc = file_set_checker.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'i386-SunOS5.9-missing', 'libnspr4')]
    files_with_metadata = fc._FilesWithMetadata(SAMPLE_FILES)
    self.assertEqual(expected, fc._CheckMissingArchs(files_with_metadata))

  def testMissingArchitectureWithOsrel(self):
    files = [
        'foo-1.0,REV=2011.03.30-SunOS5.9-i386-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.9-sparc-CSW.pkg.gz',
        'foo-1.0,REV=2011.03.30-SunOS5.10-i386-CSW.pkg.gz',
        # Intentionally missing
        # 'foo-1.0,REV=2011.03.30-SunOS5.10-sparc-CSW.pkg.gz',
    ]
    fc = file_set_checker.FileSetChecker()
    expected = [tag.CheckpkgTag(None, 'sparc-SunOS5.10-missing', 'foo')]
    files_with_metadata = fc._FilesWithMetadata(files)
    self.assertEqual(expected, fc._CheckMissingArchs(files_with_metadata))

  def testUncommitted(self):
    fc = file_set_checker.FileSetChecker()
    expected = [
        tag.CheckpkgTag(
          None, 'bad-vendor-tag',
          'filename=nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-UNCOMMITTED.pkg.gz expected=CSW actual=UNCOMMITTED'),
        tag.CheckpkgTag(
          None, 'bad-vendor-tag',
          'filename=nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-UNCOMMITTED.pkg.gz expected=CSW actual=UNCOMMITTED'),
    ]
    files = ['/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-sparc-UNCOMMITTED.pkg.gz',
             '/home/experimental/maciej/'
             'nspr_devel-4.8.6,REV=2010.10.16-SunOS5.9-i386-UNCOMMITTED.pkg.gz']
    files_with_metadata = fc._FilesWithMetadata(files)
    self.assertEqual(expected, fc._CheckUncommitted(files_with_metadata))

  def testBadInput(self):
    fc = file_set_checker.FileSetChecker()
    expected = [
        tag.CheckpkgTag(None, 'bad-vendor-tag', 'filename=csw-upload-pkg expected=CSW actual=UNKN')
    ]
    expected_2 = [
        tag.CheckpkgTag(None, 'bad-arch-or-os-release', 'csw-upload-pkg arch=pkg osrel=unspecified'),
    ]
    files = ['csw-upload-pkg']
    files_with_metadata = fc._FilesWithMetadata(files)
    self.assertEqual(expected, fc._CheckUncommitted(files_with_metadata))
    self.assertEqual(expected_2, fc._CheckMissingArchs(files_with_metadata))

  def testFilenames(self):
    fc = file_set_checker.FileSetChecker()
    expected = [
        tag.CheckpkgTag(None, 'bad-filename', 'filename=csw-upload-pkg'),
    ]
    files = ['csw-upload-pkg']
    files_with_metadata = fc._FilesWithMetadata(files)
    self.assertEqual(expected, fc._CheckFilenames(files_with_metadata))

  def testFilenamesGood(self):
    fc = file_set_checker.FileSetChecker()
    files = ['/home/experimental/maciej/'
             'nspr-4.8.6,REV=2010.10.16-SunOS5.9-all-CSW.pkg.gz']
    files_with_metadata = fc._FilesWithMetadata(files)
    self.assertEqual([], fc._CheckFilenames(files_with_metadata))


if __name__ == '__main__':
	unittest.main()
