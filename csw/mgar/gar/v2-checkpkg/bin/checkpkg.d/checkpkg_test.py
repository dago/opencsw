#!/opt/csw/bin/python2.6
# $Id$

import unittest
import checkpkg
import checkpkg_test_data_CSWmysql51rt as d1
import checkpkg_test_data_CSWmysql51client as d2
import checkpkg_test_data_CSWmysql51 as d3

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
    # set(['CSWmysql51rt', 'CSWosslrt', 'CSWncurses', 'CSWzlib'])
    self.assertEquals(set([]), self.surplus_deps)

  def testOrphanSonames(self):
    self.assertEquals(set([]), self.orphan_sonames)

  def testMissingDeps(self):
    # expected = set([u'SUNWlmsx', u'SUNWlibCx', u'CSWosslrt', u'SUNWcsl', u'SUNWcslx'])
    self.assertEquals(set([u'SUNWlibC', u'SUNWcsl', u'SUNWlibms']), self.missing_deps)


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
    self.assertEquals(set([u'SUNWlibC', u'SUNWcsl', u'SUNWlibms']), self.missing_deps)


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


if __name__ == '__main__':
	unittest.main()
