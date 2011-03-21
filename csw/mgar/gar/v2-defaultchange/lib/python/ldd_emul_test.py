#!/usr/bin/env python2.6

import unittest
import ldd_emul
import mox

import testdata.dump_output_1 as dump_1
import testdata.dump_output_2 as dump_2
import testdata.dump_output_3 as dump_3

class GetLinesBySonameUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()
    self.e = ldd_emul.LddEmulator()

  def testExpandRunpath_1(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/lib/$ISALIST"
    expected = ["/opt/csw/lib", "/opt/csw/lib/foo", "/opt/csw/lib/bar"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_2(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/mysql5/lib/$ISALIST/mysql"
    expected = ["/opt/csw/mysql5/lib/mysql",
                "/opt/csw/mysql5/lib/foo/mysql",
                "/opt/csw/mysql5/lib/bar/mysql"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_OriginSimple(self):
    isalist = ()
    runpath = "$ORIGIN"
    expected = ["/opt/csw/lib"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_OriginDots(self):
    isalist = ()
    runpath = "$ORIGIN/.."
    expected = ["/opt/csw/lib"]
    bin_path = "opt/csw/lib/subdir"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_Caching(self):
    """Make sure that the cache doesn't mess it up.

    Two invocations, where the only difference is the binary path.
    """
    isalist = ()
    runpath = "/opt/csw/lib/foo"
    expected = ["/opt/csw/lib/foo"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))
    expected = ["/opt/csw/lib/foo"]
    bin_path = "/opt/csw/lib/foo"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_OriginCaching(self):
    """Make sure that the cache doesn't mess it up.

    Two invocations, where the only difference is the binary path.
    """
    isalist = ()
    runpath = "$ORIGIN"
    expected = ["/opt/csw/lib"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected,
                      self.e.ExpandRunpath(runpath, isalist, bin_path))
    expected = ["/opt/csw/foo/lib"]
    bin_path = "/opt/csw/foo/lib"
    self.assertEquals(expected,
                      self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testExpandRunpath_OnlyIsalist(self):
    """Make sure that the cache doesn't mess it up.

    Two invocations, where the only difference is the binary path.
    """
    isalist = ("bar",)
    runpath = "/opt/csw/lib/$ISALIST"
    expected = ["/opt/csw/lib", "/opt/csw/lib/bar"]
    bin_path = "opt/csw/lib"
    self.assertEquals(expected, self.e.ExpandRunpath(runpath, isalist, bin_path))

  def testEmulate64BitSymlinks_1(self):
    runpath_list = ["/opt/csw/mysql5/lib/foo/mysql/64"]
    expected = "/opt/csw/mysql5/lib/foo/mysql/amd64"
    self.assertTrue(expected in self.e.Emulate64BitSymlinks(runpath_list))

  def testEmulate64BitSymlinks_2(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/amd64/mysql/foo"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulate64BitSymlinks_3(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/sparcv9/mysql/foo"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulate64BitSymlinks_4(self):
    """No repeated paths because of symlink expansion"""
    runpath_list = ["/opt/csw/lib"]
    expected = "/opt/csw/lib"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertEquals(1, len(result), "len(%s) != %s" % (result, 1))

  def testEmulateSymlinks_3(self):
    runpath_list = ["/opt/csw/bdb4"]
    expected = "/opt/csw/bdb42"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_4(self):
    runpath_list = ["/opt/csw/bdb42"]
    expected = "/opt/csw/bdb42"
    not_expected = "/opt/csw/bdb422"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result,
                    "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result,
                     "%s is in %s" % (not_expected, result))

  def SystemLibSymlinkExpansion_LibPresent(self, lib_symlink):
    """Install time symlink expansion."""
    runpath_list = [lib_symlink]
    expected = "/opt/csw/lib"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def SystemLibSymlinkExpansion_LibSubdirAbsent(self, lib_symlink):
    """ExpandSymlink for /opt/csw/lib/i386."""
    runpath_list = [lib_symlink]
    expected = "/opt/csw/lib"
    not_expected = lib_symlink
    result = self.e.ExpandSymlink(lib_symlink,
                                  "/opt/csw/lib",
                                  lib_symlink)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result,
                     "%s is in %s" % (not_expected, result))

  def testLibPresent_i386(self):
    self.SystemLibSymlinkExpansion_LibPresent("/opt/csw/lib/i386")

  def testLibPresent_sparcv8(self):
    self.SystemLibSymlinkExpansion_LibPresent("/opt/csw/lib/sparcv8")

  def testLibSubdirAbsent_i386(self):
    self.SystemLibSymlinkExpansion_LibSubdirAbsent("/opt/csw/lib/i386")

  def testLibSubdirAbsent_sparcv8(self):
    self.SystemLibSymlinkExpansion_LibSubdirAbsent("/opt/csw/lib/sparcv8")

  def testSanitizeRunpath_1(self):
    self.assertEqual("/opt/csw/lib",
                     self.e.SanitizeRunpath("/opt/csw/lib/"))

  def testSanitizeRunpath_2(self):
    self.assertEqual("/opt/csw/lib",
                     self.e.SanitizeRunpath("/opt//csw////lib/"))


class LddEmulartorUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()
    self.e = ldd_emul.LddEmulator()

  def testResolveSoname_1(self):
    # runpath_list, soname, isalist, path_list, binary_path
    runpath_list = ["/opt/csw/bdb47/lib", "/opt/csw/lib"]
    soname = "foo.so.1"
    path_list = ["/opt/csw/lib", "/opt/csw/bdb47/lib", "/usr/lib"]
    binary_path = "unused"
    isalist = ["amd64"]
    result = self.e.ResolveSoname(runpath_list, soname, isalist,
                                  path_list, binary_path)
    self.assertEqual("/opt/csw/bdb47/lib", result)


class ParseDumpOutputUnitTest(unittest.TestCase):

  def test_1(self):
    expected = {
        'RPATH set': True,
        'RUNPATH RPATH the same': True,
        'RUNPATH set': True,
        'needed sonames': ('librt.so.1',
                           'libresolv.so.2',
                           'libc.so.1',
                           'libgen.so.1',
                           'libsocket.so.1',
                           'libnsl.so.1',
                           'libm.so.1',
                           'libz.so.1'),
        'runpath': ('/opt/csw/lib/$ISALIST',
                    '/opt/csw/lib',
                    '/opt/csw/mysql5/lib/$ISALIST',
                    '/opt/csw/mysql5/lib',
                    '/opt/csw/mysql5/lib/$ISALIST/mysql'),
        'soname': 'libmysqlclient.so.15',
    }
    self.assertEqual(expected,
                     ldd_emul.ParseDumpOutput(dump_1.DATA_DUMP_OUTPUT))

  def testEmpty(self):
    expected_runpath = ()
    self.assertEqual(
        expected_runpath,
        ldd_emul.ParseDumpOutput(dump_2.DATA_DUMP_OUTPUT)["runpath"])

  def testRpathOnly(self):
    expected = {
        'RPATH set': True,
        'RUNPATH RPATH the same': False,
        'RUNPATH set': False,
        'needed sonames': ('librt.so.1',
                           'libresolv.so.2',
                           'libc.so.1',
                           'libgen.so.1',
                           'libsocket.so.1',
                           'libnsl.so.1',
                           'libm.so.1',
                           'libz.so.1'),
        'runpath': ('/opt/csw/lib/$ISALIST',
                    '/opt/csw/lib',
                    '/opt/csw/mysql5/lib/$ISALIST',
                    '/opt/csw/mysql5/lib',
                    '/opt/csw/mysql5/lib/$ISALIST/mysql'),
        'soname': 'libmysqlclient.so.15',
    }
    self.assertEqual(
        expected,
        ldd_emul.ParseDumpOutput(dump_3.DATA_DUMP_OUTPUT))


if __name__ == '__main__':
  unittest.main()
