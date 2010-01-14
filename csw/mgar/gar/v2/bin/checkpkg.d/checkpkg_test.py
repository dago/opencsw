#!/opt/csw/bin/python2.6
# $Id$

import unittest
import mox
import difflib
import checkpkg
import testdata.checkpkg_test_data_CSWmysql51rt as d1
import testdata.checkpkg_test_data_CSWmysql51client as d2
import testdata.checkpkg_test_data_CSWmysql51 as d3
import testdata.checkpkg_test_data_CSWmysql51devel as d4
import testdata.checkpkg_test_data_CSWlibpq_84 as d5
import testdata.checkpkg_test_data_CSWmysql5client_8x as d6
import testdata.checkpkg_test_data_CSWpostfix as d7
import testdata.dump_output_1 as dump_1
import testdata.dump_output_2 as dump_2

"""A set of unit tests for the library checking code.

A bunch of lines to test in the interactive Python shell.

import sys
sys.path.append("gar/bin/checkpkg.d")
import checkpkg
import testdata.checkpkg_test_data_CSWmysql5client_8x as d6

checkpkg.SharedObjectDependencies("CSWmysql5client",
d6.DATA_BINARIES_BY_PKGNAME, d6.DATA_NEEDED_SONAMES_BY_BINARY,
d6.DATA_PKGS_BY_FILENAME, d6.DATA_FILENAMES_BY_SONAME,
d6.DATA_PKG_BY_ANY_FILENAME)

sqlite3 ~/.checkpkg/var-sadm-install-contents-cache-build8x
SELECT * FROM systempkgmap WHERE basename = 'libncursesw.so.5';
"""

class DependenciesUnitTest_1(unittest.TestCase):

  def setUp(self):
    self.missing_deps, self.surplus_deps, self.orphan_sonames = checkpkg.AnalyzeDependencies(
        d1.DATA_PKGNAME,
        d1.DATA_DECLARED_DEPENDENCIES,
        d1.DATA_BINARIES_BY_PKGNAME,
        d1.DATA_NEEDED_SONAMES_BY_BINARY,
        d1.DATA_PKGS_BY_FILENAME,
        d1.DATA_FILENAMES_BY_SONAME,
        d1.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set([])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_2(unittest.TestCase):

  def setUp(self):
    self.missing_deps, self.surplus_deps, self.orphan_sonames = checkpkg.AnalyzeDependencies(
        d2.DATA_PKGNAME,
        d2.DATA_DECLARED_DEPENDENCIES,
        d2.DATA_BINARIES_BY_PKGNAME,
        d2.DATA_NEEDED_SONAMES_BY_BINARY,
        d2.DATA_PKGS_BY_FILENAME,
        d2.DATA_FILENAMES_BY_SONAME,
        d2.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set([])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_3(unittest.TestCase):

  def setUp(self):
    self.missing_deps, self.surplus_deps, self.orphan_sonames = checkpkg.AnalyzeDependencies(
        d3.DATA_PKGNAME,
        d3.DATA_DECLARED_DEPENDENCIES,
        d3.DATA_BINARIES_BY_PKGNAME,
        d3.DATA_NEEDED_SONAMES_BY_BINARY,
        d3.DATA_PKGS_BY_FILENAME,
        d3.DATA_FILENAMES_BY_SONAME,
        d3.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([u'CSWmysql51client']), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set(['CSWmysql51rt'])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_4(unittest.TestCase):

  def setUp(self):
    self.missing_deps, self.surplus_deps, self.orphan_sonames = checkpkg.AnalyzeDependencies(
        d4.DATA_PKGNAME,
        d4.DATA_DECLARED_DEPENDENCIES,
        d4.DATA_BINARIES_BY_PKGNAME,
        d4.DATA_NEEDED_SONAMES_BY_BINARY,
        d4.DATA_PKGS_BY_FILENAME,
        d4.DATA_FILENAMES_BY_SONAME,
        d4.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set([])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_5(unittest.TestCase):

  def setUp(self):
    self.missing_deps, self.surplus_deps, self.orphan_sonames = checkpkg.AnalyzeDependencies(
        d5.DATA_PKGNAME,
        d5.DATA_DECLARED_DEPENDENCIES,
        d5.DATA_BINARIES_BY_PKGNAME,
        d5.DATA_NEEDED_SONAMES_BY_BINARY,
        d5.DATA_PKGS_BY_FILENAME,
        d5.DATA_FILENAMES_BY_SONAME,
        d5.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    # This tends to report itself...
    expected = set([u'SUNWgss'])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_6(unittest.TestCase):

  def setUp(self):
    (self.missing_deps,
     self.surplus_deps,
     self.orphan_sonames) = checkpkg.AnalyzeDependencies(
        d6.DATA_PKGNAME,
        d6.DATA_DECLARED_DEPENDENCIES,
        d6.DATA_BINARIES_BY_PKGNAME,
        d6.DATA_NEEDED_SONAMES_BY_BINARY,
        d6.DATA_PKGS_BY_FILENAME,
        d6.DATA_FILENAMES_BY_SONAME,
        d6.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set([])
    self.assertEquals(expected, self.missing_deps)


class DependenciesUnitTest_7(unittest.TestCase):

  def setUp(self):
    (self.missing_deps,
     self.surplus_deps,
     self.orphan_sonames) = checkpkg.AnalyzeDependencies(
        d7.DATA_PKGNAME,
        d7.DATA_DECLARED_DEPENDENCIES,
        d7.DATA_BINARIES_BY_PKGNAME,
        d7.DATA_NEEDED_SONAMES_BY_BINARY,
        d7.DATA_PKGS_BY_FILENAME,
        d7.DATA_FILENAMES_BY_SONAME,
        d7.DATA_PKG_BY_ANY_FILENAME,
    )

  def testSurplusDeps(self):
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    expected = set([u'SUNWcslx'])
    self.assertEquals(expected, self.missing_deps)


class GuessDepsUnitTest(unittest.TestCase):

  def testGuessDepsByFilename1(self):
    expected = set([u"CSWpython"])
    pkgname = u"CSWfoo"
    pkg_by_filename = {
        "/opt/csw/bin/bar": u"CSWfoo",
        "/opt/csw/lib/python/site-packages/foo.py": u"CSWfoo",
    }
    self.assertEqual(expected,
                     checkpkg.GuessDepsByFilename(pkgname, pkg_by_filename))

  def testGuessDepsByFilename2(self):
    expected = set([])
    pkgname = u"CSWfoo"
    pkg_by_filename = {
        "/opt/csw/bin/bar": u"CSWfoo",
        "/opt/csw/lib/python/site-packages/foo.py": u"CSWbar",
    }
    self.assertEqual(expected,
                     checkpkg.GuessDepsByFilename(pkgname, pkg_by_filename))

  def testGuessDepsByPkgname1(self):
    expected = set([u"CSWfoo"])
    pkgname = u"CSWfoo-devel"
    pkg_by_filename = {
        "/opt/csw/bin/bar": u"CSWfoo",
        "/opt/csw/bin/barfoo": u"CSWfoobar",
        "/opt/csw/lib/python/site-packages/foo.py": u"CSWfoo",
    }
    self.assertEqual(expected,
                     checkpkg.GuessDepsByPkgname(pkgname, pkg_by_filename))

  def testGuessDepsByPkgname2(self):
    expected = set([])
    pkgname = u"CSWzfoo-devel"
    pkg_by_filename = {
        "/opt/csw/bin/bar": u"CSWfoo",
        "/opt/csw/bin/barfoo": u"CSWfoobar",
        "/opt/csw/lib/python/site-packages/foo.py": u"CSWfoo",
    }
    self.assertEqual(expected,
                     checkpkg.GuessDepsByPkgname(pkgname, pkg_by_filename))

  def testGuessDepsByPkgname3(self):
    self.assertEqual(set([u"CSWmysql51"]),
                     checkpkg.GuessDepsByPkgname(u"CSWmysql51devel",
                                                 d4.DATA_PKG_BY_ANY_FILENAME))

  def testGuessDepsByPkgname4(self):
    data1 = set(['CSWmysql51', 'CSWmysql51rt', 'CSWmysql51test',
                 'CSWmysql51client', 'CSWmysql51bench', 'CSWmysql51devel'])
    data2 = dict(((x, x) for x in data1))
    self.assertEqual(set([u"CSWmysql51"]), checkpkg.GuessDepsByPkgname(u"CSWmysql51devel", data2))

  def testGuessDepsByPkgname4(self):
    data1 = set(['CSWmysql51', 'CSWmysql51rt', 'CSWmysql51test',
                 'CSWmysql51client', 'CSWmysql51bench', 'CSWmysql51devel'])
    data2 = dict(((x, x) for x in data1))
    self.assertEqual(set([]), checkpkg.GuessDepsByPkgname(u"CSWmysql51rt", data2))


class GetLinesBySonameUnitTest(unittest.TestCase):

  class PkgmapStub(object):

    def __init__(self, cache):
      self.cache = cache

    def GetPkgmapLineByBasename(self, soname):
      return self.cache[soname]

  def setUp(self):
    self.pkgmap_mocker = mox.Mox()

  def testExpandRunpath_1(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/lib/$ISALIST"
    expected = ["/opt/csw/lib/foo", "/opt/csw/lib/bar"]
    self.assertEquals(expected, checkpkg.ExpandRunpath(runpath, isalist))

  def testExpandRunpath_2(self):
    isalist = ["foo", "bar"]
    runpath = "/opt/csw/mysql5/lib/$ISALIST/mysql"
    expected = ["/opt/csw/mysql5/lib/foo/mysql", "/opt/csw/mysql5/lib/bar/mysql"]
    self.assertEquals(expected, checkpkg.ExpandRunpath(runpath, isalist))

  def testEmulate64BitSymlinks_1(self):
    runpath_list = ["/opt/csw/mysql5/lib/foo/mysql/64"]
    expected = "/opt/csw/mysql5/lib/foo/mysql/amd64"
    self.assertTrue(expected in checkpkg.Emulate64BitSymlinks(runpath_list))

  def testEmulate64BitSymlinks_2(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/amd64/mysql/foo"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulate64BitSymlinks_3(self):
    runpath_list = ["/opt/csw/mysql5/lib/64/mysql/foo"]
    expected = "/opt/csw/mysql5/lib/sparcv9/mysql/foo"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_3(self):
    runpath_list = ["/opt/csw/bdb4"]
    expected = "/opt/csw/bdb42"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))

  def testEmulateSymlinks_4(self):
    runpath_list = ["/opt/csw/bdb42"]
    expected = "/opt/csw/bdb42"
    not_expected = "/opt/csw/bdb422"
    result = checkpkg.Emulate64BitSymlinks(runpath_list)
    self.assertTrue(expected in result, "%s not in %s" % (expected, result))
    self.assertFalse(not_expected in result, "%s is in %s" % (not_expected, result))

  def testGetLinesBySoname(self):
    expected = {'foo.so.1': '/opt/csw/lib/isa-value-1/foo.so.1 foo'}
    pkgmap = self.pkgmap_mocker.CreateMock(checkpkg.SystemPkgmap)
    pkgmap.GetPkgmapLineByBasename("foo")
    lines1 = {"/opt/csw/lib/isa-value-1": "/opt/csw/lib/isa-value-1/foo.so.1 foo",
              "/usr/lib":                  "/usr/lib/foo.so.1 foo"}
    # pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    self.pkgmap_mocker.ReplayAll()
    pkgmap.GetPkgmapLineByBasename("foo")
    needed_sonames = set(["foo.so.1"])
    runpath_by_needed_soname = {"foo.so.1": ["/opt/csw/lib/$ISALIST", "/usr/lib"]}
    isalist = ["isa-value-1", "isa-value-2"]
    result = checkpkg.GetLinesBySoname(pkgmap, needed_sonames, runpath_by_needed_soname, isalist)
    self.pkgmap_mocker.VerifyAll()
    self.assertEqual(expected, result)

  def testGetLinesBySoname_3(self):
    expected = {'foo.so.1': '/opt/csw/lib/isa-value-1/foo.so.1 foo'}
    pkgmap = self.pkgmap_mocker.CreateMock(checkpkg.SystemPkgmap)
    pkgmap.GetPkgmapLineByBasename("foo")
    lines1 = {
        "/opt/csw/lib/isa-value-1": "/opt/csw/lib/isa-value-1/foo.so.1 foo",
        "/opt/csw/lib":             "/opt/csw/lib/foo.so.1 foo",
        "/usr/lib":                 "/usr/lib/foo.so.1 foo"}
    # pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    self.pkgmap_mocker.ReplayAll()
    pkgmap.GetPkgmapLineByBasename("foo")
    needed_sonames = set(["foo.so.1"])
    runpath_by_needed_soname = {
        "foo.so.1": ["/opt/csw/lib/$ISALIST", "/usr/lib"]}
    isalist = ["isa-value-1", "isa-value-2"]
    result = checkpkg.GetLinesBySoname(
        pkgmap, needed_sonames, runpath_by_needed_soname, isalist)
    self.pkgmap_mocker.VerifyAll()
    self.assertEqual(expected, result)

  def testGetLinesBySoname_4(self):
    """A more complex test, four ISAs."""
    expected = {'foo.so.1': '/opt/csw/lib/isa-value-1/foo.so.1 foo'}
    pkgmap = self.pkgmap_mocker.CreateMock(checkpkg.SystemPkgmap)
    pkgmap.GetPkgmapLineByBasename("foo")
    lines1 = {
        "/opt/csw/lib/isa-value-1":
            "/opt/csw/lib/isa-value-1/foo.so.1 foo",
        "/opt/csw/mysql5/lib/isa-value-2":
            "/opt/csw/mysql5/lib/isa-value-2/foo.so.1 foo",
        "/opt/csw/mysql5/lib/isa-value-1":
            "/opt/csw/mysql5/lib/isa-value-1/foo.so.1 foo",
        "/opt/csw/lib":
            "/opt/csw/lib/foo.so.1 foo",
        "/usr/lib":
            "/usr/lib/foo.so.1 foo"}
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    self.pkgmap_mocker.ReplayAll()
    pkgmap.GetPkgmapLineByBasename("foo")
    needed_sonames = set(["foo.so.1"])
    runpath_by_needed_soname = {
        "foo.so.1": ["/opt/csw/mysql5/lib/$ISALIST/mysql",
                     "/opt/csw/lib/$ISALIST",
                     "/usr/lib"]}
    isalist = ["isa-value-1", "isa-value-2"]
    result = checkpkg.GetLinesBySoname(
        pkgmap, needed_sonames, runpath_by_needed_soname, isalist)
    self.pkgmap_mocker.VerifyAll()
    self.assertEqual(expected, result)

  def testGetLinesBySoname_5(self):
    """Based on CSWmysql5client on build8x."""
    soname = u'libm.so.1'
    expected = {u'libm.so.1': u'/usr/lib/libm.so.1 f none 0755 root bin '
                              u'99844 3884 1050525375 SUNWlibms\n'}

    pkgmap_stub = self.PkgmapStub(d6.DATA_PKGMAP_CACHE)
    (needed_sonames,
     binaries_by_soname,
     runpath_by_needed_soname) = checkpkg.BuildIndexesBySoname(
         d6.DATA_NEEDED_SONAMES_BY_BINARY)
    result = checkpkg.GetLinesBySoname(
        pkgmap_stub,
        set([soname]),
        runpath_by_needed_soname,
        d6.DATA_ISALIST)
    self.assertEqual(expected, result)

  def testGetLinesBySoname_6(self):
    """Based on CSWmysql5client on build8x."""
    soname = u'libz.so.1'
    expected = {u'libz.so.1': u'/opt/csw/lib/pentium_pro+mmx/libz.so.1=libz.so.1.2.3 '
                              u's none CSWzlib\n'}
    pkgmap_stub = self.PkgmapStub(d6.DATA_PKGMAP_CACHE)
    (needed_sonames,
     binaries_by_soname,
     runpath_by_needed_soname) = checkpkg.BuildIndexesBySoname(
         d6.DATA_NEEDED_SONAMES_BY_BINARY)
    result = checkpkg.GetLinesBySoname(
        pkgmap_stub,
        set([soname]),
        runpath_by_needed_soname,
        d6.DATA_ISALIST)
    self.assertEqual(expected, result)

  def testGetLinesBySoname_7(self):
    """A test for 64-bit symlink expansion."""
    soname = u'libncursesw.so.5'
    # To test the 64-bit symlink expansion
    expected = {
    	  u'libncursesw.so.5':
    	    u'/opt/csw/lib/amd64/libncursesw.so.5=libncursesw.so.5.7 '
    	    u's none CSWncurses\n'}
    pkgmap_stub = self.PkgmapStub(d6.DATA_PKGMAP_CACHE)
    (needed_sonames,
     binaries_by_soname,
     runpath_by_needed_soname) = checkpkg.BuildIndexesBySoname(
         d6.DATA_NEEDED_SONAMES_BY_BINARY)
    result = checkpkg.GetLinesBySoname(
        pkgmap_stub,
        set([soname]),
        runpath_by_needed_soname,
        d6.DATA_ISALIST)
    self.assertEqual(expected, result)

  def testGetLinesBySoname_8(self):
    expected = {'foo.so.1': '/opt/csw/postgresql/lib/foo.so.1 foo'}
    pkgmap = self.pkgmap_mocker.CreateMock(checkpkg.SystemPkgmap)
    pkgmap.GetPkgmapLineByBasename("foo")
    lines1 = {"/opt/csw/lib/postgresql": "/opt/csw/lib/postgresql/foo.so.1 foo"}
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    pkgmap.GetPkgmapLineByBasename("foo.so.1").AndReturn(lines1)
    self.pkgmap_mocker.ReplayAll()
    pkgmap.GetPkgmapLineByBasename("foo")
    needed_sonames = set(["foo.so.1"])
    runpath_by_needed_soname = {"foo.so.1": ["/opt/csw/postgresql/lib/", "/usr/lib"]}
    isalist = ["isa-value-1", "isa-value-2"]
    result = checkpkg.GetLinesBySoname(pkgmap, needed_sonames, runpath_by_needed_soname, isalist)
    self.pkgmap_mocker.VerifyAll()
    self.assertEqual(expected, result)

  def testSanitizeRunpath_1(self):
    self.assertEqual("/opt/csw/lib", checkpkg.SanitizeRunpath("/opt/csw/lib/"))

  def testSanitizeRunpath_2(self):
    self.assertEqual("/opt/csw/lib", checkpkg.SanitizeRunpath("/opt//csw////lib/"))



class ParseDumpOutputUnitTest(unittest.TestCase):

  def test_1(self):
    expected = {
        'soname': 'libmysqlclient.so.15',
        'runpath': ['/opt/csw/lib/$ISALIST',
                    '/opt/csw/lib',
                    '/opt/csw/mysql5/lib/$ISALIST',
                    '/opt/csw/mysql5/lib',
                    '/opt/csw/mysql5/lib/$ISALIST/mysql',
                    # These four are artificially appended
                    '/usr/lib/$ISALIST',
                    '/usr/lib',
                    '/lib/$ISALIST',
                    '/lib'],
        'needed sonames': ['librt.so.1',
                           'libresolv.so.2',
                           'libc.so.1',
                           'libgen.so.1',
                           'libsocket.so.1',
                           'libnsl.so.1',
                           'libm.so.1',
                           'libz.so.1']}
    self.assertEqual(expected,
                     checkpkg.ParseDumpOutput(dump_1.DATA_DUMP_OUTPUT))

  def test_2(self):
    expected_runpath = ['/usr/lib/$ISALIST', '/usr/lib', '/lib/$ISALIST', '/lib']
    self.assertEqual(
        expected_runpath,
        checkpkg.ParseDumpOutput(dump_2.DATA_DUMP_OUTPUT)["runpath"])


class FormatDepsReportUnitTest(unittest.TestCase):

  def AssertTextEqual(self, text1, text2):
    difference = "\n".join(difflib.context_diff(text2.splitlines(), text1.splitlines()))
    self.assertEqual(text1, text2, difference)

  def testAll(self):
    missing_deps = set([u'SUNWgss', u'*SUNWlxsl'])
    surplus_deps = set(['CSWsudo', 'CSWlibxslt'])
    orphan_sonames = set([u'libm.so.2'])
    testdata = (missing_deps, surplus_deps, orphan_sonames)
    checker = checkpkg.CheckpkgBase("/tmp/nonexistent", "CSWfoo")
    expected = u"""CSWfoo:
SUGGESTION: you may want to add some or all of the following as depends:
   (Feel free to ignore SUNW or SPRO packages)
> *SUNWlxsl
> SUNWgss
The following packages might be unnecessary dependencies:
? CSWlibxslt
? CSWsudo
The following sonames don't belong to any package:
! libm.so.2
"""
    result = checker.FormatDepsReport(*testdata)
    self.AssertTextEqual(result, expected)

  def testNone(self):
    missing_deps = set([])
    surplus_deps = set([])
    orphan_sonames = set([])
    testdata = (missing_deps, surplus_deps, orphan_sonames)
    checker = checkpkg.CheckpkgBase("/tmp/nonexistent", "CSWfoo")
    expected = u"""CSWfoo:
+ Dependencies of CSWfoo look good.
"""
    result = checker.FormatDepsReport(*testdata)
    self.AssertTextEqual(result, expected)


if __name__ == '__main__':
  unittest.main()
