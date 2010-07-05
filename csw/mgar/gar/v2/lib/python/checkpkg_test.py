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

LDD_R_OUTPUT_1 =  """\tlibc.so.1 =>  /lib/libc.so.1
\tsymbol not found: check_encoding_conversion_args    (/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so)
\tsymbol not found: LocalToUtf    (/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so)
\tsymbol not found: UtfToLocal    (/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so)
\tlibm.so.2 =>   /lib/libm.so.2
\t/usr/lib/secure/s8_preload.so.1
\tlibXext.so.0 (SUNW_1.1) =>\t (version not found)
\trelocation R_SPARC_COPY symbol: ASN1_OCTET_STRING_it: file /opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.8: relocation bound to a symbol with STV_PROTECTED visibility
\trelocation R_SPARC_COPY sizes differ: _ZTI7QWidget
\t\t(file /tmp/pkg_GqCk0P/CSWkdeartworkgcc/root/opt/csw/kde-gcc/bin/kslideshow.kss size=0x28; file /opt/csw/kde-gcc/lib/libqt-mt.so.3 size=0x20)
"""

class GetLinesBySonameUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()

  def testExpandRunpath_1(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/lib/$ISALIST"
    expected = ["/opt/csw/lib/foo", "/opt/csw/lib/bar"]
    self.assertEquals(expected, checkpkg.ExpandRunpath(runpath, isalist))

  def testExpandRunpath_2(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/mysql5/lib/$ISALIST/mysql"
    expected = ["/opt/csw/mysql5/lib/foo/mysql",
                "/opt/csw/mysql5/lib/bar/mysql"]
    self.assertEquals(expected, checkpkg.ExpandRunpath(runpath, isalist))

  def testEmulate64BitSymlinks_1(self):
    runpath_list = ["/opt/csw/mysql5/lib/foo/mysql/64"]
    expected = "/opt/csw/mysql5/lib/foo/mysql/amd64"
    self.assertTrue(expected in checkpkg.Emulate64BitSymlinks(runpath_list))

  def testEmulate64BitSymlinks_2(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/amd64/mysql/foo"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulate64BitSymlinks_3(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/sparcv9/mysql/foo"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulate64BitSymlinks_4(self):
    """No repeated paths because of symlink expansion"""
    runpath_list = ["/opt/csw/lib"]
    expected = "/opt/csw/lib"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertEquals(1, len(result), "len(%s) != %s" % (result, 1))

  def testEmulateSymlinks_3(self):
    runpath_list = ["/opt/csw/bdb4"]
    expected = "/opt/csw/bdb42"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_4(self):
    runpath_list = ["/opt/csw/bdb42"]
    expected = "/opt/csw/bdb42"
    not_expected = "/opt/csw/bdb422"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result,
                    "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result,
                     "%s is in %s" % (not_expected, result))

  def testEmulateSymlinks_5(self):
    """Install time symlink expansion."""
    runpath_list = ["/opt/csw/lib/i386"]
    expected = "/opt/csw/lib"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_6(self):
    """ExpandSymlink for /opt/csw/lib/i386."""
    runpath_list = ["/opt/csw/lib/i386"]
    expected = "/opt/csw/lib"
    not_expected = "/opt/csw/lib/i386"
    result = checkpkg.ExpandSymlink("/opt/csw/lib/i386",
                                    "/opt/csw/lib",
                                    "/opt/csw/lib/i386")
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result,
                     "%s is in %s" % (not_expected, result))

  def testSanitizeRunpath_1(self):
    self.assertEqual("/opt/csw/lib",
                     checkpkg.SanitizeRunpath("/opt/csw/lib/"))

  def testSanitizeRunpath_2(self):
    self.assertEqual("/opt/csw/lib",
                     checkpkg.SanitizeRunpath("/opt//csw////lib/"))



class ParseDumpOutputUnitTest(unittest.TestCase):

  def test_1(self):
    expected = {
        'RPATH set': True,
        'RUNPATH RPATH the same': True,
        'RUNPATH set': True,
        'needed sonames': ['librt.so.1',
                           'libresolv.so.2',
                           'libc.so.1',
                           'libgen.so.1',
                           'libsocket.so.1',
                           'libnsl.so.1',
                           'libm.so.1',
                           'libz.so.1'],
        'runpath': ['/opt/csw/lib/$ISALIST',
                    '/opt/csw/lib',
                    '/opt/csw/mysql5/lib/$ISALIST',
                    '/opt/csw/mysql5/lib',
                    '/opt/csw/mysql5/lib/$ISALIST/mysql'],
        'soname': 'libmysqlclient.so.15',
    }
    self.assertEqual(expected,
                     checkpkg.ParseDumpOutput(dump_1.DATA_DUMP_OUTPUT))

  def testEmpty(self):
    expected_runpath = []
    self.assertEqual(
        expected_runpath,
        checkpkg.ParseDumpOutput(dump_2.DATA_DUMP_OUTPUT)["runpath"])

  def testRpathOnly(self):
    expected = {
        'RPATH set': True,
        'RUNPATH RPATH the same': False,
        'RUNPATH set': False,
        'needed sonames': ['librt.so.1',
                           'libresolv.so.2',
                           'libc.so.1',
                           'libgen.so.1',
                           'libsocket.so.1',
                           'libnsl.so.1',
                           'libm.so.1',
                           'libz.so.1'],
        'runpath': ['/opt/csw/lib/$ISALIST',
                    '/opt/csw/lib',
                    '/opt/csw/mysql5/lib/$ISALIST',
                    '/opt/csw/mysql5/lib',
                    '/opt/csw/mysql5/lib/$ISALIST/mysql'],
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


class PackageStatsUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkgstats = checkpkg.PackageStats(None)

  def test_ParseNmSymLineGoodLine(self):
    line = '0000097616 T aliases_lookup'
    expected = {
        'address': '0000097616',
        'type': 'T',
        'name': 'aliases_lookup',
    }
    self.assertEqual(expected, self.pkgstats._ParseNmSymLine(line))

  def test_ParseNmSymLineBadLine(self):
    line = 'foo'
    self.assertEqual(None, self.pkgstats._ParseNmSymLine(line))

  def test_ParseLddDashRlineFound(self):
    line = '\tlibc.so.1 =>  /lib/libc.so.1'
    expected = {
        'state': 'OK',
        'soname': 'libc.so.1',
        'path': '/lib/libc.so.1',
        'symbol': None,
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLddDashRlineSymbolMissing(self):
    line = ('\tsymbol not found: check_encoding_conversion_args    '
            '(/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so)')
    expected = {
        'state': 'symbol-not-found',
        'soname': None,
        'path': '/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so',
        'symbol': 'check_encoding_conversion_args',
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLddDashRlineFound(self):
    line = '\t/usr/lib/secure/s8_preload.so.1'
    expected = {
        'state': 'OK',
        'soname': None,
        'path': '/usr/lib/secure/s8_preload.so.1',
        'symbol': None,
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLdd_VersionNotFound(self):
    line = '\tlibXext.so.0 (SUNW_1.1) =>\t (version not found)'
    expected = {
        'symbol': None,
        'soname': 'libXext.so.0',
        'path': None,
        'state': 'version-not-found',
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLdd_StvProtectedVisibility(self):
    line = ('\trelocation R_SPARC_COPY symbol: ASN1_OCTET_STRING_it: '
            'file /opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.8: '
            'relocation bound to a symbol with STV_PROTECTED visibility')
    expected = {
        'symbol': 'ASN1_OCTET_STRING_it',
        'soname': None,
        'path': '/opt/csw/lib/sparcv8plus+vis/libcrypto.so.0.9.8',
        'state': 'relocation-bound-to-a-symbol-with-STV_PROTECTED-visibility',
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLdd_SizesDiffer(self):
    line = '\trelocation R_SPARC_COPY sizes differ: _ZTI7QWidget'
    expected = {
        'symbol': '_ZTI7QWidget',
        'soname': None,
        'path': None,
        'state': 'sizes-differ',
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLdd_SizesDifferInfo(self):
    line = ('\t\t(file /tmp/pkg_GqCk0P/CSWkdeartworkgcc/root/opt/csw/kde-gcc/bin/'
            'kslideshow.kss size=0x28; '
            'file /opt/csw/kde-gcc/lib/libqt-mt.so.3 size=0x20)')
    expected = {
        'symbol': None,
        'path': ('/tmp/pkg_GqCk0P/CSWkdeartworkgcc/root/opt/csw/kde-gcc/'
                 'bin/kslideshow.kss /opt/csw/kde-gcc/lib/libqt-mt.so.3'),
        'state': 'sizes-diff-info',
        'soname': None,
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLdd_SizesDifferOneUsed(self):
    line = ('\t\t/opt/csw/kde-gcc/lib/libqt-mt.so.3 size used; '
            'possible insufficient data copied')
    expected = {
        'symbol': None,
        'path': '/opt/csw/kde-gcc/lib/libqt-mt.so.3',
        'state': 'sizes-diff-one-used',
        'soname': None,
    }
    self.assertEqual(expected, self.pkgstats._ParseLddDashRline(line))

  def test_ParseLddDashRlineManyLines(self):
    for line in LDD_R_OUTPUT_1.splitlines():
      parsed = self.pkgstats._ParseLddDashRline(line)


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
    self.assertEqual(expected, tags_report)

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
    self.assertEqual(expected, tags_report)



if __name__ == '__main__':
  unittest.main()
