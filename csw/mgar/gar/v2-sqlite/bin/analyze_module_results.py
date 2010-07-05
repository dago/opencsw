#!/opt/csw/bin/python2.6
# $Id$

import operator
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
import overrides

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
  override_list = reduce(operator.add, overrides_list)
  (tags_after_overrides,
   unapplied_overrides) = overrides.ApplyOverrides(error_tags, override_list)
  exit_code = bool(tags_after_overrides)
  if tags_after_overrides:
    print "If any of the reported errors were false positives, you can"
    print "override them pasting the lines below to the GAR recipe."
    for checkpkg_tag in tags_after_overrides:
      print checkpkg_tag.ToGarSyntax()
    print "Please note that checkpkg isn't suggesting you should "
    print "use these overrides.  It only informs what the overrides could "
    print "look like.  You need to understand what are the reported issues about"
    print "and use your best judgement to decide whether to fix the underlying"
    print "problems or override them."
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
