# $Id$

import os.path
import sys
import unittest
sys.path.append("../lib/python")
import gartest

class OverridesUnitTest(unittest.TestCase):
  """Tests CHECKPKG_OVERRIDES support."""

  def testOneOverride(self):
    """Checks that CHECKPKG_OVERRIDES variable creates an override."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("GARNAME", "overrides-test")
    mybuild.SetGarVariable("CATALOGNAME", "overrides_test")
    mybuild.SetGarVariable("CHECKPKG_OVERRIDES",
                           "CSWoverrides-test|example-tag|example-parameter")
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    overr_file = "/opt/csw/share/checkpkg/overrides/overrides_test"
    expected = 'CSWoverrides-test: example-tag example-parameter\n'
    self.assertEqual(expected, pkg.GetFileContent(overr_file))
    overrides = pkg.GetOverrides()
    self.assertEqual(1, len(overrides))

  def testTwoOverriders(self):
    """Checks that CHECKPKG_OVERRIDES variable creates overrides."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("GARNAME", "overrides-test")
    mybuild.SetGarVariable("CATALOGNAME", "overrides_test")
    mybuild.SetGarVariable(
        "CHECKPKG_OVERRIDES",
        ("CSWoverrides-test|example-tag-1|example-parameter-1 "
         "CSWoverrides-test|example-tag-2|example-parameter-2"))
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    overr_file = "/opt/csw/share/checkpkg/overrides/overrides_test"
    expected = ('CSWoverrides-test: example-tag-1 example-parameter-1\n'
                'CSWoverrides-test: example-tag-2 example-parameter-2\n')
    self.assertEqual(expected, pkg.GetFileContent(overr_file))
    overrides = pkg.GetOverrides()
    self.assertEqual(2, len(overrides))
