#!/usr/bin/env python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import pprint
import logging
import datetime

from lib.python import common_constants
from lib.python import models
from lib.python import representations
from lib.python import shell
from lib.python import system_pkgmap
from lib.python import test_base

PKGINFO_LINE_1 = ("system      SUNWwpau                Wireless WPA Supplicant, (Usr)")
PKGINFO_LINE_2 = ("system      SUNWpcan                Cisco-Aironet 802.11b driver")

PKGLIST_LINE_1 = ("developer/versioning/sccs "
                  "                              Source Code Control System")
PKGLIST_LINE_2 = ("developer/solarisstudio-122/c++ (solarisstudio) "
                  "        C++ Compilers")

PKGMAP_LINE_1 = ("/usr/lib/sparcv9/libpthread.so.1 f none "
                 "0755 root bin 41296 28258 1018129099 SUNWcslx")
PKGMAP_LINE_2 = ("/usr/lib/libCrun.so.1 f none "
                 "0755 root bin 63588 6287 1256043984 SUNWlibC")
PKGMAP_LINE_3 = ("/opt/csw/apache2/lib/libapr-1.so.0=libapr-1.so.0.3.8 s none "
                 "CSWapache2rt")
PKGMAP_LINE_4 = ("/opt/csw/sbin d none "
                 "0755 root bin CSWfping CSWbonobo2 "
                 "CSWkrb5libdev CSWsasl CSWschilybase CSWschilyutils CSWstar "
                 "CSWcommon CSWcacertificates CSWfacter")
# This line does not follow the spec[1], but was spotted in the wild.
# http://docs.sun.com/app/docs/doc/816-5174/contents-4?l=en&a=view
# The problem is that file type is declared as '?'.
PKGMAP_LINE_5 = ("/opt/csw/gcc3/lib/gcc/sparc-sun-solaris2.8/3.4.6/include "
                 "? none CSWgcc3g77 CSWgcc3core")
PKGMAP_LINE_6 = ("/usr/lib/libc.so.1 f none 0755 root bin 867444 58567 "
                 "1250803966 SUNWcsl")
PKGMAP_LINE_7 = ("/opt/csw/include/mozilla/accessibility/nsAccessNode.h "
                 "f none 0644 root bin 5557 10685 1068611657 !CSWmozilla")
PKGMAP_LINE_8 = ("/etc/scn/scn_aa_read p none 0600 root sys SUNWscn-agentfacade-r")

PKGCONTENT_LINE_1 = ("bin\tlink\tsystem/core-os\t./usr/bin")
PKGCONTENT_LINE_2 = ("dev\tdir\tsystem/core-os\t\t0755\troot\tsys")
PKGCONTENT_LINE_3 = ("etc/svc/profile/platform_SUNW,UltraSPARC-IIe-NetraCT-40.xml\thardlink\t"
                     "system/core-os\t./platform_SUNW,UltraSPARC-IIi-Netract.xml")
PKGCONTENT_LINE_4 = ("lib/libc.so.1\tfile\tsystem/library\t\t0755\troot\tbin")

# Example data, using the format as collected from the file system.
EX1_PKGINFO = {
    'SUNWexa1': 'SUNW example package',
}

# This is the known to be expensive pattern of a list of dicts. It could
# be better transformed to named tuples (defined in the representations
# module).
EX1_CONTENTS = [
    ['does not matter here',
     'none', '0755', 'root', 'bin',
     '/boot/grub/bin/grub',
     None, 'f', None, None, None, None, None, ['SUNWexa1']],
    ['does not matter here',
     'none', '0644', 'root', 'other',
     '/etc/example/file',
     None, 'f', None, None, None, None, None, ['SUNWexa1']],
]

EX1_FILES_METADATA = [
    ('/boot/grub/bin/grub', 'application/x-executable; charset=binary',
     3),
    ('/etc/example/file', 'application/xml; charset=us-ascii', None),
]

EX1_BINARIES_DUMP_INFO = [
    ('boot/grub/bin/grub', 'grub', None, ('libcurses.so.1', 'libc.so.1'),
     ('/usr/sfw/lib',), True, True, True),
]

EX1_PKGSTATS = (
        {'bad_paths': {},
         'basic_stats': {
           'catalogname': 'sunw_exa1',
           'md5_sum': '420981de03da1a42dfc9a3925ba5aae6',
           'parsed_basename': {'arch': 'i386',
                               'catalogname': None,
                               'full_version_string': 'fakeversion,REV=0000.00.00',
                               'osrel': 'SunOS5.42',
                               'revision_info': {'REV': 'REV=0000.00.00'},
                               'vendortag': None,
                               'version': 'fakeversion',
                               'version_info': {'major version': '0',
                                                'minor version': '0',
                                                'patchlevel': '0'}},
           'pkg_basename': 'sunw_exa1-fakeversion,REV=0000.00.00-SunOS5.42-'
                           'i386-FAKE.pkg.gz',
           'pkg_path': None,
           'pkgname': 'SUNWexa1',
           'size': 0,
           'stats_version': 10L},
         'binaries': ['boot/grub/bin/grub'],
         'binary_md5_sums': [], # Maybe there should be a fake md5 here?
         'binaries_dump_info': [],
         'depends': [],
         'i_depends': [],
         'files_metadata': [
           ('boot/grub/bin/grub', 'application/x-executable; charset=binary', 3),
           ('etc/example/file', 'application/xml; charset=us-ascii', None),
         ],
         'isalist': ['amd64', 'pentium+mmx', 'pentium', 'i486', 'i386', 'pentium_pro',
                     'i86', 'pentium_pro+mmx'],
         'mtime': '2010-07-05T23:48:10',
         'overrides': [],
         'pkgchk': {
             'return_code': 0,
             'stderr_lines': [],
             'stdout_lines': ['This is a fake package']},
         'pkginfo': {'ARCH': 'i386',
                     'CATEGORY': 'fake-package',
                     'CLASSES': 'none',
                     'EMAIL': 'fake-maintainer@opencsw.org',
                     'HOTLINE': 'No hotline',
                     'NAME': 'A fake, autogenerated package',
                     'OPENCSW_CATALOGNAME': 'sunw_exa1',
                     'PKG': 'SUNWexa1',
                     'PSTAMP': 'fake@unknown-00000000000000',
                     'VENDOR': 'A fake package packaged for CSW by The Buildfarm',
                     'VERSION': 'fake_version'},
         'pkgmap': [
           representations.PkgmapEntry(
             line='does not matter here', class_='none', mode='0755',
             owner='root', group='bin', path='/boot/grub/bin/grub',
             target=None, type_='f', major=None, minor=None, size=None,
             cksum=None, modtime=None, pkgnames=['SUNWexa1']),
           representations.PkgmapEntry(
             line='does not matter here', class_='none', mode='0644',
             owner='root', group='other', path='/etc/example/file',
             target=None, type_='f', major=None, minor=None, size=None,
             cksum=None, modtime=None, pkgnames=['SUNWexa1']),
           ]
         }
)


class IndexerUnitTest(unittest.TestCase):

  def setUp(self):
    super(IndexerUnitTest, self).setUp()
    self.maxDiff = None

  def test_ParseSrv4PkginfoLine(self):
    spi = system_pkgmap.Indexer()
    expected = ('SUNWwpau', 'Wireless WPA Supplicant, (Usr)')
    self.assertEqual(expected, spi._ParseSrv4PkginfoLine(PKGINFO_LINE_1))
 
  def test_ParseIpsPkgListLine(self):
    spi = system_pkgmap.Indexer()
    expected = ('SUNWdeveloper-versioning-sccs', 'Source Code Control System')
    self.assertEqual(expected, spi._ParseIpsPkgListLine(PKGLIST_LINE_1))

  def test_ParseSrv4PkgmapLineFile(self):
    spi = system_pkgmap.Indexer()
    expected = {
        'cksum': '28258',
        'class_': 'none',
        'group': 'bin',
        'major': None,
        'minor': None,
        'mode': '0755',
        'modtime': '1018129099',
        'owner': 'root',
        'path': '/usr/lib/sparcv9/libpthread.so.1',
        'pkgnames': ['SUNWcslx'],
        'size': '41296',
        'target': None,
        'type_': 'f',
        'line': PKGMAP_LINE_1}
    self.assertEqual(expected,
                     spi._ParseSrv4PkgmapLine(PKGMAP_LINE_1)._asdict())

  def test_ParseSrv4PkgmapLineTypeSymlink(self):
    spi = system_pkgmap.Indexer()
    expected = {
        'cksum': None,
        'class_': 'none',
        'major': None,
        'minor': None,
        'group': None,
        'mode': None,
        'modtime': None,
        'owner': None,
        'path': '/opt/csw/apache2/lib/libapr-1.so.0',
        'pkgnames': ['CSWapache2rt'],
        'size': None,
        'target': 'libapr-1.so.0.3.8',
        'type_': 's',
        'line': PKGMAP_LINE_3,
    }
    self.assertEqual(expected,
                     spi._ParseSrv4PkgmapLine(PKGMAP_LINE_3)._asdict())

  def test_ParseSrv4PkgmapLineTypeQuestionMark(self):
    """A question mark is not a valid type, but we have to cope with it."""
    spi = system_pkgmap.Indexer()
    expected = {
        'modtime': None, 'major': None,
        'pkgnames': ['CSWgcc3g77', 'CSWgcc3core'],
        'cksum': None, 'owner': None,
        'path': '/opt/csw/gcc3/lib/gcc/sparc-sun-solaris2.8/3.4.6/include',
        'line': PKGMAP_LINE_5,
        'class_': 'none', 'size': None,
        'group': None, 'target': None,
        'mode': None, 'type_': 'd',
        'minor': None,
    }
    self.assertEqual(expected,
                     spi._ParseSrv4PkgmapLine(PKGMAP_LINE_5)._asdict())

  def test_ParseSrv4PkgmapLineTypePipe(self):
    """A pipe is a valid type and we have to cope with it."""
    spi = system_pkgmap.Indexer()
    expected = {
        'modtime': None,
        'major': None,
        'pkgnames': ['SUNWscn-agentfacade-r'],
        'cksum': None,
        'owner': 'root',
        'path': '/etc/scn/scn_aa_read',
        'line': PKGMAP_LINE_8,
        'class_': 'none',
        'size': None,
        'group': 'sys',
        'target': None,
        'mode': '0600',
        'type_': 'p',
        'minor': None,
    }
    self.assertEqual(expected,
                     spi._ParseSrv4PkgmapLine(PKGMAP_LINE_8)._asdict())

  def test_ParseSrv4PkgmapLibc(self):
    """A question mark is not a valid type, but we have to cope with it."""
    spi = system_pkgmap.Indexer()
    expected = {
        'modtime': '1250803966',
        'major': None,
        'pkgnames': ['SUNWcsl'],
        'cksum': '58567',
        'owner': 'root',
        'path': '/usr/lib/libc.so.1',
        'line': '/usr/lib/libc.so.1 f none 0755 root bin 867444 58567 1250803966 SUNWcsl',
        'class_': 'none',
        'size': '867444',
        'group': 'bin',
        'target': None,
        'mode': '0755',
        'type_': 'f',
        'minor': None,
    }
    self.assertEqual(expected,
                     spi._ParseSrv4PkgmapLine(PKGMAP_LINE_6)._asdict())

  def test_ParseSrv4PkgmapExclamationMark(self):
    spi = system_pkgmap.Indexer()
    self.assertEqual(
        ["!CSWmozilla"],
        spi._ParseSrv4PkgmapLine(PKGMAP_LINE_7).pkgnames)

  def test_ParseSrv4PkgmapLineTypeWrongSyntax(self):
    spi = system_pkgmap.Indexer()
    self.assertRaises(
        system_pkgmap.ParsingError,
        spi._ParseSrv4PkgmapLine, "/")

  def test_ParseIpsPkgContentsLineLink(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_1
    expected = representations.PkgmapEntry(
        line=PKGCONTENT_LINE_1, class_=None, mode=None, owner=None,
        group=None, type_='s', major=None, minor=None, size=None,
        path='/bin', target='./usr/bin', cksum=None, modtime=None,
        pkgnames=['SUNWsystem-core-os'],
    )
    self.assertEqual(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineDir(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_2
    expected = representations.PkgmapEntry(
        line=PKGCONTENT_LINE_2, class_=None, mode='0755',
        owner='root', group='sys', path='/dev',
        target=None, type_='d', major=None, minor=None, size=None,
        cksum=None, modtime=None, pkgnames=['SUNWsystem-core-os'],
    )
    self.assertEqual(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineHardlink(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_3
    expected = representations.PkgmapEntry(
        line=PKGCONTENT_LINE_3, class_=None, mode=None, owner=None,
        group=None, type_='l', major=None, minor=None, size=None,
        path='/etc/svc/profile/platform_SUNW,UltraSPARC-IIe-NetraCT-40.xml',
        target='./platform_SUNW,UltraSPARC-IIi-Netract.xml',
        cksum=None, modtime=None, pkgnames=['SUNWsystem-core-os'],
    )
    self.assertEqual(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineFile(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_4
    expected = representations.PkgmapEntry(
        line=PKGCONTENT_LINE_4, class_=None, mode='0755', owner='root',
        group='bin', type_='f', major=None, minor=None, size=None,
        path='/lib/libc.so.1', target=None, cksum=None, modtime=None,
        pkgnames=['SUNWsystem-library'],
    )
    self.assertEqual(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_IpsNameToSrv4Name(self):
    spi = system_pkgmap.Indexer()
    self.assertEqual(
        'SUNWsystem-core-os',
        spi._IpsNameToSrv4Name("system/core-os"))

  def test_ParsePkgContents(self):
    spi = system_pkgmap.Indexer()
    srv4_stream = (
          PKGMAP_LINE_1,
          PKGMAP_LINE_2,
          PKGMAP_LINE_3,
          PKGMAP_LINE_4
    )
    ips_stream = (
          PKGCONTENT_LINE_1,
          PKGCONTENT_LINE_2,
          PKGCONTENT_LINE_3,
          PKGCONTENT_LINE_4
    )
    self.assertEqual(4, len(spi._ParsePkgContents(srv4_stream, spi._ParseSrv4PkgmapLine, False)))
    self.assertEqual(4, len(spi._ParsePkgContents(ips_stream, spi._ParseIpsPkgContentsLine, False)))

  def Disabledtest_GetDataStructure(self):
    spi = system_pkgmap.Indexer()
    expected = {'arch': 'sparc', 'osrel': 'SunOS5.11',
                'contents': [
                 {'cksum': '28258', 'class': 'none', 'group': 'bin', 
                  'line': '/usr/lib/sparcv9/libpthread.so.1 f none 0755 root bin 41296 28258 1018129099 SUNWcslx',
                   'major': None, 'minor': None, 'mode': '0755', 'modtime': '1018129099', 'owner': 'root',
                   'path': '/usr/lib/sparcv9/libpthread.so.1', 'pkgnames': ['SUNWcslx'], 'size': '41296', 
                   'target': None, 'type': 'f'},
                 {'cksum': '6287', 'class': 'none', 'group': 'bin',
                  'line': '/usr/lib/libCrun.so.1 f none 0755 root bin 63588 6287 1256043984 SUNWlibC',
                  'major': None, 'minor': None, 'mode': '0755', 'modtime': '1256043984', 'owner': 'root',
                  'path': '/usr/lib/libCrun.so.1', 'pkgnames': ['SUNWlibC'], 'size': '63588',
                  'target': None, 'type': 'f'},
                 {'group': None, 'line': 'bin\tlink\tsystem/core-os\t./usr/bin', 'mode': None, 'owner': None,
                  'path': '/bin', 'pkgnames': ['SUNWsystem-core-os'], 'target': './usr/bin', 'type': 's'},
                 {'group': 'sys', 'line': 'dev\tdir\tsystem/core-os\t\t0755\troot\tsys', 'mode': '0755', 'owner': 'root',
                  'path': '/dev', 'pkgnames': ['SUNWsystem-core-os'], 'target': None, 'type': 'd'}],
                'pkginfo': {'SUNWdeveloper-solarisstudio-122-c': u'C++ Compilers',
                            'SUNWdeveloper-versioning-sccs': u'Source Code Control System',
                            'SUNWpcan': u'Cisco-Aironet 802.11b driver',
                            'SUNWwpau': u'Wireless WPA Supplicant, (Usr)'}
               }
    srv4_pkginfos_stream = (
          PKGINFO_LINE_1,
          PKGINFO_LINE_2,
    )
    ips_pkginfos_stream = (
          PKGLIST_LINE_1,
          PKGLIST_LINE_2,
    )
    srv4_pkgcontents_stream = (
          PKGMAP_LINE_1,
          PKGMAP_LINE_2,
    )
    ips_pkgcontents_stream = (
          PKGCONTENT_LINE_1,
          PKGCONTENT_LINE_2,
    )
    self.assertEqual(expected, spi.GetDataStructure(srv4_pkgcontents_stream, srv4_pkginfos_stream,
                                                    ips_pkgcontents_stream, ips_pkginfos_stream,
                                                    'SunOS5.11', 'sparc', False))



class InstallContentsImporterUnitTest(test_base.SqlObjectTestMixin,
                                      unittest.TestCase):

  def setUp(self):
    super(InstallContentsImporterUnitTest, self).setUp()
    self.importer = system_pkgmap.InstallContentsImporter("SunOS5.42", "mips")

  def Disabledtest_GetFakeSrv4(self):
    self.dbc.InitialDataImport()
    importer = self.importer
    data = {
        "pkginfo": { "SUNWfoo": "sunwfoo - a fake Sun package", },
    }
    importer._ImportPackages(data)
    fake_srv4 = importer._GetFakeSrv4("SUNWfoo", "SunOS5.9", "i386")
    self.assertEqual(u"68d6e9124bff1c0ce56994fae50cc9b1", fake_srv4.md5_sum)

  def Disabledtest_ImportFiles(self):
    self.dbc.InitialDataImport()
    contents = [
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'SUNWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
        'pkgnames': ['SUNWfontconfig-root'],
        'size': '263', 'target': None, 'type_': 'f'},
     ]
    data = {
        'pkginfo': {
          "SUNWfontconfig-root": "sunw_fontconfig_root fake package",
        },
        'contents': contents,
        'osrel': 'SunOS5.9',
        'arch': 'i386',
    }
    importer = self.importer
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEqual(1, len(list(models.Srv4FileStats.select())))
    self.assertEqual(1, len(list(models.CswFile.select())))

  def Disabledtest_ImportFilesAddToCatalog(self):
    self.dbc.InitialDataImport()
    contents = [
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'SUNWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
        'pkgnames': ['SUNWfontconfig-root'],
        'size': '263', 'target': None, 'type': 'f'},
     ]
    data = {
        'pkginfo': {
          "SUNWfontconfig-root": "sunw_fontconfig_root fake package",
        },
        'contents': contents,
        'osrel': 'SunOS5.9',
        'arch': 'i386',
    }
    importer = self.importer
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEqual(1, len(list(models.Srv4FileStats.select())))
    self.assertEqual(1, len(list(models.CswFile.select())))
    # There are 5 catalog releases by default.  This should match
    # common_constants.DEFAULT_CATALOG_RELEASES
    self.assertEqual(len(common_constants.DEFAULT_CATALOG_RELEASES),
                      len(list(models.Srv4FileInCatalog.select())))

  def Disabledtest_CompilePkgstatsList(self):
    self.dbc.InitialDataImport()
    contents = [
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'SUNWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
        'pkgnames': ['SUNWfontconfig-root'],
        'size': '263', 'target': None, 'type': 'f'},
       {'modtime': '1316730516',
        'major': None,
        'group': 'bin',
        'target': None,
        'pkgnames': ['FAKEtree'],
        'mode': '0755',
        'cksum': '20315',
        'owner': 'root',
        'path': '/opt/csw/bin/tree',
        'line': '/opt/csw/bin/tree f none 0755 root bin 65976 20315 1316730516 FAKEtree\n',
        'type': 'f',
        'class': 'none',
        'minor': None,
        'size': '65976'}
     ]
    indexed_metadata = [
        {
          'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
          'mime_type': 'text/plain; charset=us-ascii',
        },
        {
          'path': '/opt/csw/bin/tree',
          'mime_type_by_hachoir': u'application/x-executable',
          'machine_id': 3,
          'mime_type': 'application/x-executable; charset=binary',
          'endian': 'Little endian'}
    ]
    indexed_binaries_dump_info = [
        {'RPATH set': True,
         'RUNPATH RPATH the same': True,
         'RUNPATH set': True,
         'base_name': 'tree',
         'needed sonames': ('libc.so.1',),
         'path': 'opt/csw/bin/tree',
         'runpath': (
           '/opt/csw/lib/$ISALIST',
           '/opt/csw/lib')}
    ]
    data = {
        'pkginfo': {
          "SUNWfontconfig-root": "sunw_fontconfig_root fake package",
          "CSWtree": "CSWtree fake package",
        },
        'contents': contents,
        'osrel': 'SunOS5.9',
        'arch': 'i386',
        'files_metadata': indexed_metadata,
    }
    importer = self.importer
    parsed_basename = {
        'version': 'fakeversion',
        'full_version_string': 'fakeversion,REV=0000.00.00',
        'version_info': {
          'minor version': '0',
          'patchlevel': '0',
          'major version': '0'},
        'revision_info': {'REV': 'REV=0000.00.00'},
        'vendortag': None,
        'arch': 'i386',
        'osrel': 'SunOS5.9',
        'catalogname': None}
    basic_stats = {
        'catalogname': 'sunw_fontconfig_root',
        'md5_sum': "0693fbafb0cad9b19ccf9404fab7839b",
        'parsed_basename': parsed_basename,
        'pkg_basename': 'sunw_fontconfig_root-fakeversion,REV=0000.00.00-SunOS5.9-i386-FAKE.pkg.gz',
        'pkg_path': None,
        'pkgname': 'SUNWfontconfig-root',
        'size': 0,
        'stats_version': 10L}
    files_metadata = [
        {
          # No leading slash
          'path': 'etc/fonts/conf.avail/70-no-bitmaps.conf',
          'mime_type': 'text/plain; charset=us-ascii',
        }
    ]
    isalist = frozenset(
           ['amd64', 'pentium+mmx', 'pentium', 'i486', 'i386',
            'pentium_pro', 'i86', 'pentium_pro+mmx'])
    pkgchk = {
           'return_code': 0,
           'stderr_lines': [],
           'stdout_lines': ["This is a fake package"]}
    pkginfo = {
        'ARCH': 'i386',
        'CATEGORY': 'fake-package',
        'CLASSES': 'none',
        'EMAIL': 'fake-maintainer@opencsw.org',
        'HOTLINE': 'No hotline',
        'NAME': 'A fake, autogenerated package',
        'OPENCSW_CATALOGNAME': 'sunw_fontconfig_root',
        'PKG': 'SUNWfontconfig-root',
        'PSTAMP': 'fake@unknown-00000000000000',
        'VENDOR': 'A fake package packaged for CSW by The Buildfarm',
        'VERSION': 'fake_version'}
    pkgmap = [
        {'group': 'bin',
         'target': None,
         'mode': '0444',
         'owner': 'root',
         'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
         'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                  'f none 0444 root bin 263 21717 1210872725 '
                  'SUNWfontconfig-root\n'),
         'type': 'f',
         'class': 'none',
         },
    ]
    # This is a harder one.  This information must be collected when
    # scanning /var/sadm/install/contents.
    binaries_dump_info = [
        {'RPATH set': True,
          'RUNPATH RPATH the same': True,
          'RUNPATH set': True,
          'base_name': 'tree',
          'needed sonames': ('libc.so.1',),
          'path': 'opt/csw/bin/tree',
          'runpath': (
            '/opt/csw/lib/$ISALIST',
            '/opt/csw/lib')}]
    expected = [
        {'bad_paths': {},
         'basic_stats': basic_stats,
         'binaries': ['opt/csw/bin/tree'],
         'binaries_dump_info': binaries_dump_info,
         'depends': frozenset(),
         'files_metadata': files_metadata,
         'isalist': isalist,
         'mtime': datetime.datetime(2010, 7, 5, 23, 48, 10),
         'overrides': [],
         'pkgchk': pkgchk,
         'pkginfo': pkginfo,
         'pkgmap': pkgmap}]
    result = importer._ComposePkgstats(data, show_progress=False)
    expected, result = expected[0], result[1]
    self.assertEqual(expected.keys(), result.keys())
    # Custom dict comparison
    self.assertEqual(
        expected["basic_stats"]["parsed_basename"],
        result["basic_stats"]["parsed_basename"])
    self.assertEqual(
        expected["basic_stats"],
        result["basic_stats"])
    self.assertEqual(expected["pkgmap"], result["pkgmap"])
    self.assertEqual(expected, result)

  def Disabledtest_ImportFilesAddToCatalogTwoFiles(self):
    self.dbc.InitialDataImport()
    contents = [
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'SUNWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
        'pkgnames': ['SUNWfontconfig-root'],
        'size': '263', 'target': None, 'type': 'f'},
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf.bak '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'SUNWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf.bak',
        'pkgnames': ['SUNWfontconfig-root'],
        'size': '263', 'target': None, 'type': 'f'},
     ]
    data = {
        'pkginfo': {
          "SUNWfontconfig-root": "sunw_fontconfig_root fake package",
        },
        'contents': contents,
        'osrel': 'SunOS5.9',
        'arch': 'i386',
    }
    importer = self.importer
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEqual(1, len(list(models.Srv4FileStats.select())))
    self.assertEqual(2, len(list(models.CswFile.select())))

  def Disabledtest_ImportFilesCsw(self):
    contents = [
       {'cksum': '21717', 'class': 'none', 'group': 'bin',
        'line': ('/etc/fonts/conf.avail/70-no-bitmaps.conf '
                 'f none 0444 root bin 263 21717 1210872725 '
                 'CSWfontconfig-root\n'),
        'major': None, 'minor': None,
        'mode': '0444',
        'modtime': '1210872725', 'owner': 'root',
        'path': '/etc/fonts/conf.avail/70-no-bitmaps.conf',
        'pkgnames': ['CSWfontconfig-root'],
        'size': '263', 'target': None, 'type': 'f'},
     ]
    data = {
        'pkginfo': {
          "CSWfontconfig-root": "fontconfig_root system fake package",
        },
        'contents': contents,
        'osrel': 'SunOS5.9',
        'arch': 'i386',
    }
    importer = self.importer
    importer._ImportPackages(data)
    importer._ImportFiles(data, show_progress=False)
    self.assertEqual(0, len(list(models.Srv4FileStats.select())))
    self.assertEqual(0, len(list(models.CswFile.select())))

  def testSanitizeInstallContentsPkgnameNone(self):
    importer = self.importer
    self.assertEqual(
        "BOstdenv",
        importer.SanitizeInstallContentsPkgname("BOstdenv:none"))

  def testSanitizeInstallContentsPkgnameTilde(self):
    importer = self.importer
    self.assertEqual(
        "BOstdenv",
        importer.SanitizeInstallContentsPkgname("~BOstdenv"))

  def testSanitizeInstallContentsPkgnameJ3link(self):
    importer = self.importer
    self.assertEqual(
        "SUNWjhrt",
        importer.SanitizeInstallContentsPkgname("SUNWjhrt:j3link"))

  def testSanitizeInstallContentsPkgnameJ3linkAi(self):
    importer = self.importer
    self.assertEqual(
        "SUNWjai",
        importer.SanitizeInstallContentsPkgname("SUNWjai:j3link"))

  def testSanitizeInstallContentsPkgnameJ5linkAi(self):
    importer = self.importer
    self.assertEqual(
        "SUNWjai",
        importer.SanitizeInstallContentsPkgname("SUNWjai:j5link"))

  def testSanitizeInstallContentsPkgnameInstallError(self):
    importer = self.importer
    self.assertEqual(
        "CSWmozilla",
        importer.SanitizeInstallContentsPkgname("!CSWmozilla"))


class PkgstatsListComposerUnitTest(unittest.TestCase):

  DATA = {
      'pkginfo': EX1_PKGINFO,
      'contents': EX1_CONTENTS,
      'files_metadata': EX1_FILES_METADATA,
      'binaries_dump_info': EX1_BINARIES_DUMP_INFO,
      'osrel': 'SunOS5.42',
      'arch': 'i386',
  }

  def setUp(self):
    super(PkgstatsListComposerUnitTest, self).setUp()
    self.importer = system_pkgmap.InstallContentsImporter("SunOS5.42", "mips")

  def AssertDictEqual(self, d1, d2):
    self.assertEqual(d1.keys(), d2.keys())
    for key in d1:
      if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        self.AssertDictEqual(d1[key], d2[key])
      else:
        self.assertEqual(d1[key], d2[key])

  def testComposeFakePackages(self):
    generated_pkgstats = self.importer._ComposePkgstats(self.DATA, show_progress=False)
    self.assertEqual(1, len(generated_pkgstats))
    self.AssertDictEqual(EX1_PKGSTATS, generated_pkgstats[0])


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  unittest.main()
