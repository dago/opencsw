#!/usr/bin/env python2.6
# coding=utf-8
# $Id$

import copy
import datetime
import unittest
import package_checks as pc
import checkpkg
import checkpkg_lib
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
from testdata.bdb48_stats import pkgstat_objs as bdb48_stats
from testdata.mercurial_stats import pkgstat_objs as mercurial_stats
from testdata import stubs

DEFAULT_PKG_STATS = None
DEFAULT_PKG_DATA = rsync_stats[0]


class CheckTestHelper(object):

  def setUp(self):
    super(CheckTestHelper, self).setUp()
    self.mox = mox.Mox()
    self.pkg_data = copy.deepcopy(DEFAULT_PKG_DATA)
    self.logger_mock = stubs.LoggerStub()
    self.SetMessenger()
    if self.FUNCTION_NAME.startswith("Set"):
      self.error_mgr_mock = self.mox.CreateMock(
          checkpkg_lib.SetCheckInterface)
    else:
      self.error_mgr_mock = self.mox.CreateMock(
          checkpkg_lib.IndividualCheckInterface)
    self.mox.ResetAll()

  def SetMessenger(self):
    """To be overridden in subclasses if needed."""
    self.messenger = stubs.MessengerStub()

  def tearDown(self):
    super(CheckTestHelper, self).tearDown()
    self.mox.ReplayAll()
    function_under_test = getattr(pc, self.FUNCTION_NAME)
    function_under_test(self.pkg_data, self.error_mgr_mock,
                        self.logger_mock, self.messenger)
    self.mox.VerifyAll()


class TestMultipleDepends(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckMultipleDepends'
  def testMultipleDependency(self):
    self.pkg_data["depends"].append(("CSWcommon", "This is surplus"))
    self.error_mgr_mock.ReportError('dependency-listed-more-than-once',
                                    'CSWcommon')


class TestDescription(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDescription'
  def testMissingDescription(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo'
    self.error_mgr_mock.ReportError('pkginfo-description-missing')

  def testLongDescription(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - ' + ('A' * 200)
    self.error_mgr_mock.ReportError('pkginfo-description-too-long', 'length=200')

  def testUppercaseDescription(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - lowercase'
    self.error_mgr_mock.ReportError(
        'pkginfo-description-not-starting-with-uppercase', 'lowercase')


class TestCheckEmailGood(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckEmail'
  def testGoodEmail(self):
    self.pkg_data["pkginfo"]["EMAIL"] = 'somebody@opencsw.org'

  def testBadDomain(self):
    self.pkg_data["pkginfo"]["EMAIL"] = 'somebody@opencsw.com'
    self.error_mgr_mock.ReportError(
        'pkginfo-email-not-opencsw-org', 'email=somebody@opencsw.com')


class TestCheckCatalogname(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckCatalogname'
  def testPkginfoAndFileDisagreement(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - foo'
    self.pkg_data["basic_stats"]["catalogname"] = "bar"
    self.error_mgr_mock.ReportError('pkginfo-catalogname-disagreement pkginfo=foo filename=bar')

  def testWithDash(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo-bar - This catalog name is bad'
    self.pkg_data["basic_stats"]["catalogname"] = "foo-bar"
    self.error_mgr_mock.ReportError('pkginfo-bad-catalogname', 'foo-bar')

  def testGoodComplex(self):
    self.pkg_data["pkginfo"]["NAME"] = (u'libsigc++_devel - '
                                        u'This catalog name is good')
    self.pkg_data["basic_stats"]["catalogname"] = u"libsigc++_devel"

  def testUppercase(self):
    self.pkg_data["pkginfo"]["NAME"] = 'Foo - This catalog name is bad'
    self.pkg_data["basic_stats"]["catalogname"] = "Foo"
    self.error_mgr_mock.ReportError('catalogname-not-lowercase')

  def testLowercase(self):
    self.pkg_data["pkginfo"]["NAME"] = 'foo - This catalog name is good'
    self.pkg_data["basic_stats"]["catalogname"] = "foo"

  def testBadCharacters(self):
    self.pkg_data["basic_stats"]["catalogname"] = "foo+abc&123"
    self.pkg_data["pkginfo"]["NAME"] = 'foo+abc&123 - This catalog name is bad'
    self.error_mgr_mock.ReportError('pkginfo-bad-catalogname', 'foo+abc&123')


class TestCheckSmfIntegrationBad(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSmfIntegration'
  def testMissingSmfClass(self):
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

  def testSmfIntegrationGood(self):
    self.pkg_data["pkgmap"].append({
      "class": "cswinitsmf",
      "group": "bin",
      "line": "1 f none /opt/csw/etc/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/etc/opt/csw/init.d/foo",
      "type": "f",
      "user": "root"
    })

  def testWrongLocation(self):
    self.pkg_data["pkgmap"].append({
      "class": "cswinitsmf",
      "group": "bin",
      "line": "1 f none /etc/opt/csw/init.d/foo 0644 root bin 36372 24688 1266395027",
      "mode": '0755',
      "path": "/opt/csw/etc/init.d/foo",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError('init-file-wrong-location',
                                    '/opt/csw/etc/init.d/foo')



class TestSetCheckDependencies(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckDependencies'
  def testUnidentifiedDependency(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    self.pkg_data[0]["depends"].append(["CSWmartian", "A package from Mars."])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)
    self.error_mgr_mock.ReportError(
        'CSWrsync', 'unidentified-dependency', 'CSWmartian')

  def testInterface(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)

  def testTwoPackagesBad(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single, copy.deepcopy(self.pkg_data_single)]
    self.pkg_data[1]["basic_stats"]["pkgname"] = "CSWsecondpackage"
    self.pkg_data[1]["depends"].append(["CSWmartian", ""])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)
    self.error_mgr_mock.ReportError(
        'CSWsecondpackage', 'unidentified-dependency', 'CSWmartian')

  def testTwoPackagesGood(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single, copy.deepcopy(self.pkg_data_single)]
    self.pkg_data[1]["basic_stats"]["pkgname"] = "CSWsecondpackage"
    self.pkg_data[1]["depends"].append(["CSWrsync", ""])
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)

class TestSetCheckDependencies(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckDependsOnSelf'
  def testDependencyOnSelf(self):
    self.pkg_data["depends"].append(("CSWrsync", ""))
    installed = ["CSWcommon", "CSWisaexec", "CSWiconv", "CSWlibpopt"]
    # self.error_mgr_mock.GetInstalledPackages().AndReturn(installed)
    self.error_mgr_mock.ReportError('depends-on-self')


class DatabaseMockingMixin(object):

  def MockDbInteraction(self):
    # Mocking out the interaction with the database
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libiconv.so.2').AndReturn({
      "/opt/csw/lib": (u"CSWlibiconv",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpopt.so.0').AndReturn({
      "/opt/csw/lib": (u"CSWlibpopt",)})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsec.so.1').AndReturn({
      "/usr/lib": (u"SUNWfoo",),
      "/usr/lib/sparcv9": (u"SUNWfoo"),})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
      "/usr/lib": (u"SUNWcsl",),
      "/usr/lib/sparcv9": (u"SUNWcslx"),})
    common_path_pkgs = [u'CSWgdbm', u'CSWbinutils', u'CSWcommon']
    paths_to_check = [
        '/opt/csw/share/man', '/opt/csw/bin', '/opt/csw/bin/sparcv8',
        '/opt/csw/bin/sparcv9', '/opt/csw/share/doc']
    for pth in paths_to_check:
      self.error_mgr_mock.GetPkgByPath(pth).AndReturn(common_path_pkgs)


class TestSetCheckDependenciesWithDb(
    DatabaseMockingMixin, CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDoNotReportSurplusForDev(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    self.pkg_data[0]["basic_stats"]["pkgname"] = "CSWfoo-dev"
    self.pkg_data[0]["depends"].append(["CSWfoo", ""])
    self.pkg_data[0]["depends"].append(["CSWbar", ""])
    self.pkg_data[0]["depends"].append(["CSWlibiconv", ""])
    self.MockDbInteraction()
    for i in range(12):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.IsA(str), mox.IsA(str))
    # There should be no error about the dependency on CSWfoo or CSWbar.

  def testReportDeps(self):
    self.pkg_data_single = self.pkg_data
    self.pkg_data = [self.pkg_data_single]
    self.MockDbInteraction()
    for i in range(12):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.IsA(str), mox.IsA(str))


class TestCheckArchitectureSanity(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureSanity'
  def testSimple(self):
    self.pkg_data["pkginfo"]["ARCH"] = "i386"
    self.error_mgr_mock.ReportError(
        'srv4-filename-architecture-mismatch',
        'pkginfo=i386 filename=rsync-3.0.7,REV=2010.02.17-SunOS5.8-sparc-CSW.pkg.gz')

class TestCheckArchitectureVsContents(CheckTestHelper, unittest.TestCase):

  FUNCTION_NAME = 'CheckArchitectureVsContents'
  def testArchallDevel(self):
    self.pkg_data["binaries"] = []
    self.pkg_data["binaries_dump_info"] = []
    self.pkg_data["pkgmap"] = []
    self.pkg_data["basic_stats"]["pkgname"] = "CSWfoo_devel"
    self.pkg_data["pkginfo"]["ARCH"] = "all"
    self.error_mgr_mock.ReportError('archall-devel-package', None, None)

  def testArchitectureVsContents(self):
    self.pkg_data["binaries"] = []
    self.pkg_data["binaries_dump_info"] = []
    self.pkg_data["pkgmap"] = []
    self.pkg_data["basic_stats"]["pkgname"] = "CSWfoodev"
    self.pkg_data["pkginfo"]["ARCH"] = "all"
    self.error_mgr_mock.ReportError('archall-devel-package', None, None)


class TestCheckFileNameSanity(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckFileNameSanity'
  def testMissingRevision(self):
    del(self.pkg_data["basic_stats"]["parsed_basename"]["revision_info"]["REV"])
    self.error_mgr_mock.ReportError('rev-tag-missing-in-filename')


class TestCheckLinkingAgainstSunX11(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckLinkingAgainstSunX11'
  def testAllowLinkingAgainstSunX11(self):
    self.pkg_data["binaries_dump_info"][0]["needed sonames"].append("libX11.so.4")
    # No errors reported here.

  def testDoNotReportDiscouragedLib(self):
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


class TestSetCheckLibraries(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def testInterface(self):
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
    for i in range(38):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.IsA(unicode), mox.IsA(str))


class TestCheckPstamp(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckPstamp'
  def testPstampRegex(self):
    self.pkg_data["pkginfo"]["PSTAMP"] = "build8s20090904191054"
    self.error_mgr_mock.ReportError(
        'pkginfo-pstamp-in-wrong-format', 'build8s20090904191054',
        "It should be 'username@hostname-timestamp', but it's "
        "'build8s20090904191054'.")


class TestCheckRpath(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckRpath'
  def testRpathList(self):
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
      self.error_mgr_mock.ReportError(
          'bad-rpath-entry', '%s opt/csw/bin/sparcv8/rsync' % bad_path)

class TestCheckLibraries(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def testDeprecatedLibrary(self):
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
    self.error_mgr_mock.NeedFile('CSWrsync', u'/opt/csw/lib/libdb-4.7.so',
        'opt/csw/bin/sparcv8/rsync needs the libdb-4.7.so soname')
    self.error_mgr_mock.ReportError(
        'CSWrsync',
        'deprecated-library',
        mox.IsA(unicode))
    self.pkg_data = [self.pkg_data]

  def testDeprecatedLibrary(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ("/opt/csw/bdb47/lib", "/opt/csw/lib",)
    binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
    self.pkg_data["depends"] = (("CSWbad", None),(u"CSWcommon", ""))
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
       u'/opt/csw/bdb47/lib':         [u'CSWbad'],
       u'/opt/csw/bdb47lib/sparcv9': [u'CSWbad'],
       u'/opt/csw/lib':               [u'CSWgood'],
       u'/opt/csw/lib/sparcv9':       [u'CSWgood'],
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
    # There should be no error here, since /opt/csw/bdb47/lib is first in the RPATH.
    self.pkg_data = [self.pkg_data]
    for i in range(2):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))

  def testBadRpath(self):
    binaries_dump_info = self.pkg_data["binaries_dump_info"]
    binaries_dump_info[0]["runpath"] = ("/opt/csw/lib", "/opt/csw/bdb47/lib",)
    binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
    self.pkg_data["depends"] = (("CSWbad", None),(u"CSWcommon", ""))
    self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
       u'/opt/csw/bdb47/lib':         [u'CSWbad'],
       u'/opt/csw/bdb47lib/sparcv9': [u'CSWbad'],
       u'/opt/csw/lib':               [u'CSWgood'],
       u'/opt/csw/lib/sparcv9':       [u'CSWgood'],
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
    for i in range(1):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))
    self.error_mgr_mock.ReportError(
        'CSWrsync',
        'deprecated-library',
        u'file=opt/csw/bin/sparcv8/rsync '
        u'lib=/opt/csw/lib/libdb-4.7.so')
    self.pkg_data = [self.pkg_data]
    for i in range(1):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))

class TestLibmLinking(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'SetCheckLibraries'
  def testLibmLinking(self):
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
    self.pkg_data = [self.pkg_data]


class TestSharedLibsInAnInstalledPackageToo(CheckTestHelper,
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

  def testMissingLibFromNewPackage(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({
       u'/opt/csw/lib': [u'CSWlibfoo'],
    })
    self.error_mgr_mock.ReportError(
        'CSWbar',
        'soname-not-found',
        'libfoo.so.1 is needed by opt/csw/bin/bar')
    self.pkg_data = [self.CSWbar_DATA, self.CSWlibfoo_DATA]


class TestSharedLibsOnlyIsalist(CheckTestHelper, unittest.TestCase):
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
  def testInterface(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.NeedFile('CSWbar', '/opt/csw/lib/libfoo.so.1',
        'opt/csw/bin/bar needs the libfoo.so.1 soname')
    self.pkg_data = [self.CSWbar_DATA]


class TestCheckLibrariesDlopenLibs_1(CheckTestHelper, unittest.TestCase):
  """For dlopen-style shared libraries, libraries from /opt/csw/lib should be
  counted as dependencies.  It's only a heuristic though."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def testMissingLibbar(self):
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

  def testLibNotFound(self):
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


class TestCheckVendorURL(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckVendorURL"
  def testBadUrl(self):
    # Injecting the data to be examined.
    self.pkg_data["pkginfo"]["VENDOR"] = "badurl"
    # Expecting the following method to be called.
    self.error_mgr_mock.ReportError(
        "pkginfo-bad-vendorurl",
        "badurl",
        "Solution: add VENDOR_URL to GAR Recipe")

  def testGoodUrl(self):
    self.pkg_data["pkginfo"]["VENDOR"] = "http://www.example.com/"
    # No call to error_mgr_mock means that no errors should be reported: the
    # URL is okay.

  def testHttps(self):
    self.pkg_data["pkginfo"]["VENDOR"] = "https://www.example.com/"


class TestCheckPythonPackageName(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckPythonPackageName"
  def testBad(self):
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

  def testGood(self):
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


class TestCheckDisallowedPaths(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckDisallowedPaths"
  def testManDir(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "doesn't matter here",
      "mode": '0755',
      "path": "/opt/csw/man",
      "type": "d",
      "user": "root"
    })
    self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
    self.error_mgr_mock.ReportError(
        'disallowed-path', 'opt/csw/man',
        'This path is already provided by CSWcommon '
        'or is not allowed for other reasons.')

  def testManFile(self):
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


class TestCheckGzippedManpages(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckGzippedManpages"
  def testGzippedManpageBad(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "",
      "mode": '0755',
      "path": "/opt/csw/share/man/man5/puppet.conf.5.gz",
      "type": "f",
      "user": "root"
    })
    self.error_mgr_mock.ReportError(
      'gzipped-manpage-in-pkgmap', '/opt/csw/share/man/man5/puppet.conf.5.gz',
      "Solaris' man cannot automatically inflate man pages. "
      "Solution: man page should be gunzipped.")

  def testUncompressedManpage(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "",
      "mode": '0755',
      "path": "/opt/csw/share/man/man5/puppet.conf.5",
      "type": "f",
      "user": "root"
    })

  # Although this is a gzipped manpage, it is not in a directory associated with
  # manpages, so we should not trigger an error here.
  def testGzippedFileGood(self):
    self.pkg_data["pkgmap"].append({
      "class": "none",
      "group": "bin",
      "line": "",
      "mode": '0755',
      "path": "/etc/opt/csw/puppet/puppet.conf.5.gz",
      "type": "f",
      "user": "root"
    })


class TestCheckArchitecture(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def testBadSparcv8Plus(self):
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
    self.error_mgr_mock.ReportError(
        'binary-architecture-does-not-match-placement',
        'file=opt/csw/bin/tree arch_id=18 arch_name=sparcv8+')

  def testGoodSparcv8Plus(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 18,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/sparcv8plus/tree'},
       ]

  def testGoodSparcv8PlusInBin(self):
    # From October 2011 on, the sparcv8+ binaries can be in bin on
    # Solaris 10.
    parsed_basename = self.pkg_data["basic_stats"]["parsed_basename"]
    parsed_basename["osrel"] = "SunOS5.10"
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 18,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/tree'},
       ]
    # No error here.

  # A similar test can't be written for i386, because pentium_pro and
  # i386 have the same machine_id, so we can't distinguish between the
  # two.

  def testGoodBinary(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-executable; charset=binary',
        'mime_type_by_hachoir': u'application/x-executable',
        'path': 'opt/csw/bin/tree'}]

  def testGoodLibrary(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-sharedlib; charset=binary',
        'path': 'opt/csw/lib/foo/subdir/libfoo.so.1'}]

  def testBadPlacement(self):
    self.pkg_data["files_metadata"] = [
       {'endian': 'Big endian',
        'machine_id': 2,
        'mime_type': 'application/x-sharedlib; charset=binary',
        'path': 'opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1'}]
    self.error_mgr_mock.ReportError(
        'binary-disallowed-placement',
        'file=opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1 '
        'arch_id=2 arch_name=sparcv8 bad_path=sparcv9')


class TestConflictingFiles(CheckTestHelper,
                           unittest.TestCase):
  """Throw an error if there's a conflicting file in the package set."""
  FUNCTION_NAME = 'SetCheckFileCollisions'
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
  def testFileCollision(self):
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
        frozenset(['CSWfoo', 'CSWbar']))
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
        frozenset(['CSWfoo', 'CSWbar']))
    self.error_mgr_mock.ReportError(
        'CSWbar', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
    self.error_mgr_mock.ReportError(
        'CSWfoo', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
    self.pkg_data = [self.CSWbar_DATA, self.CSWfoo_DATA]

  def testFileCollisionNotInCatalog(self):
    # What if these two packages are not currently in the catalog?
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
        frozenset([]))
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
        frozenset([]))
    self.error_mgr_mock.ReportError(
        'CSWbar', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
    self.error_mgr_mock.ReportError(
        'CSWfoo', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
    self.pkg_data = [self.CSWbar_DATA, self.CSWfoo_DATA]


class TestSetCheckSharedLibraryConsistencyIvtools(CheckTestHelper,
                                                  unittest.TestCase):
  """This tests for a case in which the SONAME that we're looking for doesn't
  match the filename."""
  FUNCTION_NAME = 'SetCheckLibraries'
  def testNeedsSoname(self):
    self.pkg_data = ivtools_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.NeedFile('CSWivtools', '/opt/csw/lib/libComUnidraw.so',
        'opt/csw/bin/comdraw needs the libComUnidraw.so soname')
    # This may be enabled once checkpkg supports directory dependencies.
    # self.error_mgr_mock.ReportError('CSWivtools', 'missing-dependency', u'CSWcommon')


class TestSetCheckDirectoryDependencies(CheckTestHelper,
                                        unittest.TestCase):
  """Test whether appropriate files are provided."""
  FUNCTION_NAME = 'SetCheckLibraries'

  def testDirectoryNeeded(self):
    self.pkg_data = ivtools_stats
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.NeedFile("CSWivtools", "/opt/csw/lib/libComUnidraw.so", mox.IsA(str))


class TestSetCheckDirectoryDependenciesTree(CheckTestHelper,
                                            unittest.TestCase):
  """Test whether appropriate files are provided."""
  FUNCTION_NAME = 'SetCheckLibraries'

  # This test is disabled for the time being.

  def disabled_testGiveMeAName(self):
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
    self.error_mgr_mock.NeedFile("CSWtree", mox.IsA(str), mox.IsA(str))


class TestCheckDiscouragedFileNamePatterns(CheckTestHelper,
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
  def testBadVar(self):
    self.pkg_data = self.CSWfoo_DATA
    self.error_mgr_mock.ReportError(
        'discouraged-path-in-pkgmap', '/opt/csw/var')

  def testGitFiles(self):
    # The data need to be copied, because otherwise all other tests will
    # also process modified data.
    self.pkg_data = copy.deepcopy(rsync_stats[0])
    self.pkg_data["pkgmap"].append(
            { "type": "f", "path": "/opt/csw/share/.git/foo", })
    self.error_mgr_mock.ReportError(
            'discouraged-path-in-pkgmap', '/opt/csw/share/.git/foo')


class TestSetCheckDirectoryDepsTwoPackages(CheckTestHelper,
                                           unittest.TestCase):
  """Test whether appropriate files are provided.

  This is a stupid test and can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'

  def testDirectoryDeps(self):
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
      "/usr/lib/sparcv9": (u"SUNWcslx"),})
    common_path_pkgs = [u'CSWgdbm', u'CSWbinutils', u'CSWcommon']
    paths_to_check = [
        '/opt/csw/share/man', '/opt/csw/bin', '/opt/csw/share', '/var/opt/csw',
        '/opt/csw/etc', '/opt/csw/sbin', '/opt/csw', '/opt/csw/share/doc']
    for path in paths_to_check:
      self.error_mgr_mock.GetPkgByPath(path).AndReturn(common_path_pkgs)
    for i in range(5):
      self.error_mgr_mock.NeedFile("CSWsudo-common", mox.IsA(str), mox.IsA(str))
    for i in range(6):
      self.error_mgr_mock.NeedFile("CSWsudo", mox.IsA(str), mox.IsA(str))


class TestSetCheckDirectoryDepsMissing(CheckTestHelper,
                                       unittest.TestCase):
  """Test whether appropriate files are provided.

  This is a stupid test and can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'

  def testNeededDirectories(self):
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
    for i in range(5):
      self.error_mgr_mock.NeedFile("CSWsudo-common", mox.IsA(str), mox.IsA(str))
    for i in range(6):
      self.error_mgr_mock.NeedFile("CSWsudo", mox.IsA(str), mox.IsA(str))
    # This is the critical test here.
    # self.error_mgr_mock.ReportError(
    #     'CSWsudo-common', 'base-dir-not-found', '/opt/csw/share/man')


class TestSetCheckDoubleDepends(CheckTestHelper, unittest.TestCase):
  """This is a class that was used for debugging.

  It can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'

  def SetMessenger(self):
    """We want to have control over the messenger object."""
    self.messenger = self.mox.CreateMock(stubs.MessengerStub)

  def testNeededFiles(self):
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

    for i in range(27):
      self.error_mgr_mock.NeedFile(
          mox.IsA(str), mox.IsA(unicode), mox.IsA(str))


class TestCheckWrongArchitecture(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckWrongArchitecture'
  def testSparcBinariesInIntelPackage(self):
    self.pkg_data = neon_stats[0]
    self.error_mgr_mock.ReportError(
        'binary-wrong-architecture',
        'file=opt/csw/lib/sparcv9/libneon.so.27.2.0 pkginfo-says=i386 actual-binary=sparc')
    self.error_mgr_mock.ReportError(
        'binary-wrong-architecture',
        'file=opt/csw/lib/sparcv9/libneon.so.26.0.4 pkginfo-says=i386 actual-binary=sparc')


class TestCheckSharedLibraryNamingPolicy(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSharedLibraryNamingPolicy'
  def testGood(self):
    self.pkg_data = bdb48_stats[0]


class TestCheckSharedLibraryPkgDoesNotHaveTheSoFile(CheckTestHelper,
                                                    unittest.TestCase):
  FUNCTION_NAME = 'CheckSharedLibraryPkgDoesNotHaveTheSoFile'

  def testBad(self):
    self.pkg_data = neon_stats[0]
    self.error_mgr_mock.ReportError(
        'shared-lib-package-contains-so-symlink',
        'file=/opt/csw/lib/libneon.so')
    self.error_mgr_mock.ReportError(
        'shared-lib-package-contains-so-symlink',
        'file=/opt/csw/lib/sparcv9/libneon.so')
    for j in range(2):
      for i in range(7):
        self.messenger.SuggestGarLine(mox.IsA(str))
      self.messenger.Message(mox.IsA(str))

  def SetMessenger(self):
    """Overriding this method to use mock instead of a stub."""
    self.messenger = self.mox.CreateMock(stubs.MessengerStub)

  def testSuggestions(self):
    self.pkg_data = neon_stats[0]
    self.error_mgr_mock.ReportError(
        'shared-lib-package-contains-so-symlink',
        'file=/opt/csw/lib/libneon.so')
    self.error_mgr_mock.ReportError(
        'shared-lib-package-contains-so-symlink',
        'file=/opt/csw/lib/sparcv9/libneon.so')
    self.messenger.SuggestGarLine("# (If CSWneon-dev doesn't exist yet)")
    self.messenger.SuggestGarLine('PACKAGES += CSWneon-dev')
    self.messenger.SuggestGarLine('CATALOGNAME_CSWneon-dev = neon_dev')
    self.messenger.SuggestGarLine(
        'SPKG_DESC_CSWneon-dev += $(DESCRIPTION), development files')
    self.messenger.SuggestGarLine(
        'PKGFILES_CSWneon-dev += /opt/csw/lib/libneon.so')
    self.messenger.SuggestGarLine('# Maybe also the generic:')
    self.messenger.SuggestGarLine(
        '# PKGFILES_CSWneon-dev += $(PKGFILES_DEVEL)')
    self.messenger.Message(mox.IsA(str))
    self.messenger.SuggestGarLine("# (If CSWneon-dev doesn't exist yet)")
    self.messenger.SuggestGarLine('PACKAGES += CSWneon-dev')
    self.messenger.SuggestGarLine('CATALOGNAME_CSWneon-dev = neon_dev')
    self.messenger.SuggestGarLine(
        'SPKG_DESC_CSWneon-dev += $(DESCRIPTION), development files')
    self.messenger.SuggestGarLine(
        'PKGFILES_CSWneon-dev += /opt/csw/lib/sparcv9/libneon.so')
    self.messenger.SuggestGarLine('# Maybe also the generic:')
    self.messenger.SuggestGarLine(
        '# PKGFILES_CSWneon-dev += $(PKGFILES_DEVEL)')
    self.messenger.Message(mox.IsA(str))


class TestCheckSharedLibraryNameMustBeAsubstringOfSonameGood(
    CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSharedLibraryNameMustBeAsubstringOfSoname'
  def testGood(self):
    self.pkg_data = neon_stats[0]
    # TODO: Implement this

  def testBad(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["binaries_dump_info"][3]["base_name"] = "foo.so.1"
    self.error_mgr_mock.ReportError(
        'soname-not-part-of-filename',
        'soname=libneon.so.27 filename=foo.so.1')


class TestCheckLicenseFilePlacementLicense(CheckTestHelper,
                                           unittest.TestCase):
  FUNCTION_NAME = 'CheckLicenseFilePlacement'
  def testBadLicensePlacement(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["pkgmap"].append({
      "class": "none", "type": "f", "line": "",
      "user": "root", "group": "bin", "mode": '0755',
      "path": "/opt/csw/share/doc/alien/license",
    })
    self.error_mgr_mock.ReportError(
        'wrong-docdir',
        'expected=/opt/csw/shared/doc/neon/... '
        'in-package=/opt/csw/share/doc/alien/license')

  def testGoodRandomFileWithSuffix(self):
    """A differently suffixed file should not trigger an error."""
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["pkgmap"].append({
      "class": "none", "type": "f", "line": "",
      "user": "root", "group": "bin", "mode": '0755',
      "path": "/opt/csw/share/doc/alien/license.html",
    })

  def testGoodRandomFile(self):
    "A random file should not trigger the message; only license files."
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["pkgmap"].append({
      "class": "none", "type": "f", "line": "",
      "user": "root", "group": "bin", "mode": '0755',
      "path": "/opt/csw/share/doc/alien/random_file",
    })


class TestCheckObsoleteDepsCups(CheckTestHelper, unittest.TestCase):
  "A random file should not trigger the message; only license files."
  FUNCTION_NAME = 'CheckObsoleteDeps'
  def testObsoleteDependency(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["depends"].append(("CSWlibcups", None))
    self.error_mgr_mock.ReportError('obsolete-dependency', 'CSWlibcups')


class TestCheckBaseDirs(CheckTestHelper,
                        unittest.TestCase):
  """Test whether appropriate base directories are provided."""
  FUNCTION_NAME = 'CheckBaseDirs'

  def testBaseDirectoryNeeded(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': '1 s none /opt/csw/lib/libneon.so.27=libneon.so.27.2.0',
         'mode': None,
         'path': '/opt/csw/lib/libneon.so.27',
         'type': 's',
         'user': None})
    self.error_mgr_mock.NeedFile('/opt/csw/lib', mox.IsA(str))


class TestCheckBaseDirsNotNoneClass(CheckTestHelper,
                                    unittest.TestCase):
  FUNCTION_NAME = 'CheckBaseDirs'

  def testNeedBaseDir(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'cswinitsmf',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/etc/opt/csw/init.d/foo',
         'type': 'f',
         'user': None})
    self.error_mgr_mock.NeedFile('/etc/opt/csw/init.d', mox.IsA(str))


class TestCheckDanglingSymlinks(CheckTestHelper,
                                unittest.TestCase):
  FUNCTION_NAME = 'CheckDanglingSymlinks'

  def testSymlinkTargetNeeded(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/opt/csw/lib/postgresql/9.0/lib/libpq.so.5',
         'type': 's',
         'user': None,
         'target': '/opt/csw/lib/libpq.so.5'})
    self.error_mgr_mock.NeedFile('/opt/csw/lib/libpq.so.5', mox.IsA(str))

  # Hardlinks work the same way.
  def testHardlinkTargetNeeded(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/opt/csw/lib/postgresql/9.0/lib/libpq.so.5',
         'type': 'l',
         'user': None,
         'target': '/opt/csw/lib/libpq.so.5'})
    self.error_mgr_mock.NeedFile('/opt/csw/lib/libpq.so.5', mox.IsA(str))


class TestCheckPrefixDirs(CheckTestHelper,
                          unittest.TestCase):
  FUNCTION_NAME = 'CheckPrefixDirs'

  def testGoodPrefix(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/opt/csw/bin/foo',
         'type': 'f',
         'user': None,
         'target': None})

  def testBadPrefix(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/opt/cswbin/foo',
         'type': 'f',
         'user': None,
         'target': None})
    self.error_mgr_mock.ReportError(
        'bad-location-of-file',
        'file=/opt/cswbin/foo')

  def testGoodVar(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/var/opt/csw/foo',
         'type': 'f',
         'user': None,
         'target': None})

  def testBadVar(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        {'class': 'none',
         'group': None,
         'line': None,
         'mode': None,
         'path': '/var/foo',
         'type': 'f',
         'user': None,
         'target': None})
    self.error_mgr_mock.ReportError(
        'bad-location-of-file',
        'file=/var/foo')


class TestCheckSonameMustNotBeEqualToFileNameIfFilenameEndsWithSo(
    CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = ('CheckSonameMustNotBeEqualToFileName'
                   'IfFilenameEndsWithSo')
  FOO_METADATA = {
      'endian': 'Little endian',
      'machine_id': 3,
      'mime_type': 'application/x-sharedlib; charset=binary',
      'mime_type_by_hachoir': u'application/x-executable',
      'path': 'opt/csw/lib/libfoo.so',
  }

  def testBad(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["binaries_dump_info"][0]["soname"] = "libfoo.so"
    self.pkg_data["binaries_dump_info"][0]["base_name"] = "libfoo.so"
    self.pkg_data["binaries_dump_info"][0]["path"] = "opt/csw/lib/libfoo.so"
    self.pkg_data["files_metadata"].append(self.FOO_METADATA)
    self.error_mgr_mock.ReportError(
        'soname-equals-filename',
        'file=/opt/csw/lib/libfoo.so')

  def testGood(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["binaries_dump_info"][0]["soname"] = "libfoo.so.1"
    self.pkg_data["binaries_dump_info"][0]["base_name"] = "libfoo.so.1"
    self.pkg_data["files_metadata"].append(self.FOO_METADATA)

  def testGoodMercurialExample(self):
    self.pkg_data = mercurial_stats[0]


class TestCheckCatalognameMatchesPkgname(CheckTestHelper,
                                         unittest.TestCase):
  FUNCTION_NAME = 'CheckCatalognameMatchesPkgname'

  def testMismatch(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    basic_stats = self.pkg_data["basic_stats"]
    basic_stats["catalogname"] = "foo_bar"
    basic_stats["pkgname"] = "CSWfoo-bar-baz"
    self.error_mgr_mock.ReportError(
        'catalogname-does-not-match-pkgname',
        'pkgname=CSWfoo-bar-baz catalogname=foo_bar '
        'expected-catalogname=foo_bar_baz')

  def testGoodMatch(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])


class TestCheckCatalognameMatchesPkgname(CheckTestHelper,
                                         unittest.TestCase):
  FUNCTION_NAME = 'CheckPkginfoOpencswRepository'

  def testRepositoryInfoGood(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    # No errors reported.

  def testRepositoryInfoMissing(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    del self.pkg_data["pkginfo"]["OPENCSW_REPOSITORY"]
    self.error_mgr_mock.ReportError('pkginfo-opencsw-repository-missing')

  def testRepositoryInfoUncommitted(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkginfo"]["OPENCSW_REPOSITORY"] = (
        "https://gar.svn.sourceforge.net/svnroot/gar/"
        "csw/mgar/pkg/puppet/trunk@UNCOMMITTED")
    self.error_mgr_mock.ReportError('pkginfo-opencsw-repository-uncommitted')


class TestCheckAlternativesDependency(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckAlternativesDependency'
  ALTERNATIVES_EXECUTABLE = "/opt/csw/sbin/alternatives"
  def testAlternativesNeeded(self):
    self.pkg_data["pkgmap"].append({
      'class': 'cswalternatives',
      'group': 'bin',
      'line': ('1 f cswalternatives /opt/csw/share/alternatives/sendmail '
               '0644 root bin 408 36322 1308243112'),
      'mode': '0644',
      'path': '/opt/csw/share/alternatives/sendmail',
      'target': None,
      'type': 'f',
      'user': 'root',
    })
    self.error_mgr_mock.NeedFile(
        self.ALTERNATIVES_EXECUTABLE,
        "The alternatives subsystem is used")


class TestCheckSharedLibrarySoExtension(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckSharedLibrarySoExtension'
  def testGoodExtension(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])

  def testBadExtension(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data["files_metadata"][11]["path"] = "foo.1"
    self.error_mgr_mock.ReportError(
        'shared-library-missing-dot-so', 'file=foo.1')


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



if __name__ == '__main__':
  unittest.main()
