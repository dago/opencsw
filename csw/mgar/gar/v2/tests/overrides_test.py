# $Id$

import os.path
import sys
import unittest
sys.path.append("../lib/python")
import gartest

class OverridesUnitTest(unittest.TestCase):
  """Tests CHECKPKG_OVERRIDES support."""

  def testPkginfoName(self):
    """Checks that the GARNAME makes it to the NAME in pkginfo."""
    mybuild = gartest.DynamicGarBuild()
    mybuild.SetGarVariable("GARNAME", "overrides-test")
    mybuild.SetGarVariable("CATALOGNAME", "overrides_test")
    mybuild.SetGarVariable("CHECKPKG_OVERRIDES", "CSWoverrides-test|example-tag|example-parameter")
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    overr_file = "/opt/csw/share/checkpkg/overrides/overrides_test"
    expected = 'CSWoverrides-test: example-tag example-parameter\n'
    self.assertEqual(expected, pkg.GetFileContent(overr_file))
    overrides = pkg.GetOverrides()
    self.assertEqual(1, len(overrides))
