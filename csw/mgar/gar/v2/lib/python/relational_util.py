"""Managing the relational (as opposed to key-value) part of the database.

There 3 states in which a package can be as far as the relational part of the
database is concerned:

  - absent: there are blobs in the database so you can get the metadata, but
    there's nothing in the relational part.

  - partially registered: there is an entry in the Srv4FileStats main table,
    but no entries in the CswFile table

  - fully registered: All relational tables are populated. This is required for
    a package to be part of any catalogs (because of the need for fast queries).

"""

import cjson
import dateutil.parser
import logging
import os
import re
import sqlobject
from sqlobject import sqlbuilder

from lib.python import errors
from lib.python import models
from lib.python import representations


PACKAGE_STATS_VERSION = 13L
logger = logging.getLogger('opencsw.relationalutil')


def GetOrSetPkginst(pkgname):
  try:
    pkginst = models.Pkginst.selectBy(pkgname=pkgname).getOne()
  except sqlobject.main.SQLObjectNotFound as exc:
    logger.debug('pkginst %s not found (%r), making a new one'
                  % (pkgname, exc))
    pkginst = models.Pkginst(pkgname=pkgname)
  return pkginst


def StatsStructToDatabaseLevelOne(md5_sum, use_in_catalogs=True):
  """Creates entries for a package in the relational part of the database.

  This function is intended to be called by the restful interface, not by
  applications directly. Therefore, we're not using the RESTful interface here.

  Note: This operation is destructive! Calling it results in the package being
  removed from all the catalogs.
  """
  # We assume stats already exist. If not, we're letting sqlobject throw an
  # exception.
  pkg_stats_sqo = models.Srv4FileStatsBlob.selectBy(md5_sum=md5_sum).getOne()
  pkg_stats = cjson.decode(pkg_stats_sqo.json)

  pkgname = pkg_stats["basic_stats"]["pkgname"]
  pkginst = GetOrSetPkginst(pkgname)

  arch_name = pkg_stats["pkginfo"]["ARCH"]
  arch = models.Architecture.selectBy(name=arch_name).getOne()

  filename_arch_str = pkg_stats["basic_stats"]["parsed_basename"]["arch"]
  filename_arch = models.Architecture.selectBy(name=filename_arch_str).getOne()

  parsed_basename = pkg_stats["basic_stats"]["parsed_basename"]
  os_rel_name = parsed_basename["osrel"]
  # os_rel_name can be completely wrong.
  try:
    os_rel = models.OsRelease.selectBy(short_name=os_rel_name).getOne()
  except sqlobject.main.SQLObjectNotFound:
    msg = ('%r is not a valid OS release name. Look into %s metadata. '
           'Probably a problem with the file name: %r'
           % (os_rel_name, md5_sum, pkg_stats["basic_stats"]["pkg_basename"]))
    logger.warning(msg)
    # This is probably a package with a file name like
    # 'mod_dav-1.0.3-sparc-CSW.pkg.gz'. We have to deal with it somehow,
    # so we'll assume it's a Solaris 8 package.
    os_rel = models.OsRelease.selectBy(short_name='SunOS5.8').getOne()

  maint_email = pkg_stats["pkginfo"]["EMAIL"]
  try:
    maintainer = models.Maintainer.selectBy(email=maint_email).getOne()
  except sqlobject.main.SQLObjectNotFound as exc:
    logger.debug(exc)
    # Try to get the maintainer name.
    maint_name = None
    vendor_str = pkg_stats["pkginfo"]["VENDOR"]
    maint_name_magic_str = 'packaged for CSW by '
    if maint_name_magic_str in vendor_str:
      maint_name = re.sub(r'^.*%s' % maint_name_magic_str, '', vendor_str)
    maintainer = models.Maintainer(email=maint_email, full_name=maint_name)

  rev=None
  if "revision_info" in parsed_basename:
    if "REV" in parsed_basename["revision_info"]:
      rev = parsed_basename["revision_info"]["REV"]

  # If the object already exists in the database, we'll replace all dependent data.
  db_pkg_stats = None
  try:
    db_pkg_stats = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    db_pkg_stats.DeleteAllDependentObjects()
  except sqlobject.main.SQLObjectNotFound:
    logger.debug('Package %s not present in the relational db, '
                 'proceeding with insert.', parsed_basename)

  register = True
  bundle = pkg_stats['pkginfo'].get("OPENCSW_BUNDLE", None)

  if db_pkg_stats:
    # If the database row exists already, update it.
    #
    # Assigning properties one by one isn't pretty, but I don't have
    # a better way of doing it.  Ideally, both creation and update would be
    # driven by the same data structure.
    db_pkg_stats.arch = arch
    db_pkg_stats.basename = pkg_stats["basic_stats"]["pkg_basename"]
    db_pkg_stats.catalogname = pkg_stats["basic_stats"]["catalogname"]
    db_pkg_stats.use_to_generate_catalogs = use_in_catalogs
    db_pkg_stats.filename_arch = filename_arch
    db_pkg_stats.maintainer = maintainer
    db_pkg_stats.md5_sum = pkg_stats["basic_stats"]["md5_sum"]
    db_pkg_stats.size = pkg_stats["basic_stats"]["size"]
    db_pkg_stats.mtime = dateutil.parser.parse(pkg_stats["mtime"])
    db_pkg_stats.os_rel = os_rel
    db_pkg_stats.osrel_str = os_rel.short_name
    db_pkg_stats.pkginst = pkginst
    db_pkg_stats.pkginst_str = pkginst.pkgname
    db_pkg_stats.registered_level_one = register
    db_pkg_stats.registered_level_two = False
    db_pkg_stats.rev = rev
    db_pkg_stats.stats_version = PACKAGE_STATS_VERSION
    db_pkg_stats.version_string = parsed_basename["full_version_string"]
    db_pkg_stats.bundle = bundle
  else:
    db_pkg_stats = models.Srv4FileStats(
        arch=arch,
        basename=pkg_stats["basic_stats"]["pkg_basename"],
        catalogname=pkg_stats["basic_stats"]["catalogname"],
        use_to_generate_catalogs=use_in_catalogs,
        filename_arch=filename_arch,
        maintainer=maintainer,
        md5_sum=md5_sum,
        size=pkg_stats["basic_stats"]["size"],
        mtime=dateutil.parser.parse(pkg_stats["mtime"]),
        os_rel=os_rel,
        osrel_str=os_rel.short_name,
        pkginst=pkginst,
        pkginst_str=pkginst.pkgname,
        registered_level_one=register,
        registered_level_two=False,
        rev=rev,
        stats_version=PACKAGE_STATS_VERSION,
        version_string=parsed_basename["full_version_string"],
        bundle=bundle)
  # Inserting overrides as rows into the database
  for override_dict in pkg_stats["overrides"]:
    models.CheckpkgOverride(srv4_file=db_pkg_stats,
                           **override_dict)

  db_pkg_stats.registered_level_one = True
  return db_pkg_stats, pkg_stats


def StatsStructToDatabaseLevelTwo(md5_sum, use_in_catalogs):
  db_pkg_stats, pkg_stats = StatsStructToDatabaseLevelOne(
      md5_sum, use_in_catalogs=use_in_catalogs)
  # Let's be lazy.
  if db_pkg_stats.registered_level_two:
    return db_pkg_stats, pkg_stats
  pkginst = db_pkg_stats.pkginst
  # Adding the catalog generation info.
  try:
    models.CatalogGenData.selectBy(md5_sum=md5_sum).getOne().destroySelf()
  except sqlobject.SQLObjectNotFound:
    pass
  finally:
    catalog_gen_data = models.CatalogGenData(
        md5_sum=pkg_stats["basic_stats"]["md5_sum"],
        deps=cjson.encode(pkg_stats["depends"]),
        pkgname=pkg_stats["basic_stats"]["pkgname"],
        i_deps=cjson.encode(pkg_stats["i_depends"]),
        pkginfo_name=pkg_stats["pkginfo"]["NAME"])

  files_metadata = [
      representations.FileMetadata._make(x)
      for x in pkg_stats["files_metadata"]]
  mimetype_by_path = dict(
      (os.path.join("/", x.path), x.mime_type)
      for x in files_metadata)
  machine_by_path = dict((x.path, x.mime_type) for x in files_metadata)
  for pkgmap_tuple in pkg_stats["pkgmap"]:
    pkgmap_entry = representations.PkgmapEntry._make(pkgmap_tuple)
    if not pkgmap_entry.path:
      continue
    try:
      # The line might be not decodable using utf-8
      line_u = pkgmap_entry.line.decode("utf-8")
      f_path, basename = os.path.split(
          pkgmap_entry.path.decode('utf-8'))
    except UnicodeDecodeError as e:
      line_u = pkgmap_entry.line.decode("latin1")
      f_path, basename = os.path.split(
          pkgmap_entry.path.decode('latin1'))
    except UnicodeEncodeError as e:
      # the line was already in unicode
      line_u = pkgmap_entry.line
      f_path, basename = os.path.split(pkgmap_entry.path)
      # If this fails too, code change will be needed.

    mimetype = None
    if pkgmap_entry.path in mimetype_by_path:
      mimetype = mimetype_by_path[pkgmap_entry.path]
    machine = None
    if pkgmap_entry.path in machine_by_path:
      machine = machine_by_path[pkgmap_entry.path]
    # Creating a file entry.
    models.CswFile(basename=basename,
                   path=f_path,
                   line=line_u,
                   pkginst=pkginst,
                   srv4_file=db_pkg_stats,
                   perm_user=pkgmap_entry.owner,
                   perm_group=pkgmap_entry.group,
                   perm_mode=pkgmap_entry.mode,
                   target=pkgmap_entry.target,
                   mimetype=mimetype,
                   machine=machine,
    )

  # Save dependencies in the database.  First remove any dependency rows that
  # might be in the database.
  # TODO(maciej): Unit test it
  deps_res = models.Srv4DependsOn.selectBy(srv4_file=db_pkg_stats)
  for dep_obj in deps_res:
    dep_obj.destroySelf()
  for dep_pkgname, unused_desc in pkg_stats["depends"]:
    dep_pkginst = GetOrSetPkginst(dep_pkgname)
    models.Srv4DependsOn(srv4_file=db_pkg_stats, pkginst=dep_pkginst)

  # Incompatible packages
  deps_res = models.Srv4IncompatibleWith.selectBy(srv4_file=db_pkg_stats)
  for dep_obj in deps_res:
    dep_obj.destroySelf()
  for dep_pkgname in pkg_stats["i_depends"]:
    dep_pkginst = GetOrSetPkginst(dep_pkgname)
    models.Srv4IncompatibleWith(srv4_file=db_pkg_stats, pkginst=dep_pkginst)

  # At this point, we've registered the srv4 file.
  # Setting the registered bit to True
  db_pkg_stats.registered_level_two = True
  return db_pkg_stats, pkg_stats
