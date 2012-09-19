#!/usr/bin/env python2.6

import unittest
import inspective_package
import mox
import hachoir_parser
import magic
import os

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

class InspectivePackageUnitTest(mox.MoxTestBase):

  def testListBinaries(self):
    self.mox.StubOutWithMock(hachoir_parser, 'createParser',
        use_mock_anything=True)
    hachoir_parser_mock = self.mox.CreateMockAnything()
    hachoir_parser.createParser(
        u'/fake/path/CSWfoo/root/foo-file').AndReturn(hachoir_parser_mock)
    self.mox.StubOutWithMock(os, 'access')
    os.access(u'/fake/path/CSWfoo/root/foo-file', os.R_OK).AndReturn(True)
    machine_mock = self.mox.CreateMockAnything()
    machine_mock.value = 2
    hachoir_parser_mock.__getitem__('/header/machine').AndReturn(machine_mock)
    endian_mock = self.mox.CreateMockAnything()
    endian_mock.display = 'fake-endian'
    hachoir_parser_mock.__getitem__('/header/endian').AndReturn(endian_mock)
    magic_cookie_mock = self.mox.CreateMockAnything()
    self.mox.StubOutWithMock(magic, 'open')
    magic.open(0).AndReturn(magic_cookie_mock)
    magic_cookie_mock.load()
    if "MAGIC_MIME" in dir(magic):
      flag = magic.MAGIC_MIME
    elif "MIME" in dir(magic):
      flag = magic.MIME
    magic_cookie_mock.setflags(flag)
    magic_cookie_mock.file(
        u'/fake/path/CSWfoo/root/foo-file').AndReturn(
            "application/x-executable")
    self.mox.StubOutWithMock(os.path, 'isdir')
    self.mox.StubOutWithMock(os.path, 'exists')
    self.mox.StubOutWithMock(os, 'walk')
    # self.mox.StubOutWithMock(__builtins__, 'open')
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.path.exists("/fake/path/CSWfoo/reloc").AndReturn(False)
    os.path.exists("/fake/path/CSWfoo/reloc").AndReturn(False)
    os.walk("/fake/path/CSWfoo/root").AndReturn(
        [
          ("/fake/path/CSWfoo/root", [], ["foo-file"]),
        ]
    )
    self.mox.ReplayAll()
    ip = inspective_package.InspectivePackage("/fake/path/CSWfoo")
    ip.pkginfo_dict = {
        "BASEDIR": "",
    }
    self.assertEqual([u'/fake/path/CSWfoo/root/foo-file'], ip.ListBinaries())


class PackageStatsUnitTest(unittest.TestCase):

  def setUp(self):
    self.ip = inspective_package.InspectivePackage("/fake/path/CSWfoo")

  def test_ParseElfdumpLineSectionHeader(self):
    line = 'Symbol Table Section:  .dynsym'
    self.assertEqual((None, "symbol table"), self.ip._ParseElfdumpLine(line, None))

  def test_ParseElfdumpLineVersionNeeded(self):
    line = '[13]                              SUNW_0.9             [ INFO ]'
    expected = { 
        'index': '13',
	'version': 'SUNW_0.9',
	'file': None
    }
    self.assertEqual((expected, "version needed"), self.ip._ParseElfdumpLine(line, 'version needed'))

  def test_ParseElfdumpLineSymbolTable(self):
    line = '    [9]  0x000224b8 0x0000001c  FUNC GLOB  D    1 .text          vsf_log_line'
    expected = { 
        'bind': 'GLOB',
	'shndx': '.text',
	'name': 'vsf_log_line',
	'ver': '1'
    }
    self.assertEqual((expected, 'symbol table'), self.ip._ParseElfdumpLine(line, 'symbol table'))

  def test_ParseElfdumpLineNeededSymbol(self):
    line = '      [152]  DB           [4] libc.so.1                strlen'
    expected = {
        'flags': 'DB',
        'library': 'libc.so.1',
        'symbol': 'strlen',
    }
    self.assertEqual((expected, "syminfo"), self.ip._ParseElfdumpLine(line, "syminfo"))

  def test_ParseElfdumpLineExportedSymbol(self):
    line = '      [116]  DB               <self>                   environ'
    expected = {
        'flags': 'DB',
        'library': None,
        'symbol': 'environ',
    }
    self.assertEqual((expected, "syminfo"), self.ip._ParseElfdumpLine(line, "syminfo"))

  def test_ParseNmSymLineGoodLine(self):
    line = '0000097616 T aliases_lookup'
    expected = {
        'address': '0000097616',
        'type': 'T',
        'name': 'aliases_lookup',
    }
    self.assertEqual(expected, self.ip._ParseNmSymLine(line))

  def test_ParseNmSymLineBadLine(self):
    line = 'foo'
    self.assertEqual(None, self.ip._ParseNmSymLine(line))

  def test_ParseLddDashRlineFound(self):
    line = '\tlibc.so.1 =>  /lib/libc.so.1'
    expected = {
        'state': 'OK',
        'soname': 'libc.so.1',
        'path': '/lib/libc.so.1',
        'symbol': None,
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLddDashRlineSymbolMissing(self):
    line = ('\tsymbol not found: check_encoding_conversion_args    '
            '(/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so)')
    expected = {
        'state': 'symbol-not-found',
        'soname': None,
        'path': '/opt/csw/lib/postgresql/8.4/utf8_and_gbk.so',
        'symbol': 'check_encoding_conversion_args',
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLddDashRlineFound(self):
    line = '\t/usr/lib/secure/s8_preload.so.1'
    expected = {
        'state': 'OK',
        'soname': None,
        'path': '/usr/lib/secure/s8_preload.so.1',
        'symbol': None,
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLdd_VersionNotFound(self):
    line = '\tlibXext.so.0 (SUNW_1.1) =>\t (version not found)'
    expected = {
        'symbol': None,
        'soname': 'libXext.so.0',
        'path': None,
        'state': 'version-not-found',
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

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
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLdd_SizesDiffer(self):
    line = '\trelocation R_SPARC_COPY sizes differ: _ZTI7QWidget'
    expected = {
        'symbol': '_ZTI7QWidget',
        'soname': None,
        'path': None,
        'state': 'sizes-differ',
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

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
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLdd_SizesDifferOneUsed(self):
    line = ('\t\t/opt/csw/kde-gcc/lib/libqt-mt.so.3 size used; '
            'possible insufficient data copied')
    expected = {
        'symbol': None,
        'path': '/opt/csw/kde-gcc/lib/libqt-mt.so.3',
        'state': 'sizes-diff-one-used',
        'soname': None,
    }
    self.assertEqual(expected, self.ip._ParseLddDashRline(line))

  def test_ParseLddDashRlineManyLines(self):
    for line in LDD_R_OUTPUT_1.splitlines():
      parsed = self.ip._ParseLddDashRline(line)


if __name__ == '__main__':
	unittest.main()
