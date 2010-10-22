#!/usr/bin/env python2.6
#
# A utility to patch an existing package.
# 
# Usage:
# patchpkg --dir /tmp/foo --patch foo.patch --catalogname foo

import optparse
import logging
import package
import subprocess
import shutil
import os.path
import pprint
import opencsw

class PackageSurgeon(package.ShellMixin):

  def __init__(self, pkg_path, debug):
    self.debug = debug
    self.pkg_path = pkg_path
    self.srv4 = package.CswSrv4File(pkg_path)
    self.dir_pkg = None
    self.exported_dir = None
    self.parsed_filename = opencsw.ParsePackageFileName(self.pkg_path)

  def Transform(self):
    if not self.dir_pkg:
      self.dir_pkg = self.srv4.GetDirFormatPkg()
      logging.debug(repr(self.dir_pkg))
      # subprocess.call(["tree", self.dir_pkg.directory])

  def Export(self, dest_dir):
    self.Transform()
    if not self.exported_dir:
      basedir, pkgname = os.path.split(self.dir_pkg.directory)
      self.exported_dir = os.path.join(dest_dir, pkgname)
      shutil.copytree(
          self.dir_pkg.directory,
          self.exported_dir)
      subprocess.call(["git", "init"], cwd=self.exported_dir)
      subprocess.call(["git", "add", "."], cwd=self.exported_dir)
      subprocess.call(["git", "commit", "-a", "-m", "Initial commit"],
                      cwd=self.exported_dir)
    else:
      logging.warn("The package was already exported to %s",
                   self.exported_dir)

  def Patch(self, patch_file):
    self.Transform()
    args = ["gpatch", "-p", "1", "-d", self.dir_pkg.directory, "-i", patch_file]
    logging.debug(args)
    subprocess.call(args)

  def ToSrv4(self, dest_dir):
    self.Transform()
    pkginfo = self.dir_pkg.GetParsedPkginfo()
    # version = pkginfo["VERSION"]
    pprint.pprint(pkginfo)
    pprint.pprint(self.parsed_filename)


def main():
  parser = optparse.OptionParser()
  parser.add_option("--dir", "-d", dest="dir",
      help="Directory with packages.")
  parser.add_option("--patch", "-p", dest="patch",
      help="Patch to apply")
  parser.add_option("--patch-sparc", dest="patch_sparc",
      help="Patch to apply (sparc specific)")
  parser.add_option("--patch-x86", dest="patch_x86",
      help="Patch to apply (x86 specific)")
  parser.add_option("--catalogname", "-c", dest="catalogname",
      help="Catalogname")
  parser.add_option("--debug", dest="debug",
      action="store_true", default=False,
      help="Debug")
  parser.add_option("--export", dest="export",
      help="Export to a directory")
  options, args = parser.parse_args()
  logging_level = logging.DEBUG if options.debug else logging.INFO
  logging.basicConfig(level=logging_level)
  logging.debug("Start!")
  ps = PackageSurgeon("/home/maciej/tmp/mozilla-1.7.5-SunOS5.8-sparc-CSW.pkg.gz",
      debug=options.debug)
  # ps.Export("/home/maciej/tmp")
  ps.Patch("/home/maciej/tmp/0001-Removing-nspr.m4-and-headers.patch")
  ps.ToSrv4("/home/maciej/tmp")

if __name__ == '__main__':
  main()
