#!/opt/csw/bin/python2.6
# $Id$

import unittest
import gartest

class ExampleEndToEndTest(unittest.TestCase):
  """An example end-to-end test of GAR."""

  def testPkginfoName(self):
    """Checks that the GARNAME makes it to the NAME in pkginfo."""
    mybuild = gartest.GarBuild()
    mybuild.SetGarVariable("GARNAME", "foo")
    mybuild.AddInstallFile("/opt/csw/share/foo", "bar!\n")
    mybuild.WriteGarFiles()
    self.assertEquals(0, mybuild.Build())
    pkg = mybuild.GetFirstBuiltPackage()
    pkginfo = pkg.GetParsedPkginfo()
    # By default, the garname should be used to create the catalog name, which
    # in turn ends up in the NAME field in pkginfo.
    self.assertTrue(pkginfo["NAME"].startswith("foo"))


if __name__ == '__main__':
  unittest.main()

# vim:set ts=2 sts=2 sw=2 expandtab:
