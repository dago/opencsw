#!/usr/bin/env python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import checkpkg_lib
import copy
import cPickle
import database
import inspective_package
import models
import mox
import package_stats
import package_stats
import pprint
import sqlobject
import tag
import test_base
from testdata import stubs

from testdata.neon_stats import pkgstats as neon_stats


class CheckpkgManager2UnitTest(mox.MoxTestBase):

  def testSingleTag(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = u'# Tags reported by testname module\nCSWfoo: foo-tag foo-info\n'
    self.assertEqual(expected, unicode(tags_report))

  def testThreeTags(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    tags = {
        "CSWfoo": [
          tag.CheckpkgTag("CSWfoo", "foo-tag", "foo-info"),
          tag.CheckpkgTag("CSWfoo", "bar-tag", "bar-info"),
          tag.CheckpkgTag("CSWfoo", "baz-tag"),
        ],
    }
    screen_report, tags_report = m.FormatReports(tags, [], [])
    expected = (u'# Tags reported by testname module\n'
                u'CSWfoo: foo-tag foo-info\n'
                u'CSWfoo: bar-tag bar-info\n'
                u'CSWfoo: baz-tag\n')
    self.assertEqual(expected, unicode(tags_report))

  def testGetAllTags(self):
    # Does not run any checks, because they are unregistered.  However,
    # needfile and needpkg mechanisms are active.
    #
    # Disabling this check for now, because there are issues with mocking out
    # some of the objects.
    # TODO(maciej): Enable this check again.
    return
    self.mox.StubOutWithMock(checkpkg_lib, 'IndividualCheckInterface',
        use_mock_anything=True)
    self.mox.StubOutWithMock(checkpkg_lib, 'SetCheckInterface',
        use_mock_anything=True)
    # checkpkg_interface_mock = self.mox.CreateMock(
    #     checkpkg_lib.IndividualCheckInterface)
    # Throws:
    # UnknownMethodCallError: Method called is not a member of the
    # object: GetPkgByPath
    checkpkg_interface_mock = self.mox.CreateMockAnything()
    # checkpkg_interface_mock = self.mox.CreateMock(
    #     checkpkg_lib.IndividualCheckInterface)
    set_interface_mock = self.mox.CreateMockAnything()
    # checkpkg_interface_mock.GetPkgByPath("/opt/csw/bin/foo").AndReturn(
    #     ["CSWbar", "CSWbaz"])
    set_interface_mock.errors = []
    set_interface_mock.needed_files = []
    set_interface_mock.needed_pkgs = []
    checkpkg_interface_mock.errors = []
    checkpkg_interface_mock.needed_files = [
        checkpkg_lib.NeededFile("CSWneon", "/opt/csw/bin/foo", "Because!"),
    ]
    checkpkg_interface_mock.needed_pkgs = []
    self.mox.StubOutWithMock(checkpkg_lib, 'Catalog',
        use_mock_anything=True)
    checkpkg_lib.IndividualCheckInterface(
        'CSWneon', '5.9', 'sparc', 'unstable', catalog_mock).AndReturn(
            checkpkg_interface_mock)
    checkpkg_lib.SetCheckInterface(
        'CSWneon', '5.9', 'sparc', 'unstable', catalog_mock).AndReturn(
            set_interface_mock)
    stat_obj = self.mox.CreateMockAnything()
    data_obj = self.mox.CreateMockAnything()
    stat_obj.data_obj = data_obj
    pkg_stats = copy.deepcopy(neon_stats[0])
    # Resetting the dependencies so that it doesn't report surplus deps.
    pkg_stats["depends"] = []
    data_obj.pickle = cPickle.dumps(pkg_stats)
    checkpkg_interface_mock.ReportErrorForPkgname(
        'CSWneon', 'missing-dependency', 'CSWbar or CSWbaz')
    catalog_mock.GetPkgByPath('/opt/csw/bin/foo', '5.9', 'sparc',
        'unstable').AndReturn(["CSWbar", "CSWbaz"])
    self.mox.ReplayAll()
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    # m._AutoregisterChecks()
    errors, messages, gar_lines = m.GetAllTags([stat_obj])
    self.mox.VerifyAll()
    # self.assertEquals(
    #     {'CSWneon': [tag.CheckpkgTag('CSWneon', 'missing-dependency', 'CSWbar or CSWbaz')]},
    #     errors)
    expected_messages =  [
        u'Dependency issues of CSWneon:',
        u'CSWbar is needed by CSWneon, because:',
        u' - Because!',
        u'RUNTIME_DEP_PKGS_CSWneon += CSWbar',
        u'CSWbaz is needed by CSWneon, because:',
        u' - Because!',
        u'RUNTIME_DEP_PKGS_CSWneon += CSWbaz',
    ]
    self.assertEquals(expected_messages, messages)
    expected_gar_lines = [
        '# One of the following:',
        '  RUNTIME_DEP_PKGS_CSWneon += CSWbar',
        '  RUNTIME_DEP_PKGS_CSWneon += CSWbaz',
        '# (end of the list of alternative dependencies)']
    self.assertEquals(expected_gar_lines, gar_lines)

  def test_ReportDependencies(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    checkpkg_interface_mock = self.mox.CreateMock(
        checkpkg_lib.IndividualCheckInterface)
    needed_files = [
        ("CSWfoo", "/opt/csw/bin/needed_file", "reason1"),
    ]
    needed_pkgs = []
    messenger_stub = stubs.MessengerStub()
    declared_deps_by_pkgname = {
        "CSWfoo": frozenset([
          "CSWbar-1",
          "CSWbar-2",
        ]),
    }
    checkpkg_interface_mock.GetPkgByPath('/opt/csw/bin/needed_file').AndReturn(
        ["CSWfoo-one", "CSWfoo-two"]
    )
    checkpkg_interface_mock.ReportErrorForPkgname(
        'CSWfoo', 'missing-dependency', 'CSWfoo-one or CSWfoo-two')
    checkpkg_interface_mock.ReportErrorForPkgname(
        'CSWfoo', 'surplus-dependency', 'CSWbar-2')
    checkpkg_interface_mock.ReportErrorForPkgname(
        'CSWfoo', 'surplus-dependency', 'CSWbar-1')
    self.mox.ReplayAll()
    m._ReportDependencies(checkpkg_interface_mock,
                          needed_files,
                          needed_pkgs,
                          messenger_stub,
                          declared_deps_by_pkgname)

  def test_ReportDependenciesDirProvidedBySelf(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    checkpkg_interface_mock = self.mox.CreateMock(
        checkpkg_lib.IndividualCheckInterface)
    needed_files = [
        ("CSWfoo", "/opt/csw/share/man/man1m", "reason1"),
    ]
    needed_pkgs = []
    messenger_stub = stubs.MessengerStub()
    declared_deps_by_pkgname = {"CSWfoo": frozenset()}
    checkpkg_interface_mock.GetPkgByPath('/opt/csw/share/man/man1m').AndReturn(
        ["CSWfoo", "CSWfoo-one", "CSWfoo-two"]
    )
    # Should not report any dependencies; the /opt/csw/share/man/man1m path is
    # provided by the package itself.
    self.mox.ReplayAll()
    m._ReportDependencies(checkpkg_interface_mock,
                          needed_files,
                          needed_pkgs,
                          messenger_stub,
                          declared_deps_by_pkgname)

  def testSurplusDeps(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    potential_req_pkgs = set([u"CSWbar"])
    declared_deps = set([u"CSWbar", u"CSWsurplus"])
    expected = set(["CSWsurplus"])
    self.assertEquals(
        expected,
        m._GetSurplusDeps("CSWfoo", potential_req_pkgs, declared_deps))

  def testMissingDepsFromReasonGroups(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    reason_groups = [
        [(u"CSWfoo1", ""),
         (u"CSWfoo2", "")],
        [(u"CSWbar", "")],
    ]
    declared_deps = set([u"CSWfoo2"])
    expected = [[u"CSWbar"]]
    result = m._MissingDepsFromReasonGroups(
        "CSWfoo", reason_groups, declared_deps)
    self.assertEqual(expected, result)

  def testMissingDepsFromReasonGroupsTwo(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    reason_groups = [
        [(u"CSWfoo1", "reason 1"),
         (u"CSWfoo2", "reason 1")],
        [(u"CSWbar", "reason 2")],
    ]
    declared_deps = set([])
    expected = [[u'CSWfoo1', u'CSWfoo2'], [u'CSWbar']]
    result = m._MissingDepsFromReasonGroups(
        "CSWfoo", reason_groups, declared_deps)
    self.assertEqual(result, expected)

  def testMissingDepsFromReasonGroupsSelf(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    reason_groups = [
        [(u"CSWfoo", "reason 1"),
         (u"CSWfoo2", "reason 1")],
    ]
    declared_deps = set([])
    expected = []
    result = m._MissingDepsFromReasonGroups(
        "CSWfoo", reason_groups, declared_deps)
    self.assertEqual(result, expected)

  def test_RemovePkgsFromMissing(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    missing_dep_groups = [['CSWfoo-one', 'CSWfoo']]
    expected = set(
        [
          frozenset(['CSWfoo', 'CSWfoo-one']),
        ]
    )
    result = m._RemovePkgsFromMissing("CSWbaz", missing_dep_groups)
    self.assertEqual(expected, result)

  def testReportMissingDependenciesOne(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    error_mgr_mock = self.mox.CreateMock(checkpkg_lib.IndividualCheckInterface)
    declared_deps = frozenset([u"CSWfoo"])
    req_pkgs_reasons = [
        [
          (u"CSWfoo", "reason 1"),
          (u"CSWfoo-2", "reason 2"),
        ],
        [
          ("CSWbar", "reason 3"),
        ],
    ]
    error_mgr_mock.ReportErrorForPkgname(
        'CSWexamined', 'missing-dependency', 'CSWbar')
    self.mox.ReplayAll()
    m._ReportMissingDependencies(
        error_mgr_mock, "CSWexamined", declared_deps, req_pkgs_reasons)

  def testReportMissingDependenciesTwo(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    error_mgr_mock = self.mox.CreateMock(checkpkg_lib.IndividualCheckInterface)
    declared_deps = frozenset([])
    req_pkgs_reasons = [
        [
          (u"CSWfoo-1", "reason 1"),
          (u"CSWfoo-2", "reason 1"),
        ],
    ]
    error_mgr_mock.ReportErrorForPkgname(
        'CSWexamined', 'missing-dependency', u'CSWfoo-1 or CSWfoo-2')
    self.mox.ReplayAll()
    m._ReportMissingDependencies(
        error_mgr_mock, "CSWexamined", declared_deps, req_pkgs_reasons)

  def DisabledtestReportMissingDependenciesIntegration(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    checkpkg_interface = checkpkg_lib.IndividualCheckInterface(
          "CSWfoo", "AlienOS5.2", "sparkle", "calcified", catalog_mock)
    declared_deps_by_pkgname = {
        "CSWfoo": frozenset(),
    }
    declared_deps = frozenset([])
    pkgs_providing_path = ["CSWproviding-%02d" % x for x in range(20)]
    catalog_mock.GetPkgByPath(
        '/opt/csw/sbin',
        'AlienOS5.2',
        'sparkle',
        'calcified').AndReturn(pkgs_providing_path)
    self.mox.ReplayAll()
    checkpkg_interface.NeedFile("/opt/csw/sbin", "reason 1")
    needed_files = checkpkg_interface.needed_files
    needed_pkgs = checkpkg_interface.needed_pkgs
    messenger_stub = stubs.MessengerStub()
    m._ReportDependencies(
        checkpkg_interface,
        needed_files,
        needed_pkgs,
        messenger_stub,
        declared_deps_by_pkgname)
    self.assertEqual(1, len(checkpkg_interface.errors))
    self.assertEqual(
        " or ".join(sorted(pkgs_providing_path)),
        checkpkg_interface.errors[0].tag_info)

  def testReportMissingDependenciesSurplus(self):
    m = checkpkg_lib.CheckpkgManager2(
            "testname", [], "5.9", "sparc", "unstable")
    error_mgr_mock = self.mox.CreateMock(checkpkg_lib.IndividualCheckInterface)
    declared_deps = frozenset([u"CSWfoo", u"CSWbar", u"CSWsurplus"])
    req_pkgs_reasons = [
        [
          (u"CSWfoo", "reason 1"),
          (u"CSWfoo-2", "reason 2"),
        ],
        [
          ("CSWbar", "reason 3"),
        ],
    ]
    error_mgr_mock.ReportErrorForPkgname(
        'CSWexamined', 'surplus-dependency', u'CSWsurplus')
    self.mox.ReplayAll()
    m._ReportMissingDependencies(
        error_mgr_mock, "CSWexamined", declared_deps, req_pkgs_reasons)


class CheckpkgManager2DatabaseIntegrationTest(
    test_base.SqlObjectTestMixin, unittest.TestCase):

  def setUp(self):
    super(CheckpkgManager2DatabaseIntegrationTest, self).setUp()
    self.mox = mox.Mox()

  def testInsertNeon(self):
    self.dbc.InitialDataImport()
    sqo_pkg = package_stats.PackageStats.SaveStats(neon_stats[0], True)
    cm = checkpkg_lib.CheckpkgManager2(
        "testname", [sqo_pkg], "SunOS5.9", "sparc", "unstable",
        show_progress=False)
    cm.Run()
    # Verifying that there are some reported error tags.
    self.assertTrue(list(models.CheckpkgErrorTag.select()))

  def testReRunCheckpkg(self):
    """Error tags should not accumulate.

    FIXME(maciej): Figure out what's wrong with this one: It errors out.
    """
    self.dbc.InitialDataImport()
    sqo_pkg = package_stats.PackageStats.SaveStats(neon_stats[0], True)
    cm = checkpkg_lib.CheckpkgManager2(
        "testname", [sqo_pkg], "SunOS5.9", "sparc", "unstable",
        show_progress=False)
    before_count = models.CheckpkgErrorTag.selectBy(srv4_file=sqo_pkg).count()
    cm.Run()
    first_run_count = models.CheckpkgErrorTag.selectBy(srv4_file=sqo_pkg).count()
    cm.Run()
    second_run_count = models.CheckpkgErrorTag.selectBy(srv4_file=sqo_pkg).count()
    self.assertEquals(0, before_count)
    self.assertEquals(first_run_count, second_run_count)


class IndividualCheckInterfaceUnitTest(mox.MoxTestBase):

  def testNeededFile(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    self.mox.ReplayAll()
    ici = checkpkg_lib.IndividualCheckInterface(
        'CSWfoo', 'AlienOS5.1', 'amd65', 'calcified', catalog_mock, {})
    ici.NeedFile("/opt/csw/bin/foo", "Because.")
    # This might look like encapsulation violation, but I think this is
    # a reasonable interface to that class.
    self.assertEqual(1, len(ici.needed_files))
    needed_file = ici.needed_files[0]
    self.assertEqual("CSWfoo", needed_file.pkgname)
    self.assertEqual("/opt/csw/bin/foo", needed_file.full_path)
    self.assertEqual("Because.", needed_file.reason)

  def testGetPkgByPathSelf(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    pkg_set_files = {
        "CSWfoo": frozenset([
          ("/opt/csw", "bin"),
          ("/opt/csw/bin", "foo"),
        ]),
        "CSWbar": frozenset([
          ("/opt/csw/bin", "bar"),
        ]),
    }
    catalog_mock.GetPkgByPath(
        '/opt/csw/bin', 'AlienOS5.1', 'amd65', 'calcified').AndReturn(frozenset())
    self.mox.ReplayAll()
    ici = checkpkg_lib.IndividualCheckInterface(
        'CSWfoo', 'AlienOS5.1', 'amd65', 'calcified', catalog_mock, pkg_set_files)
    pkgs = ici.GetPkgByPath("/opt/csw/bin")
    self.assertEqual(frozenset(["CSWfoo"]), pkgs)

  def testGetPathsAndPkgnamesByBasename(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    pkg_set_files = {
        "CSWfoo": frozenset([
          ("/opt/csw", "bin"),
          ("/opt/csw/bin", "foo"),
        ]),
        "CSWbar": frozenset([
          ("/opt/csw/bin", "bar"),
        ]),
    }
    in_catalog = {
        "/opt/csw/bin": ["CSWbar"],
        "/opt/csw/share/unrelated": ["CSWbaz"],
    }
    catalog_mock.GetPathsAndPkgnamesByBasename(
        'foo', 'AlienOS5.1', 'amd65', 'calcified').AndReturn(in_catalog)
    expected = {
        "/opt/csw/bin": ["CSWfoo"],
        "/opt/csw/share/unrelated": ["CSWbaz"],
    }
    self.mox.ReplayAll()
    ici = checkpkg_lib.IndividualCheckInterface(
        'CSWfoo', 'AlienOS5.1', 'amd65', 'calcified', catalog_mock, pkg_set_files)
    paths_and_pkgnames = ici.GetPathsAndPkgnamesByBasename("foo")
    self.assertEqual(expected, paths_and_pkgnames)

  def testNeededPackage(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    self.mox.ReplayAll()
    ici = checkpkg_lib.IndividualCheckInterface(
        'CSWfoo', 'AlienOS5.1', 'amd65', 'calcified', catalog_mock, {})
    ici.NeedPackage("CSWbar", "Because foo needs bar")
    # This might look like encapsulation violation, but I think this is
    # a reasonable interface to that class.
    self.assertEqual(1, len(ici.needed_pkgs))
    needed_pkg = ici.needed_pkgs[0]
    self.assertEqual("CSWfoo", needed_pkg.pkgname)
    self.assertEqual("CSWbar", needed_pkg.needed_pkg)
    self.assertEqual("Because foo needs bar", needed_pkg.reason)


class SetCheckInterfaceUnitTest(mox.MoxTestBase):

  def testNeededFile(self):
    catalog_mock = self.mox.CreateMock(checkpkg_lib.Catalog)
    # Test that when you declare a file is needed, the right error
    # functions are called.
    self.mox.ReplayAll()
    sci = checkpkg_lib.SetCheckInterface(
        'AlienOS5.1', 'amd65', 'calcified', catalog_mock, {})
    sci.NeedFile("CSWfoo", "/opt/csw/bin/foo", "Because.")
    # This might look like encapsulation violation, but I think this is
    # a reasonable interface to that class.
    self.assertEqual(1, len(sci.needed_files))
    needed_file = sci.needed_files[0]
    self.assertEqual("CSWfoo", needed_file.pkgname)
    self.assertEqual("/opt/csw/bin/foo", needed_file.full_path)
    self.assertEqual("Because.", needed_file.reason)


if __name__ == '__main__':
  unittest.main()
