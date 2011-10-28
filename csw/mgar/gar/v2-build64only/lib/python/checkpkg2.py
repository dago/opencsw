#!/usr/bin/env python2.6
#
# checkpkg
#

import logging
import operator
import optparse
import os
import sys
import textwrap
import configuration
import datetime
import database

import package_stats
import struct_util
import checkpkg
import checkpkg_lib
import overrides
import models
import sqlobject

USAGE = """%prog [ options ] pkg1 [ pkg2 [ ... ] ]"""
CHECKPKG_MODULE_NAME = "The main checking module."
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


class Error(Exception):
  """Generic error."""


class UsageError(Error):
  """Problem with usage, e.g. command line options."""


def main():
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug",
      dest="debug",
      action="store_true",
      default=False,
      help="Switch on debugging messages")
  parser.add_option("-q", "--quiet",
      dest="quiet",
      action="store_true",
      default=False,
      help="Display less messages")
  parser.add_option("--catalog-release",
      dest="catrel",
      default="current",
      help="A catalog release: current, unstable, testing, stable.")
  parser.add_option("-r", "--os-releases",
      dest="osrel_commas",
      help=("Comma separated list of ['SunOS5.9', 'SunOS5.10'], "
            "e.g. 'SunOS5.9,SunOS5.10'."))
  parser.add_option("-a", "--architecture",
      dest="arch",
      help="Architecture: i386, sparc.")
  parser.add_option("--profile", dest="profile",
      default=False, action="store_true",
      help="Enable profiling (a developer option).")
  options, args = parser.parse_args()
  assert len(args), "The list of files or md5 sums must be not empty."
  logging_level = logging.INFO
  if options.quiet:
    logging_level = logging.WARNING
  elif options.debug:
    # If both flags are set, debug wins.
    logging_level = logging.DEBUG
  logging.basicConfig(level=logging_level)
  logging.debug("Starting.")

  configuration.SetUpSqlobjectConnection()
  dm = database.DatabaseManager()
  dm.AutoManage()


  err_msg_list = []
  if not options.osrel_commas:
    err_msg_list.append("Please specify --os-releases.")
  if not options.arch:
    err_msg_list.append("Please specify --architecture.")
  if err_msg_list:
    raise UsageError(" ".join(err_msg_list))

  stats_list = []
  collector = package_stats.StatsCollector(
      logger=logging,
      debug=options.debug)
  # We need to separate files and md5 sums.
  md5_sums, file_list = [], []
  for arg in args:
    if struct_util.IsMd5(arg):
      md5_sums.append(arg)
    else:
      file_list.append(arg)
  if file_list:
    stats_list = collector.CollectStatsFromFiles(file_list, None)
  # We need the md5 sums of these files
  md5_sums.extend([x["basic_stats"]["md5_sum"] for x in stats_list])
  assert md5_sums, "The list of md5 sums must not be empty."
  logging.debug("md5_sums: %s", md5_sums)
  osrel_list = options.osrel_commas.split(",")
  logging.debug("Reading packages data from the database.")
  # This part might need improvements in order to handle a whole
  # catalog.  On the other hand, if we already have the whole catalog in
  # the database, we can do it altogether differently.
  # Transforming the result to a list in order to force object
  # retrieval.
  sqo_pkgs = list(models.Srv4FileStats.select(
    sqlobject.IN(models.Srv4FileStats.q.md5_sum, md5_sums)))
  tags_for_all_osrels = []
  try:
    sqo_catrel = models.CatalogRelease.selectBy(name=options.catrel).getOne()
  except sqlobject.main.SQLObjectNotFound, e:
    logging.fatal("Fetching from the db has failed: catrel=%s",
                  repr(str(options.catrel)))
    logging.fatal("Available catalog releases:")
    sqo_catrels = models.CatalogRelease.select()
    for sqo_catrel in sqo_catrels:
      logging.fatal(" - %s", sqo_catrel.name)
    raise
  sqo_arch = models.Architecture.selectBy(name=options.arch).getOne()
  for osrel in osrel_list:
    sqo_osrel = models.OsRelease.selectBy(short_name=osrel).getOne()
    dm.VerifyContents(sqo_osrel, sqo_arch)
    check_manager = checkpkg_lib.CheckpkgManager2(
        CHECKPKG_MODULE_NAME,
        sqo_pkgs,
        osrel,
        options.arch,
        options.catrel,
        debug=options.debug,
        show_progress=(os.isatty(1) and not options.quiet))
    # Running the checks, reporting and exiting.
    exit_code, screen_report, tags_report = check_manager.Run()
    screen_report = unicode(screen_report)
    if not options.quiet and screen_report:
      # TODO: Write this to screen only after overrides are applied.
      sys.stdout.write(screen_report)
    else:
      logging.debug("No screen report.")

    overrides_list = [list(pkg.GetOverridesResult()) for pkg in sqo_pkgs]
    override_list = reduce(operator.add, overrides_list)
    args = (sqo_osrel, sqo_arch, sqo_catrel)
    tag_lists = [list(pkg.GetErrorTagsResult(*args)) for pkg in sqo_pkgs]
    error_tags = reduce(operator.add, tag_lists)
    (tags_after_overrides,
     unapplied_overrides) = overrides.ApplyOverrides(error_tags, override_list)
    tags_for_all_osrels.extend(tags_after_overrides)
    if not options.quiet:
      if tags_after_overrides:
        print textwrap.fill(BEFORE_OVERRIDES, 80)
        for checkpkg_tag in tags_after_overrides:
          print checkpkg_tag.ToGarSyntax()
        print textwrap.fill(AFTER_OVERRIDES, 80)
      if unapplied_overrides:
        print textwrap.fill(UNAPPLIED_OVERRIDES, 80)
        for override in unapplied_overrides:
          print u"* Unused %s" % override
  exit_code = bool(tags_for_all_osrels)
  sys.exit(exit_code)


if __name__ == '__main__':
  if "--profile" in sys.argv:
    import cProfile
    t_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    home = os.environ["HOME"]
    cprof_file_name = os.path.join(
        home, ".checkpkg", "run-modules-%s.cprof" % t_str)
    cProfile.run("main()", sort=1, filename=cprof_file_name)
  else:
    main()
