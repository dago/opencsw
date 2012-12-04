#!/usr/bin/env python2.6

import unittest2 as unittest
import system_pkgmap
import test_base
import models
import logging
import common_constants

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
        'class': 'none',
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
        'type': 'f',
        'line': PKGMAP_LINE_1}
    self.assertEqual(expected, spi._ParseSrv4PkgmapLine(PKGMAP_LINE_1))

  def test_ParseSrv4PkgmapLineTypeSymlink(self):
    spi = system_pkgmap.Indexer()
    expected = {
        'cksum': None,
        'class': 'none',
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
        'type': 's',
        'line': PKGMAP_LINE_3,
    }
    self.assertEqual(expected, spi._ParseSrv4PkgmapLine(PKGMAP_LINE_3))

  def test_ParseSrv4PkgmapLineTypeQuestionMark(self):
    """A question mark is not a valid type, but we have to cope with it."""
    spi = system_pkgmap.Indexer()
    expected = {
        'modtime': None, 'major': None,
        'pkgnames': ['CSWgcc3g77', 'CSWgcc3core'],
        'cksum': None, 'owner': None,
        'path': '/opt/csw/gcc3/lib/gcc/sparc-sun-solaris2.8/3.4.6/include',
        'line': PKGMAP_LINE_5,
        'class': 'none', 'size': None,
        'group': None, 'target': None,
        'mode': None, 'type': 'd',
        'minor': None,
    }
    self.assertEqual(expected, spi._ParseSrv4PkgmapLine(PKGMAP_LINE_5))

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
        'class': 'none',
        'size': None,
        'group': 'sys',
        'target': None,
        'mode': '0600',
        'type': 'p',
        'minor': None,
    }
    self.assertEqual(expected, spi._ParseSrv4PkgmapLine(PKGMAP_LINE_8))

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
        'class': 'none',
        'size': '867444',
        'group': 'bin',
        'target': None,
        'mode': '0755',
        'type': 'f',
        'minor': None,
    }
    self.assertEqual(expected, spi._ParseSrv4PkgmapLine(PKGMAP_LINE_6))

  def test_ParseSrv4PkgmapExclamationMark(self):
    spi = system_pkgmap.Indexer()
    self.assertEqual(
        ["!CSWmozilla"],
        spi._ParseSrv4PkgmapLine(PKGMAP_LINE_7)["pkgnames"])

  def test_ParseSrv4PkgmapLineTypeWrongSyntax(self):
    spi = system_pkgmap.Indexer()
    self.assertRaises(
        system_pkgmap.ParsingError,
        spi._ParseSrv4PkgmapLine, "/")

  def test_ParseIpsPkgContentsLineLink(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_1
    expected = {
        'pkgnames': ['SUNWsystem-core-os'],
        'group': None,
        'target': './usr/bin',
        'owner': None,
        'path': '/bin',
        'line': PKGCONTENT_LINE_1,
        'type': 's',
        'mode': None,
    }
    self.assertEquals(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineDir(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_2
    expected = {
        'pkgnames': ['SUNWsystem-core-os'],
        'group': 'sys',
        'target': None,
        'owner': 'root',
        'path': '/dev',
        'line': PKGCONTENT_LINE_2,
        'type': 'd',
        'mode': '0755',
    }
    self.assertEquals(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineHardlink(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_3
    expected = {
        'pkgnames': ['SUNWsystem-core-os'],
        'group': None,
        'target': './platform_SUNW,UltraSPARC-IIi-Netract.xml',
        'owner': None,
        'path': '/etc/svc/profile/platform_SUNW,UltraSPARC-IIe-NetraCT-40.xml',
        'line': PKGCONTENT_LINE_3,
        'type': 'l',
        'mode': None,
    }
    self.assertEquals(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_ParseIpsPkgContentsLineFile(self):
    spi = system_pkgmap.Indexer()
    line = PKGCONTENT_LINE_4
    expected = {
        'pkgnames': ['SUNWsystem-library'],
        'group': 'bin',
        'target': None,
        'owner': 'root',
        'path': '/lib/libc.so.1',
        'line': PKGCONTENT_LINE_4,
        'type': 'f',
        'mode': '0755',
    }
    self.assertEquals(
        expected,
        spi._ParseIpsPkgContentsLine(line))

  def test_IpsNameToSrv4Name(self):
    spi = system_pkgmap.Indexer()
    self.assertEquals(
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

  def test_GetDataStructure(self):
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

  def test_GetFakeSrv4(self):
    self.dbc.InitialDataImport()
    importer = system_pkgmap.InstallContentsImporter()
    data = {
        "pkginfo": { "SUNWfoo": "sunwfoo - a fake Sun package", },
    }
    importer._ImportPackages(data)
    fake_srv4 = importer._GetFakeSrv4("SUNWfoo", "SunOS5.9", "i386")
    self.assertEqual(u"68d6e9124bff1c0ce56994fae50cc9b1", fake_srv4.md5_sum)

  def test_ImportFiles(self):
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
    importer = system_pkgmap.InstallContentsImporter()
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEquals(1, len(list(models.Srv4FileStats.select())))
    self.assertEquals(1, len(list(models.CswFile.select())))

  def test_ImportFilesAddToCatalog(self):
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
    importer = system_pkgmap.InstallContentsImporter()
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEquals(1, len(list(models.Srv4FileStats.select())))
    self.assertEquals(1, len(list(models.CswFile.select())))
    # There are 5 catalog releases by default.  This should match
    # common_constants.DEFAULT_CATALOG_RELEASES
    self.assertEquals(len(common_constants.DEFAULT_CATALOG_RELEASES),
                      len(list(models.Srv4FileInCatalog.select())))

  def test_ImportFilesAddToCatalogTwoFiles(self):
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
    importer = system_pkgmap.InstallContentsImporter()
    importer._ImportPackages(data)
    importer._ImportFiles(data)
    self.assertEquals(1, len(list(models.Srv4FileStats.select())))
    self.assertEquals(2, len(list(models.CswFile.select())))

  def test_ImportFilesCsw(self):
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
    importer = system_pkgmap.InstallContentsImporter()
    importer._ImportPackages(data)
    importer._ImportFiles(data, show_progress=False)
    self.assertEquals(0, len(list(models.Srv4FileStats.select())))
    self.assertEquals(0, len(list(models.CswFile.select())))

  def testSanitizeInstallContentsPkgnameNone(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "BOstdenv",
        importer.SanitizeInstallContentsPkgname("BOstdenv:none"))

  def testSanitizeInstallContentsPkgnameTilde(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "BOstdenv",
        importer.SanitizeInstallContentsPkgname("~BOstdenv"))

  def testSanitizeInstallContentsPkgnameJ3link(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "SUNWjhrt",
        importer.SanitizeInstallContentsPkgname("SUNWjhrt:j3link"))

  def testSanitizeInstallContentsPkgnameJ3linkAi(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "SUNWjai",
        importer.SanitizeInstallContentsPkgname("SUNWjai:j3link"))

  def testSanitizeInstallContentsPkgnameJ5linkAi(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "SUNWjai",
        importer.SanitizeInstallContentsPkgname("SUNWjai:j5link"))

  def testSanitizeInstallContentsPkgnameInstallError(self):
    importer = system_pkgmap.InstallContentsImporter()
    self.assertEquals(
        "CSWmozilla",
        importer.SanitizeInstallContentsPkgname("!CSWmozilla"))


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  unittest.main()
