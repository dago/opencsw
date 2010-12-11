#!/usr/bin/env python2.6

import unittest
import system_pkgmap
import test_base
import models
import logging
import common_constants

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


class IndexerUnitTest(unittest.TestCase):

  def test_ParsePkgmapLineFile(self):
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
    self.assertEqual(expected, spi._ParsePkgmapLine(PKGMAP_LINE_1))

  def test_ParsePkgmapLineTypeSymlink(self):
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
    self.assertEqual(expected, spi._ParsePkgmapLine(PKGMAP_LINE_3))

  def test_ParsePkgmapLineTypeQuestionMark(self):
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
    self.assertEqual(expected, spi._ParsePkgmapLine(PKGMAP_LINE_5))

  def test_ParsePkgmapLibc(self):
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
    self.assertEqual(expected, spi._ParsePkgmapLine(PKGMAP_LINE_6))

  def test_ParsePkgmapLineTypeWrongSyntax(self):
    spi = system_pkgmap.Indexer()
    self.assertRaises(
        system_pkgmap.ParsingError,
        spi._ParsePkgmapLine, "/")

  def test_ParseInstallContents(self):
    spi = system_pkgmap.Indexer()
    data = (
        PKGMAP_LINE_1,
        PKGMAP_LINE_2,
        PKGMAP_LINE_3,
        PKGMAP_LINE_4)
    self.assertEqual(4, len(spi._ParseInstallContents(data, False)))


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


if __name__ == '__main__':
  logging.basicConfig(level=logging.CRITICAL)
  unittest.main()
