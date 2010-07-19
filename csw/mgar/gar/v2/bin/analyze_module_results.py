#!/opt/csw/bin/python2.6
# $Id$

import itertools
import operator
import optparse
import os
import pprint
import progressbar
import sys
import textwrap

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import overrides

BEFORE_OVERRIDES = """If any of the reported errors were false positives, you
can override them pasting the lines below to the GAR recipe."""

AFTER_OVERRIDES = """Please note that checkpkg isn't suggesting you should
simply add these overrides do the Makefile.  It only informs what the overrides
could look like.  You need to understand what are the reported issues about and
use your best judgement to decide whether to fix the underlying problems or
override them. For more information, scroll up and read the detailed
messages."""

UNAPPLIED_OVERRIDES = """WARNING: Some overrides did not match any errors.
They can be removed, as they don't take any effect anyway.  If you're getting
errors at the same time, maybe you didn't specify the overrides correctly."""

def main():
  parser = optparse.OptionParser()
  parser.add_option("-c", "--catalog_file", dest="catalog",
                    help="Optional catalog file")
  parser.add_option("-q", "--quiet", dest="quiet",
                    default=False, action="store_true",
                    help=("Display less messages"))
  options, args = parser.parse_args()
  filenames = args

  # This might be bottleneck.  Perhaps a list of md5 sums can be given to this
  # script instead.

  # It might be a good idea to store the error tags in the database and
  # eliminate the need to access the directory with the error tag files.

  pkgstats = checkpkg.StatsListFromCatalog(filenames, options.catalog)
  overrides_list = [pkg.GetSavedOverrides() for pkg in pkgstats]
  override_list = reduce(operator.add, overrides_list)
  error_tags = reduce(operator.add, [stat.GetSavedErrorTags() for stat in pkgstats])
  (tags_after_overrides,
   unapplied_overrides) = overrides.ApplyOverrides(error_tags, override_list)
  if not options.quiet:
    if tags_after_overrides:
      print textwrap.fill(BEFORE_OVERRIDES, 80)
      for checkpkg_tag in tags_after_overrides:
        print checkpkg_tag.ToGarSyntax()
      print textwrap.fill(AFTER_OVERRIDES, 80)
    if unapplied_overrides:
      print textwrap.fill(UNAPPLIED_OVERRIDES, 80)
      for override in unapplied_overrides:
        print "* Unused %s" % override
  exit_code = bool(tags_after_overrides)
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
