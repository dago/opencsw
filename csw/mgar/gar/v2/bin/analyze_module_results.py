#!/opt/csw/bin/python2.6
# $Id$

import optparse
import os
import sys

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw

def main():
  parser = optparse.OptionParser()
  parser.add_option("-e", "--extract-dir", dest="extractdir",
                    help="Directory with extracted packages")
  options, args = parser.parse_args()
  pkgnames = args
  packages = [opencsw.DirectoryFormatPackage(
                  os.path.join(options.extractdir, pkgname))
              for pkgname in pkgnames]
  overrides_list = [pkg.GetOverrides() for pkg in packages]
  files = os.listdir(options.extractdir)
  error_tags = []
  for file_name in files:
    if file_name.startswith("tags."):
      fd = open(os.path.join(options.extractdir, file_name))
      for line in fd:
        if line.startswith("#"):
        	continue
        pkgname, tag_name, tag_info = checkpkg.ParseTagLine(line)
        error_tags.append(checkpkg.CheckpkgTag(pkgname, tag_name, tag_info))
  overrides = reduce(lambda x, y: x + y, overrides_list)
  tags_after_overrides = checkpkg.ApplyOverrides(error_tags, overrides)
  exit_code = bool(tags_after_overrides)
  if tags_after_overrides:
    print "The reported error tags are:"
    for tag in tags_after_overrides:
    	print "*", repr(tag)
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
