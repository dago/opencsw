#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import copy
import datetime
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
from testdata.rsync_pkg_stats import pkgstats as rsync_stats
from testdata.tree_stats import pkgstats as tree_stats
from testdata.ivtools_stats import pkgstats as ivtools_stats
from testdata.sudo_stats import pkgstats as sudo_stats
from testdata.javasvn_stats import pkgstats as javasvn_stats
from testdata.neon_stats import pkgstats as neon_stats
from testdata import stubs

DEFAULT_PKG_STATS = None
DEFAULT_PKG_DATA = rsync_stats[0]


class CheckpkgUnitTestHelper(object):
  """Wraps common components of checkpkg tests."""

  def setUp(self):
    self.pkg_stats = DEFAULT_PKG_STATS
    self.pkg_data = copy.deepcopy(DEFAULT_PKG_DATA)
    self.mocker = mox.Mox()

  def SetMessenger(self):
    self.messenger = stubs.MessengerStub()

  def testDefault(self):
    self.logger_mock = stubs.LoggerStub()
    self.error_mgr_mock = self.mocker.CreateMock(
        checkpkg.IndividualCheckInterface)
    self.SetMessenger()
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


class TestCheckSmfIntegrationBad(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "1 f none /opt/csw/etc/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/etc/opt/csw/init.d/foo",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError('init-file-missing-cswinitsmf-class',
                                    '/etc/opt/csw/init.d/foo class=none')

class TestCheckCheckSmfIntegrationGood(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "cswinitsmf",
      "group": "bin",
      "line": "1 f none /opt/csw/etc/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/etc/opt/csw/init.d/foo",
      "type": "f",
      "user": "root"
    })


class TestCheckCheckSmfIntegrationWrongLocation(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "cswinitsmf",
      "group": "bin",
      "line": "1 f none /etc/opt/csw/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/opt/csw/etc/init.d/foo",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError('init-file-wrong-location', '/opt/csw/etc/init.d/foo')


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

class TestCheckArchitectureVsContents_Devel_1(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureVsContents'
  def CheckpkgTest(self):
    self.pkg_data["binaries"] = []
    self.pkg_data["binaries_dump_info"] = []
    self.pkg_data["pkgmap"] = []
    self.pkg_data["basic_stats"]["pkgname"] = "CSWfoo_devel"
    self.pkg_data["pkginfo"]["ARCH"] = "all"
    self.error_mgr_mock.ReportError('archall-devel-package', None, None)

class TestCheckArchitectureVsContents_Devel_2(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureVsContents'
  def CheckpkgTest(self):
    self.pkg_data["binaries"] = []
    self.pkg_data["binaries_dump_info"] = []
    self.pkg_data["pkgmap"] = []
    self.pkg_data["basic_stats"]["pkgname"] = "CSWfoodev"
    self.pkg_data["pkginfo"]["ARCH"] = "all"
    self.error_mgr_mock.ReportError('archall-devel-package', None, None)

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
         'runpath': ('/opt/csw/lib/$ISALIST',
                     '/opt/csw/lib',
                     '/usr/lib/$ISALIST',
                     '/usr/lib',
                     '/lib/$ISALIST',
                     '/lib'),
         'soname': 'libImlib2.so.1',
         'soname_guessed': False,
    })
    # This no longer should throw an error.
    # self.error_mgr_mock.ReportError('linked-against-discouraged-library',
    #                                 'libImlib2.so.1.4.2 libX11.so.4')

class TestSetCheckSharedLibraryConsistency2_1(CheckpkgUnitTestHelper,
                                              unittest.TestCase):
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
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/doc').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/lib/sparcv9').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.ReportError(
        'CSWdjvulibrert', 'missing-dependency', u'CSWiconv')


class TestCheckPstamp(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckPstamp'
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["PSTAMP"] = "build8s20090904191054"
    self.error_mgr_mock.ReportError(
        'pkginfo-pstamp-in-wrong-format', 'build8s20090904191054',
        "It should be 'username@hostname-timestamp', but it's "
        "'build8s20090904191054'.")


class TestCheckRpath(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckRpath'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = tuple(testdata.rpaths.all_rpaths)
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    BAD_PATHS = [
        # Whether this is a valid rpath, is debatable.
        # '$ORIGIN/..',
        '$ORIGIN/../../../usr/lib/v9',
        '$ORIGIN/../../usr/lib',
        '$ORIGIN/../lib',
        '$ORIGIN/../ure-link/lib',
        '../../../../../dist/bin',
        '../../../../dist/bin',
        '../../../dist/bin',
        '../../dist/bin',
        '/bin',
        '/export/home/buysse/build/expect-5.42.1/cswstage/opt/csw/lib',
        '/export/home/phil/build/gettext-0.14.1/gettext-tools/intl/.libs',
        '/export/medusa/kenmays/build/qt-x11-free-3.3.3/lib',
        '/export/medusa/kenmays/build/s_qt/qt-x11-free-3.3.3/lib',
        '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/lib',
        '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/designer',
        '/export/medusa/kenmays/build/sparc_qt/qt-x11-free-3.3.4/plugins/sqldrivers',
        '/home/harpchad/local/sparc/lib',
        '/lib',
        '/lib/sparcv9',
        '/opt/SUNWcluster/lib',
        '/opt/SUNWmlib/lib',
        '/opt/SUNWspro/lib',
        '/opt/SUNWspro/lib/rw7',
        '/opt/SUNWspro/lib/stlport4',
        '/opt/SUNWspro/lib/v8',
        '/opt/SUNWspro/lib/v8plus',
        '/opt/SUNWspro/lib/v8plusa',
        '/opt/SUNWspro/lib/v8plusb',
        '/opt/SUNWspro/lib/v9',
        '/opt/build/michael/synce-0.8.9-buildroot/opt/csw/lib',
        '/opt/csw/$ISALIST',
        '/opt/csw//lib',
        '/opt/csw/X11/lib/',
        '/opt/csw/bdb4/lib/',
        '/opt/csw/lib/',
        '/opt/csw/lib/$',
        '/opt/csw/lib/$$ISALIST',
        '/opt/csw/lib/-R/opt/csw/lib',
        '/opt/csw/lib/\\$ISALIST',
        '/opt/csw/lib/\\SALIST',
        '/opt/csw/lib/sparcv8plus+vis',
        '/opt/csw/mysql4//lib/mysql',
        '/opt/csw/nagios/lib/\\$ISALIST',
        '/opt/csw/openoffice.org/basis3.1/program',
        '/opt/csw/openoffice.org/ure/lib',
        '/opt/cw/gcc3/lib',
        '/opt/forte8/SUNWspro/lib',
        '/opt/forte8/SUNWspro/lib/rw7',
        '/opt/forte8/SUNWspro/lib/rw7/v9',
        '/opt/forte8/SUNWspro/lib/v8',
        '/opt/forte8/SUNWspro/lib/v9',
        '/opt/schily/lib',
        '/opt/sfw/lib',
        '/opt/studio/SOS10/SUNWspro/lib',
        '/opt/studio/SOS10/SUNWspro/lib/rw7',
        '/opt/studio/SOS10/SUNWspro/lib/v8',
        '/opt/studio/SOS10/SUNWspro/lib/v8plus',
        '/opt/studio/SOS11/SUNWspro/lib',
        '/opt/studio/SOS11/SUNWspro/lib/rw7',
        '/opt/studio/SOS11/SUNWspro/lib/rw7/v9',
        '/opt/studio/SOS11/SUNWspro/lib/stlport4',
        '/opt/studio/SOS11/SUNWspro/lib/stlport4/v9',
        '/opt/studio/SOS11/SUNWspro/lib/v8',
        '/opt/studio/SOS11/SUNWspro/lib/v8plus',
        '/opt/studio/SOS11/SUNWspro/lib/v9',
        '/opt/studio/SOS8/SUNWspro/lib',
        '/opt/studio/SOS8/SUNWspro/lib/rw7',
        '/opt/studio/SOS8/SUNWspro/lib/rw7/v9',
        '/opt/studio/SOS8/SUNWspro/lib/v8',
        '/opt/studio/SOS8/SUNWspro/lib/v8plusa',
        '/opt/studio/SOS8/SUNWspro/lib/v9',
        '/opt/studio10/SUNWspro/lib',
        '/opt/studio10/SUNWspro/lib/rw7',
        '/opt/studio10/SUNWspro/lib/rw7/v9',
        '/opt/studio10/SUNWspro/lib/stlport4',
        '/opt/studio10/SUNWspro/lib/stlport4/v9',
        '/opt/studio10/SUNWspro/lib/v8',
        '/opt/studio10/SUNWspro/lib/v9',
        '/oracle/product/9.2.0/lib32',
        '/usr/X/lib',
        '/usr/local/lib',
        '/usr/local/openldap-2.3/lib',
        '/usr/sfw/lib',
        '/usr/ucblib',
        '/usr/xpg4/lib',
        'RIGIN/../lib',
    ]
    # Calculating the parameters on the fly, it allows to write it a terse manner.
    for bad_path in BAD_PATHS:
      self.error_mgr_mock.ReportError('bad-rpath-entry', '%s opt/csw/bin/sparcv8/rsync' % bad_path)


class TestCheckRpathBadPath(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ("/opt/csw/lib",)
    binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
    self.pkg_data["depends"] = (("CSWfoo", None),(u"CSWcommon", ""))
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
       u'/opt/csw/lib': [u'CSWfoo'],
       u'/opt/csw/lib/sparcv9': [u'CSWfoo'],
    })
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/man').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/doc').AndReturn(["CSWcommon"])
    self.error_mgr_mock.ReportError(
        'CSWrsync',
        'deprecated-library',
        u'opt/csw/bin/sparcv8/rsync Deprecated Berkeley DB location '
        u'/opt/csw/lib/libdb-4.7.so')
    self.pkg_data = [self.pkg_data]


class TestSetCheckLibmLinking(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ("/opt/csw/lib",)
    binaries_dump_info[0]["needed sonames"] = ["libm.so.2"]
    self.pkg_data["depends"] = ((u"CSWcommon", ""),)
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libm.so.2').AndReturn({
    })
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/man').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/doc').AndReturn(["CSWcommon"])
    # self.error_mgr_mock.ReportError(
    #     'CSWrsync',
    #     'deprecated-library',
    #     u'opt/csw/bin/sparcv8/rsync Deprecated Berkeley DB location '
    #     u'/opt/csw/lib/libdb-4.7.so')
    self.pkg_data = [self.pkg_data]


class TestRemovePackagesUnderInstallation(unittest.TestCase):

  def testRemoveNone(self):
    paths_and_pkgs_by_soname = {
        'libfoo.so.1': {u'/opt/csw/lib': [u'CSWlibfoo']}}
    packages_to_be_installed = [u'CSWbar']
    self.assertEqual(
        paths_and_pkgs_by_soname,
        pc.RemovePackagesUnderInstallation(paths_and_pkgs_by_soname,
                                           packages_to_be_installed))

  def testRemoveOne(self):
    paths_and_pkgs_by_soname = {
        'libfoo.so.1': {u'/opt/csw/lib': [u'CSWlibfoo']}}
    packages_to_be_installed = [u'CSWlibfoo']
    self.assertEqual(
        {'libfoo.so.1': {}},
        pc.RemovePackagesUnderInstallation(paths_and_pkgs_by_soname,
                                           packages_to_be_installed))


class TestSharedLibsInAnInstalledPackageToo(CheckpkgUnitTestHelper,
                                            unittest.TestCase):
  """If a shared library is provided by one of the packages that are in the set
  under test, take into account that the installed library will be removed at
  install time.

  The idea for the test:
    - Test two packages: CSWbar and CSWlibfoo
    - CSWbar depends on a library from libfoo
    - CSWlibfoo is installed
    - The new CSWlibfoo is broken and is missing the library
  """
  FUNCTION_NAME = 'SetCheckLibraries'
  # Contains only necessary bits.  The data listed in full.
  CSWbar_DATA = {
        'basic_stats': {'catalogname': 'bar',
                        'pkgname': 'CSWbar',
                        'stats_version': 1},
        'binaries_dump_info': [{'base_name': 'bar',
                                'needed sonames': ['libfoo.so.1'],
                                'path': 'opt/csw/bin/bar',
                                'runpath': ('/opt/csw/lib',),
                                # Making sonames optional, because they are.
                                # 'soname': 'rsync',
                                # 'soname_guessed': True
                                }],
        'depends': (('CSWlibfoo', None),),
        'isalist': (),
        'pkgmap': [],
        }
  CSWlibfoo_DATA = {
        'basic_stats': {'catalogname': 'libfoo',
                        'pkgname': 'CSWlibfoo',
                        'stats_version': 1},
        'binaries_dump_info': [],
        'depends': [],
        'isalist': (),
        'pkgmap': [],
      }
  def CheckpkgTest(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({
       u'/opt/csw/lib': [u'CSWlibfoo'],
    })
    self.error_mgr_mock.ReportError(
        'CSWbar',
        'soname-not-found',
        'libfoo.so.1 is needed by opt/csw/bin/bar')
    self.error_mgr_mock.ReportError('CSWbar', 'surplus-dependency', 'CSWlibfoo')
    self.pkg_data = [self.CSWbar_DATA, self.CSWlibfoo_DATA]


class TestSharedLibsOnlyIsalist(CheckpkgUnitTestHelper,
                                            unittest.TestCase):
  """/opt/csw/lib/$ISALIST in RPATH without the bare /opt/csw/lib."""
  FUNCTION_NAME = 'SetCheckLibraries'
  # Contains only necessary bits.  The data listed in full.
  CSWbar_DATA = {
        'basic_stats': {'catalogname': 'bar',
                        'pkgname': 'CSWbar',
                        'stats_version': 1},
        'binaries_dump_info': [
                               {'base_name': 'bar',
                                'needed sonames': ['libfoo.so.1'],
                                'path': 'opt/csw/bin/bar',
                                'runpath': ('/opt/csw/lib/$ISALIST',),
                               },
                               {'base_name': 'libfoo.so.1',
                                'needed sonames': (),
                                'path': 'opt/csw/lib/libfoo.so.1',
                                'runpath': ('/opt/csw/lib/$ISALIST',),
                               },
                              ],
        # 'depends': (),
        'depends': ((u"CSWcommon", ""),),
        'isalist': ('foo'),
        'pkgmap': [
          { 'path': '/opt/csw/lib/libfoo.so.1', },
          { 'path': '/opt/csw/bin/bar', },
                  ],
        }
  def CheckpkgTest(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn([u"CSWcommon"])
    self.pkg_data = [self.CSWbar_DATA]


class TestCheckLibrariesDlopenLibs_1(CheckpkgUnitTestHelper, unittest.TestCase):
  """For dlopen-style shared libraries, libraries from /opt/csw/lib should be
  counted as dependencies.  It's only a heuristic though."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ()
    binaries_dump_info[0]["needed sonames"] = ["libbar.so"]
    binaries_dump_info[0]["path"] = 'opt/csw/lib/python/site-packages/foo.so'
    self.pkg_data["depends"] = ((u"CSWcommon", "This one provides directories"),)
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libbar.so').AndReturn({
       u'/opt/csw/lib': [u'CSWlibbar'],
       u'/opt/csw/lib/sparcv9': [u'CSWlibbar'],
    })
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/man').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/doc').AndReturn(["CSWcommon"])
    self.error_mgr_mock.ReportError('CSWrsync', 'soname-not-found',
                                    'libbar.so is needed by '
                                    'opt/csw/lib/python/site-packages/foo.so')
    self.pkg_data = [self.pkg_data]


class TestCheckLibrariesDlopenLibs_2(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ()
    binaries_dump_info[0]["needed sonames"] = ["libnotfound.so"]
    binaries_dump_info[0]["path"] = 'opt/csw/lib/foo.so'
    self.pkg_data["depends"] = ((u"CSWcommon","This is needed"),)
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename(
        'libnotfound.so').AndReturn({})
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/man').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath(
        '/opt/csw/share/doc').AndReturn(["CSWcommon"])
    self.error_mgr_mock.ReportError(
        'CSWrsync', 'soname-not-found',
        'libnotfound.so is needed by opt/csw/lib/foo.so')
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


class TestCheckVendorURL_Https(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckVendorURL"
  def CheckpkgTest(self):
    self.pkg_data["pkginfo"]["VENDOR"] = "https://www.example.com/"


class TestCheckPythonPackageName(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckPythonPackageName"
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "",
      "mode": '0755',
      "path": "/opt/csw/lib/python/site-packages/hachoir_parser/video/mov.py",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError('pkgname-does-not-start-with-CSWpy-')
    self.error_mgr_mock.ReportError('catalogname-does-not-start-with-py_')


class TestCheckPythonPackageName_good(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckPythonPackageName"
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "",
      "mode": '0755',
      "path": "/opt/csw/lib/python/site-packages/hachoir_parser/video/mov.py",
      "type": "f",
      "user": "root"
    })
    self.pkg_data["basic_stats"]["catalogname"] = "py_foo"
    self.pkg_data["basic_stats"]["pkgname"] = "CSWpy-foo"


class TestCheckDisallowedPaths_1(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckDisallowedPaths"
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "doesn't matter here",
      "mode": '0755',
      "path": "/opt/csw/man",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
    self.error_mgr_mock.ReportError(
        'disallowed-path', 'opt/csw/man',
        'This path is already provided by CSWcommon '
        'or is not allowed for other reasons.')


class TestCheckDisallowedPaths_2(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckDisallowedPaths"
  def CheckpkgTest(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "doesn't matter here",
      "mode": '0755',
      "path": "/opt/csw/man/man1/foo.1",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
    self.error_mgr_mock.ReportError(
        'disallowed-path', 'opt/csw/man/man1/foo.1',
        'This path is already provided by CSWcommon '
        'or is not allowed for other reasons.')

class TestCheckArchitecture_sparcv8plus(CheckpkgUnitTestHelper,
                                        unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def CheckpkgTest(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 18,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/tree'},
       {'mime_type': 'text/troff; charset=us-ascii',
        'path': 'opt/csw/share/man/man1/tree.1'},
       {'mime_type': 'text/plain; charset=us-ascii',
        'path': 'opt/csw/share/doc/tree/license'}]
    self.error_mgr_mock.ReportError('binary-wrong-architecture',
                                    'id=18 name=sparcv8+ subdir=bin')


class TestCheckArchitecture_sparcv8plus(CheckpkgUnitTestHelper,
                                        unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def CheckpkgTest(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 18,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/sparcv8plus/tree'},
       ]


class TestCheckArchitecture_sparcv8(CheckpkgUnitTestHelper,
                                    unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def CheckpkgTest(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/tree'}]


class TestCheckArchitecture_LibSubdir(CheckpkgUnitTestHelper,
                                      unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def CheckpkgTest(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-sharedlib; charset=binary',
        'path': 'opt/csw/lib/foo/subdir/libfoo.so.1'}]


class TestCheckArchitecture_LibSubdirWrong(CheckpkgUnitTestHelper,
                                      unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def CheckpkgTest(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-sharedlib; charset=binary',
        'path': 'opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1'}]
    self.error_mgr_mock.ReportError(
        'binary-disallowed-placement',
        'file=opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1 '
        'arch_id=2 arch_name=sparcv8 bad_path=sparcv9')


class TestConflictingFiles(CheckpkgUnitTestHelper,
                           unittest.TestCase):
  """Throw an error if there's a conflicting file in the package set."""
  FUNCTION_NAME = 'SetCheckFileConflicts'
  # Contains only necessary bits.  The data listed in full.
  CSWbar_DATA = {
        'basic_stats': {'catalogname': 'bar',
                        'pkgname': 'CSWbar',
                        'stats_version': 1},
        'binaries_dump_info': [],
        'depends': tuple(),
        'isalist': [],
        'pkgmap': [
          {
            "type": "f",
            "path": "/opt/csw/share/foo",
          }
        ],
  }
  # This one has a conflicting file, this time it's a link, for a change.
  CSWfoo_DATA = {
        'basic_stats': {'catalogname': 'foo',
                        'pkgname': 'CSWfoo',
                        'stats_version': 1},
        'binaries_dump_info': [],
        'depends': tuple(),
        'isalist': [],
        'pkgmap': [
          {
            "type": "l",
            "path": "/opt/csw/share/foo",
          }
        ],
  }
  def CheckpkgTest(self):
    self.error_mgr_mock.ReportError(
        'CSWbar', 'file-conflict', '/opt/csw/share/foo CSWbar CSWfoo')
    self.error_mgr_mock.ReportError(
        'CSWfoo', 'file-conflict', '/opt/csw/share/foo CSWbar CSWfoo')
    self.pkg_data = [self.CSWbar_DATA, self.CSWfoo_DATA]


class TestSetCheckSharedLibraryConsistencyIvtools(CheckpkgUnitTestHelper,
                                                  unittest.TestCase):
  """This tests for a case in which the SONAME that we're looking for doesn't
  match the filename."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def CheckpkgTest(self):
    self.pkg_data = ivtools_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    # This may be enabled once checkpkg supports directory dependencies.
    # self.error_mgr_mock.ReportError('CSWivtools', 'missing-dependency', u'CSWcommon')


class TestSetCheckDirectoryDependencies(CheckpkgUnitTestHelper,
                                        unittest.TestCase):
  """Test whether appropriate files are provided."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDefault(self):
    # This test is disabled
    pass
  def CheckpkgTest(self):
    self.pkg_data = ivtools_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.ReportError('CSWivtools', 'missing-dependency', u'CSWcommon')


class TestSetCheckDirectoryDependenciesTree(CheckpkgUnitTestHelper,
                                        unittest.TestCase):
  """Test whether appropriate files are provided."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDefault(self):
    # This test is disabled
    pass
  def CheckpkgTest(self):
    self.pkg_data = tree_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
    })
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/man').AndReturn(
        [u'CSWgdbm', u'CSWlibnet', u'CSWbinutils', u'CSWtcpwrap',
          u'CSWenscript', u'CSWffcall', u'CSWflex', u'CSWfltk', u'CSWfping',
          u'CSWglib', u'CSWgmake', u'CSWgstreamer', u'CSWgtk', u'CSWgwhois',
          u'CSWbonobo2', u'CSWkrb5libdev', u'CSWksh', u'CSWlibgphoto2',
          u'CSWmikmod', u'CSWlibxine', u'CSWlsof', u'CSWngrep', u'CSWocaml',
          u'CSWpmmd5', u'CSWpmlclemktxtsimple', u'CSWpmtextdiff', u'CSWsasl',
          u'CSWpmprmsvldt', u'CSWpmmathinterpolate', u'CSWpmprmscheck',
          u'CSWrdist', u'CSWsbcl', u'CSWtetex', u'CSWnetcat', u'CSWjikes',
          u'CSWfoomaticfilters', u'CSWlibgnome', u'CSWexpect', u'CSWdejagnu',
          u'CSWnetpbm', u'CSWpmmailsendmail', u'CSWgnomedocutils', u'CSWnmap',
          u'CSWsetoolkit', u'CSWntop', u'CSWtransfig', u'CSWxmms',
          u'CSWpstoedit', u'CSWgdb', u'CSWschilybase', u'CSWschilyutils',
          u'CSWstar', u'CSWfindutils', u'CSWfakeroot', u'CSWautogen',
          u'CSWpmmimetools', u'CSWpmclsautouse', u'CSWpmlogmessage',
          u'CSWpmlogmsgsimple', u'CSWpmsvnsimple', u'CSWpmlistmoreut',
          u'CSWpmunivrequire', u'CSWpmiodigest', u'CSWpmsvnmirror',
          u'CSWpmhtmltmpl', u'CSWemacscommon', u'CSWcommon', u'CSWgnuplot',
          u'CSWpkgget', u'CSWsamefile', u'CSWpmnetdnsreslvprg',
          u'CSWpmx11protocol', u'CSWmono', u'CSWgstplugins',
          u'CSWgnomedesktop', u'CSWevince', u'CSWgedit', u'CSWfacter',
          u'CSWpmiopager', u'CSWxpm', u'CSWgawk', u'CSWpmcfginifls',
          u'CSWlibxft2', u'CSWpango', u'CSWgtk2', u'CSWpkgutil'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn( [u'CSWlibnet',
      u'CSWbinutils', u'CSWenscript', u'CSWflex', u'CSWfltk', u'CSWglib',
      u'CSWgmake', u'CSWgstreamer', u'CSWgtk', u'CSWgtkmmdevel', u'CSWgwhois',
      u'CSWbonobo2', u'CSWimlib', u'CSWjove', u'CSWkrb5libdev', u'CSWksh',
      u'CSWlibgphoto2', u'CSWmikmod', u'CSWlibxine', u'CSWlsof', u'CSWngrep',
      u'CSWtcl', u'CSWtk', u'CSWocaml', u'CSWpmlclemktxtsimple',
      u'CSWpmnetsnmp', u'CSWpstree', u'CSWqt', u'CSWrdist', u'CSWsbcl',
      u'CSWsdlsound', u'CSWt1lib', u'CSWtaglibgcc', u'CSWtetex', u'CSWcvs',
      u'CSWnetcat', u'CSWemacschooser', u'CSWhtmltidy', u'CSWgperf',
      u'CSWjikes', u'CSWfoomaticfilters', u'CSWlibgnome', u'CSWlibbonoboui',
      u'CSWexpect', u'CSWdejagnu', u'CSWnetpbm', u'CSWgnomedocutils',
      u'CSWmbrowse', u'CSWnmap', u'CSWsetoolkit', u'CSWntop', u'CSWtransfig',
      u'CSWisaexec', u'CSWguile', u'CSWlibxml', u'CSWxmms', u'CSWhevea',
      u'CSWopensp', u'CSWpstoedit', u'CSWlibdvdreaddevel', u'CSWvte',
      u'CSWgdb', u'CSWcryptopp', u'CSWschilybase', u'CSWschilyutils',
      u'CSWstar', u'CSWlatex2html', u'CSWfindutils', u'CSWfakeroot',
      u'CSWautogen', u'CSWlibotf', u'CSWlibotfdevel', u'CSWpmsvnmirror',
      u'CSWlibm17n', u'CSWm17ndb', u'CSWlibm17ndevel', u'CSWzope',
      u'CSWemacsbincommon', u'CSWemacs', u'CSWcommon', u'CSWgnuplot',
      u'CSWpkgget', u'CSWsamefile', u'CSWmono', u'CSWgstplugins',
      u'CSWgnomemenus', u'CSWgnomedesktop', u'CSWnautilus', u'CSWevince',
      u'CSWggv', u'CSWgedit', u'CSWlibofx', u'CSWfacter', u'CSWxpm',
      u'CSWgawk', u'CSWlibxft2', u'CSWpango', u'CSWgtk2', u'CSWpkgutil',
      u'CSWlibgegl'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/doc').AndReturn(
      [u'CSWcairomm', u'CSWtcpwrap', u'CSWfltk', u'CSWgsfonts',
        u'CSWlibsigc++rt', u'CSWglibmmdevel', u'CSWgstreamer', u'CSWgtkmm2',
        u'CSWksh', u'CSWlibgphoto2', u'CSWlibxine', u'CSWmeanwhile',
        u'CSWsasl', u'CSWsbcl', u'CSWsilctoolkit', u'CSWt1lib',
        u'CSWtaglibgcc', u'CSWtetex', u'CSWgperf', u'CSWjikes', u'CSWlibgnome',
        u'CSWdejagnu', u'CSWnetpbm', u'CSWlibgnomeui', u'CSWsetoolkit',
        u'CSWgtksourceview', u'CSWhevea', u'CSWopensprt', u'CSWopensp',
        u'CSWplotutilrt', u'CSWplotutildevel', u'CSWpstoeditrt',
        u'CSWpstoedit', u'CSWpstoeditdevel', u'CSWopenspdevel',
        u'CSWlibdvdread', u'CSWlibdvdreaddevel', u'CSWschilyutils', u'CSWstar',
        u'CSWautogenrt', u'CSWlatex2html', u'CSWautogen', u'CSWlibotf',
        u'CSWlibotfdevel', u'CSWgcc3corert', u'CSWgcc3g++rt', u'CSWlibofxrt',
        u'CSWgcc3adart', u'CSWgcc3rt', u'CSWgcc3g++', u'CSWgcc3ada',
        u'CSWgcc3', u'CSWlibm17n', u'CSWm17ndb', u'CSWlibm17ndevel',
        u'CSWgcc2core', u'CSWgcc2g++', u'CSWgcc3g77rt', u'CSWgcc3g77',
        u'CSWgcc4g95', u'CSWemacscommon', u'CSWemacsbincommon', u'CSWemacs',
        u'CSWcommon', u'CSWbashcmplt', u'CSWcacertificates', u'CSWgstplugins',
        u'CSWgnomemenus', u'CSWgnomedesktop', u'CSWnautilus', u'CSWlibofx',
        u'CSWgamin', u'CSWpkgutil', u'CSWgcc3core', u'CSWgnomemime2'])


class TestCheckDiscouragedFileNamePatterns(CheckpkgUnitTestHelper,
                                           unittest.TestCase):
  """Throw an error if there's a conflicting file in the package set."""
  FUNCTION_NAME = 'CheckDiscouragedFileNamePatterns'
  CSWfoo_DATA = {
        'basic_stats': {'catalogname': 'foo',
                        'pkgname': 'CSWfoo',
                        'stats_version': 1},
        'binaries_dump_info': [],
        'depends': tuple(),
        'isalist': [],
        'pkgmap': [
          { "type": "d", "path": "/opt/csw/var", },
          { "type": "d", "path": "/opt/csw/bin", },
        ],
  }
  def CheckpkgTest(self):
    self.pkg_data = self.CSWfoo_DATA
    self.error_mgr_mock.ReportError(
        'discouraged-path-in-pkgmap', '/opt/csw/var')


class TestSetCheckDirectoryDepsTwoPackages(CheckpkgUnitTestHelper,
                                           unittest.TestCase):
  """Test whether appropriate files are provided.
  
  This is a stupid test and can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDefault(self):
    # This test is disabled
    pass
  def CheckpkgTest(self):
    self.pkg_data = sudo_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdl.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn({
      "/opt/csw/lib": (u"CSWggettextrt",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpam.so.1').AndReturn({
      "/usr/dt/lib": (u"SUNWdtbas",),
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),
    })
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),
    })
    common_path_pkgs = [u'CSWgdbm', u'CSWbinutils', u'CSWcommon']
    paths_to_check = [
        '/opt/csw/share/man', '/opt/csw/bin', '/opt/csw/share', '/var/opt/csw',
        '/opt/csw/etc', '/opt/csw/sbin', '/opt/csw', '/opt/csw/share/doc']
    for path in paths_to_check:
      self.error_mgr_mock.GetPkgByPath(path).AndReturn(common_path_pkgs)
    self.error_mgr_mock.ReportError('CSWsudo', 'surplus-dependency', 'CSWalternatives')
    self.error_mgr_mock.ReportError('CSWsudo', 'surplus-dependency', 'CSWsudo-common')


class TestSetCheckDirectoryDepsMissing(CheckpkgUnitTestHelper,
                                           unittest.TestCase):
  """Test whether appropriate files are provided.

  This is a stupid test and can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDefault(self):
    # This test is disabled
    pass
  def CheckpkgTest(self):
    self.pkg_data = sudo_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdl.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn({
      "/opt/csw/lib": (u"CSWggettextrt",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpam.so.1').AndReturn({
      "/usr/dt/lib": (u"SUNWdtbas",),
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),
    })
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),
    })
    common_path_pkgs = [u'CSWgdbm', u'CSWbinutils', u'CSWcommon']
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/man').AndReturn([])
    paths_to_check = [
        '/opt/csw/bin', '/opt/csw/share', '/var/opt/csw',
        '/opt/csw/etc', '/opt/csw/sbin', '/opt/csw', '/opt/csw/share/doc']
    for path in paths_to_check:
      self.error_mgr_mock.GetPkgByPath(path).AndReturn(common_path_pkgs)
    # This is the critical test here.
    self.error_mgr_mock.ReportError('CSWsudo-common', 'base-dir-not-found', '/opt/csw/share/man')
    self.error_mgr_mock.ReportError('CSWsudo', 'surplus-dependency', 'CSWalternatives')
    self.error_mgr_mock.ReportError('CSWsudo', 'surplus-dependency', 'CSWsudo-common')


class TestSetCheckDoubleDepends(CheckpkgUnitTestHelper, unittest.TestCase):
  """This is a class that was used for debugging.

  It can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'

  def SetMessenger(self):
    self.messenger = self.mocker.CreateMock(stubs.MessengerStub)

  def CheckpkgTest(self):
    self.pkg_data = javasvn_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCrun.so.1').AndReturn({u'/usr/lib': [u'SUNWlibC'], u'/usr/lib/sparcv9': [u'SUNWlibCx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCstd.so.1').AndReturn({u'/usr/lib': [u'SUNWlibC'], u'/usr/lib/sparcv9': [u'SUNWlibCx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libapr-1.so.0').AndReturn({u'/opt/csw/apache2/lib': [u'CSWapache2rt'], u'/opt/csw/lib': [u'CSWapr'], u'/opt/csw/lib/sparcv9': [u'CSWapr']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libaprutil-1.so.0').AndReturn({u'/opt/csw/apache2/lib': [u'CSWapache2rt']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/libp/sparcv9': [u'SUNWdplx'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdl.so.1').AndReturn({u'/etc/lib': [u'SUNWcsr'], u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libexpat.so.1').AndReturn({u'/opt/csw/lib': [u'CSWexpat'], u'/opt/csw/lib/sparcv9': [u'CSWexpat']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libiconv.so.2').AndReturn({u'/opt/csw/lib': [u'CSWiconv'], u'/opt/csw/lib/sparcv9': [u'CSWiconv']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn({u'/opt/csw/lib': [u'CSWggettextrt'], u'/opt/csw/lib/sparcv9': [u'CSWggettextrt']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('liblber-2.4.so.2').AndReturn({u'/opt/csw/lib': [u'CSWoldaprt'], u'/opt/csw/lib/sparcv9': [u'CSWoldaprt']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libldap-2.4.so.2').AndReturn({u'/opt/csw/lib': [u'CSWoldaprt'], u'/opt/csw/lib/sparcv9': [u'CSWoldaprt']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libneon.so.27').AndReturn({u'/opt/csw/lib': [u'CSWneon'], u'/opt/csw/lib/sparcv9': [u'CSWneon']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpthread.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('librt.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsendfile.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_client-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_delta-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_diff-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_fs-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_ra-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_repos-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_subr-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_wc-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libuuid.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/sparcv9': [u'SUNWcslx']})

    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u'CSWgdbm',
      u'CSWlibnet', u'CSWbinutils', u'CSWcairomm', u'CSWtcpwrap',
      u'CSWkrb5lib', u'CSWffcall', u'CSWflex', u'CSWfreeglut',
      u'CSWgcc2corert', u'CSWgcc2g++rt', u'CSWgstreamer', u'CSWgtk',
      u'CSWgtkspell', u'CSWimlib', u'CSWjove', u'CSWksh', u'CSWlibgphoto2',
      u'CSWmikmod', u'CSWlibsigsegv', u'CSWlibxine', u'CSWmeanwhile',
      u'CSWtcl', u'CSWtk', u'CSWocaml', u'CSWpmmd5', u'CSWpmlclemktxtsimple',
      u'CSWpmtextdiff', u'CSWsasl', u'CSWpmmathinterpolate', u'CSWpmprmscheck',
      u'CSWsbcl', u'CSWsdlsound', u'CSWsdlttf', u'CSWsilctoolkit', u'CSWt1lib',
      u'CSWtaglibgcc', u'CSWtetex', u'CSWimaprt', u'CSWimap-devel',
      u'CSWgnomevfs2', u'CSWlibgnomecups', u'CSWlibgnomeprint',
      u'CSWlibgnomeprintui', u'CSWlibgsf', u'CSWhtmltidy',
      u'CSWfoomaticfilters', u'CSWexpect', u'CSWnetpbm', u'CSWpmmailsendmail',
      u'CSWgnomedocutils', u'CSWguilelib12', u'CSWlibgadu', u'CSWsetoolkit',
      u'CSWntop', u'CSWtransfig', u'CSWsdlnet', u'CSWguile', u'CSWlibxml',
      u'CSWxmms', u'CSWhevea', u'CSWopensprt', u'CSWplotutilrt',
      u'CSWplotutildevel', u'CSWpstoeditrt', u'CSWpstoeditdevel',
      u'CSWopenspdevel', u'CSWlibdvdread', u'CSWlibdvdreaddevel', u'CSWvte',
      u'CSWcryptopp', u'CSWschilybase', u'CSWautogenrt', u'CSWlatex2html',
      u'CSWfindutils', u'CSWfakeroot', u'CSWautogen', u'CSWpmmimetools',
      u'CSWlibotf', u'CSWlibotfdevel', u'CSWgcc3corert', u'CSWgcc3g++rt',
      u'CSWlibofxrt', u'CSWgcc3adart', u'CSWpmclsautouse', u'CSWpmlogmessage',
      u'CSWpmlogmsgsimple', u'CSWpmsvnsimple', u'CSWpmunivrequire',
      u'CSWpmiodigest', u'CSWpmsvnmirror', u'CSWlibm17n', u'CSWlibm17ndevel',
      u'CSWzope', u'CSWpmhtmltmpl', u'CSWgcc3g77rt', u'CSWcommon',
      u'CSWgnuplot', u'CSWpmx11protocol', u'CSWx11sshaskp', u'CSWmono',
      u'CSWlibwnck', u'CSWgstplugins', u'CSWgnomemenus', u'CSWgnomedesktop',
      u'CSWeel', u'CSWnautilus', u'CSWevince', u'CSWggv', u'CSWfacter',
      u'CSWpmiopager', u'CSWxpm', u'CSWpmcfginifls', u'CSWlibxft2',
      u'CSWpango', u'CSWgtk2', u'CSWgamin', u'CSWgcc3core', u'CSWlibbabl',
      u'CSWgtkengines', u'CSWglib', u'CSWbonobo2', u'CSWlibgnomecanvas',
      u'CSWgtksourceview', u'CSWgedit', u'CSWlibgnome', u'CSWlibbonoboui',
      u'CSWlibgnomeui', u'CSWlibgegl'])

    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/doc').AndReturn([u'CSWcairomm',
      u'CSWtcpwrap', u'CSWgsfonts', u'CSWgstreamer', u'CSWksh',
      u'CSWlibgphoto2', u'CSWlibxine', u'CSWmeanwhile', u'CSWsasl', u'CSWsbcl',
      u'CSWsilctoolkit', u'CSWt1lib', u'CSWtaglibgcc', u'CSWtetex',
      u'CSWgperf', u'CSWjikes', u'CSWdejagnu', u'CSWnetpbm', u'CSWsetoolkit',
      u'CSWhevea', u'CSWopensprt', u'CSWopensp', u'CSWplotutilrt',
      u'CSWplotutildevel', u'CSWpstoeditrt', u'CSWpstoedit',
      u'CSWpstoeditdevel', u'CSWopenspdevel', u'CSWlibdvdread',
      u'CSWlibdvdreaddevel', u'CSWschilyutils', u'CSWstar', u'CSWautogenrt',
      u'CSWlatex2html', u'CSWautogen', u'CSWlibotf', u'CSWlibotfdevel',
      u'CSWgcc3corert', u'CSWgcc3g++rt', u'CSWlibofxrt', u'CSWgcc3adart',
      u'CSWgcc3rt', u'CSWgcc3g++', u'CSWgcc3ada', u'CSWgcc3', u'CSWlibm17n',
      u'CSWm17ndb', u'CSWlibm17ndevel', u'CSWgcc2core', u'CSWgcc2g++',
      u'CSWgcc3g77rt', u'CSWgcc3g77', u'CSWgcc4g95', u'CSWemacscommon',
      u'CSWemacsbincommon', u'CSWemacs', u'CSWcommon', u'CSWbashcmplt',
      u'CSWcacertificates', u'CSWgstplugins', u'CSWgnomemenus',
      u'CSWgnomedesktop', u'CSWnautilus', u'CSWlibofx', u'CSWgamin',
      u'CSWpkgutil', u'CSWgcc3core', u'CSWgnomemime2', u'CSWglib'])

    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWneon')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWapache2rt')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWoldaprt')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWggettextrt')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWapache2rt or CSWapr')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWexpat')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWsvn')
    self.error_mgr_mock.ReportError('CSWjavasvn', 'missing-dependency', u'CSWiconv')
    self.messenger.Message(u'Dependency issues of CSWjavasvn:')
    self.messenger.Message(u'CSWapache2rt, reasons:')
    self.messenger.Message(u' - provides /opt/csw/apache2/lib/libaprutil-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - provides /opt/csw/apache2/lib/libapr-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWapache2rt')
    # Here's the debugged and fixed duplicated dependency report.
    # self.messenger.Message(u'CSWapache2rt, reasons:')
    # self.messenger.Message(u' - provides /opt/csw/apache2/lib/libaprutil-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    # self.messenger.Message(u' - provides /opt/csw/apache2/lib/libapr-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    # self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWapache2rt')
    self.messenger.Message(u'CSWapr, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libapr-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWapr')
    self.messenger.Message(u'CSWexpat, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libexpat.so.1 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWexpat')
    self.messenger.Message(u'CSWggettextrt, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libintl.so.8 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWggettextrt')
    self.messenger.Message(u'CSWiconv, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libiconv.so.2 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWiconv')
    self.messenger.Message(u'CSWneon, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libneon.so.27 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWneon')
    self.messenger.Message(u'CSWoldaprt, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/libldap-2.4.so.2 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - provides /opt/csw/lib/liblber-2.4.so.2 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWoldaprt')
    self.messenger.Message(u'CSWsvn, reasons:')
    self.messenger.Message(u' - provides /opt/csw/lib/svn/libsvn_repos-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - provides /opt/csw/lib/svn/libsvn_client-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - provides /opt/csw/lib/svn/libsvn_wc-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - provides /opt/csw/lib/svn/libsvn_ra-1.so.0 needed by opt/csw/lib/svn/libsvnjavahl-1.so.0.0.0')
    self.messenger.Message(u' - ...and more.')
    self.messenger.Message(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWsvn')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWneon')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWapache2rt')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWoldaprt')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWggettextrt')
    self.messenger.SuggestGarLine('# One of the following:')
    self.messenger.SuggestGarLine(u'  RUNTIME_DEP_PKGS_CSWjavasvn += CSWapache2rt')
    self.messenger.SuggestGarLine(u'  RUNTIME_DEP_PKGS_CSWjavasvn += CSWapr')
    self.messenger.SuggestGarLine('# (end of the list of alternative dependencies)')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWexpat')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWsvn')
    self.messenger.SuggestGarLine(u'RUNTIME_DEP_PKGS_CSWjavasvn += CSWiconv')


class TestCheckWrongArchitecture(CheckpkgUnitTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckWrongArchitecture'
  def CheckpkgTest(self):
    self.pkg_data = neon_stats[0]
    self.error_mgr_mock.ReportError(
        'binary-wrong-architecture',
        'file=opt/csw/lib/sparcv9/libneon.so.27.2.0 pkginfo-says=i386 actual-binary=sparc')
    self.error_mgr_mock.ReportError(
        'binary-wrong-architecture',
        'file=opt/csw/lib/sparcv9/libneon.so.26.0.4 pkginfo-says=i386 actual-binary=sparc')


if __name__ == '__main__':
  unittest.main()
