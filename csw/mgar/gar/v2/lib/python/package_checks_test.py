#!/usr/bin/env python2.6
# coding=utf-8
# $Id$

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import copy
import datetime
import os.path
import mox
import logging
import pprint

from lib.python.testdata.djvulibre_rt_stats import pkgstats as djvulibre_rt_stats

from lib.python import checkpkg_lib
from lib.python import fake_pkgstats_composer
from lib.python import package_checks as pc
from lib.python import representations
from lib.python import test_base
from lib.python.testdata import rpaths
from lib.python.testdata import stubs

from lib.python.testdata.berkeleydb48_stats import pkgstats as bdb48_stats
# from lib.python.testdata.cadaver_stats import pkgstats as cadaver_stats
# from lib.python.testdata.ivtools_stats import pkgstats as ivtools_stats
# from lib.python.testdata.javasvn_stats import pkgstats as javasvn_stats
# from lib.python.testdata.mercurial_stats import pkgstats as mercurial_stats
from lib.python.testdata.neon_stats import pkgstats as neon_stats
from lib.python.testdata.rsync_stats import pkgstats as rsync_stats
from lib.python.testdata.sudo_stats import pkgstats as sudo_stats
from lib.python.testdata.tree_stats import pkgstats as tree_stats
from lib.python.testdata.vsftpd_stats import pkgstats as vsftpd_stats

DEFAULT_PKG_STATS = None
DEFAULT_PKG_DATA = rsync_stats[0]


class CheckTestHelper(test_base.PackageStatsMixin):
  """Class responsible for making calls to package check functions."""

  def setUp(self):
    super(CheckTestHelper, self).setUp()
    self.mox = mox.Mox()
    self.pkg_data = copy.deepcopy(DEFAULT_PKG_DATA)
    self.PrepareElfinfo(self.pkg_data)
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

  def TestPkgmapEntry(self, entry_path, class_="none", type_='f',
      target=None):
    return representations.PkgmapEntry(
        line=None, class_=class_, mode=None, owner=None, group=None,
        path=entry_path,
        target=target, type_=type_, major=None, minor=None, size=None,
        cksum=None, modtime=None, pkgnames=[],
    )

  def TestBinaryDumpInfo(self, binary_path, needed_sonames, runpath):
    return representations.BinaryDumpInfo(
        base_name=os.path.basename(binary_path),
        needed_sonames=needed_sonames,
        path=binary_path, rpath_set=True, runpath_rpath_the_same=True,
        runpath_set=True, runpath=runpath, soname=None)


# Test cases below.

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
    self.pkg_data['pkgmap'].append(
        self.TestPkgmapEntry(entry_path='/etc/opt/csw/init.d/foo'))
    self.error_mgr_mock.ReportError('init-file-missing-cswinitsmf-class',
                                    '/etc/opt/csw/init.d/foo class=none')

  def testSmfIntegrationGood(self):
    self.pkg_data["pkgmap"].append(
        self.TestPkgmapEntry(entry_path="/etc/opt/csw/init.d/foo",
          class_='cswinitsmf'))

  def testWrongLocation(self):
    self.pkg_data['pkgmap'].append(
        self.TestPkgmapEntry(entry_path='/opt/csw/etc/init.d/foo',
                             class_='cswinitsmf'))
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

  def testInterfaceInTestSetCheckDependencies(self):
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


# class TestSetCheckDependenciesWithDb(
#     DatabaseMockingMixin, CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testDoNotReportSurplusForDev(self):
#     self.pkg_data_single = self.pkg_data
#     self.pkg_data = [self.pkg_data_single]
#     self.pkg_data[0]["basic_stats"]["pkgname"] = "CSWfoo-dev"
#     self.pkg_data[0]["depends"].append(["CSWfoo", ""])
#     self.pkg_data[0]["depends"].append(["CSWbar", ""])
#     self.pkg_data[0]["depends"].append(["CSWlibiconv", ""])
#     self.MockDbInteraction()
#     for i in range(12):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(str), mox.IsA(str))
#     # There should be no error about the dependency on CSWfoo or CSWbar.
# 
#   def testReportDeps(self):
#     self.pkg_data_single = self.pkg_data
#     self.pkg_data = [self.pkg_data_single]
#     self.MockDbInteraction()
#     for i in range(12):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(str), mox.IsA(str))


class TestCheckArchitectureSanity(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckArchitectureSanity'
  def testSimple(self):
    self.pkg_data["pkginfo"]["ARCH"] = "i386"
    self.error_mgr_mock.ReportError(
        'srv4-filename-architecture-mismatch',
        'pkginfo=i386 '
        'filename=rsync-3.0.9,REV=2011.10.24-SunOS5.9-sparc-CSW.pkg.gz')

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


# class TestCheckLinkingAgainstSunX11(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckLinkingAgainstSunX11'
#   def testAllowLinkingAgainstSunX11(self):
#     self.pkg_data["binaries_dump_info"][0]["needed sonames"].append("libX11.so.4")
#     # No errors reported here.
# 
#   def testDoNotReportDiscouragedLib(self):
#     self.pkg_data["binaries_dump_info"].append({
#          'base_name': 'libImlib2.so.1.4.2',
#          'needed sonames': ['libfreetype.so.6',
#                             'libz.so',
#                             'libX11.so.4',
#                             'libXext.so.0',
#                             'libdl.so.1',
#                             'libm.so.1',
#                             'libc.so.1'],
#          'path': 'opt/csw/lib/libImlib2.so.1.4.2',
#          'runpath': ('/opt/csw/lib/$ISALIST',
#                      '/opt/csw/lib',
#                      '/usr/lib/$ISALIST',
#                      '/usr/lib',
#                      '/lib/$ISALIST',
#                      '/lib'),
#          'soname': 'libImlib2.so.1',
#          'soname_guessed': False,
#     })
#     # This no longer should throw an error.
#     # self.error_mgr_mock.ReportError('linked-against-discouraged-library',
#     #                                 'libImlib2.so.1.4.2 libX11.so.4')


# Broken test. This is hard to maintain, we need to find another way.
# class TestSetCheckLibraries(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testInterfaceInTestSetCheckLibraries(self):
#     self.pkg_data = djvulibre_rt_stats
#     self.PrepareElfinfo(self.pkg_data[0])
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCrun.so.1').AndReturn(
#       {u'/usr/lib': [u'SUNWlibC'],
#        u'/usr/lib/sparcv9': [u'SUNWlibC']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCstd.so.1').AndReturn(
#       {u'/usr/lib': [u'SUNWlibC'],
#        u'/usr/lib/sparcv9': [u'SUNWlibC']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn(
#       {u'/lib': [u'SUNWcslr'],
#        u'/lib/sparcv9': [u'SUNWcslr'],
#        u'/usr/lib': [u'SUNWcsl'],
#        u'/usr/lib/libp': [u'SUNWdpl'],
#        u'/usr/lib/libp/sparcv9': [u'SUNWdpl'],
#        u'/usr/lib/sparcv9': [u'SUNWcsl']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libiconv.so.2').AndReturn(
#       {u'/opt/csw/lib': [u'CSWiconv'],
#        u'/opt/csw/lib/sparcv9': [u'CSWiconv']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libjpeg.so.62').AndReturn(
#       {u'/opt/csw/lib': [u'CSWjpeg'],
#        u'/opt/csw/lib/sparcv9': [u'CSWjpeg'],
#        u'/usr/lib': [u'SUNWjpg'],
#        u'/usr/lib/sparcv9': [u'SUNWjpg']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libjpeg.so.7').AndReturn(
#       {u'/opt/csw/lib': [u'CSWjpeg'],
#        u'/opt/csw/lib/sparcv9': [u'CSWjpeg']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libm.so.1').AndReturn(
#       {u'/lib': [u'SUNWlibmsr'],
#        u'/lib/sparcv9': [u'SUNWlibmsr'],
#        u'/usr/lib': [u'SUNWlibms'],
#        u'/usr/lib/sparcv9': [u'SUNWlibms']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpthread.so.1').AndReturn(
#       {u'/lib': [u'SUNWcslr'],
#        u'/lib/sparcv9': [u'SUNWcslr'],
#        u'/usr/lib': [u'SUNWcsl'],
#        u'/usr/lib/sparcv9': [u'SUNWcsl']})
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/lib').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/lib/sparcv9').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.GetElfdumpInfo('da9a87a824e119029a94a9b5af1bbc07').AndReturn(
#         fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/opt/csw/lib/libjpeg.so.7', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libjpeg.so.7 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/lib/libpthread.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libpthread.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/usr/lib/libpthread.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libpthread.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/lib/libm.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libm.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/usr/lib/libm.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libm.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/usr/lib/libCstd.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libCstd.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/usr/lib/libCrun.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libCrun.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/lib/libc.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libc.so.1 soname')
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/usr/lib/libc.so.1', 'opt/csw/lib/libdjvulibre.so.21.1.0 needs the libc.so.1 soname')
#     self.error_mgr_mock.NeedFile('CSWdjvulibrert', mox.IsA(basestring), mox.IsA(str)).MultipleTimes()
#     self.error_mgr_mock.GetElfdumpInfo('985a73c1273736503296041e32dc2711').AndReturn(
#         fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', u'/opt/csw/lib/libjpeg.so.7', 'opt/csw/lib/sparcv9/libdjvulibre.so.21.1.0 needs the libjpeg.so.7 soname')
#     self.error_mgr_mock.NeedFile('CSWdjvulibrert', mox.IsA(basestring), mox.IsA(str)).MultipleTimes()
#     self.error_mgr_mock.GetElfdumpInfo('fdac3cd4b20414394b3f1be1fbfb4a70').AndReturn(
#         fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
#     # self.error_mgr_mock.NeedFile('CSWdjvulibrert', mox.IsA(basestring), mox.IsA(str)).MultipleTimes()
#     self.error_mgr_mock.ReportError('CSWdjvulibrert', 'no-direct-binding', mox.IsA(str))
#     self.error_mgr_mock.ReportError('CSWdjvulibrert', 'no-direct-binding', mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.ReportError('CSWdjvulibrert', 'no-direct-binding', mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.NeedFile(mox.IsA(str), mox.IsA(unicode), mox.IsA(str))
#     self.error_mgr_mock.ReportError('CSWdjvulibrert', 'no-direct-binding', mox.IsA(str))


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
    binaries_dump_info = [
        representations.BinaryDumpInfo._make(x)
        for x in binaries_dump_info]
    d = binaries_dump_info[0]._asdict()
    # Changing to a mutable (dict) representation.
    d["runpath"] = sorted(rpaths.all_rpaths)
    binaries_dump_info[0] = representations.BinaryDumpInfo(**d)
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
          'bad-rpath-entry', '%s opt/csw/bin/rsync' % bad_path)

# class TestCheckLibraries(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testDeprecatedLibrary(self):
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ("/opt/csw/lib",)
#     binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
#     self.pkg_data["depends"] = (("CSWfoo", None),(u"CSWcommon", ""))
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["binaries_elf_info"]['opt/csw/bin/sparcv8/rsync'] = {
#       'version definition': [],
#       'version needed': [],
#       'symbol table': [
#         { 'soname': 'libdb-4.7.so', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' }
#       ]
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
#        u'/opt/csw/lib': [u'CSWfoo'],
#        u'/opt/csw/lib/sparcv9': [u'CSWfoo'],
#     })
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.NeedFile('CSWrsync', u'/opt/csw/lib/libdb-4.7.so',
#         'opt/csw/bin/sparcv8/rsync needs the libdb-4.7.so soname')
#     self.error_mgr_mock.ReportError(
#         'CSWrsync',
#         'deprecated-library',
#         mox.IsA(unicode))
#     self.pkg_data = [self.pkg_data]
# 
#   def testDeprecatedLibrary(self):
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ("/opt/csw/bdb47/lib", "/opt/csw/lib",)
#     binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
#     self.pkg_data["depends"] = (("CSWbad", None),(u"CSWcommon", ""))
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["binaries_elf_info"]['opt/csw/bin/sparcv8/rsync'] = {
#       'version definition': [],
#       'version needed': [],
#       'symbol table': [
#         { 'soname': 'libdb-4.7.so', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' }
#       ]
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
#        u'/opt/csw/bdb47/lib':         [u'CSWbad'],
#        u'/opt/csw/bdb47lib/sparcv9': [u'CSWbad'],
#        u'/opt/csw/lib':               [u'CSWgood'],
#        u'/opt/csw/lib/sparcv9':       [u'CSWgood'],
#     })
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     # There should be no error here, since /opt/csw/bdb47/lib is first in the RPATH.
#     self.pkg_data = [self.pkg_data]
#     for i in range(2):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))
# 
#   def testBadRpath(self):
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ("/opt/csw/lib", "/opt/csw/bdb47/lib",)
#     binaries_dump_info[0]["needed sonames"] = ["libdb-4.7.so"]
#     self.pkg_data["depends"] = (("CSWbad", None),(u"CSWcommon", ""))
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["binaries_elf_info"]['opt/csw/bin/sparcv8/rsync'] = {
#       'version definition': [],
#       'version needed': [],
#       'symbol table': [{ 'symbol': 'foo',
#                          'soname': 'libdb-4.7.so',
#                          'bind': 'GLOB',
#                          'shndx': 'UNDEF',
#                          'flags': 'DBL' }],
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdb-4.7.so').AndReturn({
#        u'/opt/csw/bdb47/lib':         [u'CSWbad'],
#        u'/opt/csw/bdb47lib/sparcv9': [u'CSWbad'],
#        u'/opt/csw/lib':               [u'CSWgood'],
#        u'/opt/csw/lib/sparcv9':       [u'CSWgood'],
#     })
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     for i in range(1):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))
#     self.error_mgr_mock.ReportError(
#         'CSWrsync',
#         'deprecated-library',
#         u'file=opt/csw/bin/sparcv8/rsync '
#         u'lib=/opt/csw/lib/libdb-4.7.so')
#     self.pkg_data = [self.pkg_data]
#     for i in range(1):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.Or(mox.IsA(str), mox.IsA(unicode)), mox.IsA(str))

# class TestLibmLinking(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testLibmLinking(self):
#     self.pkg_data = [self.pkg_data]
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ("/opt/csw/lib",)
#     binaries_dump_info[0]["needed sonames"] = ["libm.so.2"]
#     self.pkg_data["depends"] = ((u"CSWcommon", ""),)
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["binaries_elf_info"] = {
#       'opt/csw/bin/sparcv8/rsync': {
#         'version definition': [],
#         'version needed': [],
#         'symbol table': [
#           { 'soname': 'libm.so.2', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' }
#         ]
#       }
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libm.so.2').AndReturn({})
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     self.pkg_data = [self.pkg_data]


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
  @property
  def CSWbar_DATA(self):
    return {
        'basic_stats': {'catalogname': 'bar',
                        'pkgname': 'CSWbar',
                        'stats_version': 1,
                        'parsed_basename': {'osrel': 'SunOS5.9'}},
        'binaries_dump_info': [
          representations.BinaryDumpInfo(
            base_name='bar',
            needed_sonames=['libfoo.so.1'],
            path='opt/csw/bin/bar',
            rpath_set=False,
            runpath_rpath_the_same=False,
            runpath_set=True,
            runpath=('/opt/csw/lib',),
            soname=None,
          ),
        ],
        'binary_md5_sums': [
          ('opt/csw/bin/bar', 'fake_md5'),
        ],

        'depends': (('CSWlibfoo', None),),
        'isalist': (),
        'pkgmap': [],
        'files_metadata': [
                    {'endian': 'Little endian',
                     'machine_id': 3,
                     'mime_type': 'application/x-sharedlib; charset=binary',
                     'mime_type_by_hachoir': u'application/x-executable',
                     'path': 'opt/csw/bin/bar/libfoo.so.1'},
        ],
        'elfdump_info': {
          'fake_md5': {
            'version definition': [],
            'version needed': [],
            'symbol table': [
              representations.ElfSymInfo(
                 soname='libfoo.so.1',
                 symbol='foo',
                 flags='DBL',
                 shndx='UNDEF',
                 bind='GLOB',
                 version=None)]}},
  }
  CSWlibfoo_DATA = {
        'basic_stats': {'catalogname': 'libfoo',
                        'pkgname': 'CSWlibfoo',
                        'stats_version': 1},
        'binary_md5_sums': [],
        'binaries_dump_info': [],
        'elfdump_info': [],
        'depends': [],
        'isalist': (),
        'pkgmap': [],
      }

  def testMissingLibFromNewPackage(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({
       u'/opt/csw/lib': [u'CSWlibfoo'],
    })
    self.error_mgr_mock.GetElfdumpInfo('fake_md5').AndReturn({
      'version definition': [],
      'version needed': [],
      'symbol table': [
        representations.ElfSymInfo(
          soname='libfoo.so.1', symbol='foo', flags='DBL', shndx='UNDEF',
          bind='GLOB', version=None)]})
    self.error_mgr_mock.ReportError(
        'CSWbar',
        'soname-not-found',
        'libfoo.so.1 is needed by opt/csw/bin/bar')
    self.pkg_data = [self.CSWbar_DATA, self.CSWlibfoo_DATA]


class TestSharedLibsOnlyIsalist(CheckTestHelper, unittest.TestCase):
  """/opt/csw/lib/$ISALIST in RPATH without the bare /opt/csw/lib."""
  FUNCTION_NAME = 'SetCheckLibraries'
  # Contains only necessary bits.  The data listed in full.

  def setUp(self):
    super(TestSharedLibsOnlyIsalist, self).setUp()
    self.plc = fake_pkgstats_composer.PkgstatsListComposer('SunOS5.9', 'sparc')
    self.plc.AddPkgname('CSWbar')
    elfinfo_1 = {
        'version definition': [],
        'version needed': [],
        'symbol table': [
          representations.ElfSymInfo(soname='libfoo.so.1', symbol='foo',
                                     flags='DBL', shndx='UNDEF',
                                     bind='GLOB', version=None)]}
    self.plc.AddFile('CSWbar', self.TestPkgmapEntry('/opt/csw/lib/libfoo.so.1'),
                     representations.FileMetadata(path='/opt/csw/lib/libfoo.so.1',
                                                  mime_type='application/x-sharedlib',
                                                  machine_id=3),
                     self.TestBinaryDumpInfo('opt/csw/bin/bar',
                                             ['libfoo.so.1'],
                                             ['/opt/csw/lib/$ISALIST']),
                     elfinfo_1)
    elfinfo_2 = {'version definition': [], 'version needed': [],
                 'symbol table': []}
    self.plc.AddFile('CSWbar', self.TestPkgmapEntry('/opt/csw/bin/bar'),
                     representations.FileMetadata(path='/opt/csw/bin/bar',
                                                  mime_type='application/x-executable',
                                                  machine_id=3),
                     self.TestBinaryDumpInfo('opt/csw/lib/libfoo.so.1',
                                             [], ['/opt/csw/lib/$ISALIST']),
                     elfinfo_2)

  def testInterface(self):
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libfoo.so.1').AndReturn({})
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn([u"CSWcommon"])
    self.error_mgr_mock.NeedFile('CSWbar', '/opt/csw/lib/libfoo.so.1',
                                 'opt/csw/bin/bar needs the libfoo.so.1 soname')
    bin_md5_1 = '710de5ad3353b4747776a7a6babb7fb0'
    self.error_mgr_mock.GetElfdumpInfo(bin_md5_1).AndReturn(
        self.plc.GetElfdumpInfo(bin_md5_1))
    bin_md5_2 = '00685f8d00958bff01952a206b6ef636'
    self.error_mgr_mock.GetElfdumpInfo(bin_md5_2).AndReturn(
        self.plc.GetElfdumpInfo(bin_md5_2))
    self.pkg_data = self.plc.GetPkgstats()


# class TestCheckLibrariesDlopenLibs_1(CheckTestHelper, unittest.TestCase):
#   """For dlopen-style shared libraries, libraries from /opt/csw/lib should be
#   counted as dependencies.  It's only a heuristic though."""
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testMissingLibbar(self):
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ()
#     binaries_dump_info[0]["needed sonames"] = ["libbar.so"]
#     binaries_dump_info[0]["path"] = 'opt/csw/lib/python/site-packages/foo.so'
#     self.pkg_data["depends"] = ((u"CSWcommon", "This one provides directories"),)
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["ldd_info"] = { 'opt/csw/lib/python/site-packages/foo.so': [] }
#     self.pkg_data["binaries_elf_info"] = {
#       'opt/csw/lib/python/site-packages/foo.so': {
#         'version definition': [],
#         'version needed': [],
#         'symbol table': [
#           { 'soname': 'libbar.so',
#               'symbol': 'foo',
#               'flags': 'DBL',
#               'shndx': 'UNDEF',
#               'bind': 'GLOB' }
#           ]
#         }
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libbar.so').AndReturn({
#        u'/opt/csw/lib': [u'CSWlibbar'],
#        u'/opt/csw/lib/sparcv9': [u'CSWlibbar'],
#     })
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.ReportError('CSWrsync', 'soname-not-found',
#                                     'libbar.so is needed by '
#                                     'opt/csw/lib/python/site-packages/foo.so')
#     self.pkg_data = [self.pkg_data]
# 
#   def testLibNotFound(self):
#     binaries_dump_info = self.pkg_data["binaries_dump_info"]
#     binaries_dump_info[0]["runpath"] = ()
#     binaries_dump_info[0]["needed sonames"] = ["libnotfound.so"]
#     binaries_dump_info[0]["path"] = 'opt/csw/lib/foo.so'
#     self.pkg_data["depends"] = ((u"CSWcommon","This is needed"),)
#     self.pkg_data["binaries_dump_info"] = binaries_dump_info[0:1]
#     self.pkg_data["ldd_info"] = { 'opt/csw/lib/foo.so': [] }
#     self.pkg_data["binaries_elf_info"] = {
#       'opt/csw/lib/foo.so': {
#         'version definition': [],
#         'version needed': [],
#         'symbol table': [
#             { 'soname': 'libnotfound.so',
#               'symbol': 'foo',
#               'flags': 'DBL',
#               'shndx': 'UNDEF',
#               'bind': 'GLOB' }
#           ]
#        }
#     }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename(
#         'libnotfound.so').AndReturn({})
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/man').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv8').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/bin/sparcv9').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath(
#         '/opt/csw/share/doc').AndReturn(["CSWcommon"])
#     self.error_mgr_mock.ReportError(
#         'CSWrsync', 'soname-not-found',
#         'libnotfound.so is needed by opt/csw/lib/foo.so')
#     self.pkg_data = [self.pkg_data]


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


class TestCheckPackageDoesNotBreakPython26(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckPackageDoesNotBreakPython26"
  def testBad(self):
    self.pkg_data["pkgmap"].append(representations.PkgmapEntry(
      path="/opt/csw/lib/python2.7/site-packages/"
           "hachoir_parser/video/mov.py",
      line="doesn't matter here", class_="none", mode='0755', owner="root", group="bin",
      target=None, type_="d", major=None, minor=None, size=None, cksum=None,
      modtime=None, pkgnames=[]))
    # There's no file in /opt/csw/lib/python/site-packages
    self.pkg_data["basic_stats"]["catalogname"] = "py_foo"
    self.pkg_data["basic_stats"]["pkgname"] = "CSWpy-foo"
    self.error_mgr_mock.ReportError('python-package-missing-py26-files')

  def testGood(self):
    self.pkg_data["pkgmap"].append(representations.PkgmapEntry(
      path="/opt/csw/lib/python/site-packages/hachoir_parser/video/mov.py",
      line="doesn't matter here", class_="none", mode='0755', owner="root", group="bin",
      target=None, type_="d", major=None, minor=None, size=None, cksum=None,
      modtime=None, pkgnames=[]))
    self.pkg_data["basic_stats"]["catalogname"] = "py_foo"
    self.pkg_data["basic_stats"]["pkgname"] = "CSWpy-foo"


class TestCheckDisallowedPaths(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckDisallowedPaths"
  def testManDir(self):
    self.pkg_data["pkgmap"].append(representations.PkgmapEntry(
      path="/opt/csw/man",
      line="doesn't matter here", class_="none", mode='0755', owner="root", group="bin",
      target=None, type_="d", major=None, minor=None, size=None, cksum=None,
      modtime=None, pkgnames=[]))
    self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
    self.error_mgr_mock.ReportError(
        'disallowed-path', 'opt/csw/man',
        'This path is already provided by CSWcommon '
        'or is not allowed for other reasons.')

  def testManFile(self):
    self.pkg_data["pkgmap"].append(representations.PkgmapEntry(
      path="/opt/csw/man/man1/foo.1",
      line="doesn't matter here", class_="none", mode='0755', owner="root", group="bin",
      target=None, type_="d", major=None, minor=None, size=None, cksum=None,
      modtime=None, pkgnames=[]))
    self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
    self.error_mgr_mock.ReportError(
        'disallowed-path', 'opt/csw/man/man1/foo.1',
        'This path is already provided by CSWcommon '
        'or is not allowed for other reasons.')


# class TestCheckPythonPackageName(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = "CheckPythonPackageName"
#   def testBad(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "",
#       "mode": '0755',
#       "path": "/opt/csw/lib/python/site-packages/hachoir_parser/video/mov.py",
#       "type": "f",
#       "user": "root"
#     })
#     self.error_mgr_mock.ReportError('pkgname-does-not-start-with-CSWpy-')
#     self.error_mgr_mock.ReportError('catalogname-does-not-start-with-py_')
# 
#   def testGood(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "",
#       "mode": '0755',
#       "path": "/opt/csw/lib/python/site-packages/hachoir_parser/video/mov.py",
#       "type": "f",
#       "user": "root"
#     })
#     self.pkg_data["basic_stats"]["catalogname"] = "py_foo"
#     self.pkg_data["basic_stats"]["pkgname"] = "CSWpy-foo"


# class TestCheckDisallowedPaths(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = "CheckDisallowedPaths"
#   def testManDir(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "doesn't matter here",
#       "mode": '0755',
#       "path": "/opt/csw/man",
#       "type": "d",
#       "user": "root"
#     })
#     self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
#     self.error_mgr_mock.ReportError(
#         'disallowed-path', 'opt/csw/man',
#         'This path is already provided by CSWcommon '
#         'or is not allowed for other reasons.')
# 
#   def testManFile(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "doesn't matter here",
#       "mode": '0755',
#       "path": "/opt/csw/man/man1/foo.1",
#       "type": "f",
#       "user": "root"
#     })
#     self.error_mgr_mock.GetCommonPaths('sparc').AndReturn([])
#     self.error_mgr_mock.ReportError(
#         'disallowed-path', 'opt/csw/man/man1/foo.1',
#         'This path is already provided by CSWcommon '
#         'or is not allowed for other reasons.')


# class TestCheckGzippedManpages(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = "CheckGzippedManpages"
#   def testGzippedManpageBad(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "",
#       "mode": '0755',
#       "path": "/opt/csw/share/man/man5/puppet.conf.5.gz",
#       "type": "f",
#       "user": "root"
#     })
#     self.error_mgr_mock.ReportError(
#       'gzipped-manpage-in-pkgmap', '/opt/csw/share/man/man5/puppet.conf.5.gz',
#       "Solaris' man cannot automatically inflate man pages. "
#       "Solution: man page should be gunzipped.")
# 
#   def testUncompressedManpage(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "",
#       "mode": '0755',
#       "path": "/opt/csw/share/man/man5/puppet.conf.5",
#       "type": "f",
#       "user": "root"
#     })
# 
#   # Although this is a gzipped manpage, it is not in a directory associated with
#   # manpages, so we should not trigger an error here.
#   def testGzippedFileGood(self):
#     self.pkg_data["pkgmap"].append({
#       "class": "none",
#       "group": "bin",
#       "line": "",
#       "mode": '0755',
#       "path": "/etc/opt/csw/puppet/puppet.conf.5.gz",
#       "type": "f",
#       "user": "root"
#     })


class TestCheckArchitecture(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = "CheckArchitecture"
  def testBadSparcv8Plus(self):
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=18,
          mime_type='application/x-executable; charset=binary',
          path='opt/csw/bin/tree')
    ]
    self.error_mgr_mock.ReportError(
        'binary-architecture-does-not-match-placement',
        'file=opt/csw/bin/tree arch_id=18 arch_name=sparcv8+')

  def testGoodSparcv8Plus(self):
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=18,
          mime_type='application/x-executable; charset=binary',
          path='opt/csw/bin/sparcv8plus/tree')]

  def testGoodSparcv8PlusInBin(self):
    # From October 2011 on, the sparcv8+ binaries can be in bin on
    # Solaris 10.
    parsed_basename = self.pkg_data["basic_stats"]["parsed_basename"]
    parsed_basename["osrel"] = "SunOS5.10"
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=18,
          mime_type='application/x-executable; charset=binary',
          path='opt/csw/bin/tree')]
    # No error here.

  # A similar test can't be written for i386, because pentium_pro and
  # i386 have the same machine_id, so we can't distinguish between the
  # two.

  def testGoodBinary(self):
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=2,
          mime_type='application/x-executable; charset=binary',
          path='opt/csw/bin/tree')]

  def testGoodLibrary(self):
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=2,
          mime_type='application/x-sharedlib; charset=binary',
          path='opt/csw/lib/foo/subdir/libfoo.so.1')]

  def testBadPlacement(self):
    self.pkg_data["files_metadata"] = [
        representations.FileMetadata(
          machine_id=2,
          mime_type='application/x-sharedlib; charset=binary',
          path='opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1')]
    self.error_mgr_mock.ReportError(
        'binary-disallowed-placement',
        'file=opt/csw/lib/sparcv9/foo/subdir/libfoo.so.1 '
        'arch_id=2 arch_name=sparcv8 bad_path=sparcv9')


# class TestConflictingFiles(CheckTestHelper,
#                            unittest.TestCase):
#   """Throw an error if there's a conflicting file in the package set."""
#   FUNCTION_NAME = 'SetCheckFileCollisions'
#   # Contains only necessary bits.  The data listed in full.
#   CSWbar_DATA = {
#         'basic_stats': {'catalogname': 'bar',
#                         'pkgname': 'CSWbar',
#                         'stats_version': 1},
#         'binaries_dump_info': [],
#         'depends': tuple(),
#         'isalist': [],
#         'pkgmap': [
#           {
#             "type": "f",
#             "path": "/opt/csw/share/foo",
#           }
#         ],
#   }
#   # This one has a conflicting file, this time it's a link, for a change.
#   CSWfoo_DATA = {
#         'basic_stats': {'catalogname': 'foo',
#                         'pkgname': 'CSWfoo',
#                         'stats_version': 1},
#         'binaries_dump_info': [],
#         'depends': tuple(),
#         'isalist': [],
#         'pkgmap': [
#           {
#             "type": "l",
#             "path": "/opt/csw/share/foo",
#           }
#         ],
#   }
#   def testFileCollision(self):
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
#         frozenset(['CSWfoo', 'CSWbar']))
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
#         frozenset(['CSWfoo', 'CSWbar']))
#     self.error_mgr_mock.ReportError(
#         'CSWbar', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
#     self.error_mgr_mock.ReportError(
#         'CSWfoo', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
#     self.pkg_data = [self.CSWbar_DATA, self.CSWfoo_DATA]
# 
#   def testFileCollisionNotInCatalog(self):
#     # What if these two packages are not currently in the catalog?
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
#         frozenset([]))
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/share/foo').AndReturn(
#         frozenset([]))
#     self.error_mgr_mock.ReportError(
#         'CSWbar', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
#     self.error_mgr_mock.ReportError(
#         'CSWfoo', 'file-collision', '/opt/csw/share/foo CSWbar CSWfoo')
#     self.pkg_data = [self.CSWbar_DATA, self.CSWfoo_DATA]


class TestSetCheckSharedLibraryConsistencyIvtools(CheckTestHelper,
                                                  unittest.TestCase):
  """This tests for a case in which the SONAME that we're looking for doesn't
  match the filename."""
  FUNCTION_NAME = 'SetCheckLibraries'

  def LeaveNamedBinaries(self, pkg_data, names_list):
    def NameMatches(name):
      return any(y in name for y in names_list)

    pkg_data[0]['binaries'] = [
        x for x in pkg_data[0]['binaries']
        if NameMatches(x)]
    pkg_data[0]['binaries_dump_info'] = [
        x for x in pkg_data[0]['binaries_dump_info']
        if NameMatches(x[0])]
    pkg_data[0]['files_metadata'] = [
        x for x in pkg_data[0]['files_metadata']
        if NameMatches(x[0])]
    pkg_data[0]['binary_md5_sums'] = [
        x for x in pkg_data[0]['binary_md5_sums']
        if NameMatches(x[0])]
    return pkg_data

#   def testNeedsSoname(self):
#     self.pkg_data = self.LeaveNamedBinaries(copy.deepcopy(ivtools_stats),
#                                             ['/libComUnidraw.so', '/comdraw'])
#     self.pkg_data[0]['binaries_dump_info'][0][3] = self.pkg_data[0]['binaries_dump_info'][0][3][:1]
#     # pprint.pprint(self.pkg_data[0])
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
#     self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
#     # self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.NeedFile('CSWivtools', '/opt/csw/lib/libComUnidraw.so',
#         'opt/csw/bin/comdraw needs the libComUnidraw.so soname')
#     self.error_mgr_mock.ReportError('CSWivtools', 'no-direct-binding',
#         '/opt/csw/bin/comdraw is not directly bound to soname libComUnidraw.so')
#     # This may be enabled once checkpkg supports directory dependencies.
#     # self.error_mgr_mock.ReportError('CSWivtools', 'missing-dependency', u'CSWcommon')


# class TestSetCheckDirectoryDependencies(CheckTestHelper,
#                                         unittest.TestCase):
#   """Test whether appropriate files are provided."""
#   FUNCTION_NAME = 'SetCheckLibraries'
# 
#   def testDirectoryNeeded(self):
#     self.pkg_data = copy.deepcopy(ivtools_stats)
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libComUnidraw.so').AndReturn({})
#     self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u"CSWcommon"])
#     self.error_mgr_mock.NeedFile("CSWivtools", "/opt/csw/lib/libComUnidraw.so", mox.IsA(str))


# class TestCheckDiscouragedFileNamePatterns(CheckTestHelper,
#                                            unittest.TestCase):
#   """Throw an error if there's a conflicting file in the package set."""
#   FUNCTION_NAME = 'CheckDiscouragedFileNamePatterns'
#   CSWfoo_DATA = {
#         'basic_stats': {'catalogname': 'foo',
#                         'pkgname': 'CSWfoo',
#                         'stats_version': 1},
#         'binaries_dump_info': [],
#         'depends': tuple(),
#         'isalist': [],
#         'pkgmap': [
#           { "type": "d", "path": "/opt/csw/var", },
#           { "type": "d", "path": "/opt/csw/bin", },
#         ],
#   }
#   def testBadVar(self):
#     self.pkg_data = self.CSWfoo_DATA
#     self.error_mgr_mock.ReportError(
#         'discouraged-path-in-pkgmap', '/opt/csw/var')
# 
#   def testGitFiles(self):
#     # The data need to be copied, because otherwise all other tests will
#     # also process modified data.
#     self.pkg_data = copy.deepcopy(rsync_stats[0])
#     self.pkg_data["pkgmap"].append(
#             { "type": "f", "path": "/opt/csw/share/.git/foo", })
#     self.error_mgr_mock.ReportError(
#             'discouraged-path-in-pkgmap', '/opt/csw/share/.git/foo')


class TestSetCheckDirectoryDepsMissing(CheckTestHelper,
                                       unittest.TestCase):
  """Test whether appropriate files are provided.
 
  This is a stupid test and can be removed if becomes annoying.
  """
  FUNCTION_NAME = 'SetCheckLibraries'

  def testNeededDirectories(self):
    self.pkg_data = sudo_stats
    self.PrepareElfinfo(self.pkg_data[0])
    # These mock calls have been autogenerated by
    # lib/python/prepare_mock_calls.py
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn(
      {     u'/lib': [u'SUNWcslr'],
      u'/lib/amd64': [u'SUNWcslr'],
      u'/usr/lib': [u'SUNWcsl'],
      u'/usr/lib/amd64': [u'SUNWcsl'],
      u'/usr/lib/libp': [u'SUNWdpl'],
      u'/usr/lib/libp/amd64': [u'SUNWdpl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdl.so.1').AndReturn(
      {     u'/etc/lib': [u'SUNWcsr'],
      u'/lib': [u'SUNWcslr'],
      u'/lib/amd64': [u'SUNWcslr'],
      u'/usr/lib': [u'SUNWcsl'],
      u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn(
      {     u'/opt/csw/lib': [u'CSWlibintl8'], u'/opt/csw/lib/amd64': [u'CSWlibintl8']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn(
      {     u'/lib': [u'SUNWcslr'], u'/lib/amd64': [u'SUNWcslr'], u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpam.so.1').AndReturn(
      {     u'/lib': [u'SUNWcslr'],
      u'/lib/amd64': [u'SUNWcslr'],
      u'/usr/dt/lib': [u'SUNWdtbas'],
      u'/usr/lib': [u'SUNWcsl'],
      u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libproject.so.1').AndReturn(
      {     u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('librt.so.1').AndReturn(
      {     u'/lib': [u'SUNWcslr'], u'/lib/amd64': [u'SUNWcslr'], u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn(
      {     u'/lib': [u'SUNWcslr'], u'/lib/amd64': [u'SUNWcslr'], u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/amd64': [u'SUNWcsl']})
    self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libz.so.1').AndReturn(
      {     u'/opt/csw/lib': [u'CSWlibz1'],
      u'/opt/csw/lib/amd64': [u'CSWlibz1'],
      u'/opt/csw/lib/pentium': [u'CSWlibz1'],
      u'/opt/csw/lib/pentium_pro+mmx': [u'CSWlibz1'],
      u'/usr/lib': [u'SUNWzlib'],
      u'/usr/lib/amd64': [u'SUNWzlib']})
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/ru/LC_MESSAGES').AndReturn(
      [     u'CSWclisp',
      u'CSWcommon',
      u'CSWenlightenment',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWminicom',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/ja/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWenlightenment',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgtk',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWminicom',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn(
      [     u'CSWacpidump',
      u'CSWarc',
      u'CSWarchivemail',
      u'CSWargus',
      u'CSWbittorrent',
      u'CSWbmon',
      u'CSWcdrdao',
      u'CSWcdrtools',
      u'CSWcksfv',
      u'CSWclex',
      u'CSWclisp',
      u'CSWcommon',
      u'CSWcryptopp',
      u'CSWdcraw',
      u'CSWddd',
      u'CSWdejagnu',
      u'CSWdict',
      u'CSWenlightenment',
      u'CSWerlang',
      u'CSWfakeroot',
      u'CSWfilter',
      u'CSWflex',
      u'CSWflowtools',
      u'CSWforemost',
      u'CSWfox',
      u'CSWfreetype',
      u'CSWgkermit',
      u'CSWgnomedocutils',
      u'CSWgnomemenus',
      u'CSWgnomespeech',
      u'CSWgnucashcommon',
      u'CSWgp2c',
      u'CSWgperf',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkchtheme',
      u'CSWgtkgnutella',
      u'CSWhexedit',
      u'CSWhylafax',
      u'CSWhypermail',
      u'CSWiasl',
      u'CSWicon',
      u'CSWimlib',
      u'CSWipaudit',
      u'CSWircii',
      u'CSWisaexec',
      u'CSWjasspame',
      u'CSWjhead',
      u'CSWjove',
      u'CSWkdrill',
      u'CSWkicad',
      u'CSWksh',
      u'CSWkshdbx',
      u'CSWlibatlas_c++',
      u'CSWlibgtop',
      u'CSWlibunicode',
      u'CSWlibxft2',
      u'CSWlog4cpp',
      u'CSWlrzsz',
      u'CSWlwm',
      u'CSWmeld',
      u'CSWmgdiff',
      u'CSWmhonarc',
      u'CSWminicom',
      u'CSWmpack',
      u'CSWmpage',
      u'CSWmpeg2codec',
      u'CSWnedit',
      u'CSWnethack',
      u'CSWneverball',
      u'CSWobconf',
      u'CSWocrad',
      u'CSWopenobex',
      u'CSWparigp',
      u'CSWpkgzip',
      u'CSWplucker',
      u'CSWpmcgiappdisp',
      u'CSWpmextutautoinst',
      u'CSWpmsdf',
      u'CSWpmtemplatetal',
      u'CSWpmtestxml',
      u'CSWpmxmldom',
      u'CSWpmxmltwig',
      u'CSWpowertop',
      u'CSWprboom',
      u'CSWpsiconv',
      u'CSWpstree',
      u'CSWptunnel',
      u'CSWpxupgrade',
      u'CSWrdist',
      u'CSWregina',
      u'CSWrocksndiamonds',
      u'CSWrwhois',
      u'CSWrxvt',
      u'CSWsamefile',
      u'CSWsbcl',
      u'CSWscala',
      u'CSWsccs',
      u'CSWschilybase',
      u'CSWschilyutils',
      u'CSWscotty',
      u'CSWsdlsound',
      u'CSWsloccount',
      u'CSWsmake',
      u'CSWspider',
      u'CSWsrm',
      u'CSWssh-proxy',
      u'CSWstar',
      u'CSWstellarium',
      u'CSWsynergy',
      u'CSWtcptraceroute',
      u'CSWtla-tools',
      u'CSWtransfig',
      u'CSWucspitcp',
      u'CSWunarj',
      u'CSWunclutter',
      u'CSWved',
      u'CSWvispan',
      u'CSWvte',
      u'CSWw9wm',
      u'CSWwmclock',
      u'CSWwmmail',
      u'CSWxpilot'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/da/LC_MESSAGES').AndReturn(
      [     u'CSWclisp',
      u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/de/LC_MESSAGES').AndReturn(
      [     u'CSWclisp',
      u'CSWcommon',
      u'CSWenlightenment',
      u'CSWfreetype',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWgtkspell',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/include').AndReturn(
      [     u'CSWcairomm',
      u'CSWcgilib',
      u'CSWcommon',
      u'CSWcryptopp',
      u'CSWdejagnu',
      u'CSWffcall',
      u'CSWflex',
      u'CSWflowtools',
      u'CSWfnlib',
      u'CSWfox',
      u'CSWfreetype',
      u'CSWgimplibs',
      u'CSWgnomemenus',
      u'CSWgnomespeech',
      u'CSWgnucashcommon',
      u'CSWgpgme',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWgtkspell',
      u'CSWimlib',
      u'CSWlibatlas_c++',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWlibmng',
      u'CSWlibunicode',
      u'CSWlibwpd',
      u'CSWlibxft2',
      u'CSWlibxklavier',
      u'CSWlibxml++',
      u'CSWlog4cpp',
      u'CSWloudmouth',
      u'CSWopenobex',
      u'CSWosndsys',
      u'CSWparigp',
      u'CSWpsiconv',
      u'CSWregina',
      u'CSWrwhois',
      u'CSWschilybase',
      u'CSWsdlttf',
      u'CSWsilctoolkit',
      u'CSWsqlite',
      u'CSWvte',
      u'CSWwv2',
      u'CSWxaw3d'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/sbin').AndReturn(
      [     u'CSWargus',
      u'CSWcdrtools',
      u'CSWcommon',
      u'CSWdirvish',
      u'CSWfping',
      u'CSWhylafax',
      u'CSWintegrit',
      u'CSWipaudit',
      u'CSWmailgraph',
      u'CSWprivoxy',
      u'CSWschilybase',
      u'CSWschilyutils',
      u'CSWstar',
      u'CSWtmpreaper',
      u'CSWucarp',
      u'CSWved'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/doc').AndReturn(
      [     u'CSWXvfb',
      u'CSWap2modjk',
      u'CSWarc',
      u'CSWarchivemail',
      u'CSWargus',
      u'CSWbittorrent',
      u'CSWbmon',
      u'CSWcairomm',
      u'CSWcdrtools',
      u'CSWcksfv',
      u'CSWclisp',
      u'CSWcommon',
      u'CSWdejagnu',
      u'CSWfox',
      u'CSWgkermit',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomespeech',
      u'CSWgnucashcommon',
      u'CSWgperf',
      u'CSWgsfonts',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWhypermail',
      u'CSWicon',
      u'CSWjasspame',
      u'CSWjhead',
      u'CSWksh',
      u'CSWlibatlas_c++',
      u'CSWlibgtop',
      u'CSWlog4cpp',
      u'CSWloudmouth',
      u'CSWmailgraph',
      u'CSWmailscanner',
      u'CSWmeld',
      u'CSWmgdiff',
      u'CSWmhonarc',
      u'CSWmpeg2codec',
      u'CSWmrtgpme',
      u'CSWnedit',
      u'CSWnethack',
      u'CSWoortgnus',
      u'CSWplucker',
      u'CSWpmfrontierrpc',
      u'CSWprboom',
      u'CSWprivoxy',
      u'CSWpsiconv',
      u'CSWpxupgrade',
      u'CSWrocksndiamonds',
      u'CSWsbcl',
      u'CSWsccs',
      u'CSWschilybase',
      u'CSWschilyutils',
      u'CSWsilctoolkit',
      u'CSWslib',
      u'CSWsloccount',
      u'CSWsmake',
      u'CSWstar',
      u'CSWsynergy',
      u'CSWtcptraceroute',
      u'CSWucspitcp',
      u'CSWunarj',
      u'CSWved',
      u'CSWvispan',
      u'CSWw9wm',
      u'CSWwmclock',
      u'CSWwmmail'])
    self.error_mgr_mock.GetPkgByPath('/etc/opt/csw').AndReturn(
      [u'CSWcommon', u'CSWjetty6', u'CSWvispan'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/zh_CN').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstreamer',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/it/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/var/opt/csw').AndReturn(
      [u'CSWcommon', u'CSWflowtools', u'CSWjetty6', u'CSWprivoxy'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/pl/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWenlightenment',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWminicom',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/uk/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/sl/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/gl/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/es/LC_MESSAGES').AndReturn(
      [     u'CSWclisp',
      u'CSWcommon',
      u'CSWenlightenment',
      u'CSWfreetype',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWminicom',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/lt/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/vi/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/man').AndReturn(
      [     u'CSWXvfb',
      u'CSWarc',
      u'CSWarchivemail',
      u'CSWargus',
      u'CSWbmon',
      u'CSWcdrdao',
      u'CSWcdrtools',
      u'CSWclex',
      u'CSWclisp',
      u'CSWcommon',
      u'CSWdcraw',
      u'CSWddd',
      u'CSWdejagnu',
      u'CSWdict',
      u'CSWdirvish',
      u'CSWenlightenment',
      u'CSWfakeroot',
      u'CSWffcall',
      u'CSWfilter',
      u'CSWflex',
      u'CSWflowtools',
      u'CSWforemost',
      u'CSWfox',
      u'CSWfping',
      u'CSWgkermit',
      u'CSWgnomedocutils',
      u'CSWgnucashcommon',
      u'CSWgp2c',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkchtheme',
      u'CSWhexedit',
      u'CSWhylafax',
      u'CSWhypermail',
      u'CSWicon',
      u'CSWintegrit',
      u'CSWipaudit',
      u'CSWjasspame',
      u'CSWjhead',
      u'CSWkdrill',
      u'CSWksh',
      u'CSWkshdbx',
      u'CSWlibxft2',
      u'CSWlrzsz',
      u'CSWlwm',
      u'CSWmgdiff',
      u'CSWmhonarc',
      u'CSWminicom',
      u'CSWmpack',
      u'CSWmpage',
      u'CSWnedit',
      u'CSWnethack',
      u'CSWparigp',
      u'CSWpkgzip',
      u'CSWplucker',
      u'CSWpmcache',
      u'CSWpmcgiappdisp',
      u'CSWpmcgiapplogdisp',
      u'CSWpmcgpcli',
      u'CSWpmclassloader',
      u'CSWpmclsautouse',
      u'CSWpmextutautoinst',
      u'CSWpmfiletype',
      u'CSWpmfrontierrpc',
      u'CSWpmlibxmlperl',
      u'CSWpmmailbox',
      u'CSWpmmd5',
      u'CSWpmregexpshellish',
      u'CSWpmsdf',
      u'CSWpmsuboverride',
      u'CSWpmtemplatetal',
      u'CSWpmtestxml',
      u'CSWpmxmldom',
      u'CSWpmxmltwig',
      u'CSWpowertop',
      u'CSWprboom',
      u'CSWprivoxy',
      u'CSWptunnel',
      u'CSWpxupgrade',
      u'CSWrdist',
      u'CSWregina',
      u'CSWrocksndiamonds',
      u'CSWrwhois',
      u'CSWrxvt',
      u'CSWsamefile',
      u'CSWsbcl',
      u'CSWscala',
      u'CSWsccs',
      u'CSWschilybase',
      u'CSWschilyutils',
      u'CSWscotty',
      u'CSWsloccount',
      u'CSWsmake',
      u'CSWspider',
      u'CSWsrm',
      u'CSWstar',
      u'CSWstellarium',
      u'CSWtcptraceroute',
      u'CSWtmpreaper',
      u'CSWtransfig',
      u'CSWucspitcp',
      u'CSWunarj',
      u'CSWunclutter',
      u'CSWved',
      u'CSWw9wm',
      u'CSWwmclock',
      u'CSWwmmail',
      u'CSWxpilot'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/eu/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemeextras',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/sv/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWenlightenment',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemeextras',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/fi/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWminicom',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale').AndReturn(
      [     u'CSWclisp',
      u'CSWcommon',
      u'CSWenlightenment',
      u'CSWfreetype',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemeextras',
      u'CSWgnomethemes',
      u'CSWgnucashcommon',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkgnutella',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWgtkspell',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWminicom',
      u'CSWucarp',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw').AndReturn(
      [     u'CSWarchivemail',
      u'CSWaspellaf',
      u'CSWaspellam',
      u'CSWaspellar',
      u'CSWaspellast',
      u'CSWaspellaz',
      u'CSWaspellbe',
      u'CSWaspellbg',
      u'CSWaspellbn',
      u'CSWaspellbr',
      u'CSWaspellca',
      u'CSWaspellcs',
      u'CSWaspellcsb',
      u'CSWaspellcy',
      u'CSWaspellda',
      u'CSWaspellde',
      u'CSWaspellel',
      u'CSWaspellen',
      u'CSWaspelleo',
      u'CSWaspelles',
      u'CSWaspellet',
      u'CSWaspellfa',
      u'CSWaspellfi',
      u'CSWaspellfo',
      u'CSWaspellfr',
      u'CSWaspellfy',
      u'CSWaspellga',
      u'CSWaspellgd',
      u'CSWaspellgl',
      u'CSWaspellgrc',
      u'CSWaspellgu',
      u'CSWaspellgv',
      u'CSWaspellhe',
      u'CSWaspellhi',
      u'CSWaspellhil',
      u'CSWaspellhr',
      u'CSWaspellhsb',
      u'CSWaspellhu',
      u'CSWaspellhy',
      u'CSWaspellia',
      u'CSWaspellid',
      u'CSWaspellis',
      u'CSWaspellit',
      u'CSWaspellku',
      u'CSWaspellky',
      u'CSWaspellla',
      u'CSWaspelllt',
      u'CSWaspelllv',
      u'CSWaspellmg',
      u'CSWaspellmi',
      u'CSWaspellmk',
      u'CSWaspellml',
      u'CSWaspellmn',
      u'CSWaspellmr',
      u'CSWaspellms',
      u'CSWaspellmt',
      u'CSWaspellnb',
      u'CSWaspellnds',
      u'CSWaspellnl',
      u'CSWaspellnn',
      u'CSWaspellny',
      u'CSWaspellor',
      u'CSWaspellpa',
      u'CSWaspellpl',
      u'CSWaspellptbr',
      u'CSWaspellptpt',
      u'CSWaspellqu',
      u'CSWaspellro',
      u'CSWaspellru',
      u'CSWaspellrw',
      u'CSWaspellsc',
      u'CSWaspellsk',
      u'CSWaspellsl',
      u'CSWaspellsr',
      u'CSWaspellsv',
      u'CSWaspellsw',
      u'CSWaspellta',
      u'CSWaspellte',
      u'CSWaspelltet',
      u'CSWaspelltk',
      u'CSWaspelltl',
      u'CSWaspelltn',
      u'CSWaspelltr',
      u'CSWaspelluk',
      u'CSWaspelluz',
      u'CSWaspellvi',
      u'CSWaspellwa',
      u'CSWaspellyi',
      u'CSWaspellzu',
      u'CSWcgilib',
      u'CSWcksfv',
      u'CSWcommon',
      u'CSWdict',
      u'CSWdirvish',
      u'CSWerlang',
      u'CSWerlangdevel',
      u'CSWerlangdoc',
      u'CSWgkermit',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomespeech',
      u'CSWgsfonts',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWhylafax',
      u'CSWisaexec',
      u'CSWjasspame',
      u'CSWjasspamedede',
      u'CSWjasspameengb',
      u'CSWjasspameenus',
      u'CSWjasspameeses',
      u'CSWjasspamefifi',
      u'CSWjasspamefrfr',
      u'CSWjasspameitit',
      u'CSWjasspameplpl',
      u'CSWjasspameptpt',
      u'CSWjasspameruye',
      u'CSWjasspameruyo',
      u'CSWjetty6',
      u'CSWjetty6doc',
      u'CSWkicad',
      u'CSWkicadcommon',
      u'CSWlibgtop',
      u'CSWloudmouth',
      u'CSWlrzsz',
      u'CSWmailgraph',
      u'CSWmesademos',
      u'CSWminicom',
      u'CSWmpack',
      u'CSWmpage',
      u'CSWmpeg2codec',
      u'CSWmrtgpme',
      u'CSWnedit',
      u'CSWnethack',
      u'CSWocrad',
      u'CSWopenobex',
      u'CSWpgjdbc',
      u'CSWpmmailbox',
      u'CSWpstree',
      u'CSWrocksndiamonds',
      u'CSWsccs',
      u'CSWtla-tools',
      u'CSWwmclock',
      u'CSWwmmail'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/hr/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWvte'])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/share/locale/sr/LC_MESSAGES').AndReturn(
      [     u'CSWcommon',
      u'CSWgnomebackgrounds',
      u'CSWgnomemenus',
      u'CSWgnomemime2',
      u'CSWgnomethemes',
      u'CSWgstplugins',
      u'CSWgstreamer',
      u'CSWgtk',
      u'CSWgtkhtml31',
      u'CSWgtksourceview',
      u'CSWgtkspell',
      u'CSWlibgnomeprintui',
      u'CSWlibgtop',
      u'CSWmeld',
      u'CSWvte'])
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libproject.so.1', 'opt/csw/bin/sudo needs the libproject.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libdl.so.1', 'opt/csw/bin/sudo needs the libdl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libdl.so.1', 'opt/csw/bin/sudo needs the libdl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libsocket.so.1', 'opt/csw/bin/sudo needs the libsocket.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libsocket.so.1', 'opt/csw/bin/sudo needs the libsocket.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libnsl.so.1', 'opt/csw/bin/sudo needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libnsl.so.1', 'opt/csw/bin/sudo needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libintl.so.8', 'opt/csw/bin/sudo needs the libintl.so.8 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libc.so.1', 'opt/csw/bin/sudo needs the libc.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libc.so.1', 'opt/csw/bin/sudo needs the libc.so.1 soname')
    self.error_mgr_mock.GetElfdumpInfo('9d4ce2de1a3bd1cfbea3c52182b28f40').AndReturn(
        fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/librt.so.1', 'opt/csw/bin/sudoreplay needs the librt.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/librt.so.1', 'opt/csw/bin/sudoreplay needs the librt.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libz.so.1', 'opt/csw/bin/sudoreplay needs the libz.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libz.so.1', 'opt/csw/bin/sudoreplay needs the libz.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libintl.so.8', 'opt/csw/bin/sudoreplay needs the libintl.so.8 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libc.so.1', 'opt/csw/bin/sudoreplay needs the libc.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libc.so.1', 'opt/csw/bin/sudoreplay needs the libc.so.1 soname')
    self.error_mgr_mock.GetElfdumpInfo('b8c805c059ba17d6746ed03df6ae0d33').AndReturn(
        fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libc.so.1', 'opt/csw/libexec/sudo_noexec.so needs the libc.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libc.so.1', 'opt/csw/libexec/sudo_noexec.so needs the libc.so.1 soname')
    self.error_mgr_mock.GetElfdumpInfo('7b384e2526665e7eb4d4bb713569bc7c').AndReturn(
        fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libpam.so.1', 'opt/csw/libexec/sudoers.so needs the libpam.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libpam.so.1', 'opt/csw/libexec/sudoers.so needs the libpam.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libdl.so.1', 'opt/csw/libexec/sudoers.so needs the libdl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libdl.so.1', 'opt/csw/libexec/sudoers.so needs the libdl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libintl.so.8', 'opt/csw/libexec/sudoers.so needs the libintl.so.8 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libsocket.so.1', 'opt/csw/libexec/sudoers.so needs the libsocket.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libsocket.so.1', 'opt/csw/libexec/sudoers.so needs the libsocket.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libnsl.so.1', 'opt/csw/libexec/sudoers.so needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libnsl.so.1', 'opt/csw/libexec/sudoers.so needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libz.so.1', 'opt/csw/libexec/sudoers.so needs the libz.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libz.so.1', 'opt/csw/libexec/sudoers.so needs the libz.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libc.so.1', 'opt/csw/libexec/sudoers.so needs the libc.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libc.so.1', 'opt/csw/libexec/sudoers.so needs the libc.so.1 soname')
    self.error_mgr_mock.GetElfdumpInfo('38fbacb0c956be5e40c5347de847292a').AndReturn(
        fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))
    self.error_mgr_mock.NeedFile('CSWsudo', u'/opt/csw/lib/libintl.so.8', 'opt/csw/sbin/visudo needs the libintl.so.8 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libnsl.so.1', 'opt/csw/sbin/visudo needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libnsl.so.1', 'opt/csw/sbin/visudo needs the libnsl.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/usr/lib/libc.so.1', 'opt/csw/sbin/visudo needs the libc.so.1 soname')
    self.error_mgr_mock.NeedFile('CSWsudo', u'/lib/libc.so.1', 'opt/csw/sbin/visudo needs the libc.so.1 soname')
    self.error_mgr_mock.GetElfdumpInfo('c5ba07bfee948ef5ca08a1ba590e06f3').AndReturn(
        fake_pkgstats_composer.CreateFakeElfdumpInfo('foo.so.1'))

# class TestSetCheckDoubleDepends(CheckTestHelper, unittest.TestCase):
#   """This is a class that was used for debugging.
# 
#   It can be removed if becomes annoying.
#   """
#   FUNCTION_NAME = 'SetCheckLibraries'
# 
#   def SetMessenger(self):
#     """We want to have control over the messenger object."""
#     self.messenger = self.mox.CreateMock(stubs.MessengerStub)
# 
#   def testNeededFiles(self):
#     self.pkg_data = javasvn_stats
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCrun.so.1').AndReturn({u'/usr/lib': [u'SUNWlibC'], u'/usr/lib/sparcv9': [u'SUNWlibCx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libCstd.so.1').AndReturn({u'/usr/lib': [u'SUNWlibC'], u'/usr/lib/sparcv9': [u'SUNWlibCx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libapr-1.so.0').AndReturn({u'/opt/csw/apache2/lib': [u'CSWapache2rt'], u'/opt/csw/lib': [u'CSWapr'], u'/opt/csw/lib/sparcv9': [u'CSWapr']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({u'/usr/lib': [u'SUNWcsl'], u'/usr/lib/libp/sparcv9': [u'SUNWdplx'], u'/usr/lib/sparcv9': [u'SUNWcslx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn({u'/opt/csw/lib': [u'CSWggettextrt'], u'/opt/csw/lib/sparcv9': [u'CSWggettextrt']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_client-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_diff-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_fs-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_repos-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_subr-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsvn_wc-1.so.0').AndReturn({u'/opt/csw/lib/svn': [u'CSWsvn']})
# 
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn([u'CSWgdbm',
#       u'CSWlibnet', u'CSWbinutils', u'CSWcairomm', u'CSWtcpwrap',
#       u'CSWkrb5lib', u'CSWffcall', u'CSWflex', u'CSWfreeglut',
#       u'CSWgcc2corert', u'CSWgcc2g++rt', u'CSWgstreamer', u'CSWgtk',
#       u'CSWgtkspell', u'CSWimlib', u'CSWjove', u'CSWksh', u'CSWlibgphoto2',
#       u'CSWmikmod', u'CSWlibsigsegv', u'CSWlibxine', u'CSWmeanwhile',
#       u'CSWtcl', u'CSWtk', u'CSWocaml', u'CSWpmmd5', u'CSWpmlclemktxtsimple',
#       u'CSWpmtextdiff', u'CSWsasl', u'CSWpmmathinterpolate', u'CSWpmprmscheck',
#       u'CSWsbcl', u'CSWsdlsound', u'CSWsdlttf', u'CSWsilctoolkit', u'CSWt1lib',
#       u'CSWtaglibgcc', u'CSWtetex', u'CSWimaprt', u'CSWimap-devel',
#       u'CSWgnomevfs2', u'CSWlibgnomecups', u'CSWlibgnomeprint',
#       u'CSWlibgnomeprintui', u'CSWlibgsf', u'CSWhtmltidy',
#       u'CSWfoomaticfilters', u'CSWexpect', u'CSWnetpbm', u'CSWpmmailsendmail',
#       u'CSWgnomedocutils', u'CSWguilelib12', u'CSWlibgadu', u'CSWsetoolkit',
#       u'CSWntop', u'CSWtransfig', u'CSWsdlnet', u'CSWguile', u'CSWlibxml',
#       u'CSWxmms', u'CSWhevea', u'CSWopensprt', u'CSWplotutilrt',
#       u'CSWplotutildevel', u'CSWpstoeditrt', u'CSWpstoeditdevel',
#       u'CSWopenspdevel', u'CSWlibdvdread', u'CSWlibdvdreaddevel', u'CSWvte',
#       u'CSWcryptopp', u'CSWschilybase', u'CSWautogenrt', u'CSWlatex2html',
#       u'CSWfindutils', u'CSWfakeroot', u'CSWautogen', u'CSWpmmimetools',
#       u'CSWlibotf', u'CSWlibotfdevel', u'CSWgcc3corert', u'CSWgcc3g++rt',
#       u'CSWlibofxrt', u'CSWgcc3adart', u'CSWpmclsautouse', u'CSWpmlogmessage',
#       u'CSWpmlogmsgsimple', u'CSWpmsvnsimple', u'CSWpmunivrequire',
#       u'CSWpmiodigest', u'CSWpmsvnmirror', u'CSWlibm17n', u'CSWlibm17ndevel',
#       u'CSWzope', u'CSWpmhtmltmpl', u'CSWgcc3g77rt', u'CSWcommon',
#       u'CSWgnuplot', u'CSWpmx11protocol', u'CSWx11sshaskp', u'CSWmono',
#       u'CSWlibwnck', u'CSWgstplugins', u'CSWgnomemenus', u'CSWgnomedesktop',
#       u'CSWeel', u'CSWnautilus', u'CSWevince', u'CSWggv', u'CSWfacter',
#       u'CSWpmiopager', u'CSWxpm', u'CSWpmcfginifls', u'CSWlibxft2',
#       u'CSWpango', u'CSWgtk2', u'CSWgamin', u'CSWgcc3core', u'CSWlibbabl',
#       u'CSWgtkengines', u'CSWglib', u'CSWbonobo2', u'CSWlibgnomecanvas',
#       u'CSWgtksourceview', u'CSWgedit', u'CSWlibgnome', u'CSWlibbonoboui',
#       u'CSWlibgnomeui', u'CSWlibgegl'])
# 
#     self.error_mgr_mock.GetPkgByPath('/opt/csw/share/doc').AndReturn([u'CSWcairomm',
#       u'CSWtcpwrap', u'CSWgsfonts', u'CSWgstreamer', u'CSWksh',
#       u'CSWlibgphoto2', u'CSWlibxine', u'CSWmeanwhile', u'CSWsasl', u'CSWsbcl',
#       u'CSWsilctoolkit', u'CSWt1lib', u'CSWtaglibgcc', u'CSWtetex',
#       u'CSWgperf', u'CSWjikes', u'CSWdejagnu', u'CSWnetpbm', u'CSWsetoolkit',
#       u'CSWhevea', u'CSWopensprt', u'CSWopensp', u'CSWplotutilrt',
#       u'CSWplotutildevel', u'CSWpstoeditrt', u'CSWpstoedit',
#       u'CSWpstoeditdevel', u'CSWopenspdevel', u'CSWlibdvdread',
#       u'CSWlibdvdreaddevel', u'CSWschilyutils', u'CSWstar', u'CSWautogenrt',
#       u'CSWlatex2html', u'CSWautogen', u'CSWlibotf', u'CSWlibotfdevel',
#       u'CSWgcc3corert', u'CSWgcc3g++rt', u'CSWlibofxrt', u'CSWgcc3adart',
#       u'CSWgcc3rt', u'CSWgcc3g++', u'CSWgcc3ada', u'CSWgcc3', u'CSWlibm17n',
#       u'CSWm17ndb', u'CSWlibm17ndevel', u'CSWgcc2core', u'CSWgcc2g++',
#       u'CSWgcc3g77rt', u'CSWgcc3g77', u'CSWgcc4g95', u'CSWemacs-common',
#       u'CSWemacs-bin-common', u'CSWemacs', u'CSWcommon', u'CSWbashcmplt',
#       u'CSWcacertificates', u'CSWgstplugins', u'CSWgnomemenus',
#       u'CSWgnomedesktop', u'CSWnautilus', u'CSWlibofx', u'CSWgamin',
#       u'CSWpkgutil', u'CSWgcc3core', u'CSWgnomemime2', u'CSWglib'])
# 
#     for i in range(11):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(unicode), mox.IsA(str))

# class TestCheckUnusedSoname(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testUnusedSoname(self):
#     self.pkg_data = cadaver_stats
# 
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libcrypto.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libcurses.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libdl.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libexpat.so.1').AndReturn({
#       "/opt/csw/lib": [u'CSWexpat'], u'/opt/csw/lib/sparcv9': [u'CSWexpat']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libiconv.so.2').AndReturn({
#       "/opt/csw/lib": [u'CSWlibiconv2'], u'/opt/csw/lib/sparcv9': [u'CSWlibiconv2']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libintl.so.8').AndReturn({
#       "/opt/csw/lib": (u"CSWggettextrt",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libm.so.2').AndReturn(
#       {'/lib': [u'SUNWlibmsr'],
#        '/lib/sparcv9': [u'SUNWlibmsr'],
#        '/usr/lib': [u'SUNWlibms'],
#        '/usr/lib/sparcv9': [u'SUNWlibms']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libmd.so.1').AndReturn(
#       {'/lib': [u'SUNWclsr'],
#        '/lib/sparcv9': [u'SUNWclsr'],
#        '/usr/lib': [u'SUNWcls'],
#        '/usr/lib/sparcv9': [u'SUNWcls']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libmp.so.2').AndReturn(
#       {'/lib': [u'SUNWclsr'],
#        '/lib/sparcv9': [u'SUNWclsr'],
#        '/usr/lib': [u'SUNWcls'],
#        '/usr/lib/sparcv9': [u'SUNWcls']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libncurses.so.5').AndReturn({
#       "/opt/csw/lib": [u'CSWlibncurses5'], u'/opt/csw/lib/sparcv9': [u'CSWlibncurses5']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libneon.so.27').AndReturn({
#       "/opt/csw/lib": [u'CSWlibneon27'], u'/opt/csw/lib/sparcv9': [u'CSWlibneon27']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libreadline.so.6').AndReturn({
#       "/opt/csw/lib": [u'CSWlibreadline6'], u'/opt/csw/lib/sparcv9': [u'CSWlibreadline6']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libssl.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libz.so.1').AndReturn({
#       "/opt/csw/lib": (u"CSWlibz1",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibz1",),
#       "/usr/lib": (u"SUNWzlib")})
# 
# 
#     for common_path in ["/opt/csw/share/locale/it/LC_MESSAGES", "/opt/csw/bin",
#                         "/opt/csw/share/locale/en@quot/LC_MESSAGES", "/opt/csw/share/man",
#                         "/opt/csw/share/doc", "/opt/csw/share/locale/es/LC_MESSAGES"]:
#       self.error_mgr_mock.GetPkgByPath(common_path).AndReturn([u"CSWcommon"])
# 
#     for i in range(21):
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(str), mox.IsA(str))
# 
#     for soname in [ 'libintl.so.8' ]:
#       self.error_mgr_mock.ReportError(
#         'CSWcadaver', 'soname-unused',
#         soname + ' is needed by /opt/csw/bin/cadaver but never used')


# class TestCheckDirectBinding(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'SetCheckLibraries'
#   def testDirectBinding(self):
#     self.pkg_data = vsftpd_stats
# 
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libcrypto.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpam.so.1').AndReturn({
#       "/usr/dt/lib": (u"SUNWdtbas",),
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),
#     })
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('librt.so.1').AndReturn({
#       '/usr/lib': [u'SUNWcsl'],
#       '/usr/lib/sparcv9': [u'SUNWcslx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsendfile.so.1').AndReturn({
#       '/usr/lib': [u'SUNWcsl'],
#       '/usr/lib/sparcv9': [u'SUNWcslx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libssl.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
# 
#     for common_path in ["/opt/csw/share/man", "/var/opt/csw", "/opt/csw/sbin",
#         "/opt/csw/share/doc", "/etc/opt/csw"]:
#       self.error_mgr_mock.GetPkgByPath(common_path).AndReturn([u"CSWcommon"])
# 
#     for soname in [ 'libnsl.so.1', 'libpam.so.1', 'libsocket.so.1', 'librt.so.1',
#         'libsendfile.so.1', 'libssl.so.1.0.0', 'libcrypto.so.1.0.0',
#         'libc.so.1' ]:
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(str), mox.IsA(str))
# 
#     for soname in ['libssl.so.1.0.0']:
#       self.error_mgr_mock.ReportError(
#         'CSWvsftpd',
#         'no-direct-binding',
#         '/opt/csw/sbin/vsftpd is not directly bound to soname ' + soname)
# 
#   def testDirectBindingNoSyminfo(self):
#     self.pkg_data = vsftpd_stats
#     self.pkg_data[0]['binaries_elf_info']['opt/csw/sbin/vsftpd'] = {
#       'version definition': [],
#       'version needed': [],
#       'symbol table': [] }
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libc.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libcrypto.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libnsl.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libpam.so.1').AndReturn({
#       "/usr/dt/lib": (u"SUNWdtbas",),
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),
#     })
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('librt.so.1').AndReturn({
#       '/usr/lib': [u'SUNWcsl'],
#       '/usr/lib/sparcv9': [u'SUNWcslx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsendfile.so.1').AndReturn({
#       '/usr/lib': [u'SUNWcsl'],
#       '/usr/lib/sparcv9': [u'SUNWcslx']})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libsocket.so.1').AndReturn({
#       "/usr/lib": (u"SUNWcsl",),
#       "/usr/lib/sparcv9": (u"SUNWcslx"),})
#     self.error_mgr_mock.GetPathsAndPkgnamesByBasename('libssl.so.1.0.0').AndReturn({
#       "/opt/csw/lib": (u"CSWlibssl1-0-0",),
#       "/opt/csw/lib/sparcv9": (u"CSWlibssl1-0-0",)})
# 
#     for common_path in ["/opt/csw/share/man", "/var/opt/csw", "/opt/csw/sbin",
#                         "/opt/csw/share/doc", "/etc/opt/csw"]:
#       self.error_mgr_mock.GetPkgByPath(common_path).AndReturn([u"CSWcommon"])
# 
#     for soname in [ 'libnsl.so.1', 'libpam.so.1', 'libsocket.so.1', 'librt.so.1',
#                     'libsendfile.so.1', 'libssl.so.1.0.0', 'libcrypto.so.1.0.0',
#                     'libc.so.1' ]:
#       self.error_mgr_mock.NeedFile(
#           mox.IsA(str), mox.IsA(str), mox.IsA(str))
# 
#     for soname in ['libcrypto.so.1.0.0', 'libpam.so.1', 'libsendfile.so.1',
#         'libssl.so.1.0.0']:
#       self.error_mgr_mock.ReportError(
#         'CSWvsftpd',
#         'no-direct-binding',
#         '/opt/csw/sbin/vsftpd is not directly bound to soname ' + soname)


# class TestCheckWrongArchitecture(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckWrongArchitecture'
#   def testSparcBinariesInIntelPackage(self):
#     self.pkg_data = neon_stats[0]
#     self.error_mgr_mock.ReportError(
#         'binary-wrong-architecture',
#         'file=opt/csw/lib/sparcv9/libneon.so.27.2.0 pkginfo-says=i386 actual-binary=sparc')
#     self.error_mgr_mock.ReportError(
#         'binary-wrong-architecture',
#         'file=opt/csw/lib/sparcv9/libneon.so.26.0.4 pkginfo-says=i386 actual-binary=sparc')


# class TestCheckSharedLibraryNamingPolicy(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckSharedLibraryNamingPolicy'
#   def testBad(self):
#     self.pkg_data = bdb48_stats[0]
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/libdb-4.8.so soname=libdb-4.8.so '
#         'pkgname=CSWbdb48 expected=CSWlibdb4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/libdb_cxx-4.8.so soname=libdb_cxx-4.8.so '
#         'pkgname=CSWbdb48 expected=CSWlibdb-cxx4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/libdb_java-4.8.so '
#         'soname=libdb_java-4.8.so pkgname=CSWbdb48 '
#         'expected=CSWlibdb-java4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/libdb_tcl-4.8.so soname=libdb_tcl-4.8.so '
#         'pkgname=CSWbdb48 expected=CSWlibdb-tcl4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/sparcv9/libdb-4.8.so soname=libdb-4.8.so '
#         'pkgname=CSWbdb48 expected=CSWlibdb4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-pkgname-mismatch',
#         'file=opt/csw/bdb48/lib/sparcv9/libdb_cxx-4.8.so '
#         'soname=libdb_cxx-4.8.so pkgname=CSWbdb48 '
#         'expected=CSWlibdb-cxx4-8-bdb48')
#     self.error_mgr_mock.ReportError(
#           'shared-lib-pkgname-mismatch',
#           'file=opt/csw/bdb48/lib/sparcv9/libdb_java-4.8.so '
#           'soname=libdb_java-4.8.so pkgname=CSWbdb48 '
#           'expected=CSWlibdb-java4-8-bdb48')

# class TestCheckSharedLibraryPkgDoesNotHaveTheSoFile(CheckTestHelper,
#                                                     unittest.TestCase):
#   FUNCTION_NAME = 'CheckSharedLibraryPkgDoesNotHaveTheSoFile'
# 
#   def testBad(self):
#     self.pkg_data = neon_stats[0]
#     self.error_mgr_mock.ReportError(
#         'shared-lib-package-contains-so-symlink',
#         'file=/opt/csw/lib/libneon.so')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-package-contains-so-symlink',
#         'file=/opt/csw/lib/sparcv9/libneon.so')
#     for j in range(2):
#       for i in range(7):
#         self.messenger.SuggestGarLine(mox.IsA(str))
#       self.messenger.Message(mox.IsA(str))
# 
#   def SetMessenger(self):
#     """Overriding this method to use mock instead of a stub."""
#     self.messenger = self.mox.CreateMock(stubs.MessengerStub)
# 
#   def testSuggestions(self):
#     self.pkg_data = neon_stats[0]
#     self.error_mgr_mock.ReportError(
#         'shared-lib-package-contains-so-symlink',
#         'file=/opt/csw/lib/libneon.so')
#     self.error_mgr_mock.ReportError(
#         'shared-lib-package-contains-so-symlink',
#         'file=/opt/csw/lib/sparcv9/libneon.so')
#     self.messenger.SuggestGarLine("# (If CSWneon-dev doesn't exist yet)")
#     self.messenger.SuggestGarLine('PACKAGES += CSWneon-dev')
#     self.messenger.SuggestGarLine('CATALOGNAME_CSWneon-dev = neon_dev')
#     self.messenger.SuggestGarLine(
#         'SPKG_DESC_CSWneon-dev += $(DESCRIPTION), development files')
#     self.messenger.SuggestGarLine(
#         'PKGFILES_CSWneon-dev += /opt/csw/lib/libneon.so')
#     self.messenger.SuggestGarLine('# Maybe also the generic:')
#     self.messenger.SuggestGarLine(
#         '# PKGFILES_CSWneon-dev += $(PKGFILES_DEVEL)')
#     self.messenger.Message(mox.IsA(str))
#     self.messenger.SuggestGarLine("# (If CSWneon-dev doesn't exist yet)")
#     self.messenger.SuggestGarLine('PACKAGES += CSWneon-dev')
#     self.messenger.SuggestGarLine('CATALOGNAME_CSWneon-dev = neon_dev')
#     self.messenger.SuggestGarLine(
#         'SPKG_DESC_CSWneon-dev += $(DESCRIPTION), development files')
#     self.messenger.SuggestGarLine(
#         'PKGFILES_CSWneon-dev += /opt/csw/lib/sparcv9/libneon.so')
#     self.messenger.SuggestGarLine('# Maybe also the generic:')
#     self.messenger.SuggestGarLine(
#         '# PKGFILES_CSWneon-dev += $(PKGFILES_DEVEL)')
#     self.messenger.Message(mox.IsA(str))


# class TestCheckSharedLibraryNameMustBeAsubstringOfSonameGood(
#     CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckSharedLibraryNameMustBeAsubstringOfSoname'
#   def testGood(self):
#     self.pkg_data = neon_stats[0]
#     # TODO: Implement this
# 
#   def testBad(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["binaries_dump_info"][3]["base_name"] = "foo.so.1"
#     self.error_mgr_mock.ReportError(
#         'soname-not-part-of-filename',
#         'soname=libneon.so.27 filename=foo.so.1')


# class TestCheckLicenseFilePlacementLicense(CheckTestHelper,
#                                            unittest.TestCase):
#   FUNCTION_NAME = 'CheckLicenseFilePlacement'
#   def testBadLicensePlacement(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["pkgmap"].append({
#       "class": "none", "type": "f", "line": "",
#       "user": "root", "group": "bin", "mode": '0755',
#       "path": "/opt/csw/share/doc/alien/license",
#     })
#     self.error_mgr_mock.ReportError(
#         'wrong-docdir',
#         'expected=/opt/csw/shared/doc/neon/... '
#         'in-package=/opt/csw/share/doc/alien/license')
# 
#   def testGoodRandomFileWithSuffix(self):
#     """A differently suffixed file should not trigger an error."""
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["pkgmap"].append({
#       "class": "none", "type": "f", "line": "",
#       "user": "root", "group": "bin", "mode": '0755',
#       "path": "/opt/csw/share/doc/alien/license.html",
#     })
# 
#   def testGoodRandomFile(self):
#     "A random file should not trigger the message; only license files."
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["pkgmap"].append({
#       "class": "none", "type": "f", "line": "",
#       "user": "root", "group": "bin", "mode": '0755',
#       "path": "/opt/csw/share/doc/alien/random_file",
#     })


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
        self.TestPkgmapEntry(entry_path='/opt/csw/lib/libneon.so.27',
          type_='s', target='libneon.so.27.2.0'))
    self.error_mgr_mock.NeedFile('/opt/csw/lib', mox.IsA(str))


class TestCheckBaseDirsNotNoneClass(CheckTestHelper,
                                    unittest.TestCase):
  FUNCTION_NAME = 'CheckBaseDirs'

  def testNeedBaseDir(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        self.TestPkgmapEntry(
          entry_path='/etc/opt/csw/init.d/foo',
          class_='cswinitsmf'
          )
        )
    self.error_mgr_mock.NeedFile('/etc/opt/csw/init.d', mox.IsA(str))


class TestCheckDanglingSymlinks(CheckTestHelper,
                                unittest.TestCase):
  FUNCTION_NAME = 'CheckDanglingSymlinks'

  def testSymlinkTargetNeeded(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        self.TestPkgmapEntry(
          entry_path='/opt/csw/lib/postgresql/9.0/lib/libpq.so.5',
          class_='none',
          type_='s',
          target='/opt/csw/lib/libpq.so.5',
        ))
    self.error_mgr_mock.NeedFile('/opt/csw/lib/libpq.so.5', mox.IsA(str))

  # Hardlinks work the same way.
  def disabledtestHardlinkTargetNeeded(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    self.pkg_data["pkgmap"].append(
        self.TestPkgmapEntry(
          entry_path='/opt/csw/lib/postgresql/9.0/lib/libpq.so.5',
          class_='none',
          type_='l',
          target='/opt/csw/lib/libpq.so.5',
        ))
    self.error_mgr_mock.NeedFile('/opt/csw/lib/libpq.so.5', mox.IsA(str))


# class TestCheckPrefixDirs(CheckTestHelper,
#                           unittest.TestCase):
#   FUNCTION_NAME = 'CheckPrefixDirs'
# 
#   def testGoodPrefix(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     self.pkg_data["pkgmap"].append(
#         {'class': 'none',
#          'group': None,
#          'line': None,
#          'mode': None,
#          'path': '/opt/csw/bin/foo',
#          'type': 'f',
#          'user': None,
#          'target': None})
# 
#   def testBadPrefix(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     self.pkg_data["pkgmap"].append(
#         {'class': 'none',
#          'group': None,
#          'line': None,
#          'mode': None,
#          'path': '/opt/cswbin/foo',
#          'type': 'f',
#          'user': None,
#          'target': None})
#     self.error_mgr_mock.ReportError(
#         'bad-location-of-file',
#         'file=/opt/cswbin/foo')
# 
#   def testGoodVar(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     self.pkg_data["pkgmap"].append(
#         {'class': 'none',
#          'group': None,
#          'line': None,
#          'mode': None,
#          'path': '/var/opt/csw/foo',
#          'type': 'f',
#          'user': None,
#          'target': None})
# 
#   def testBadVar(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     self.pkg_data["pkgmap"].append(
#         {'class': 'none',
#          'group': None,
#          'line': None,
#          'mode': None,
#          'path': '/var/foo',
#          'type': 'f',
#          'user': None,
#          'target': None})
#     self.error_mgr_mock.ReportError(
#         'bad-location-of-file',
#         'file=/var/foo')


# class TestCheckSonameMustNotBeEqualToFileNameIfFilenameEndsWithSo(
#     CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = ('CheckSonameMustNotBeEqualToFileName'
#                    'IfFilenameEndsWithSo')
#   FOO_METADATA = {
#       'endian': 'Little endian',
#       'machine_id': 3,
#       'mime_type': 'application/x-sharedlib; charset=binary',
#       'mime_type_by_hachoir': u'application/x-executable',
#       'path': 'opt/csw/lib/libfoo.so',
#   }
# 
#   def testBad(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["binaries_dump_info"][0]["soname"] = "libfoo.so"
#     self.pkg_data["binaries_dump_info"][0]["base_name"] = "libfoo.so"
#     self.pkg_data["binaries_dump_info"][0]["path"] = "opt/csw/lib/libfoo.so"
#     self.pkg_data["files_metadata"].append(self.FOO_METADATA)
#     self.error_mgr_mock.ReportError(
#         'soname-equals-filename',
#         'file=/opt/csw/lib/libfoo.so')
# 
#   def testGood(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["binaries_dump_info"][0]["soname"] = "libfoo.so.1"
#     self.pkg_data["binaries_dump_info"][0]["base_name"] = "libfoo.so.1"
#     self.pkg_data["files_metadata"].append(self.FOO_METADATA)
# 
#   def testGoodMercurialExample(self):
#     self.pkg_data = mercurial_stats[0]


# class TestCheckCatalognameMatchesPkgname(CheckTestHelper,
#                                          unittest.TestCase):
#   FUNCTION_NAME = 'CheckCatalognameMatchesPkgname'
# 
#   def testMismatch(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     basic_stats = self.pkg_data["basic_stats"]
#     basic_stats["catalogname"] = "foo_bar"
#     basic_stats["pkgname"] = "CSWfoo-bar-baz"
#     self.error_mgr_mock.ReportError(
#         'catalogname-does-not-match-pkgname',
#         'pkgname=CSWfoo-bar-baz catalogname=foo_bar '
#         'expected-catalogname=foo_bar_baz')
# 
#   def testGoodMatch(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])


# class TestCheckCatalognameMatchesPkgname(CheckTestHelper,
#                                          unittest.TestCase):
#   FUNCTION_NAME = 'CheckPkginfoOpencswRepository'
# 
#   def testRepositoryInfoGood(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     # No errors reported.
# 
#   def testRepositoryInfoMissing(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     del self.pkg_data["pkginfo"]["OPENCSW_REPOSITORY"]
#     self.error_mgr_mock.ReportError('pkginfo-opencsw-repository-missing')
# 
#   def testRepositoryInfoUncommitted(self):
#     self.pkg_data = copy.deepcopy(tree_stats[0])
#     self.pkg_data["pkginfo"]["OPENCSW_REPOSITORY"] = (
#         "https://gar.svn.sourceforge.net/svnroot/gar/"
#         "csw/mgar/pkg/puppet/trunk@UNCOMMITTED")
#     self.error_mgr_mock.ReportError('pkginfo-opencsw-repository-uncommitted')
# 
# 
# class TestCheckAlternativesDependency(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckAlternativesDependency'
#   ALTERNATIVES_EXECUTABLE = "/opt/csw/sbin/alternatives"
#   def testAlternativesNeeded(self):
#     self.pkg_data["pkgmap"].append({
#       'class': 'cswalternatives',
#       'group': 'bin',
#       'line': ('1 f cswalternatives /opt/csw/share/alternatives/sendmail '
#                '0644 root bin 408 36322 1308243112'),
#       'mode': '0644',
#       'path': '/opt/csw/share/alternatives/sendmail',
#       'target': None,
#       'type': 'f',
#       'user': 'root',
#     })
#     self.error_mgr_mock.NeedFile(
#         self.ALTERNATIVES_EXECUTABLE,
#         "The alternatives subsystem is used")


# class TestCheckSharedLibrarySoExtension(CheckTestHelper, unittest.TestCase):
#   FUNCTION_NAME = 'CheckSharedLibrarySoExtension'
#   def testGoodExtension(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
# 
#   def testBadExtension(self):
#     self.pkg_data = copy.deepcopy(neon_stats[0])
#     self.pkg_data["files_metadata"][11]["path"] = "foo.1"
#     self.error_mgr_mock.ReportError(
#         'shared-library-missing-dot-so', 'file=foo.1')


class TestCheck64bitBinariesPresence(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'Check64bitBinariesPresence'
  def testFull32bitsPackage(self):
    self.pkg_data = copy.deepcopy(vsftpd_stats[0])

  def testMissingIntel64bitLibraries(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    # Stripping 64-bit binaries for the test.
    bdi = self.pkg_data['binaries_dump_info']
    bdi = [representations.BinaryDumpInfo._make(x)
           for x in bdi]
    bdi = [x for x in bdi if 'amd64' not in x.path]
    self.pkg_data['binaries_dump_info'] = bdi
    self.error_mgr_mock.ReportError('64-bit-binaries-missing')

  def testMissingPkginfoEntry(self):
    del self.pkg_data["pkginfo"]["OPENCSW_MODE64"]
    self.error_mgr_mock.ReportError(
        'pkginfo-opencsw-mode64-missing',
        'OPENCSW_MODE64 is missing from pkginfo')

  def testMissingSparc64bitLibraries(self):
    # sudo contains a shared library, and is 32-bit only
    self.pkg_data = copy.deepcopy(sudo_stats[0])
    self.pkg_data["pkginfo"]["OPENCSW_MODE64"] = '32/64'
    self.error_mgr_mock.ReportError('64-bit-binaries-missing')

  def testMissing64bitExecutable(self):
    self.pkg_data = copy.deepcopy(sudo_stats[0])
    self.pkg_data["pkginfo"]["OPENCSW_MODE64"] = '32/64/isaexec'
    self.error_mgr_mock.ReportError('64-bit-binaries-missing')


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


class TestCheckBadContent(CheckTestHelper, unittest.TestCase):
  FUNCTION_NAME = 'CheckBadContent'

  def testGoodFiles(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data['bad_paths'] = {
        'bad-regex': ['root/opt/csw/share/doc/foo'],
    }

  def testBadFiles(self):
    self.pkg_data = copy.deepcopy(neon_stats[0])
    self.pkg_data['bad_paths'] = {
        'bad-regex': ['root/opt/csw/bin/foo'],
    }
    self.error_mgr_mock.ReportError(
        'file-with-bad-content',
        'bad-regex root/opt/csw/bin/foo')


if __name__ == '__main__':
  unittest.main()
