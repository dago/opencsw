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
