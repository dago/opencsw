#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import unittest
import package_checks as pc
import yaml
import os.path

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")

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

  def LoadData(self, name):
    file_name = os.path.join(TESTDATA_DIR, "%s.yml" % name)
    f = open(file_name, "rb")
    data = yaml.safe_load(f)
    f.close()
    return data

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

  def testCheckArchitectureVsContents(self):
    self.pkg_data_2["pkgmap"] = self.LoadData("example-1-pkgmap")
    self.pkg_data_2["binaries"] = []
    self.pkg_data_2["pkginfo"] = self.LoadData("example-1-pkginfo")
    errors = pc.CheckArchitectureVsContents(self.pkg_data_2, False)
    print errors


if __name__ == '__main__':
  unittest.main()
