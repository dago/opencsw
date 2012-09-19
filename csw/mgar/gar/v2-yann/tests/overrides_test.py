# $Id$

import os.path
import sys
import unittest
sys.path.append("../lib/python")
import gartest
import opencsw

class OverridesUnitTest_1(unittest.TestCase):
  """Tests CHECKPKG_OVERRIDES support."""

  def testOneOverride(self):
    """Checks that CHECKPKG_OVERRIDES variable creates an override."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("NAME", "overrides-test")
    mybuild.SetGarVariable("CATALOGNAME", "overrides_test")
    mybuild.SetGarVariable("CHECKPKG_OVERRIDES",
                           "example-tag|example-parameter")
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    overr_file = "/opt/csw/share/checkpkg/overrides/overrides_test"
    expected = 'CSWoverrides-test: example-tag example-parameter\n'
    try:
      self.assertEqual(expected, pkg.GetFileContent(overr_file))
      overrides = pkg.GetOverrides()
      self.assertEqual(1, len(overrides))
    except opencsw.PackageError, e:
      mybuild.cleanup = False
      self.fail(e)

  def testTwoOverriders(self):
    """Checks that CHECKPKG_OVERRIDES variable creates overrides."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("NAME", "overrides-test")
    mybuild.SetGarVariable("CATALOGNAME", "overrides_test")
    mybuild.SetGarVariable(
        "CHECKPKG_OVERRIDES",
        ("example-tag-1|example-parameter-1 "
         "example-tag-2|example-parameter-2"))
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    overr_file = "/opt/csw/share/checkpkg/overrides/overrides_test"
    expected = ('CSWoverrides-test: example-tag-1 example-parameter-1\n'
                'CSWoverrides-test: example-tag-2 example-parameter-2\n')
    self.assertEqual(expected, pkg.GetFileContent(overr_file))
    overrides = pkg.GetOverrides()
    self.assertEqual(2, len(overrides))

# This bit fails, needs more work.
#
# class OverridesUnitTest_2(unittest.TestCase):
#   """Tests CHECKPKG_OVERRIDES support."""
# 
#   def testOverridersForTwoPackages(self):
#     """http://sourceforge.net/apps/trac/gar/ticket/17"""
#     overr_file_1 = "/opt/csw/share/checkpkg/overrides/overrides_test_1"
#     mybuild = gartest.DynamicGarBuild()
#     mybuild.SetGarVariable("NAME", "overrides-test")
#     mybuild.SetGarVariable("PACKAGES", "CSWoverrides-test-1 "
#                                        "CSWoverrides-test-2")
#     mybuild.SetGarVariable("CATALOGNAME_CSWoverrides-test-1",
#                            "overrides_test_1")
#     mybuild.SetGarVariable("CATALOGNAME_CSWoverrides-test-2",
#                            "overrides_test_2")
#     mybuild.SetGarVariable("SPKG_DESC_CSWoverrides-test-1",
#                            "Test package 1")
#     mybuild.SetGarVariable("SPKG_DESC_CSWoverrides-test-1",
#                            "Test package 2")
#     mybuild.SetGarVariable("PKGFILES_CSWoverrides-test-1",
#                            overr_file_1)
#     mybuild.SetGarVariable(
#         "CHECKPKG_OVERRIDESCSWoverrides-test-1",
#         "example-tag-1|example-parameter-1")
#     mybuild.SetGarVariable(
#         "CHECKPKG_OVERRIDESCSWoverrides-test-2",
#         "example-tag-2|example-parameter-2")
#     mybuild.WriteGarFiles()
#     self.assertEquals(0, mybuild.Build())
#     pkg = mybuild.GetFirstBuiltPackage()
#     expected = ('CSWoverrides-test-1: example-tag-1 example-parameter-1\n')
#     self.assertEqual(expected, pkg.GetFileContent(overr_file_1))
#     overrides = pkg.GetOverrides()
#     self.assertEqual(1, len(overrides))

if __name__ == '__main__':
	unittest.main()
