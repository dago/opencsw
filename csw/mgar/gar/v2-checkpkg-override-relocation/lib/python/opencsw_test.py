#!/opt/csw/bin/python2.6
# $Id$

import copy
import datetime
import opencsw
import os.path
import re
import unittest
from Cheetah import Template

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

PKGMAP_1 = """1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW 0644 root bin 4053 20987 1264420689
"""

PKGMAP_2 = """: 1 18128
1 d none /etc/opt/csw/cups 0755 root bin
1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW 0644 root bin 4053 20987 1264420689
1 f none /etc/opt/csw/cups/cupsd.conf.default 0640 root bin 4053 20987 1264420689
1 d none /etc/opt/csw/cups/interfaces 0755 root bin
1 d none /etc/opt/csw/cups/ppd 0755 root bin
1 f cswinitsmf /etc/opt/csw/init.d/cswcups 0555 root bin 4547 14118 1264420798
1 i depend 122 11155 1264524848
1 i pkginfo 489 41685 1264524852
1 i postremove 151 12419 1256302505
1 i preinstall 1488 45678 125630250
"""

SUBMITPKG_DATA_1 = {
    'NEW_PACKAGE': 'new package',
    'to': u'Release Manager <somebody@example.com>',
    'NO_VERSION_CHANGE': 'no version change',
    'from': u'Maciej Blizinski <maintainer@example.com>',
    'date': datetime.datetime(2010, 2, 21, 12, 52, 44, 295766),
    'cc': None,
    'pkg_groups': [
      {'upgrade_msg': '1.5.2.2,REV=2009.09.04 --> 1.5.3,REV=2010.02.02',
       'versions': ('1.5.2.2,REV=2009.09.04', '1.5.3,REV=2010.02.02'),
       'pkgs': [
         {'basename': 'tree-1.5.3,REV=2010.02.02-SunOS5.8-i386-CSW.pkg.gz'},
         {'basename': 'tree-1.5.3,REV=2010.02.02-SunOS5.8-sparc-CSW.pkg.gz'}
       ],
       'name': 'tree',
       'upgrade_type': opencsw.PATCHLEVEL,
      }
    ],
    'subject': u'newpkgs tree'
}
SUBMITPKG_EXPECTED_1 = u"""From: Maciej Blizinski <maintainer@example.com>
To: Release Manager <somebody@example.com>
Subject: newpkgs tree

* tree: patchlevel upgrade
  - from: 1.5.2.2,REV=2009.09.04
  -   to: 1.5.3,REV=2010.02.02
  + tree-1.5.3,REV=2010.02.02-SunOS5.8-i386-CSW.pkg.gz
  + tree-1.5.3,REV=2010.02.02-SunOS5.8-sparc-CSW.pkg.gz

-- 
Generated by submitpkg
"""

class ParsePackageFileNameTest(unittest.TestCase):

  def testParsePackageFileName1(self):
    test_data = open(os.path.join(os.path.split(__file__)[0],
                                  "testdata/example-catalog.txt"))
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


class ParsePackageFileNameTest_2(unittest.TestCase):

  def setUp(self):
    self.file_name = 'mysql5client-5.0.87,REV=2010.02.28-SunOS5.8-i386-CSW.pkg.gz'
    self.parsed = opencsw.ParsePackageFileName(self.file_name)

  def testParsePackageFileName_2_1(self):
    self.assertTrue("arch" in self.parsed)
    self.assertEqual(self.parsed["arch"], "i386")

  def testParsePackageFileName_2_2(self):
    self.assertTrue("osrel" in self.parsed)
    self.assertEqual(self.parsed["osrel"], "SunOS5.8")

  def testParsePackageFileName_2_3(self):
    self.assertTrue("vendortag" in self.parsed)
    self.assertEqual(self.parsed["vendortag"], "CSW")

  def testParsePackageFileName_OldFormat(self):
    """Old srv4 file name."""
    file_name = "achievo-0.8.4-all-CSW.pkg.gz"
    parsed = opencsw.ParsePackageFileName(file_name)
    self.assertEqual("unspecified", parsed["osrel"])


class UpgradeTypeTest(unittest.TestCase):

  def testUpgradeType_1(self):
    pkg = opencsw.CatalogBasedOpencswPackage("analog")
    pkg.LazyDownloadCatalogData(CATALOG_DATA_1.splitlines())
    expected_data = {
        'version': '5.32',
        'full_version_string': '5.32,REV=2003.9.12',
        'version_info': {'minor version': '32', 'major version': '5'},
        'vendortag': 'CSW',
        'revision_info': {'REV': '2003.9.12'},
        'arch': 'sparc',
        'osrel': 'SunOS5.8',
        'catalogname': 'analog'
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
        ("foo_ba", ["foo_bar", "foo_baz"]),
        ("foo", ["foo_a", "foo_b"]),
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


class PkgmapUnitTest(unittest.TestCase):

  def test_1(self):
    pkgmap = opencsw.Pkgmap(PKGMAP_1.splitlines())
    expected = [
        {
            'group': 'bin',
            'user':  'root',
            'path':  '/etc/opt/csw/cups/cupsd.conf.CSW',
            'line':  '1 f cswcpsampleconf /etc/opt/csw/cups/cupsd.conf.CSW 0644 root bin 4053 20987 1264420689',
            'type':  'f',
            'class': 'cswcpsampleconf',
            'mode':  '0644'
        }
    ]
    self.assertEqual(expected, pkgmap.entries)

  def test_2(self):
    pkgmap = opencsw.Pkgmap(PKGMAP_2.splitlines())
    line = ": 1 18128"
    self.assertTrue(line in pkgmap.entries_by_line)

  def test_3(self):
    pkgmap = opencsw.Pkgmap(PKGMAP_2.splitlines())
    self.assertTrue("cswcpsampleconf" in pkgmap.entries_by_class)


class IndexByUnitTest(unittest.TestCase):

  def testIndexDictsBy_1(self):
    list_of_dicts = [
        {"a": 1},
        {"a": 2},
        {"a": 3},
    ]
    expected = {
        1: [{'a': 1}],
        2: [{'a': 2}],
        3: [{'a': 3}],
    }
    self.assertEquals(expected, opencsw.IndexDictsBy(list_of_dicts, "a"))

  def testIndexDictsBy_2(self):
    list_of_dicts = [
        {"a": 1, "b": 1},
        {"a": 1, "b": 2},
        {"a": 1, "b": 3},
    ]
    expected = {
        1: [
          {'a': 1, 'b': 1},
          {'a': 1, 'b': 2},
          {'a': 1, 'b': 3},
        ]
    }
    self.assertEquals(expected, opencsw.IndexDictsBy(list_of_dicts, "a"))


class SubmitpkgTemplateUnitTest(unittest.TestCase):

  def testTypicalUpgradeStrict(self):
    """Strict testing of standard upgrade."""
    t = Template.Template(opencsw.SUBMITPKG_TMPL,
                          searchList=[SUBMITPKG_DATA_1])
    self.assertEquals(SUBMITPKG_EXPECTED_1, unicode(t))

  def testWarningOnNoChange(self):
    """If there's no version change, a warning is needed."""
    submitpkg_data = copy.deepcopy(SUBMITPKG_DATA_1)
    submitpkg_data["pkg_groups"][0]["upgrade_type"] = opencsw.NO_VERSION_CHANGE
    t = Template.Template(opencsw.SUBMITPKG_TMPL,
                          searchList=[submitpkg_data])
    self.assertTrue(re.search(r"WARNING", unicode(t)), unicode(t))

  def testNewPackage(self):
    """Tests for "new package" somewhere in the message."""
    submitpkg_data = copy.deepcopy(SUBMITPKG_DATA_1)
    submitpkg_data["pkg_groups"][0]["upgrade_type"] = opencsw.NEW_PACKAGE
    t = Template.Template(opencsw.SUBMITPKG_TMPL,
                          searchList=[submitpkg_data])
    self.assertTrue(re.search(r"new package", unicode(t)), unicode(t))

class OpencswCatalogUnitTest(unittest.TestCase):

  def test_ParseCatalogLine_1(self):
    line = (
        'tmux 1.2,REV=2010.05.17 CSWtmux '
        'tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz '
        '145351cf6186fdcadcd169b66387f72f 214091 '
        'CSWcommon|CSWlibevent none none\n')
    oc = opencsw.OpencswCatalog(None)
    parsed = oc._ParseCatalogLine(line)
    expected = {'catalogname': 'tmux',
                'deps': 'CSWcommon|CSWlibevent',
                'file_basename': 'tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz',
                'md5sum': '145351cf6186fdcadcd169b66387f72f',
                'none_thing_1': 'none',
                'none_thing_2': 'none',
                'pkgname': 'CSWtmux',
                'size': '214091',
                'version': '1.2,REV=2010.05.17'}
    self.assertEquals(expected, parsed)



if __name__ == '__main__':
  unittest.main()
