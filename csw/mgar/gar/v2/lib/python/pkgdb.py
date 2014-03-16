#!/opt/csw/bin/python2.6
# coding=utf-8
#
# $Id$

import ConfigParser
import datetime
import getpass
import hashlib
import itertools
import logging
import optparse
import os
import os.path
import progressbar
import progressbar.widgets
import re
import socket
import sqlobject
import sys

from sqlobject import sqlbuilder
from Cheetah.Template import Template

from lib.python import catalog
from lib.python import checkpkg_lib
from lib.python import common_constants
from lib.python import configuration
from lib.python import database
from lib.python import models as m
from lib.python import package_checks
from lib.python import package_stats
from lib.python import rest
from lib.python import shell
from lib.python import struct_util
from lib.python import system_pkgmap

USAGE = """
  Preparing the database:
       %prog initdb
       %prog system-metadata-to-disk [ <infile-contents> <infile-pkginfo>
                                    [ <outfile> [ <osrel> <arch> ] ] ]
       %prog import-system-metadata <osrel> <arch>

  Managing individual packages:
       %prog importpkg <file1> [ ... ]
       %prog removepkg <md5sum> [ ... ]

  Managing catalogs:
       %prog add-to-cat <osrel> <arch> <cat-release> <md5sum> [ ... ]
       %prog del-from-cat <osrel> <arch> <cat-release> <md5sum> [ ... ]
       %prog sync-cat-from-file <osrel> <arch> <cat-release> <catalog-file>
       %prog sync-catalogs-from-tree <cat-release> <opencsw-dir>
       %prog show cat [options]

  Inspecting individual packages:
       %prog show errors <md5sum> [ ... ]
       %prog show pkg <pkgname> [ ... ]
       %prog gen-html <md5sum> [ ... ]
       %prog pkg search <catalogname>
       %prog show basename [options] <filename>
       %prog show filename [options] <filename>
       %prog show files <md5-sum>

  osrel := SunOS5.8 | SunOS5.9 | SunOS5.10 | SunOS5.11
  arch := i386 | sparc

Examples:
    %prog add-to-cat SunOS5.9 sparc unstable <md5sum>
    %prog del-from-cat SunOS5.10 i386 testing <md5sum>
"""

SHOW_PKG_TMPL = """catalogname:    $catalogname
pkgname:        $pkginst.pkgname
basename:       $basename
mtime:          $mtime
md5_sum:        $md5_sum
arch:           $arch.name
os_rel:         $os_rel.short_name
maintainer:     $maintainer.email
version_string: $version_string
rev:            $rev
stats_version:  $stats_version
"""

DEFAULT_TEMPLATE_FILENAME = "../lib/python/pkg-review-template.html"
CATALOGS_ALLOWED_TO_GENERATE = frozenset([
  "beanie",
  "bratislava",
  "dublin",
  "kiel",
  "unstable",
])
CATALOGS_ALLOWED_TO_BE_IMPORTED = frozenset([
  "beanie",
  "bratislava",
  "dublin",
  "kiel",
  "legacy",
  "unstable",
])


class Error(Exception):
  "Generic error in the program."


class UsageError(Error):
  "Error in command line options."


class OpencswTreeError(Error):
  "A problem with the OpenCSW directory tree."


class HtmlGenerator(object):

  def __init__(self, identifiers, template=None, rest_client=None, debug=False):
    """Initialize the object

    args: identifiers: md5 sums or file names of packages
    template: Optional HTML template
    """
    self.template = template
    self.identifiers = identifiers
    self.debug = debug
    assert rest_client is not None, 'You need to pass rest_client here'
    self.rest_client = rest_client

  def GetErrorTagsResult(self, srv4):
    res = m.CheckpkgErrorTag.select(
        m.CheckpkgErrorTag.q.srv4_file==srv4)
    return res

  def GetOverrideResult(self, srv4):
    res = m.CheckpkgOverride.select(
        m.CheckpkgOverride.q.srv4_file==srv4)
    return res

  def GenerateHtml(self):
    pkgstats = []
    # Add error tags
    for identifier in self.identifiers:
      srv4 = GetPkg(identifier)
      data = self.rest_client.GetPkgstatsByMd5(srv4.md5_sum)
      build_src_url_svn = srv4.GetSvnUrl()
      build_src_url_trac = srv4.GetTracUrl()
      if "OPENCSW_REPOSITORY" in data["pkginfo"]:
        data["build_src"] = data["pkginfo"]["OPENCSW_REPOSITORY"]
      else:
        data["build_src"] = u"Repository address unknown"
      data["build_src_url_svn"] = build_src_url_svn
      data["build_src_url_trac"] = build_src_url_trac
      data["error_tags"] = list(self.GetErrorTagsResult(srv4))
      data["overrides"] = list(self.GetOverrideResult(srv4))
      pkgstats.append(data)
    # This assumes the program is run as "bin/pkgdb", and not "lib/python/pkgdb.py".
    if not self.template:
      tmpl_filename = os.path.join(os.path.split(__file__)[0],
                                   DEFAULT_TEMPLATE_FILENAME)
    else:
      tmpl_filename = self.template
    tmpl_str = open(tmpl_filename, "r").read()
    t = Template(tmpl_str, searchList=[{
      "pkgstats": pkgstats,
      "hachoir_machines": common_constants.MACHINE_ID_METADATA,
    }])
    return unicode(t)


def NormalizeId(some_id):
  """Used to normalize identifiers (md5, filename).

  Currently, strips paths off given package paths."""
  if not struct_util.IsMd5(some_id):
    logging.warning(
        "Given Id (%s) is not an md5 sum. Will attempt to retrieve "
        "it from the datbase, but it might fail.",
        repr(some_id))
  return os.path.basename(some_id)


def GetPkg(some_id):
  some_id = NormalizeId(some_id)
  logging.debug("Selecting from db: %s", repr(some_id))
  res = m.Srv4FileStats.select(
      sqlobject.OR(
        m.Srv4FileStats.q.md5_sum==some_id,
        m.Srv4FileStats.q.catalogname==some_id))
  try:
    srv4 = res.getOne()
  except sqlobject.main.SQLObjectIntegrityError, e:
    logging.warning(e)
    for row in res:
      print "- %s %s %s" % (row.md5_sum, row.version_string, row.mtime)
    raise
  except sqlobject.main.SQLObjectNotFound, e:
    logging.fatal("Could not locate a package identified by %s",
                  repr(some_id))
    raise
  logging.debug("Got: %s", srv4)
  return srv4


class CatalogImporter(object):

  def __init__(self, debug=False):
    self.debug = debug
    config = configuration.GetConfig()
    username, password = rest.GetUsernameAndPassword()
    self.rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        username=username,
        password=password,
        debug=debug)

  def SyncFromCatalogFile(self, osrel, arch, catrel, catalog_file,
      force_unpack=False):
    """Syncs a given catalog from a catalog file.

    Imports srv4 files if necessary.
    """
    if catrel not in CATALOGS_ALLOWED_TO_BE_IMPORTED:
      raise UsageError("Catalogs that can be imported: %s"
                       % CATALOGS_ALLOWED_TO_BE_IMPORTED)

    catalog_dir = os.path.dirname(catalog_file)
    # The plan:
    # - read in the catalog file, and build a md5-filename correspondence
    # data structure.
    logging.debug("Reading the catalog file from disk.")
    src_catalog = catalog.OpencswCatalog(open(catalog_file, "rb"))
    catalog_data = src_catalog.GetCatalogData()
    cat_entry_by_md5 = {}
    cat_entry_by_basename = {}
    for catalog_entry in catalog_data:
      cat_entry_by_md5[catalog_entry["md5sum"]] = catalog_entry
      cat_entry_by_basename[catalog_entry["file_basename"]] = catalog_entry

    # - import all srv4 files that were not in the database so far
    entries_to_import = []

    logging.debug("Checking which srv4 files have already been indexed.")
    existence_data = (
        self.rest_client.BulkQueryStatsExistence(list(cat_entry_by_md5)))
    entries_to_import = [cat_entry_by_md5[x]
                         for x in existence_data['missing_stats']]

    md5_sums = []
    if entries_to_import:
      collector = package_stats.StatsCollector(logger=logging, debug=self.debug)
      for entry in entries_to_import:
        entry['pkg_path'] = os.path.join(catalog_dir, entry['file_basename'])
      if len(entries_to_import) < 15:
        logging.info("Srv4 files to unpack:")
        for basename in sorted(x['file_basename'] for x in entries_to_import):
          logging.info(" + %s", basename)
      else:
        logging.info('Importing %d packages.', len(entries_to_import))
      md5_sums = collector.CollectStatsFromCatalogEntries(
          entries_to_import, force_unpack=force_unpack)

    # - sync the specific catalog
    #   - find the md5 sum list of the current catalog
    logging.debug("Retrieving current catalog assigments from the db.")
    sqo_osrel = m.OsRelease.selectBy(short_name=osrel).getOne()
    sqo_arch = m.Architecture.selectBy(name=arch).getOne()
    sqo_catrel = m.CatalogRelease.selectBy(name=catrel).getOne()
    res = m.Srv4FileInCatalog.select(
        sqlobject.AND(
          m.Srv4FileInCatalog.q.osrel==sqo_osrel,
          m.Srv4FileInCatalog.q.arch==sqo_arch,
          m.Srv4FileInCatalog.q.catrel==sqo_catrel))
    db_srv4s_in_cat_by_md5 = {}
    # TODO(maciej): Convert package removals to REST. Maybe in bulk?
    for srv4_in_cat in res:
      try:
        srv4 = srv4_in_cat.srv4file
        if srv4.use_to_generate_catalogs:
          db_srv4s_in_cat_by_md5[srv4.md5_sum] = srv4_in_cat
      except sqlobject.main.SQLObjectNotFound as e:
        logging.warning("Could not retrieve a srv4 file from the db: %s", e)
        # Since the srv4_in_cat object has lost its reference, there's no use
        # keeping it around.
        srv4_in_cat.destroySelf()

    disk_md5s = set(cat_entry_by_md5)
    db_md5s = set(db_srv4s_in_cat_by_md5)
    #   - match the md5 sum lists between db and disk
    md5_sums_to_add = disk_md5s.difference(db_md5s)
    md5_sums_to_remove = db_md5s.difference(disk_md5s)
    logging.info("There are %s packages to remove and %s to add",
                 len(md5_sums_to_remove),
                 len(md5_sums_to_add))
    if md5_sums_to_remove:
      logging.info("To remove from %s %s %s:", osrel, arch, catrel)
      for md5 in md5_sums_to_remove:
        logging.info(
            " - %s",
            db_srv4s_in_cat_by_md5[md5].srv4file.basename)

    if md5_sums_to_add and len(md5_sums_to_add) < 15:
      logging.info("To add to from %s %s %s:", osrel, arch, catrel)
      for md5 in md5_sums_to_add:
        logging.info(
            " + %s",
            cat_entry_by_md5[md5]["file_basename"])

    user = getpass.getuser()
    # Remove
    # We could use checkpkg_lib.Catalog.RemoveSrv4(), but it would redo
    # many of the database queries and would be much slower.
    if md5_sums_to_remove:
      logging.info("Removing %d packages from the %s %s %s catalog.",
                   len(md5_sums_to_remove), osrel, arch, catrel)
      for md5 in md5_sums_to_remove:
        db_srv4s_in_cat_by_md5[md5].destroySelf()

    if not md5_sums_to_add:
      return
    logging.info("Adding %d packages to the %s %s %s catalog.",
                 len(md5_sums_to_add),
                 osrel, arch, catrel)
    pbar = progressbar.ProgressBar(widgets=[
      progressbar.widgets.Percentage(),
      ' ',
      progressbar.widgets.ETA(),
      ' ',
      progressbar.widgets.Bar()
    ])
    pbar.maxval = len(md5_sums_to_add)
    pbar.start()
    counter = itertools.count(1)
    for md5 in md5_sums_to_add:
      logging.debug("Adding %s", cat_entry_by_md5[md5]["file_basename"])

      # Explicitly calling the RegisterLevelTwo function, in case the
      # packages have the flag "use_in_catalogs" set to False. Calling
      # this function will set it to True.
      # Note: This makes populating catalogs really, really slow, and
      # causes subsequent runs to be slow as well. It should only be
      # a temporary measure.
      try:
        pkg = m.Srv4FileStats.selectBy(md5_sum=md5).getOne()
        if (not pkg.registered_level_two or
            not pkg.use_to_generate_catalogs):
          self.rest_client.RegisterLevelTwo(md5, use_in_catalogs=True)
      except sqlobject.main.SQLObjectNotFound:
        pass

      # No need to explicitly register the package here; the REST
      # interface will implicitly take care of that (except it will not
      # touch the "use_package_in_catalogs" flag.
      self.rest_client.AddSvr4ToCatalog(catrel, arch, osrel, md5)
      pbar.update(counter.next())
    pbar.finish()

  def SyncFromCatalogTree(self, catrel, base_dir, force_unpack=False):
    logging.debug("SyncFromCatalogTree(%s, %s, force_unpack=%s)",
                  repr(catrel), repr(base_dir), force_unpack)
    if not os.path.isdir(base_dir):
      raise UsageError("%s is not a diractory" % repr(base_dir))
    if catrel not in common_constants.DEFAULT_CATALOG_RELEASES:
      logging.warning(
          "The catalog release %s is not one of the default releases.",
          repr(catrel))
    sqo_catrel = m.CatalogRelease.selectBy(name=catrel).getOne()
    for osrel in common_constants.OS_RELS:
      logging.info("  OS release: %s", repr(osrel))
      sqo_osrel = m.OsRelease.selectBy(short_name=osrel).getOne()
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        logging.info("    Architecture: %s", repr(arch))
        sqo_arch = m.Architecture.selectBy(name=arch).getOne()
        catalog_file = self.ComposeCatalogFilePath(base_dir, osrel, arch)
        if not os.path.exists(catalog_file):
          logging.warning("Could not find %s, skipping.", repr(catalog_file))
          continue
        logging.info("      %s", catalog_file)
        self.SyncFromCatalogFile(osrel, arch, catrel, catalog_file,
            force_unpack=force_unpack)

  def ComposeCatalogFilePath(self, base_dir, osrel, arch):
    short_osrel = osrel.replace("SunOS", "")
    return os.path.join(base_dir, arch, short_osrel, "catalog")


def main():
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-t", "--pkg-review-template", dest="pkg_review_template",
                    help="A Cheetah template used for package review reports.")
  parser.add_option("-r", "--os-release", dest="osrel",
                    default="SunOS5.10",
                    help="E.g. SunOS5.10")
  parser.add_option("-a", "--arch", dest="arch",
                    default="sparc",
                    help="'i386' or 'sparc'")
  parser.add_option("-c", "--catalog-release", dest="catrel",
                    default="unstable",
                    help="E.g. unstable, dublin")
  parser.add_option("--replace", dest="replace",
                    default=False, action="store_true",
                    help="Replace packages when importing (importpkg)")
  parser.add_option("--profile", dest="profile",
                    default=False, action="store_true",
                    help="Turn on profiling")
  parser.add_option("--force-unpack", dest="force_unpack",
                    default=False, action="store_true",
                    help="Force unpacking of packages")
  options, args = parser.parse_args()

  logging_level = logging.INFO
  if options.debug:
    logging_level = logging.DEBUG
  fmt = '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'
  logging.basicConfig(format=fmt, level=logging_level)

  if not args:
    raise UsageError("Please specify a command.  See --help.")
  # SetUpSqlobjectConnection needs to be called after
  # logging.basicConfig
  configuration.SetUpSqlobjectConnection()
  command = args[0]
  args = args[1:]
  if command == 'show':
    subcommand = args[0]
    args = args[1:]
  elif command == 'pkg':
    subcommand = args[0]
    args = args[1:]
  else:
    subcommand = None

  md5_sums = args

  if (command, subcommand) == ('show', 'errors'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      res = m.CheckpkgErrorTag.select(m.CheckpkgErrorTag.q.srv4_file==srv4)
      for row in res:
        print row.pkgname, row.tag_name, row.tag_info, row.catrel.name, row.arch.name,
        print row.os_rel.short_name
  elif (command, subcommand) == ('show', 'overrides'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      res = m.CheckpkgOverride.select(m.CheckpkgOverride.q.srv4_file==srv4)
      for row in res:
        print row.pkgname, row.tag_name, row.tag_info
  elif (command, subcommand) == ('show', 'pkg'):
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      t = Template(SHOW_PKG_TMPL, searchList=[srv4])
      sys.stdout.write(unicode(t))
  elif command == 'gen-html':
    config = configuration.GetConfig()
    username, password = rest.GetUsernameAndPassword()
    rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        username=username,
        password=password,
        debug=options.debug)

    g = HtmlGenerator(md5_sums, options.pkg_review_template, rest_client, options.debug)
    sys.stdout.write(g.GenerateHtml())
  elif command == 'initdb':
    config = configuration.GetConfig()
    database.InitDB(config)
  elif command == 'importpkg':
    collector = package_stats.StatsCollector(
        logger=logging,
        debug=options.debug)
    file_list = args
    catalog_entries = []
    for file_name in file_list:
      file_hash = hashlib.md5()
      chunk_size = 2 * 1024 * 1024
      with open(file_name, 'rb') as fd:
        data = fd.read(chunk_size)
        while data:
          file_hash.update(data)
          data = fd.read(chunk_size)
      data_md5_sum = file_hash.hexdigest()
      catalog_entry = {
          'md5sum': data_md5_sum,
          'file_basename': os.path.basename(file_name),
          'pkg_path': file_name,
      }
      catalog_entries.append(catalog_entry)
    md5_list = collector.CollectStatsFromCatalogEntries(catalog_entries,
        force_unpack=options.force_unpack)
    config = configuration.GetConfig()
    rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        debug=options.debug)

    for md5_sum in md5_list:
      logging.debug("Importing %s", md5_sum)
      rest_client.RegisterLevelTwo(md5_sum)

  elif command == 'removepkg':
    for md5_sum in md5_sums:
      srv4 = GetPkg(md5_sum)
      in_catalogs = list(srv4.in_catalogs)
      if in_catalogs:
        for in_catalog in in_catalogs:
          logging.warning("%s", in_catalog)
        logging.warning(
            "Not removing from the database, because the package "
            "in question is part of at least one catalog.")
      else:
        logging.info("Removing %s", srv4)
        srv4.DeleteAllDependentObjects()
        srv4.destroySelf()
  elif command == 'add-to-cat':
    if len(args) < 4:
      raise UsageError("Not enough arguments, see usage.")
    user = getpass.getuser()
    osrel, arch, catrel = args[:3]
    username, password = rest.GetUsernameAndPassword()
    rest_client = rest.RestClient(username=username, password=password)
    md5_sums = args[3:]
    for md5_sum in md5_sums:
      rest_client.AddSvr4ToCatalog(catrel, arch, osrel, md5_sum)
  elif command == 'del-from-cat':
    if len(args) < 4:
      raise UsageError("Not enough arguments, see usage.")
    osrel, arch, catrel= args[:3]
    md5_sums = args[3:]
    username, password = rest.GetUsernameAndPassword()
    rest_client = rest.RestClient(username=username, password=password)
    for md5_sum in md5_sums:
      rest_client.RemoveSvr4FromCatalog(catrel, arch, osrel, md5_sum)
  elif command == 'system-metadata-to-disk':
    logging.debug("Args: %s", args)
    outfile = None
    infile_contents = common_constants.DEFAULT_INSTALL_CONTENTS_FILE
    infile_pkginfo = None
    osrel, arch = (None, None)
    if len(args) >= 2:
      infile_contents = args[0]
      infile_pkginfo = args[1]
    if len(args) >= 3:
      outfile = args[2]
    if len(args) >= 4:
      if len(args) == 5:
        osrel, arch = args[3:5]
      else:
        raise UsageError("Wrong number of arguments (%s), see usage."
                    % len(args))
    spi = system_pkgmap.Indexer(outfile,
                                infile_contents,
                                infile_pkginfo,
                                osrel,
                                arch)
    spi.IndexAndSave()
  elif command == 'import-system-metadata':
    if len(args) < 2:
      raise UsageError("Usage: ... import-system-metadata <osrel> <arch>")
    osrel = args[0]
    arch = args[1]
    importer = system_pkgmap.InstallContentsImporter(osrel, arch,
                                                     debug=options.debug)
    importer.Import(show_progress=(not options.debug))
  elif (command, subcommand) == ('pkg', 'search'):
    logging.debug("Searching for %s", args)
    sqo_osrel = m.OsRelease.selectBy(short_name=options.osrel).getOne()
    sqo_arch = m.Architecture.selectBy(name=options.arch).getOne()
    sqo_catrel = m.CatalogRelease.selectBy(name=options.catrel).getOne()
    if len(args) < 1:
      logging.fatal("Wrong number of arguments: %s", len(args))
      raise SystemExit
    for catalogname in args:
      join = [
          sqlbuilder.INNERJOINOn(None,
            m.Srv4FileInCatalog,
            m.Srv4FileInCatalog.q.srv4file==m.Srv4FileStats.q.id),
      ]
      res = m.Srv4FileStats.select(
          sqlobject.AND(
            m.Srv4FileInCatalog.q.osrel==sqo_osrel,
            m.Srv4FileInCatalog.q.arch==sqo_arch,
            m.Srv4FileInCatalog.q.catrel==sqo_catrel,
            m.Srv4FileStats.q.catalogname.contains(catalogname),
            m.Srv4FileStats.q.use_to_generate_catalogs==True),
          join=join,
      ).orderBy("catalogname")
      for sqo_srv4 in res:
        print "%s %s" % (sqo_srv4.basename, sqo_srv4.md5_sum)
  elif command == 'sync-cat-from-file':
    if len(args) != 4:
      raise UsageError("Wrong number of arguments, see usage.")
    osrel, arch, catrel, catalog_file = args
    ci = CatalogImporter(debug=options.debug)
    ci.SyncFromCatalogFile(osrel, arch, catrel, catalog_file)
  elif command == 'sync-catalogs-from-tree':
    if len(args) != 2:
      raise UsageError("Wrong number of arguments, see usage.")
    ci = CatalogImporter(debug=options.debug)
    catrel, base_dir = args
    ci.SyncFromCatalogTree(catrel, base_dir, options.force_unpack)
  elif (command, subcommand) == ('show', 'cat'):
    sqo_osrel, sqo_arch, sqo_catrel = m.GetSqoTriad(
        options.osrel, options.arch, options.catrel)
    res = m.GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel)
    for obj in res:
      print obj.catalogname, obj.basename, obj.md5_sum
  elif (command, subcommand) == ('show', 'files'):
    md5_sum = args[0]
    join = [
        sqlbuilder.INNERJOINOn(None,
          m.Srv4FileStats,
          m.CswFile.q.srv4_file==m.Srv4FileStats.q.id),
    ]
    res = m.CswFile.select(
        m.Srv4FileStats.q.md5_sum==md5_sum,
        join=join,
    )
    for obj in res:
      print os.path.join(obj.path, obj.basename)
  elif (command, subcommand) == ('show', 'basename'):
    db_catalog = checkpkg_lib.Catalog()
    for arg in args:
      pkgs_by_path = db_catalog.GetPathsAndPkgnamesByBasename(
          arg, options.osrel, options.arch, options.catrel)
      for file_path in pkgs_by_path:
        print os.path.join(file_path, arg), ", ".join(pkgs_by_path[file_path])
  elif (command, subcommand) == ('show', 'filename'):
    db_catalog = checkpkg_lib.Catalog()
    for arg in args:
      pkgs = db_catalog.GetPkgByPath(
          arg, options.osrel, options.arch, options.catrel)
      print " ".join(pkgs)
  else:
    raise UsageError("Command unrecognized: %s" % command)


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
