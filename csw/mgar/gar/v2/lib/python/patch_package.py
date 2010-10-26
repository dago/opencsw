#!/usr/bin/env python2.6
#
# A utility to patch an existing package.
# 
# Usage:
# patchpkg --srv4-file /tmp/foo-1.0-sparc-CSW.pkg.gz --export /work/dir
# cd /work/dir/CSWfoo
# vim ...
# git commit -a -m "Change description..."
# git format-patch HEAD^
# patchpkg --srv4-file /tmp/foo-1.0-sparc-CSW.pkg.gz --patch /work/dir/0001-...patch

import datetime
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
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    self.parsed_filename["revision_info"]["REV"] = date_str
    new_filename = opencsw.ComposePackageFileName(self.parsed_filename)
    pprint.pprint(self.parsed_filename)
    pprint.pprint(new_filename)


>>>>>>> mGAR v2: patchpkg, new function to compose package names.
def main():
  parser = optparse.OptionParser()
  parser.add_option("--srv4-file", "-s", dest="srv4_file",
      help="Package to modify, e.g. foo-1.0-sparc-CSW.pkg.gz")
  parser.add_option("--patch", "-p", dest="patch",
      help="Patch to apply")
  parser.add_option("--debug", dest="debug",
      action="store_true", default=False,
      help="Debug")
  parser.add_option("--export", dest="export",
      help="Export to a directory")
  options, args = parser.parse_args()
  logging_level = logging.DEBUG if options.debug else logging.INFO
  logging.basicConfig(level=logging_level)
  if options.export and options.srv4_file:
    ps = package.PackageSurgeon(
        options.srv4_file,
        debug=options.debug)
    ps.Export(options.export)
  elif options.srv4_file and options.patch:
    ps = package.PackageSurgeon(
        options.srv4_file,
        debug=options.debug)
    ps.Patch(options.patch)
    base_dir, pkg_basename = os.path.split(options.srv4_file)
    ps.ToSrv4(base_dir)
  else:
    print "See --help for usage information"

if __name__ == '__main__':
  main()
