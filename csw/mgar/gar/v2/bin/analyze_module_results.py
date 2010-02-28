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
  (tags_after_overrides,
   unapplied_overrides) = checkpkg.ApplyOverrides(error_tags, overrides)
  exit_code = bool(tags_after_overrides)
  if tags_after_overrides:
    print "There were errors reported."
    print "If you know they are false positives, you can override them:"
    for tag in tags_after_overrides:
      print tag.ToGarSyntax()
  if unapplied_overrides:
    print "WARNING: Some overrides did not match any errors."
    print "         They can be removed, as they don't take any effect anyway."
    print "         If you're getting errors at the same time, maybe you didn't"
    print "         specify the overrides correctly."
    for override in unapplied_overrides:
      print "* %s" % override
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
