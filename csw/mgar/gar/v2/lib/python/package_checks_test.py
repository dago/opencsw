#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import unittest
import package_checks as pc

class PackageChecksUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkg_data_1 = {
    	  "basic_stats": {
    	  	"pkgname": "CSWfoo"
        }
    }
    self.pkg_data_2 = {
        'basic_stats': {
          'parsed_basename':
              {'revision_info': {'REV': '2010.02.15'},
               'catalogname': 'python_tk',
               'full_version_string': '2.6.4,REV=2010.02.15',
               'version': '2.6.4',
               'version_info': {
                 'minor version': '6',
                 'major version': '2',
                 'patchlevel': '4'}},
          'pkgname': 'CSWpython-tk',
          'stats_version': 1,
          'pkg_basename': 'python_tk-2.6.4,REV=2010.02.15-SunOS5.8-sparc-CSW.pkg.gz',
          'pkg_path': '/tmp/pkg_lL0HDH/python_tk-2.6.4,REV=2010.02.15-SunOS5.8-sparc-CSW.pkg.gz',
          'catalogname': 'python_tk'}}

  def testCatalogName_1(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "Foo"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failUnless(errors)

  def testCatalogName_2(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "foo"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failIf(errors)

  def testCatalogNameSpecialCharacters(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "foo+abc&123"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failUnless(errors)

  def testFileNameSanity(self):
    del(self.pkg_data_2["basic_stats"]["parsed_basename"]["revision_info"]["REV"])
    errors = pc.FileNameSanity(self.pkg_data_2, False)
    self.failUnless(errors)


if __name__ == '__main__':
  unittest.main()
