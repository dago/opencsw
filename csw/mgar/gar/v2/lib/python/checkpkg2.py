#!/opt/csw/bin/python2.6
#
# checkpkg
#

import datetime
import hashlib
import logging
import operator
import optparse
import os
import sqlobject
import sys
import textwrap

from lib.python import checkpkg_lib
from lib.python import common_constants
from lib.python import configuration
from lib.python import errors
from lib.python import models
from lib.python import overrides
from lib.python import package_stats
from lib.python import rest
from lib.python import struct_util

USAGE = """%prog [ options ] pkg1 [ pkg2 [ ... ] ]"""
CHECKPKG_MODULE_NAME = "The main checking module."
BEFORE_OVERRIDES = """If any of the reported errors were false positives, you
can override them pasting the lines below to the GAR recipe."""

AFTER_OVERRIDES = (
  "Do not copy/paste these overrides without thinking!",

  "If you're not sure, scroll up and read the details. If you're still not "
  "sure, go to the wiki and read about the error tags you see, or ask "
  "on the maintainers@ mailing list.",

  "http://wiki.opencsw.org/checkpkg-error-tags",
)

UNAPPLIED_OVERRIDES = (
"""WARNING: Some overrides did not match any errors.  They can probably be
removed, as they don't take any effect anyway.  If you're getting errors at the
same time, maybe you didn't specify your overrides correctly.""")

cc = common_constants

class UsageError(errors.Error):
  """Problem with usage, e.g. command line options."""


def VerifyContents(sqo_osrel, sqo_arch):
  """Verify that we know the system files on the OS release and architecture."""
  res = models.Srv4FileStats.select(
      sqlobject.AND(
        models.Srv4FileStats.q.use_to_generate_catalogs==False,
        models.Srv4FileStats.q.registered_level_two==True,
        models.Srv4FileStats.q.os_rel==sqo_osrel,
        models.Srv4FileStats.q.arch==sqo_arch))
  # logging.warning("VerifyContents(): Packages Count: %s", res.count())
  system_pkgs = res.count()
  logging.debug("VerifyContents(%s, %s): %s", sqo_osrel, sqo_arch, system_pkgs)
  if system_pkgs < 10:
    msg = (
        "Checkpkg can't find system files for %s %s in the cache database.  "
        "These are files such as /usr/lib/libc.so.1.  "
        "Private DB setup: "
        "you can only check packages built for the same Solaris version "
        "you're running on this machine.  "
        "For instance, you can't check a SunOS5.9 package on SunOS5.10. "
        "Shared DB setup (e.g. OpenCSW maintainers): "
        "If you have one home directory on multiple hosts, make sure you "
        "run checkpkg on the host you intended to.  "
        "To fix, go to a %s %s host and execute: pkgdb system-files-to-file; "
        "pkgdb import-system-file install-contents-%s-%s.marshal; "
        "See http://wiki.opencsw.org/checkpkg for more information."
        % (sqo_osrel.short_name, sqo_arch.name,
           sqo_arch.name, sqo_osrel.short_name,
           sqo_osrel.short_name, sqo_arch.name))
    logging.fatal(msg)
    raise errors.DatabaseContentsError('OS files not indexed.')


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
  parser.add_option("-a", "--catalog-architecture",
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

  err_msg_list = []
  if not options.osrel_commas:
    err_msg_list.append("Please specify --os-releases.")
  if not options.arch:
    err_msg_list.append("Please specify --catalog-architecture.")
  if options.arch not in cc.PHYSICAL_ARCHITECTURES:
    err_msg_list.append(
        "Valid --catalog-architecture values are: %s, you passed: %r"
        % (cc.PHYSICAL_ARCHITECTURES, options.arch))
  if err_msg_list:
    raise UsageError(" ".join(err_msg_list))

  md5_sums_from_files = []
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

  config = configuration.GetConfig()
  rest_client = rest.RestClient(
      pkgdb_url=config.get('rest', 'pkgdb'),
      releases_url=config.get('rest', 'releases'))

  if file_list:
    def MakeEntry(file_name):
      file_hash = hashlib.md5()
      with open(file_name, "r") as fd:
        chunk_size = 2 * 1024 * 1024
        data = fd.read(chunk_size)
        while data:
          file_hash.update(data)
          data = fd.read(chunk_size)
        md5_sum = file_hash.hexdigest()
        del file_hash
      _, file_basename = os.path.split(file_name)
      return {
          'pkg_path': file_name,
          'md5sum': md5_sum,
          'file_basename': file_basename,
      }
    entries = [MakeEntry(x) for x in file_list]
    md5_sums_from_files = collector.CollectStatsFromCatalogEntries(entries, False)
    for md5_sum in md5_sums_from_files:
      rest_client.RegisterLevelOne(md5_sum)
  # We need the md5 sums of these files
  md5_sums.extend(md5_sums_from_files)
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
  except sqlobject.main.SQLObjectNotFound as e:
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
    VerifyContents(sqo_osrel, sqo_arch)
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
        print(textwrap.fill(BEFORE_OVERRIDES, 80))
        for checkpkg_tag in tags_after_overrides:
          print checkpkg_tag.ToGarSyntax()
        print
        for paragraph in AFTER_OVERRIDES:
          print(textwrap.fill(paragraph, 80))
          print
      elif error_tags:
        msg = (
            'Fair enough, there were %d error tags, '
            'but they were all overridden. '
            "Just make sure you didn't override anything silly, like "
            'sparc binaries in a i386 package.'
            % len(error_tags))
        print
      else:
        print('Jolly good! All checks passed, no error tags reported.')

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
