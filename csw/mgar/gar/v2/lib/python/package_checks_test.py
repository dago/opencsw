#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import copy
import unittest
import package_checks as pc
import checkpkg
import yaml
import os.path
import mox
import logging
import pprint

import testdata.checkpkg_test_data_CSWdjvulibrert as td_1
import testdata.checkpkg_pkgs_data_minimal as td_2

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")
CHECKPKG_STATS_DIR = os.path.join(TESTDATA_DIR, "stats")
DEFAULT_DATA_MD5 = "461a24f02dd5020b4aa014b76f3ec2cc"
DEFAULT_PKG_STATS = checkpkg.PackageStats(None, CHECKPKG_STATS_DIR, DEFAULT_DATA_MD5)
DEFAULT_PKG_DATA = DEFAULT_PKG_STATS.GetAllStats()

class CheckpkgUnitTestHelper(object):
  """Wraps common components of checkpkg tests."""

  def setUp(self):
    # This is slow. Let's speed it up somehow.  Move away from yaml and create
    # a Python module with the data.
    self.pkg_stats = DEFAULT_PKG_STATS
    self.pkg_data = self.pkg_stats.GetAllStats()
    # This makes one of the test break. To be investigated.
    # self.pkg_data = DEFAULT_PKG_DATA
    self.mocker = mox.Mox()

  def testDefault(self):

    class LoggerStub(object):

      def debug(self, debug_s, *kwords):
        pass

      def info(self, debug_s, *kwords):
        pass
    # self.logger_mock = self.mocker.CreateMock(logging.Logger)
    self.logger_mock = LoggerStub()
    self.error_mgr_mock = self.mocker.CreateMock(
        checkpkg.IndividualCheckInterface)
    self.CheckpkgTest()
    self.mocker.ReplayAll()
    getattr(pc, self.FUNCTION_NAME)(self.pkg_data,
                                    self.error_mgr_mock,
                                    self.logger_mock)
    self.mocker.VerifyAll()


class TestMultipleDepends(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckMultipleDepends'
  def CheckpkgTest(self):
    self.pkg_data["depends"].append(("CSWcommon", "This is surplus"))
    self.error_mgr_mock.ReportError('dependency-listed-more-than-once',
                                    'CSWcommon')

class TestDescription(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDescription'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo'
    self.error_mgr_mock.ReportError('pkginfo-description-missing')


class TestDescriptionLong(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDescription'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - ' 'A' * 200
    self.error_mgr_mock.ReportError('pkginfo-description-too-long', 'length=1394')


class TestDescriptionNotCapitalized(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDescription'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - lowercase'
    self.error_mgr_mock.ReportError('pkginfo-description-not-starting-with-uppercase',
                                    'lowercase')


class TestCheckCatalogname_1(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckCatalogname'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo-bar - This catalog name is bad'
    self.error_mgr_mock.ReportError('pkginfo-bad-catalogname', 'foo-bar')


class TestCheckCatalogname_2(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckCatalogname'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["NAME"] = 'libsigc++_devel - This catalog name is good'


class TestCheckSmfIntegration(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "1 f none /etc/opt/csw/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/etc/opt/csw/init.d/foo",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError('init-file-missing-cswinitsmf-class',
                                    '/etc/opt/csw/init.d/foo class=none')

class TestCheckCatalognameGood(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "cswinitsmf",
      "group": "bin",
      "line": "1 f none /etc/opt/csw/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/etc/opt/csw/init.d/foo",
      "type": "f",
      "user": "root"
    })


class TestCatalognameLowercase_1(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CatalognameLowercase'
  def CheckpkgTest(self):
    self.pkg_data["basic_stats"]["catalogname"] = "Foo"
    self.error_mgr_mock.ReportError('catalogname-not-lowercase')

class TestCatalognameLowercase_2(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CatalognameLowercase'
  def CheckpkgTest(self):
    self.pkg_data["basic_stats"]["catalogname"] = "foo"

class TestCatalognameLowercase_3(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CatalognameLowercase'
  def CheckpkgTest(self):
    self.pkg_data["basic_stats"]["catalogname"] = "foo+abc&123"
    self.error_mgr_mock.ReportError('catalogname-is-not-a-simple-word')


class TestSetCheckDependencies(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckDependencies'
  def CheckpkgTest(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    self.pkg_data[0]["depends"].append(["CSWmarsian", "A package from Mars."])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)
    self.error_mgr_mock.ReportError('CSWrsync', 'unidentified-dependency', 'CSWmarsian')


class TestSetCheckDependenciesGood(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckDependencies'
  def CheckpkgTest(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)


class TestSetCheckDependenciesTwoPkgsBad(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckDependencies'
  def CheckpkgTest(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single, copy.deepcopy(self.pkg_data_single)]
    self.pkg_data[1]["basic_stats"]["pkgname"] = "CSWsecondpackage"
    self.pkg_data[1]["depends"].append(["CSWmartian", ""])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)
    self.error_mgr_mock.ReportError(
        'CSWsecondpackage', 'unidentified-dependency', 'CSWmartian')


class TestSetCheckDependenciesTwoPkgsGood(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckDependencies'
  def CheckpkgTest(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single, copy.deepcopy(self.pkg_data_single)]
    self.pkg_data[1]["basic_stats"]["pkgname"] = "CSWsecondpackage"
    self.pkg_data[1]["depends"].append(["CSWrsync", ""])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)


class TestCheckCheckDependsOnSelf(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDependsOnSelf'
  def CheckpkgTest(self):
    self.pkg_data["depends"].append(["CSWrsync", ""])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.ReportError('depends-on-self')


class TestCheckArchitectureSanity(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureSanity'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["ARCH"] = "i386"
    self.error_mgr_mock.ReportError(
        'srv4-filename-architecture-mismatch',
        'pkginfo=i386 filename=rsync-3.0.7,REV=2010.02.17-SunOS5.8-sparc-CSW.pkg.gz')

class TestCheckArchitectureVsContents(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureVsContents'
  def CheckpkgTest(self):
    # TODO: Update this.
    # self.pkg_data["pkgmap"] = self.LoadData("example-1-pkgmap")
    # self.pkg_data["binaries"] = []
    # self.pkg_data["pkginfo"] = self.LoadData("example-1-pkginfo")
    # errors = pc.CheckArchitectureVsContents(self.pkg_data_2, False)
    # self.failIf(errors)
    pass

class TestCheckFileNameSanity(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckFileNameSanity'
  def CheckpkgTest(self):
    del(self.pkg_data["basic_stats"]["parsed_basename"]["revision_info"]["REV"])
    self.error_mgr_mock.ReportError('rev-tag-missing-in-filename')


class TestCheckLinkingAgainstSunX11(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckLinkingAgainstSunX11'
  def CheckpkgTest(self):
    self.pkg_data["binaries_dump_info"][0]["needed sonames"].append("libX11.so.4")

class TestCheckLinkingAgainstSunX11_Bad(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckLinkingAgainstSunX11'
  def CheckpkgTest(self):
    self.pkg_data["binaries_dump_info"].append({
         'base_name': 'libImlib2.so.1.4.2',
         'needed sonames': ['libfreetype.so.6',
                            'libz.so',
                            'libX11.so.4',
                            'libXext.so.0',
                            'libdl.so.1',
                            'libm.so.1',
                            'libc.so.1'],
         'path': 'opt/csw/lib/libImlib2.so.1.4.2',
         'runpath': ['/opt/csw/lib/$ISALIST',
                     '/opt/csw/lib',
                     '/usr/lib/$ISALIST',
                     '/usr/lib',
                     '/lib/$ISALIST',
                     '/lib'],
         'soname': 'libImlib2.so.1',
         'soname_guessed': False,
    })
    self.error_mgr_mock.ReportError('linked-against-discouraged-library',
                                    'libImlib2.so.1.4.2 libX11.so.4')

class TestSetCheckSharedLibraryConsistency2_1(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    self.pkg_data = [td_1.pkg_data]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCrun.so.1').AndReturn(
      {u'/usr/lib': [u'SUNWlibC'],
       u'/usr/lib/sparcv9': [u'SUNWlibC']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCstd.so.1').AndReturn(
      {u'/usr/lib': [u'SUNWlibC'],
       u'/usr/lib/sparcv9': [u'SUNWlibC']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn(
      {u'/lib': [u'SUNWcslr'],
       u'/lib/sparcv9': [u'SUNWcslr'],
       u'/usr/lib': [u'SUNWcsl'],
       u'/usr/lib/libp': [u'SUNWdpl'],
       u'/usr/lib/libp/sparcv9': [u'SUNWdpl'],
       u'/usr/lib/sparcv9': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libiconv.so.2').AndReturn(
      {u'/opt/csw/lib': [u'CSWiconv'],
       u'/opt/csw/lib/sparcv9': [u'CSWiconv']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libjpeg.so.62').AndReturn(
      {u'/opt/csw/lib': [u'CSWjpeg'],
       u'/opt/csw/lib/sparcv9': [u'CSWjpeg'],
       u'/usr/lib': [u'SUNWjpg'],
       u'/usr/lib/sparcv9': [u'SUNWjpg']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libjpeg.so.7').AndReturn(
      {u'/opt/csw/lib': [u'CSWjpeg'],
       u'/opt/csw/lib/sparcv9': [u'CSWjpeg']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libm.so.1').AndReturn(
      {u'/lib': [u'SUNWlibmsr'],
       u'/lib/sparcv9': [u'SUNWlibmsr'],
       u'/usr/lib': [u'SUNWlibms'],
       u'/usr/lib/sparcv9': [u'SUNWlibms']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpthread.so.1').AndReturn(
      {u'/lib': [u'SUNWcslr'],
       u'/lib/sparcv9': [u'SUNWcslr'],
       u'/usr/lib': [u'SUNWcsl'],
       u'/usr/lib/sparcv9': [u'SUNWcsl']})
    self.error_mgr_mock.ReportError('CSWdjvulibrert', 'missing-dependency', u'CSWiconv')


class TestCheckPstamp(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckPstamp'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["PSTAMP"] = "build8s20090904191054"
    self.error_mgr_mock.ReportError(
        'pkginfo-pstamp-in-wrong-format', 'build8s20090904191054',
        "It should be 'username@hostname-timestamp', but it's 'build8s20090904191054'.")


if __name__ == '__main__':
  unittest.main()
