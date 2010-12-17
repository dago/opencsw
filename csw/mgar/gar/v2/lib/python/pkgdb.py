#!/usr/bin/env python2.6
# coding=utf-8
#
# $Id$

import ConfigParser
import optparse
import models as m
import sqlobject
import cPickle
import logging
import code
import os
import os.path
import re
import socket
import sys
import package_checks
import package_stats
import database
import configuration
import checkpkg_lib
import common_constants
import system_pkgmap
import catalog
from Cheetah.Template import Template

USAGE = """
  Preparing the database:
       %prog initdb
       %prog importpkg <file1> [ ... ]
       %prog system-files-to-file [ <infile-contents> <infile-pkginfo>
                                    [ <outfile> [ <osrel> <arch> ] ] ]
       %prog import-system-file <infile>

  Managing catalogs:
       %prog add-to-cat <osrel> <arch> <cat-release> <md5sum> [ ... ]
       %prog del-from-cat <osrel> <arch> <cat-release> <md5sum> [ ... ]
       %prog sync-cat-from-file <osrel> <arch> <cat-release> <catalog-file>
       %prog sync-catalogs-from-tree <cat-release> <directory>

  Inspecting individual packages:
       %prog show errors <md5sum> [ ... ]
       %prog show pkg <pkgname> [ ... ]
       %prog gen-html <md5sum> [ ... ]
       %prog pkg search <catalogname>
       %prog show basename [options] <filename>


Examples:
    %prog add-to-cat <md5sum> SunOS5.9 sparc unstable
    %prog del-from-cat <md5sum> SunOS5.10 i386 testing
"""

SHOW_PKG_TMPL = """catalogname:    $catalogname
pkgname:        $pkginst.pkgname
basename:       $basename
mtime:          $mtime
md5_sum:        $md5_sum
arch:           $arch.name
os_rel:         $os_rel.short_name
maintainer:     $maintainer.email
latest:         $latest
version_string: $version_string
rev:            $rev
stats_version:  $stats_version
"""

DEFAULT_TEMPLATE_FILENAME = "../lib/python/pkg-review-template.html"


class Error(Exception):
  "Generic error in the program."


class UsageError(Error):
  "Error in command line options."


class HtmlGenerator(object):

  def __init__(self, md5_sums, template=None):
    self.md5_sums = md5_sums
    self.template = template

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
    for md5_sum in self.md5_sums:
      srv4 = GetPkg(md5_sum)
      data = cPickle.loads(str(srv4.data_obj.pickle))
      if "OPENCSW_REPOSITORY" in data["pkginfo"]:
        build_src = data["pkginfo"]["OPENCSW_REPOSITORY"]
        build_src_url_svn = re.sub(r'([^@]*).*', r'\1/Makefile', build_src)
        build_src_url_trac = re.sub(
            r'https://gar.svn.(sf|sourceforge).net/svnroot/gar/([^@]+)@(.*)',
            r'http://sourceforge.net/apps/trac/gar/browser/\2/Makefile?rev=\3',
            build_src)
      else:
        build_src = None
        build_src_url_svn = None
        build_src_url_trac = None
      data["build_src"] = build_src
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
      "hachoir_machines": package_checks.HACHOIR_MACHINES,
      }])
    return unicode(t)


def GetPkg(some_id):
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
  logging.debug("Got: %s", srv4)
  return srv4


class CatalogImporter(object):

  def __init__(self, debug=False):
    self.debug = debug

  def SyncFromCatalogFile(self, osrel, arch, catrel, catalog_file):
    """Syncs a given catalog from a catalog file.

    Imports srv4 files if necessary.
    """
    catalog_dir = os.path.dirname(catalog_file)
    # The plan:
    # - read in the catalog file, and build a md5-filename correspondence
    # data structure.
    logging.debug("Reading the catalog file from disk.")
    src_catalog = catalog.OpencswCatalog(catalog_file)
    catalog_data = src_catalog.GetCatalogData()
    cat_entry_by_md5 = {}
    cat_entry_by_basename = {}
    for catalog_entry in catalog_data:
      cat_entry_by_md5[catalog_entry["md5sum"]] = catalog_entry
      cat_entry_by_basename[catalog_entry["file_basename"]] = catalog_entry
    # - import all srv4 files that were not in the database so far
    sqo_objects = set()
    entries_to_import = []
    logging.debug("Checking which srv4 files are already in the db.")
    for md5 in cat_entry_by_md5:
      try:
        sqo_list = m.Srv4FileStats.selectBy(md5_sum=md5).getOne()
      except sqlobject.main.SQLObjectNotFound, e:
        entries_to_import.append(cat_entry_by_md5[md5])
    basenames = [x["file_basename"] for x in entries_to_import]
    file_list = []
    if entries_to_import:
      logging.info("Srv4 files to import:")
      for basename in sorted(basenames):
        logging.info(" + %s", basename)
        file_list.append(os.path.join(catalog_dir, basename))
    new_statdicts = []
    if file_list:
      collector = package_stats.StatsCollector(
          logger=logging,
          debug=self.debug)
      new_statdicts = collector.CollectStatsFromFiles(file_list, None)
    new_statdicts_by_md5 = {}
    if new_statdicts:
      logging.info("Marking imported packages as registered.")
      for statdict in new_statdicts:
        new_statdicts_by_md5[statdict["basic_stats"]["md5_sum"]] = statdict
        package_stats.PackageStats.ImportPkg(statdict)
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
    for srv4_in_cat in res:
      if srv4_in_cat.srv4file.use_to_generate_catalogs:
        db_srv4s_in_cat_by_md5[srv4_in_cat.srv4file.md5_sum] = srv4_in_cat
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
    if md5_sums_to_add:
      logging.info("To add to from %s %s %s:", osrel, arch, catrel)
      for md5 in md5_sums_to_add:
        logging.info(
            " + %s",
            cat_entry_by_md5[md5]["file_basename"])
    # Remove
    # We could use checkpkg_lib.Catalog.RemoveSrv4(), but it would redo
    # many of the database queries and would be much slower.
    if md5_sums_to_remove:
      logging.info("Removing assignments from the catalog.")
      for md5 in md5_sums_to_remove:
        db_srv4s_in_cat_by_md5[md5].destroySelf()
    # Add
    if md5_sums_to_add:
      logging.info("Adding srv4 files to the %s %s %s catalog.",
                   osrel, arch, catrel)
      db_catalog = checkpkg_lib.Catalog()
      for md5 in md5_sums_to_add:
        logging.debug("Adding %s", cat_entry_by_md5[md5]["file_basename"])
        sqo_srv4 = m.Srv4FileStats.selectBy(md5_sum=md5).getOne()

        # If a package was previously examined, but not registered, we need to
        # register it now, to allow inclusion in a catalog.
        if not sqo_srv4.registered:
          logging.warning(
              "Package %s was not registered for releases. Registering it.",
              sqo_srv4.basename)
          sqo_srv4.registered = True
        db_catalog.AddSrv4ToCatalog(
            sqo_srv4, osrel, arch, catrel)

  def SyncFromCatalogTree(self, catrel, base_dir):
    logging.debug("SyncFromCatalogTree(%s, %s)",
                  repr(catrel), repr(base_dir))
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
        self.SyncFromCatalogFile(osrel, arch, catrel, catalog_file)

  def ComposeCatalogFilePath(self, base_dir, osrel, arch):
    short_osrel = osrel.replace("SunOS", "")
    return os.path.join(base_dir, arch, short_osrel, "catalog")


def main():
  configuration.SetUpSqlobjectConnection()

  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-t", "--pkg-review-template", dest="pkg_review_template",
                    help="A Cheetah template used for package review reports.")
  parser.add_option("-r", "--os-release", dest="osrel",
                    default="SunOS5.9",
                    help="E.g. SunOS5.9")
  parser.add_option("-a", "--arch", dest="arch",
                    default="sparc",
                    help="'i386' or 'sparc'")
  parser.add_option("-c", "--catalog-release", dest="catrel",
                    default="current",
                    help="E.g. current, unstable, testing, stable")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  if not args:
    raise UsageError("Please specify a command.  Se --help.")
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
        print row.pkgname, row.tag_name, row.tag_info
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
    g = HtmlGenerator(md5_sums, options.pkg_review_template)
    sys.stdout.write(g.GenerateHtml())
  elif command == 'initdb':
    config = configuration.GetConfig()
    db_uri = configuration.ComposeDatabaseUri(config)
    dbc = database.CatalogDatabase(uri=db_uri)
    dbc.CreateTables()
    dbc.InitialDataImport()
  elif command == 'importpkg':
    collector = package_stats.StatsCollector(
        logger=logging,
        debug=options.debug)
    file_list = args
    stats_list = collector.CollectStatsFromFiles(file_list, None)
    for stats in stats_list:
      logging.debug(
          "Importing %s, %s",
          stats["basic_stats"]["md5_sum"],
          stats["basic_stats"]["pkg_basename"])
      package_stats.PackageStats.ImportPkg(stats)
  elif command == 'add-to-cat':
    if len(args) <= 3:
      raise UsageError("Not enough arguments, see usage.")
    osrel, arch, catrel= args[:3]
    c = checkpkg_lib.Catalog()
    md5_sums = args[3:]
    for md5_sum in md5_sums:
      logging.debug("Adding %s to the catalog", md5_sum)
      try:
        sqo_srv4 = m.Srv4FileStats.select(
            m.Srv4FileStats.q.md5_sum==md5_sum).getOne()
        c.AddSrv4ToCatalog(sqo_srv4, osrel, arch, catrel)
      except sqlobject.main.SQLObjectNotFound, e:
        logging.warning("Srv4 file %s was not found in the database.",
                        md5_sum)
  elif command == 'del-from-cat':
    if len(args) <= 4:
      raise UsageError("Not enough arguments, see usage.")
    osrel, arch, catrel= args[:3]
    md5_sums = args[3:]
    for md5_sum in md5_sums:
      sqo_srv4 = m.Srv4FileStats.select(
          m.Srv4FileStats.q.md5_sum==md5_sum).getOne()
      c.RemoveSrv4(sqo_srv4, osrel, arch, catrel)
  elif command == 'system-files-to-file':
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
  elif command == 'import-system-file':
    infile = args[0]
    importer = system_pkgmap.InstallContentsImporter()
    infile_fd = open(infile, "r")
    importer.ImportFromFile(infile_fd, show_progress=True)
  elif (command, subcommand) == ('pkg', 'search'):
    logging.debug("Searching for %s", args)
    if len(args) < 1:
      logging.fatal("Wrong number of arguments: %s", len(args))
      raise SystemExit
    for catalogname in args:
      res = m.Srv4FileStats.select(
          sqlobject.AND(
            m.Srv4FileStats.q.catalogname.contains(catalogname),
            m.Srv4FileStats.q.use_to_generate_catalogs==True)
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
    ci.SyncFromCatalogTree(catrel, base_dir)
  elif (command, subcommand) == ('show', 'basename'):
    db_catalog = checkpkg_lib.Catalog()
    for arg in args:
      pkgs_by_path = db_catalog.GetPathsAndPkgnamesByBasename(
          arg, options.osrel, options.arch, options.catrel)
      for file_path in pkgs_by_path:
        print os.path.join(file_path, arg), ", ".join(pkgs_by_path[file_path])
  else:
    raise UsageError("Command unrecognized: %s" % command)


if __name__ == '__main__':
  main()
