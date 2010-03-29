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
import testdata.rpaths

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")
CHECKPKG_STATS_DIR = os.path.join(TESTDATA_DIR, "stats")
DEFAULT_DATA_MD5 = "461a24f02dd5020b4aa014b76f3ec2cc"
DEFAULT_PKG_STATS = checkpkg.PackageStats(None, CHECKPKG_STATS_DIR, DEFAULT_DATA_MD5)
DEFAULT_PKG_DATA = DEFAULT_PKG_STATS.GetAllStats()

class CheckpkgUnitTestHelper(object):
  """Wraps common components of checkpkg tests."""

  def setUp(self):
    self.pkg_stats = DEFAULT_PKG_STATS
    # self.pkg_data = self.pkg_stats.GetAllStats()
    # This makes one of the test break. To be investigated.
    self.pkg_data = copy.deepcopy(DEFAULT_PKG_DATA)
    self.mocker = mox.Mox()

  def testDefault(self):

    class LoggerStub(object):
      def debug(self, debug_s, *kwords):
        pass
      def info(self, debug_s, *kwords):
        pass
    class MessengerStub(object):
      def Message(self, m):
        pass
      def SuggestGarLine(self, m):
        pass
    # self.logger_mock = self.mocker.CreateMock(logging.Logger)
    self.logger_mock = LoggerStub()
    self.error_mgr_mock = self.mocker.CreateMock(
        checkpkg.IndividualCheckInterface)
    self.messenger = MessengerStub()
    self.CheckpkgTest()
    self.mocker.ReplayAll()
    getattr(pc, self.FUNCTION_NAME)(self.pkg_data,
                                    self.error_mgr_mock,
                                    self.logger_mock,
                                    self.messenger)
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


class TestCheckRpath(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckRpath'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = testdata.rpaths.all_rpaths
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.ReportError('bad-rpath-entry', '$ORIGIN/..')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '$ORIGIN/../../../usr/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '$ORIGIN/../../usr/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '$ORIGIN/../lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '$ORIGIN/../ure-link/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '../../../../../dist/bin')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '../../../../dist/bin')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '../../../dist/bin')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '../../dist/bin')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/bin')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/home/buysse/build/expect-5.42.1/cswstage/opt/csw/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/home/phil/build/gettext-0.14.1/gettext-tools/intl/.libs')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/medusa/kenmays/build/qt-x11-free-3.3.3/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/medusa/kenmays/build/s_qt/qt-x11-free-3.3.3/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/designer')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/sqldrivers')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/home/harpchad/local/sparc/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/lib/sparcv9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWcluster/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWmlib/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/stlport4')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/v8plus')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/v8plusa')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/v8plusb')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/SUNWspro/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/build/michael/synce-0.8.9-buildroot/opt/csw/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/$ISALIST')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw//lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/X11/lib/')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/bdb4/lib/')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/$')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/$$ISALIST')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/-R/opt/csw/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/\\$ISALIST')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/\\SALIST')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/lib/sparcv8plus+vis')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/mysql4//lib/mysql')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/nagios/lib/\\$ISALIST')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/openoffice.org/basis3.1/program')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/csw/openoffice.org/ure/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/cw/gcc3/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/forte8/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/forte8/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/forte8/SUNWspro/lib/rw7/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/forte8/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/forte8/SUNWspro/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/schily/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/sfw/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS10/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS10/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS10/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS10/SUNWspro/lib/v8plus')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/rw7/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/stlport4')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/stlport4/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/v8plus')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS11/SUNWspro/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib/rw7/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib/v8plusa')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio/SOS8/SUNWspro/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/rw7')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/rw7/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/stlport4')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/stlport4/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/v8')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/opt/studio10/SUNWspro/lib/v9')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/oracle/product/9.2.0/lib32')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/X/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/local/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/local/openldap-2.3/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/sfw/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/ucblib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', '/usr/xpg4/lib')
    self.error_mgr_mock.ReportError('bad-rpath-entry', 'RIGIN/../lib')


class TestCheckRpathBadPath(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ["/opt/csw/lib"]
    binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
    self.pkg_data["depends"] = (("CSWfoo", None),)
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
       u'/opt/csw/lib': [u'CSWfoo'],
       u'/opt/csw/lib/sparcv9': [u'CSWfoo'],
    })
    self.error_mgr_mock.ReportError(
        'CSWrsync',
        'deprecated-library',
        u'opt/csw/bin/sparcv9/rsync Deprecated Berkeley DB location '
        u'/opt/csw/lib/libdb-4.7.so')
    self.pkg_data = [self.pkg_data]


class TestCheckVendorURL_BadUrl(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckVendorURL"
  def CheckpkgTest(self):
    # Injecting the data to be examined.
    self.pkg_data["pkginfo"]["VENDOR"] = "badurl"
    # Expecting the following method to be called.
    self.error_mgr_mock.ReportError(
        "pkginfo-bad-vendorurl",
        "badurl",
        "Solution: add VENDOR_URL to GAR Recipe")


class TestCheckVendorURL_Good(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckVendorURL"
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["VENDOR"] = "http://www.example.com/"
    # No call to error_mgr_mock means that no errors should be reported: the
    # URL is okay.


if __name__ == '__main__':
  unittest.main()
