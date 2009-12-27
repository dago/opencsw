#!/opt/csw/bin/python2.6
# $Id$

import unittest
import checkpkg
import checkpkg_test_data_CSWmysql51rt as d1
import checkpkg_test_data_CSWmysql51client as d2
import checkpkg_test_data_CSWmysql51 as d3
import checkpkg_test_data_CSWmysql51devel as d4

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
    expected = set([u'SUNWcsl', u'SUNWlibms', u'SUNWlibC'])
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
    expected = set([u'SUNWlibC', u'SUNWcsl', u'SUNWlibms'])
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
    expected = set(['CSWmysql51rt', u'SUNWcsl', u'SUNWlibms', u'SUNWlibC'])
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


if __name__ == '__main__':
	unittest.main()
