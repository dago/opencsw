#!/usr/bin/env python2.6
#
# A utility to patch an existing package.
# 
# Usage:
# patchpkg --dir /tmp/foo --patch foo.patch --catalogname foo

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
  ps = package.PackageSurgeon(
      "/home/maciej/tmp/mozilla-1.7.5-SunOS5.8-sparc-CSW.pkg.gz",
      debug=options.debug)
  # ps.Export("/home/maciej/tmp")
  ps.Patch("/home/maciej/tmp/0001-Removing-nspr.m4-and-headers.patch")
  ps.ToSrv4("/home/maciej/tmp")

if __name__ == '__main__':
  main()
