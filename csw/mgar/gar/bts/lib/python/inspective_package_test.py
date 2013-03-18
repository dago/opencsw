#!/opt/csw/bin/python2.6

import unittest2 as unittest
import inspective_package
import package
import shell
import mox
import hachoir_parser
import magic
import os
import common_constants

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

DUMP_OUTPUT = '''
  **** DYNAMIC SECTION INFORMATION ****
.dynamic:
[INDEX] Tag         Value
[1]     NEEDED          libXext.so.0
[2]     NEEDED          libX11.so.4
[3]     NEEDED          libsocket.so.1
[4]     NEEDED          libnsl.so.1
[5]     NEEDED          libc.so.1
[6]     INIT            0x80531e4
[7]     FINI            0x8053200
[8]     HASH            0x80500e8
[9]     STRTAB          0x8050cb0
[10]    STRSZ           0x511
[11]    SYMTAB          0x80504e0
[12]    SYMENT          0x10
[13]    CHECKSUM        0x9e8
[14]    VERNEED         0x80511c4
[15]    VERNEEDNUM      0x2
[16]    PLTSZ           0x1a0
[17]    PLTREL          0x11
[18]    JMPREL          0x8051224
[19]    REL             0x8051214
[20]    RELSZ           0x1b0
[21]    RELENT          0x8
[22]    DEBUG           0
[23]    FEATURE_1       PARINIT
[24]    FLAGS           0
[25]    FLAGS_1         0
[26]    PLTGOT          0x806359c
'''

BINARY_DUMP_INFO = {
  'base_name': 'foo',
  'RUNPATH RPATH the same': True,
  'runpath': (),
  'RPATH set': False,
  'needed sonames': (
    'libXext.so.0',
    'libX11.so.4',
    'libsocket.so.1',
    'libnsl.so.1',
    'libc.so.1'),
  'path': 'opt/csw/bin/foo',
  'RUNPATH set': False,
  }

ELFDUMP_OUTPUT = '''
Version Definition Section:  .SUNW_version
     index  version                     dependency
       [1]  libssl.so.1.0.0                                  [ BASE ]
       [2]  OPENSSL_1.0.0
       [3]  OPENSSL_1.0.1               OPENSSL_1.0.0

Version Needed Section:  .SUNW_version
     index  file                        version
       [4]  libcrypto.so.1.0.0          OPENSSL_1.0.0        [ INFO ]
       [5]                              OPENSSL_1.0.1
       [6]  libnsl.so.1                 SUNW_1.9.1

Symbol Table Section:  .dynsym
     index    value      size      type bind oth ver shndx          name
       [0]  0x00000000 0x00000000  NOTY LOCL  D    0 UNDEF
       [1]  0x00000000 0x00000000  FUNC GLOB  D    4 UNDEF          EVP_DigestSignFinal
       [2]  0x0003ead4 0x000000dc  FUNC GLOB  P    2 .text          SSL_get_shared_ciphers
       [3]  0x0004f8f8 0x00000014  FUNC GLOB  P    3 .text          SSL_CTX_set_srp_client_pwd_callback
       [4]  0x00000000 0x00000000  FUNC GLOB  D    5 UNDEF          SRP_Calc_client_key
       [5]  0x000661a0 0x00000000  OBJT GLOB  P    1 .got           _GLOBAL_OFFSET_TABLE_

Syminfo Section:  .SUNW_syminfo
     index  flags            bound to                 symbol
       [1]  DBL          [1] libcrypto.so.1.0.0       EVP_DigestSignFinal
       [2]  DB               <self>                   SSL_get_shared_ciphers
       [3]  DB               <self>                   SSL_CTX_set_srp_client_pwd_callback
       [4]  DBL          [1] libcrypto.so.1.0.0       SRP_Calc_client_key
       [5]  DB               <self>                   _GLOBAL_OFFSET_TABLE_
'''

BINARY_ELFINFO = {'opt/csw/lib/libssl.so.1.0.0': {
  'symbol table': [
    {'shndx': 'UNDEF', 'soname': None, 'bind': 'LOCL',
      'symbol': None, 'version': None, 'flags': None, 'type': 'NOTY'},
    {'shndx': 'UNDEF', 'soname': 'libcrypto.so.1.0.0', 'bind': 'GLOB',
      'symbol': 'EVP_DigestSignFinal', 'version': 'OPENSSL_1.0.0',
      'flags': 'DBL', 'type': 'FUNC'},
    {'shndx': 'UNDEF', 'soname': 'libcrypto.so.1.0.0', 'bind': 'GLOB',
      'symbol': 'SRP_Calc_client_key', 'version': 'OPENSSL_1.0.1',
      'flags': 'DBL', 'type': 'FUNC'},
    {'shndx': '.text', 'soname': None, 'bind': 'GLOB',
      'symbol': 'SSL_CTX_set_srp_client_pwd_callback',
      'version': 'OPENSSL_1.0.1', 'flags': 'DB', 'type': 'FUNC'},
    {'shndx': '.text', 'soname': None, 'bind': 'GLOB',
      'symbol': 'SSL_get_shared_ciphers', 'version': 'OPENSSL_1.0.0',
      'flags': 'DB', 'type': 'FUNC'},
    {'shndx': '.got', 'soname': None, 'bind': 'GLOB',
      'symbol': '_GLOBAL_OFFSET_TABLE_', 'version': None,
      'flags': 'DB', 'type': 'OBJT'},
    ],
  'version definition': [
    {'dependency': None, 'version': 'OPENSSL_1.0.0'},
    {'dependency': 'OPENSSL_1.0.0', 'version': 'OPENSSL_1.0.1'},
    ],
  'version needed': [
    {'version': 'OPENSSL_1.0.0', 'soname': 'libcrypto.so.1.0.0'},
    {'version': 'OPENSSL_1.0.1', 'soname': 'libcrypto.so.1.0.0'},
    {'version': 'SUNW_1.9.1', 'soname': 'libnsl.so.1'},
    ]
  }
  }



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
    self.assertEqual([u'foo-file'], ip.ListBinaries())

  def testGetBinaryDumpInfoRoot(self):
    fake_binary = 'opt/csw/bin/foo'
    fake_package_path = '/fake/path/CSWfoo'

    ip = inspective_package.InspectivePackage(fake_package_path)
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    ip.ListBinaries().AndReturn([fake_binary])
    ip.GetBasedir().AndReturn('')
    ip.GetFilesDir().AndReturn('root')

    self.mox.StubOutWithMock(shell, 'ShellCommand')
    args = [common_constants.DUMP_BIN,
            '-Lv',
            os.path.join(fake_package_path, "root", fake_binary)]
    shell.ShellCommand(args, mox.IgnoreArg()).AndReturn((0, DUMP_OUTPUT, ""))
    self.mox.ReplayAll()

    self.assertEqual([BINARY_DUMP_INFO], ip.GetBinaryDumpInfo())

  def testGetBinaryDumpInfoReloc(self):
    fake_binary = 'bin/foo'
    fake_package_path = '/fake/path/CSWfoo'

    ip = inspective_package.InspectivePackage(fake_package_path)
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    ip.ListBinaries().AndReturn([fake_binary])
    ip.GetBasedir().AndReturn('opt/csw')
    ip.GetFilesDir().AndReturn('reloc')

    self.mox.StubOutWithMock(shell, 'ShellCommand')
    args = [common_constants.DUMP_BIN,
            '-Lv',
            os.path.join(fake_package_path, "reloc", fake_binary)]
    shell.ShellCommand(args, mox.IgnoreArg()).AndReturn((0, DUMP_OUTPUT, ""))
    self.mox.ReplayAll()

    self.assertEqual([BINARY_DUMP_INFO], ip.GetBinaryDumpInfo())


  def testGetBinaryElfInfoRoot(self):
    fake_binary = 'opt/csw/lib/libssl.so.1.0.0'
    fake_package_path = '/fake/path/CSWfoo'

    ip = inspective_package.InspectivePackage(fake_package_path)
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    ip.ListBinaries().AndReturn([fake_binary])
    ip.GetBasedir().AndReturn('')
    ip.GetFilesDir().AndReturn('root')

    self.mox.StubOutWithMock(shell, 'ShellCommand')
    args = [common_constants.ELFDUMP_BIN,
            '-svy',
            os.path.join(fake_package_path, "root", fake_binary)]
    shell.ShellCommand(args).AndReturn((0, ELFDUMP_OUTPUT, ""))
    self.mox.ReplayAll()

    self.assertEqual(BINARY_ELFINFO, ip.GetBinaryElfInfo())

  def testGetBinaryElfInfoReloc(self):
    fake_binary = 'lib/libssl.so.1.0.0'
    fake_package_path = '/fake/path/CSWfoo'

    ip = inspective_package.InspectivePackage(fake_package_path)
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    ip.ListBinaries().AndReturn([fake_binary])
    ip.GetBasedir().AndReturn('opt/csw')
    ip.GetFilesDir().AndReturn('reloc')

    self.mox.StubOutWithMock(shell, 'ShellCommand')
    args = [common_constants.ELFDUMP_BIN,
            '-svy',
            os.path.join(fake_package_path, "reloc", fake_binary)]
    shell.ShellCommand(args).AndReturn((0, ELFDUMP_OUTPUT, ""))
    self.mox.ReplayAll()

    self.assertEqual(BINARY_ELFINFO, ip.GetBinaryElfInfo())

  def testGetBinaryElfInfoWithIgnoredErrors(self):
    fake_binary = 'opt/csw/bin/foo'
    fake_package_path = '/fake/path/CSWfoo'
    fake_elfdump_output = '''
Version Needed Section:  .SUNW_version
     index  file                        version
       [2]  libc.so.1                 SUNW_1.1

Symbol Table Section:  .dynsym
     index    value      size      type bind oth ver shndx          name
       [1]  0x00000000 0x00000000  FUNC GLOB  D    2 UNDEF          fopen64

Syminfo Section:  .SUNW_syminfo
     index  flags            bound to                 symbol
       [1]  DBL          [1] libc.so.1                fopen64
'''
    fake_elfdump_errors = '''
/opt/csw/bin/foo: .dynsym: index[26]: bad symbol entry: : invalid shndx: 26
/opt/csw/bin/foo: .dynsym: bad symbol entry: : invalid shndx: 23
/opt/csw/bin/foo: .dynsym: index[108]: suspicious local symbol entry: _END_: lies within global symbol range (index >= 27)
/opt/csw/bin/foo: .dynsym: index[4]: bad symbol entry: toto: section[24] size: 0: symbol (address 0x36b7fc, size 0x4) lies outside of containing section
/opt/csw/bin/foo: .dynsym: bad symbol entry: Xt_app_con: section[28] size: 0: is smaller than symbol size: 4
'''
    fake_binary_elfinfo = {'opt/csw/bin/foo': {
      'symbol table': [
        {'shndx': 'UNDEF', 'soname': 'libc.so.1', 'bind': 'GLOB',
          'symbol': 'fopen64', 'version': 'SUNW_1.1',
          'flags': 'DBL', 'type': 'FUNC'},
        ],
      'version needed': [
        {'version': 'SUNW_1.1', 'soname': 'libc.so.1'},
        ],
      'version definition': [],
      }
    }
    ip = inspective_package.InspectivePackage(fake_package_path)
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    ip.ListBinaries().AndReturn([fake_binary])
    ip.GetBasedir().AndReturn('')
    ip.GetFilesDir().AndReturn('root')

    self.mox.StubOutWithMock(shell, 'ShellCommand')
    args = [common_constants.ELFDUMP_BIN,
            '-svy',
            os.path.join(fake_package_path, "root", fake_binary)]
    shell.ShellCommand(args).AndReturn((0, fake_elfdump_output, fake_elfdump_errors))
    self.mox.ReplayAll()

    self.assertEqual(fake_binary_elfinfo, ip.GetBinaryElfInfo())

  def testGetLddMinusRlinesRoot(self):
    ip = inspective_package.InspectivePackage("/tmp/CSWfake")
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    self.mox.StubOutWithMock(os, 'chmod')
    self.mox.StubOutWithMock(os, 'uname')
    ip.GetBasedir().AndReturn('')
    os.chmod('/tmp/CSWfake/root/opt/csw/bin/foo', 0755)
    ip.ListBinaries().AndReturn(['opt/csw/bin/foo'])
    ip.GetFilesDir().AndReturn('root')
    self.mox.StubOutWithMock(shell, 'ShellCommand')
    shell.ShellCommand(
        ['ldd', '-Ur', '/tmp/CSWfake/root/opt/csw/bin/foo'],
        timeout=10).AndReturn((0, "", ""))
    self.mox.StubOutWithMock(ip, '_ParseLddDashRline')
    self.mox.ReplayAll()
    self.assertEqual({'opt/csw/bin/foo': []}, ip.GetLddMinusRlines())

  def testGetLddMinusRlinesReloc(self):
    ip = inspective_package.InspectivePackage("/tmp/CSWfake")
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    self.mox.StubOutWithMock(os, 'chmod')
    self.mox.StubOutWithMock(os, 'uname')
    ip.GetBasedir().AndReturn('opt/csw')
    os.chmod('/tmp/CSWfake/reloc/bin/foo', 0755)
    ip.ListBinaries().AndReturn(['bin/foo'])
    ip.GetFilesDir().AndReturn('reloc')
    self.mox.StubOutWithMock(shell, 'ShellCommand')
    shell.ShellCommand(
        ['ldd', '-Ur', '/tmp/CSWfake/reloc/bin/foo'],
        timeout=10).AndReturn((0, "", ""))
    self.mox.StubOutWithMock(ip, '_ParseLddDashRline')
    self.mox.ReplayAll()
    self.assertEqual({'opt/csw/bin/foo': []}, ip.GetLddMinusRlines())

  def testGetLddMinusRlinesThrows(self):
    ip = inspective_package.InspectivePackage("/tmp/CSWfake")
    self.mox.StubOutWithMock(ip, 'GetBasedir')
    self.mox.StubOutWithMock(ip, 'ListBinaries')
    self.mox.StubOutWithMock(ip, 'GetFilesDir')
    self.mox.StubOutWithMock(os, 'chmod')
    self.mox.StubOutWithMock(os, 'uname')
    ip.GetBasedir().AndReturn('/')
    os.chmod('/tmp/CSWfake/root/opt/csw/bin/foo', 0755)
    os.uname().AndReturn('i86pc')
    ip.GetFilesDir().AndReturn('root')
    ip.ListBinaries().AndReturn(['opt/csw/bin/foo'])
    self.mox.StubOutWithMock(shell, 'ShellCommand')
    shell.ShellCommand(
        ['ldd', '-Ur', '/tmp/CSWfake/root/opt/csw/bin/foo'],
        timeout=10).AndReturn((1, "", "boo"))
    self.mox.StubOutWithMock(ip, '_ParseLddDashRline')
    self.mox.ReplayAll()
    self.assertRaises(package.SystemUtilityError,
                      ip.GetLddMinusRlines)


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
      'soname': None
    }
    self.assertEqual((expected, "version needed"), self.ip._ParseElfdumpLine(line, 'version needed'))

  def test_ParseElfdumpLineSymbolTable(self):
    line = '    [9]  0x000224b8 0x0000001c  FUNC GLOB  D    1 .text          vsf_log_line'
    expected = {
      'bind': 'GLOB',
      'shndx': '.text',
      'symbol': 'vsf_log_line',
      'version': '1',
      'type': 'FUNC',
    }
    self.assertEqual((expected, 'symbol table'), self.ip._ParseElfdumpLine(line, 'symbol table'))

  def test_ParseElfdumpLineNeededSymbol(self):
    line = '      [152]  DB           [4] libc.so.1                strlen'
    expected = {
        'flags': 'DB',
        'soname': 'libc.so.1',
        'symbol': 'strlen',
    }
    self.assertEqual((expected, "syminfo"), self.ip._ParseElfdumpLine(line, "syminfo"))

  def test_ParseElfdumpLineExportedSymbol(self):
    line = '      [116]  DB               <self>                   environ'
    expected = {
        'flags': 'DB',
        'soname': None,
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
