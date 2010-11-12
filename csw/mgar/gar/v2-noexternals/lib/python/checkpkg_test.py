#!/opt/csw/bin/python2.6
# $Id$

import re
import unittest
import mox
import difflib
import checkpkg
import tag
import testdata.dump_output_1 as dump_1
import testdata.dump_output_2 as dump_2
import testdata.dump_output_3 as dump_3

"""A set of unit tests for the library checking code.

A bunch of lines to test in the interactive Python shell.

import sys
sys.path.append("lib/python")
import checkpkg

sqlite3 ~/.checkpkg/var-sadm-install-contents-cache-build8x
SELECT * FROM systempkgmap WHERE basename = 'libncursesw.so.5';
"""

class GetLinesBySonameUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()
    self.e = checkpkg.LddEmulator()

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

  def testEmulateSymlinks_5(self):
    """Install time symlink expansion."""
    runpath_list = ["/opt/csw/lib/i386"]
    expected = "/opt/csw/lib"
    result = self.e.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_6(self):
    """ExpandSymlink for /opt/csw/lib/i386."""
    runpath_list = ["/opt/csw/lib/i386"]
    expected = "/opt/csw/lib"
    not_expected = "/opt/csw/lib/i386"
    result = self.e.ExpandSymlink("/opt/csw/lib/i386",
                                    "/opt/csw/lib",
                                    "/opt/csw/lib/i386")
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result,
                     "%s is in %s" % (not_expected, result))

  def testSanitizeRunpath_1(self):
    self.assertEqual("/opt/csw/lib",
                     self.e.SanitizeRunpath("/opt/csw/lib/"))

  def testSanitizeRunpath_2(self):
    self.assertEqual("/opt/csw/lib",
                     self.e.SanitizeRunpath("/opt//csw////lib/"))



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
                     checkpkg.ParseDumpOutput(dump_1.DATA_DUMP_OUTPUT))

  def testEmpty(self):
    expected_runpath = ()
    self.assertEqual(
        expected_runpath,
        checkpkg.ParseDumpOutput(dump_2.DATA_DUMP_OUTPUT)["runpath"])

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
        checkpkg.ParseDumpOutput(dump_3.DATA_DUMP_OUTPUT))


class SystemPkgmapUnitTest(unittest.TestCase):

  def testParsePkginfoLine(self):
    line = ('application CSWcswclassutils     '
            'cswclassutils - CSW class action utilities')
    expected = ('CSWcswclassutils',
                'cswclassutils - CSW class action utilities')
    spkgmap = checkpkg.SystemPkgmap()
    self.assertEqual(expected, spkgmap._ParsePkginfoLine(line))

  def test_InferPackagesFromPkgmapLine(self):
    line = ("/opt/csw/sbin d none 0755 root bin CSWfping CSWbonobo2 "
            "CSWkrb5libdev CSWsasl CSWschilybase CSWschilyutils CSWstar "
            "CSWcommon CSWcacertificates CSWfacter")
    expected = ["CSWfping", "CSWbonobo2", "CSWkrb5libdev", "CSWsasl",
                "CSWschilybase", "CSWschilyutils", "CSWstar", "CSWcommon",
                "CSWcacertificates", "CSWfacter"]
    spkgmap = checkpkg.SystemPkgmap()
    self.assertEqual(expected, spkgmap._InferPackagesFromPkgmapLine(line))

  def test_InferPackagesFromPkgmapLine_2(self):
    line = ("/usr/lib/sparcv9/libpthread.so.1 f none 0755 root bin 41296 28258 "
            "1018129099 SUNWcslx")
    expected = ["SUNWcslx"]
    spkgmap = checkpkg.SystemPkgmap()
    self.assertEqual(expected, spkgmap._InferPackagesFromPkgmapLine(line))

  def test_InferPackagesFromPkgmapLine_3(self):
    line = ("/usr/lib/libCrun.so.1 f none 0755 root bin 63588 "
            "6287 1256043984 SUNWlibC")
    expected = ["SUNWlibC"]
    spkgmap = checkpkg.SystemPkgmap()
    self.assertEqual(expected, spkgmap._InferPackagesFromPkgmapLine(line))

  def test_InferPackagesFromPkgmapLine_4(self):
    line = ("/opt/csw/apache2/lib/libapr-1.so.0=libapr-1.so.0.3.8 s none "
            "CSWapache2rt")
    expected = ["CSWapache2rt"]
    spkgmap = checkpkg.SystemPkgmap()
    self.assertEqual(expected, spkgmap._InferPackagesFromPkgmapLine(line))


class ExtractorsUnitTest(unittest.TestCase):

  def testExtractDescriptionFromGoodData(self):
    data = {"NAME": "nspr_devel - Netscape Portable Runtime header files"}
    result = "Netscape Portable Runtime header files"
    self.assertEqual(result, checkpkg.ExtractDescription(data))

  def testExtractDescriptionWithBadCatalogname(self):
    data = {"NAME": "foo-bar - Bad catalogname shouldn't break this function"}
    result = "Bad catalogname shouldn't break this function"
    self.assertEqual(result, checkpkg.ExtractDescription(data))

  def testExtractMaintainerName(self):
    data = {"VENDOR": "https://ftp.mozilla.org/pub/mozilla.org/"
                      "nspr/releases/v4.8/src/ packaged for CSW by "
                      "Maciej Blizinski"}
    result = "Maciej Blizinski"
    self.assertEqual(result, checkpkg.ExtractMaintainerName(data))

  def testPstampRegex(self):
    pstamp = "hson@solaris9s-csw-20100313144445"
    expected = {
        'username': 'hson',
        'timestamp': '20100313144445',
        'hostname': 'solaris9s-csw'
    }
    self.assertEqual(expected, re.match(checkpkg.PSTAMP_RE, pstamp).groupdict())


class CheckpkgManager2UnitTest(unittest.TestCase):

  def test_1(self):
    m = checkpkg.CheckpkgManager2("testname", "/tmp", ["CSWfoo"])
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = u'# Tags reported by testname module\nCSWfoo: foo-tag foo-info\n'
    self.assertEqual(expected, unicode(tags_report))

  def test_2(self):
    m = checkpkg.CheckpkgManager2("testname", "/tmp", ["CSWfoo"])
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
          tag.CheckpkgTag("CSWfoo", "bar-tag", "bar-info"),
          tag.CheckpkgTag("CSWfoo", "baz-tag"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = (u'# Tags reported by testname module\n'
                u'CSWfoo: foo-tag foo-info\n'
                u'CSWfoo: bar-tag bar-info\n'
                u'CSWfoo: baz-tag\n')
    self.assertEqual(expected, unicode(tags_report))


class SliceListUnitTest(unittest.TestCase):

  def testOne(self):
    l = [1, 2, 3, 4, 5]
    s = 1
    expected = [[1], [2], [3], [4], [5]]
    self.assertTrue(expected, checkpkg.SliceList(l, s))

  def testTwo(self):
    l = [1, 2, 3, 4, 5]
    s = 2
    expected = [[1, 2], [3, 4], [5]]
    self.assertTrue(expected, checkpkg.SliceList(l, s))


class LddEmulartorUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()
    self.e = checkpkg.LddEmulator()

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


if __name__ == '__main__':
  unittest.main()
