#!/opt/csw/bin/python2.6
# $Id$

import opencsw
import os.path
import re
import unittest

CATALOG_DATA_1 = """amavisd_new 2.6.3,REV=2009.04.23 CSWamavisdnew amavisd_new-2.6.3,REV=2009.04.23-SunOS5.8-all-CSW.pkg.gz 831f063d1ba20eb8bea0e0e60ceef3cb 813802 CSWperl|CSWcswclassutils|CSWpmunixsyslog|CSWpmiostringy|CSWpmnetserver|CSWpmmailtools|CSWpmmimetools|CSWpmcompresszlib|CSWpmarchivetar|CSWpmarchivezip|CSWspamassassin|CSWpmberkeleydb|CSWpmconverttnef|CSWpmconvertuulib|CSWpmmaildkim|CSWcommon none
amsn 0.94 CSWamsn amsn-0.94-SunOS5.8-all-CSW.pkg.gz 99afd828dd38fb39a37cb8ffd448b098 2420919 CSWtcl|CSWtk|CSWtcltls none
analog 5.32,REV=2003.9.12 CSWanalog analog-5.32,REV=2003.9.12-SunOS5.8-sparc-CSW.pkg.gz a2550ef2e37c67d475a19348b7276a38 711992 CSWcommon none
angband 3.0.3 CSWangband angband-3.0.3-SunOS5.8-sparc-CSW.pkg.gz 9280ff14bde4523d6032ede46c7630e3 1402841 CSWcommon|CSWgtk none
anjuta 1.2.2,REV=2005.03.01 CSWanjuta anjuta-1.2.2,REV=2005.03.01-SunOS5.8-sparc-CSW.pkg.gz 095ba6d763f157b0ce38922447c923b2 6502489 CSWaudiofile|CSWbonobo2|CSWcommon|CSWesound|CSWexpat|CSWfconfig|CSWftype2|CSWgconf2|CSWggettext|CSWglib2|CSWgnomekeyring|CSWgnomevfs2|CSWgtk2|CSWiconv|CSWjpeg|CSWlibart|CSWlibatk|CSWlibbonoboui|CSWlibglade2|CSWlibgnome|CSWlibgnomecanvas|CSWlibgnomeprint|CSWlibgnomeprintui|CSWlibgnomeui|CSWlibpopt|CSWlibxft2|CSWlibxml2|CSWlibxrender|CSWorbit2|CSWossl|CSWpango|CSWpcre|CSWvte|CSWzlib none
ant 1.7.1,REV=2008.10.29 CSWant ant-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
foo 1.7.1,REV=2008.10.29 CSWfoo foo-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
foo_devel 1.7.1,REV=2008.10.29 CSWfoo_devel foo_devel-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
libfoo 1.7.1,REV=2008.10.29 CSWlibfoo libfoo-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
foodoc 1.7.1,REV=2008.10.29 CSWfoodoc foodoc-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
bar 1.7.1,REV=2008.10.29 CSWbar bar-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz 0945884a52a3b43b743650c60ac21236 2055045 CSWcommon|CSWxercesj|CSWxmlcommonsext none
antdoc 1.7.1,REV=2008.10.29 CSWantdoc antdoc-1.7.1,REV=2008.10.29-SunOS5.8-all-CSW.pkg.gz e6555e61e7e7f1740935d970e5efad57 5851724 CSWcommon none"""
TEST_PKGINFO="""ARCH=i386
BASEDIR=/
CATEGORY=system
DESC=GNU Bourne-Again shell (bash) version 3.0
EMAIL=
HOTLINE=Please contact your local service provider
MAXINST=1000
NAME=GNU Bourne-Again shell (bash)
PKG=SUNWbash
SUNW_PKGTYPE=usr
SUNW_PKGVERS=1.0
SUNW_PRODNAME=SunOS
SUNW_PRODVERS=5.10/SunOS Development
VENDOR=Sun Microsystems, Inc.
VERSION=11.10.0,REV=2005.01.08.01.09
PSTAMP=sfw10-patch-x20070430084427
CLASSES=none
PATCHLIST=126547-01
PATCH_INFO_126547-01=Installed: Mon Oct 27 08:52:07 PDT 2008 From: mum Obsoletes:  Requires:  Incompatibles:
PKG_SRC_NOVERIFY= none
PKG_DST_QKVERIFY= none
PKG_CAS_PASSRELATIVE= none
#FASPACD= none
"""


class ParsePackageFileNameTest(unittest.TestCase):

  def testParsePackageFileName1(self):
    test_data = open(os.path.join(os.path.split(__file__)[0], "testdata/example-catalog.txt"))
    split_re = re.compile(r"\s+")
    for line in test_data:
      fields = re.split(split_re, line)
      catalogname = fields[0]
      pkg_version = fields[1]
      pkgname = fields[2]
      file_name = fields[3]
      pkg_md5 = fields[4]
      pkg_size = fields[5]
      depends_on = fields[6]
      compiled = opencsw.ParsePackageFileName(file_name)
      self.assertTrue(compiled, "File name %s did not compile" % repr(file_name))
      self.assertEqual(catalogname, compiled["catalogname"])
      self.assertEqual(pkg_version, compiled["full_version_string"])


class UpgradeTypeTest(unittest.TestCase):

  def testUpgradeType_1(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    expected_data = {
        'catalogname': 'analog',
        'full_version_string': '5.32,REV=2003.9.12',
        'version': '5.32',
        'version_info': {opencsw.MAJOR_VERSION: '5',
                         opencsw.MINOR_VERSION: '32'},
        'revision_info': {'REV': '2003.9.12'},
    }
    self.assertEqual(expected_data, pkg.GetCatalogPkgData())

  def testUpgradeType_2(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "5.32,REV=2003.9.12"
    new_version_string        = "5.32,REV=2003.9.13"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.REVISION, upgrade_type)

  def testUpgradeType_3(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "5.32,REV=2003.9.12"
    new_version_string        = "5.33,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.MINOR_VERSION, upgrade_type)

  def testUpgradeType_4(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "5.32,REV=2003.9.12"
    new_version_string        = "6.0,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.MAJOR_VERSION, upgrade_type)

  def testUpgradeType_5(self):
    pkg = opencsw.CatalogBasedOpencswPackage("nonexisting")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "5.32,REV=2003.9.12"
    new_version_string        = "6.0,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.NEW_PACKAGE, upgrade_type)

  def testUpgradeType_6(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "5.32,REV=2003.9.12"
    new_version_string        = "5.32,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.NO_VERSION_CHANGE, upgrade_type)

  def testUpgradeType_7(self):
    pkg = opencsw.CatalogBasedOpencswPackage("angband")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "3.0.3"
    new_version_string        = "3.0.3,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.REVISION_ADDED, upgrade_type)

  def testUpgradeType_8(self):
    pkg = opencsw.CatalogBasedOpencswPackage("angband")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    unused_old_version_string = "3.0.3"
    new_version_string        = "3.0.4,REV=2003.9.12"
    upgrade_type, upgrade_description, vs = pkg.UpgradeType(new_version_string)
    self.assertEqual(opencsw.PATCHLEVEL, upgrade_type)

class PackageTest(unittest.TestCase):

  def test_2(self):
    expected = {
        'SUNW_PRODVERS': '5.10/SunOS Development',
        'PKG_CAS_PASSRELATIVE': ' none',
        'PKG_SRC_NOVERIFY': ' none',
        'PSTAMP': 'sfw10-patch-x20070430084427',
        'ARCH': 'i386',
        'EMAIL': '',
        'MAXINST': '1000',
        'PATCH_INFO_126547-01': 'Installed: Mon Oct 27 08:52:07 PDT 2008 From: mum Obsoletes:  Requires:  Incompatibles:',
        'PKG': 'SUNWbash',
        'SUNW_PKGTYPE': 'usr',
        'PKG_DST_QKVERIFY': ' none',
        'SUNW_PKGVERS': '1.0',
        'VENDOR': 'Sun Microsystems, Inc.',
        'BASEDIR': '/',
        'CLASSES': 'none',
        'PATCHLIST': '126547-01',
        'DESC': 'GNU Bourne-Again shell (bash) version 3.0',
        'CATEGORY': 'system',
        'NAME': 'GNU Bourne-Again shell (bash)',
        'SUNW_PRODNAME': 'SunOS',
        'VERSION': '11.10.0,REV=2005.01.08.01.09',
        'HOTLINE': 'Please contact your local service provider',
    }
    self.assertEquals(expected,
                      opencsw.ParsePkginfo(TEST_PKGINFO.splitlines()))

  def testSplitByCase1(self):
    self.assertEquals(["aaa", "bbb"], opencsw.SplitByCase("AAAbbb"))

  def testSplitByCase2(self):
    self.assertEquals(["aaa", "bbb", "ccc"], opencsw.SplitByCase("AAAbbb-ccc"))

  def testPkgnameToCatName1(self):
    self.assertEquals("sunw_bash", opencsw.PkgnameToCatName("SUNWbash"))

  def testPkgnameToCatName2(self):
    self.assertEquals("sunw_bash_s", opencsw.PkgnameToCatName("SUNWbashS"))

  def testPkgnameToCatName3(self):
    """These are the rules!"""
    self.assertEquals("sunw_p_ython", opencsw.PkgnameToCatName("SUNWPython"))

  def testPkgnameToCatName4(self):
    self.assertEquals("stuf_with_some_dashes",
                      opencsw.PkgnameToCatName("STUFwith-some-dashes"))

  def test_4(self):
    pkginfo_dict = opencsw.ParsePkginfo(TEST_PKGINFO.splitlines())
    expected = "sunw_bash-11.10.0,REV=2005.01.08.01.09-SunOS5.10-i386-SUNW.pkg"
    self.assertEquals(expected, opencsw.PkginfoToSrv4Name(pkginfo_dict))


class PackageGroupNameTest(unittest.TestCase):

  @classmethod
  def CreatePkgList(self, catalogname_list):
    pkg_list = []
    for name in catalogname_list:
      pkg = opencsw.CatalogBasedOpencswPackage("foo")
      pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
      pkg_list.append(pkg)
    return pkg_list

  def testPackageGroupName_0(self):
    data = [
        ("foo", ["foo"]),
        ("foo", ["foo", "libfoo"]),
        ("foo", ["foo", "libfoo", "foo_devel"]),
        ("various packages", ["foo", "libfoo", "foo_devel", "bar"]),
    ]
    for expected_name, catalogname_list in data:
      result = opencsw.CatalogNameGroupName(catalogname_list)
      self.assertEqual(expected_name, result,
          "data: %s, expected: %s, got: %s" % (catalogname_list,
                                               repr(expected_name),
                                               repr(result)))

  def testLongestCommonSubstring_1(self):
    self.assertEqual(set(["foo"]), opencsw.LongestCommonSubstring("foo", "foo"))

  def testLongestCommonSubstring_2(self):
    self.assertEqual(set([]), opencsw.LongestCommonSubstring("foo", "bar"))

  def testLongestCommonSubstring_3(self):
    self.assertEqual(set(["bar"]), opencsw.LongestCommonSubstring("barfoobar", "bar"))

  def testLongestCommonSubstring_4(self):
    self.assertEqual(set(['bcd', 'hij']), opencsw.LongestCommonSubstring("abcdefghijk", "bcdhij"))


if __name__ == '__main__':
  unittest.main()
