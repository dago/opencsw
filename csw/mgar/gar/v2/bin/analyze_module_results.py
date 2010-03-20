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
                    help="Directory with extracted packages "
                         "(with error tag files)")
  options, args = parser.parse_args()
  filenames = args
  srv4_pkgs = [opencsw.CswSrv4File(x) for x in filenames]
  pkgstats = [checkpkg.PackageStats(x) for x in srv4_pkgs]
  overrides_list = [pkg.GetSavedOverrides() for pkg in pkgstats]
  files = os.listdir(options.extractdir)
  error_tags = []
  for file_name in files:
    full_path = os.path.join(options.extractdir, file_name)
    error_tags.extend(checkpkg.ErrorTagsFromFile(full_path))
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
      print "* Unused %s" % override
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
