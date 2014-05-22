#!/opt/csw/bin/python2.6

# A webpy application to allow HTTP access to the checkpkg database.

import sys
import os
# sys.path.append(os.path.join(os.path.split(__file__)[0], "..", ".."))

import cjson
import datetime
import json
import logging
import pprint
import sqlobject
import time
import re
import web

from sqlobject import sqlbuilder

# sys.stderr.write("Running Python binary from {}.\n".format(sys.executable))
# sys.stderr.write("Python path is {}.\n".format(sys.path))

from lib.python import checkpkg_lib
from lib.python import configuration
from lib.python import models
from lib.python import representations
from lib.web import web_lib


config = configuration.GetConfig()
LOG_FILE_TMPL = config.get("pkgdb_app", "log_file")

urls_html = (
  r'/', 'index',
  r'/favicon\.ico', 'Favicon',
  r'/srv4/', 'Srv4List',
  r'/srv4/([0-9a-f]{32})/', 'Srv4Detail',
  r'/srv4/([0-9a-f]{32})/files/', 'Srv4DetailFiles',
  r'/srv4/([0-9a-f]{32})/struct-dump/', 'Srv4StructDump',
  r'/elfdump/([0-9a-f]{32})/', 'Elfdump',
  r'/catalogs/', 'CatalogList',
  r'/catalogs/([\w-]+)-(sparc|i386)-(SunOS[^-]+)/', 'CatalogDetail',
  r'/maintainers/', 'MaintainerList',
  r'/maintainers/(\d+)/', 'MaintainerDetail',
  r'/maintainers/(\d+)/checkpkg/', 'MaintainerCheckpkgReport',
  r'/error-tags/', 'ErrorTagList',
  r'/error-tags/([^/]+)/', 'ErrorTagDetail',
  r'/catalognames/', 'CatalognameList',
  r'/catalognames/([^/]+)/', 'Catalogname',
  r'/form-redirect/', 'Redirection',
)
urls_rest = (
  r'/rest/svr4/recent/', 'RestSrv4List',
  r'/rest/catalogs/', 'RestCatalogList',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/', 'RestCatalogDetail',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgname-by-filename',
      'PkgnameByFilename',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgnames-and-paths-by-basename',
      'PkgnamesAndPathsByBasename',  # with ?basename=...
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgnames-and-paths-by-basedir',
      'PkgnamesAndPathsByBasedir',  # with ?basedir=...
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/for-generation/as-dicts/',
      'CatalogForGenerationAsDicts',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/for-generation/',
      'CatalogForGenerationAsDicts',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/timing/',
      'CatalogTiming',
  # Query by catalog release, arch, OS release and catalogname
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/catalognames/([^/]+)/',
      'Srv4ByCatAndCatalogname',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgnames/([^/]+)/',
      'Srv4ByCatAndPkgname',
  r'/rest/maintainers/', 'RestMaintainerList',
  r'/rest/maintainers/by-email/', 'RestMaintainerDetailByName', # with ?email=...
  r'/rest/maintainers/([0-9]+)/', 'RestMaintainerDetail',
  r'/rest/srv4/([0-9a-f]{32})/', 'RestSrv4Detail',
  r'/rest/srv4/([0-9a-f]{32})/files/', 'RestSrv4DetailFiles',
  r'/rest/srv4/([0-9a-f]{32})/pkg-stats/', 'RestSrv4FullStats',
  r'/rest/srv4/([0-9a-f]{32})/catalog-data/', 'RestSvr4CatalogData',
)
urls = urls_html + urls_rest

templatedir = os.path.join(os.path.dirname(__file__), "templates/")
render = web.template.render(templatedir)


def SanitizeDescription(catalogname, desc):
  prefix = '%s - ' % catalogname
  if desc.startswith(prefix):
    return desc[len(prefix):]
  return desc


def FormatPkginstList(lst):
  if lst:
    return '|'.join(lst)
  else:
    return 'none'


class index(object):

  def GET(self):
    return render.index()


class Favicon(object):

  def GET(self):
    return ""


class Srv4List(object):
  def GET(self):
    pkgs = models.Srv4FileStats.select().orderBy('-mtime')[:30]
    now = datetime.datetime.now()
    def Ago(timedelta):
      # Not sure why there is a time difference between mysql and the datetime
      # module.
      timezone_diff = 1.0
      return "%.1fh" % (timedelta.seconds / 60.0 / 60.0 - timezone_diff)
    pkgs_ago = [(x, Ago(now - x.mtime)) for x in pkgs]
    return render.Srv4List(pkgs_ago)


class Srv4Detail(object):
  def GET(self, md5_sum):
    try:
      pkg = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    overrides = pkg.GetOverridesResult()
    tags_by_cat = {}
    tags_and_catalogs = []
    osrels = models.OsRelease.select()
    catrels = models.CatalogRelease.select()
    all_tags = list(models.CheckpkgErrorTag.selectBy(srv4_file=pkg))
    pkg_stats_sqo = models.Srv4FileStatsBlob.selectBy(md5_sum=md5_sum).getOne()
    pkg_stats = cjson.decode(pkg_stats_sqo.json)
    pkg_stats_raw = pprint.pformat(pkg_stats, width=200)
    if pkg.arch.name == 'all':
      archs = models.Architecture.select(models.Architecture.q.name!='all')
    else:
      archs = [pkg.arch]

    pkgmap = []
    for pkgmap_entry in pkg_stats['pkgmap']:
      pkgmap_entry = representations.PkgmapEntry._make(pkgmap_entry)
      pkgmap.append(pkgmap_entry.line)

    for catrel in catrels:
      for arch in archs:
        for osrel in osrels:
          tags = pkg.GetErrorTagsResult(osrel, arch, catrel)
          key = (osrel, arch, catrel)
          tags = list(tags)
          tags_by_cat[key] = tags
          tags_and_catalogs.append((osrel, arch, catrel, tags))
    binary_md5_sums = pkg_stats['binary_md5_sums']
    return render.Srv4Detail(pkg, overrides, tags_by_cat, all_tags,
        tags_and_catalogs, pkg_stats_raw, pkgmap, binary_md5_sums)


class Srv4StructDump(object):

  def GET(self, md5_sum):
    try:
      blob = models.Srv4FileStatsBlob.selectBy(md5_sum=md5_sum).getOne()
      struct = cjson.decode(blob.json)
      basename = struct['basic_stats']['pkg_basename']
      struct_dump = pprint.pformat(struct, width=200)
      return render.Srv4StructDump(basename, struct_dump)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()


class Elfdump(object):

  def GET(self, md5_sum):
    try:
      blob = models.ElfdumpInfoBlob.selectBy(md5_sum=md5_sum).getOne()
      struct = cjson.decode(blob.json)
      struct_dump = pprint.pformat(struct, width=200)
      return render.ElfdumpInfoBlob(md5_sum, struct_dump)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()


class Catalogname(object):

  def GET(self, catalogname):
    try:
      pkgs = models.Srv4FileStats.selectBy(
          catalogname=catalogname,
          registered_level_two=True).orderBy('mtime')
      return render.Catalogname(catalogname, pkgs)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()


class CatalognameList(object):

  def GET(self):
    try:
      connection = models.Srv4FileStats._connection
      rows = connection.queryAll(connection.sqlrepr(
        sqlbuilder.Select(
          [models.Srv4FileStats.q.catalogname],
          distinct=True,
          where=sqlobject.AND(
            models.Srv4FileStats.q.use_to_generate_catalogs==True,
            models.Srv4FileStats.q.registered_level_two==True),
          orderBy=models.Srv4FileStats.q.catalogname)))
      rows_by_letter = {}
      for row in rows:
        initial = row[0][0]
        rows_by_letter.setdefault(initial, [])
        rows_by_letter[initial].append(row)
      return render.CatalognameList(rows_by_letter, sorted(rows_by_letter))
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()


class Srv4DetailFiles(object):

  def GET(self, md5_sum):
    try:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound as e:
      raise web.notfound()
    files = models.CswFile.selectBy(srv4_file=srv4)
    return render.Srv4DetailFiles(srv4, files)


class CatalogList(object):

  def GET(self):
    """Return a list of catalogs.

    Make it table:

               5.8        5.9        5.10       5.11
    beanie     i386 sparc i386 sparc i386 sparc i386 sparc
    dublin     i386 sparc i386 sparc i386 sparc i386 sparc
    kiel       i386 sparc i386 sparc i386 sparc i386 sparc
    legacy     i386 sparc i386 sparc i386 sparc i386 sparc
    """
    archs = models.Architecture.select()
    osrels = models.OsRelease.select()
    catrels = models.CatalogRelease.select().orderBy('name')
    table = []
    for catrel in catrels:
      row = [catrel.name]
      for osrel in osrels:
        cell = []
        if osrel.full_name == 'unspecified': continue
        for arch in archs:
          if arch.name in ('all'): continue
          # tags = pkg.GetErrorTagsResult(osrel, arch, catrel)
          cell.append({
            'osrel': osrel,
            'arch': arch,
            'catrel': catrel
          })
          # tags_by_cat[key] = list(tags)
        row.append(cell)
      table.append(row)
    return render.CatalogList(table, osrels)


class CatalogDetail(object):

  def GET(self, catrel_name, arch_name, osrel_name):
    cat_name = " ".join((catrel_name, arch_name, osrel_name))
    try:
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    t2 = time.time()
    pkgs = list(models.GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel))
    t3 = time.time()
    timeinfo = "Query evaluation: %.2fs" % (t3-t2)
    return render.CatalogDetail(cat_name, pkgs, timeinfo, len(pkgs))


class MaintainerList(object):

  def GET(self):
    maintainers = models.Maintainer.select().orderBy('email')
    names = []
    for m in maintainers:
      email = m.email.split("@")
      # In case the email is not valid.
      if len(email) >= 2:
        names.append((email[0], email[1], m))
      else:
        names.append((email[0], "no domain", m))
    return render.MaintainerList(names)


class MaintainerDetail(object):

  def GET(self, id):
    maintainer = models.Maintainer.selectBy(id=id).getOne()
    pkgs = models.Srv4FileStats.select(
        sqlobject.AND(
          models.Srv4FileStats.q.maintainer==maintainer,
          models.Srv4FileStats.q.registered_level_two==True,
        ),
    ).orderBy('basename')
    return render.MaintainerDetail(maintainer, pkgs)


class RestMaintainerList(object):

  def GET(self):
    maintainers = models.Maintainer.select().orderBy('email')
    maintainers = [m.GetRestRepr() for m in maintainers]
    return cjson.encode(maintainers)


class RestMaintainerDetail(object):

  def GET(self, id):
    try:
      maintainer = models.Maintainer.selectBy(id=id).getOne()
      return cjson.encode(maintainer.GetRestRepr())
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()


class RestMaintainerDetailByName(object):

  def GET(self):
    user_data = web.input()
    email = user_data.email
    try:
      maintainer = models.Maintainer.selectBy(email=email).getOne()
      return cjson.encode(maintainer.GetRestRepr())
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()


class MaintainerCheckpkgReport(object):

  def GET(self, id):
    maintainer = models.Maintainer.selectBy(id=id).getOne()
    pkgs = models.Srv4FileStats.select(
        sqlobject.AND(
          models.Srv4FileStats.q.maintainer==maintainer,
          models.Srv4FileStats.q.registered_level_two==True,
        ),
    ).orderBy('basename')
    tags_by_md5 = {}
    pkgs = list(pkgs)
    for pkg in pkgs:
      tags = list(models.CheckpkgErrorTag.selectBy(srv4_file=pkg).orderBy(
        ('tag_name', 'tag_info')))
      tags_by_cat_id = {}
      for tag in tags:
        key = (tag.catrel.name, tag.arch.name, tag.os_rel.short_name)
        tags_by_cat_id.setdefault(key, []).append(tag)
      tags_by_md5.setdefault(pkg.md5_sum, tags_by_cat_id)
    return render.MaintainerCheckpkgReport(maintainer, pkgs, tags_by_md5)


class ErrorTagDetail(object):

  def GET(self, tag_name):
    join = [
        sqlbuilder.INNERJOINOn(None,
          models.Srv4FileStats,
          models.CheckpkgErrorTag.q.srv4_file==models.Srv4FileStats.q.id),
    ]
    tags = models.CheckpkgErrorTag.select(
        sqlobject.AND(
          models.CheckpkgErrorTag.q.tag_name==tag_name,
          models.Srv4FileStats.q.registered_level_two==True,
          models.Srv4FileStats.q.use_to_generate_catalogs==True,
          ),
        join=join,
    ).orderBy(('basename', 'tag_info', 'os_rel_id', 'arch_id', 'catrel_id'))
    return render.ErrorTagDetail(tag_name, tags)

class ErrorTagList(object):

  def GET(self):
    connection = models.CheckpkgErrorTag._connection
    rows = connection.queryAll(connection.sqlrepr(
      sqlbuilder.Select(
        [models.CheckpkgErrorTag.q.tag_name],
        distinct=True,
        orderBy=models.CheckpkgErrorTag.q.tag_name)))
    return render.ErrorTagList(rows)


class RestCatalogDetail(object):

  def GET(self, catrel_name, arch_name, osrel_name):
    try:
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    pkgs = list(models.GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel))
    if not len(pkgs):
      raise web.notfound()
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=srv4-list')
    # We never want to return complete data for every object (too slow).
    pkgs_data = [p.GetRestRepr(quick=True)[1] for p in pkgs]
    response = cjson.encode(pkgs_data)
    web.header('Content-Length', str(len(response)))
    return response


class PkgnameByFilename(object):

  def GET(self, catrel, arch, osrel):
    user_data = web.input()
    filename = user_data.filename
    send_filename = (
        '%s-%s-%s-%s-packages.txt'
        % (catrel, arch, osrel, filename.replace('/', '-')))
    db_catalog = checkpkg_lib.Catalog()
    try:
      pkgs = db_catalog.GetPkgByPath(filename, osrel, arch, catrel)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=pkgname-list')
    web.header('X-Rest-Info', 'I could tell you about the format, but I won\'t')
    web.header('Content-Disposition',
               'attachment; filename=%s' % send_filename)
    return cjson.encode(sorted(pkgs))


class PkgnamesAndPathsByBasename(object):

  def GET(self, catrel, arch, osrel):
    user_data = web.input()
    try:
      basename = user_data.basename
    except AttributeError, e:
      raise web.badrequest()
    send_filename = (
        '%s-%s-%s-%s-packages.txt'
        % (catrel, arch, osrel, basename.replace('/', '-')))
    db_catalog = checkpkg_lib.Catalog()
    try:
      data = db_catalog.GetPathsAndPkgnamesByBasename(
          basename, osrel, arch, catrel)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=pkgname-list')
    web.header('Content-Disposition',
               'attachment; filename=%s' % send_filename)
    response = cjson.encode(data)
    web.header('Content-Length', str(len(response)))
    return response


class PkgnamesAndPathsByBasedir(object):

  def GET(self, catrel, arch, osrel):
    user_data = web.input()
    try:
      basedir = user_data.basedir
    except AttributeError:
      raise web.badrequest()
    send_filename = (
        '%s-%s-%s-%s-packages.txt'
        % (catrel, arch, osrel, basedir.replace('/', '-')))
    db_catalog = checkpkg_lib.Catalog()
    try:
      data = db_catalog.GetPathsAndPkgnamesByBasedir(
          basedir, osrel, arch, catrel)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=pkgname-list')
    web.header('Content-Disposition',
               'attachment; filename=%s' % send_filename)
    response = cjson.encode(data)
    web.header('Content-Length', str(len(response)))
    return response


class RestSrv4Detail(object):

  def GET(self, md5_sum):
    try:
      pkg = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    mimetype, data_structure = pkg.GetRestRepr()
    web.header('Content-type', mimetype)
    web.header('Access-Control-Allow-Origin', '*')
    return cjson.encode(data_structure)


class RestSrv4DetailFiles(object):

  def GET(self, md5_sum):
    try:
      pkg = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    files = models.CswFile.selectBy(srv4_file=pkg)
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=file-list')
    web.header('Access-Control-Allow-Origin', '*')
    def FileDict(file_obj):
      return {
          "basename": file_obj.basename,
          "path": file_obj.path,
          "line": file_obj.line,
      }
    serializable_files = [FileDict(x) for x in files]
    return cjson.encode(serializable_files)


class RestSrv4FullStats(object):

  def GET(self, md5_sum):
    try:
      blob = models.Srv4FileStatsBlob.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=pkg-stats')
    return blob.json


class Srv4ByCatAndCatalogname(object):

  def GET(self, catrel_name, arch_name, osrel_name, catalogname):
    """Get a srv4 reference by catalog ane catalogname."""
    web.header('Access-Control-Allow-Origin', '*')
    try:
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound(
          cjson.encode({'message': 'catalog %s %s %s not found'
                                   % (osrel_name, arch_name, catrel_name)}))
    join = [
        sqlbuilder.INNERJOINOn(None,
          models.Srv4FileInCatalog,
          models.Srv4FileInCatalog.q.srv4file==models.Srv4FileStats.q.id),
    ]
    res = models.Srv4FileStats.select(
        sqlobject.AND(
          models.Srv4FileInCatalog.q.osrel==sqo_osrel,
          models.Srv4FileInCatalog.q.arch==sqo_arch,
          models.Srv4FileInCatalog.q.catrel==sqo_catrel,
          models.Srv4FileStats.q.catalogname==catalogname,
          models.Srv4FileStats.q.use_to_generate_catalogs==True),
        join=join,
    )
    try:
      srv4 = res.getOne()
      mimetype, data = srv4.GetRestRepr(quick=True)
      web.header('Content-type', mimetype)
      return cjson.encode(data)
    except sqlobject.main.SQLObjectNotFound:
      data = {'message': 'no %s %s %s %s packages found'
              % (catrel_name, arch_name, osrel_name, catalogname)}
      raise web.notfound(cjson.encode(data))
    except sqlobject.dberrors.OperationalError as exc:
      raise web.internalerror(exc)


class Srv4ByCatAndPkgname(object):

  def GET(self, catrel_name, arch_name, osrel_name, pkgname):
    """Get a srv4 reference by catalog ane pkgname."""
    try:
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    join = [
        sqlbuilder.INNERJOINOn(None,
          models.Srv4FileInCatalog,
          models.Srv4FileInCatalog.q.srv4file==models.Srv4FileStats.q.id),
        sqlbuilder.INNERJOINOn(None,
          models.Pkginst,
          models.Pkginst.q.id==models.Srv4FileStats.q.pkginst),
    ]
    res = models.Srv4FileStats.select(
        sqlobject.AND(
          models.Srv4FileInCatalog.q.osrel==sqo_osrel,
          models.Srv4FileInCatalog.q.arch==sqo_arch,
          models.Srv4FileInCatalog.q.catrel==sqo_catrel,
          models.Pkginst.q.pkgname==pkgname,
          models.Srv4FileStats.q.use_to_generate_catalogs==True),
        join=join,
    )
    try:
      srv4 = res.getOne()
      mimetype, data = srv4.GetRestRepr()
      web.header('Content-type', mimetype)
      web.header('Access-Control-Allow-Origin', '*')
      return cjson.encode(data)
    except sqlobject.main.SQLObjectNotFound:
      return cjson.encode(None)
    except sqlobject.dberrors.OperationalError, e:
      raise web.internalerror(e)


class RestSrv4List(object):

  def GET(self):
    pkgs = models.Srv4FileStats.select().orderBy('-mtime')[:30]
    now = datetime.datetime.now()
    def Ago(timedelta):
      # Not sure why there is a time difference between mysql and the datetime
      # module.
      timezone_diff = 1.0
      return "%.1fh" % (timedelta.seconds / 60.0 / 60.0 - timezone_diff)
    pkgs_ago = [(x, Ago(now - x.mtime)) for x in pkgs]
    def PrepareForJson(pkg_ago):
      pkg, ago = pkg_ago
      _, pkg_dict = pkg.GetRestRepr(quick=True)
      pkg_dict['ago'] = ago
      pkg_dict['maintainer'] = pkg.maintainer.GetRestRepr()
      return pkg_dict
    response = cjson.encode([PrepareForJson(x) for x in pkgs_ago])
    web.header('Content-Length', str(len(response)))
    return response


class Redirection(object):
  """A helper URL to redirect POST forms into GET urls."""

  def GET(self):
    user_data = web.input(redirection_type='', md5_sum='')
    if user_data['redirection_type'] == 'svr4_struct_dump':
      raise web.seeother('../srv4/%s/struct-dump/' % user_data['md5_sum'])
    raise web.badrequest('Could not handle your redirection request (%r).'
                         % user_data['redirection_type'])


class RestCatalogList(object):

  def GET(self):
    archs = models.Architecture.select()
    osrels = models.OsRelease.select()
    catrels = models.CatalogRelease.select()
    catalogs = []
    for catrel in catrels:
      for arch in archs:
        if arch.name in ('all'): continue
        for osrel in osrels:
          if osrel.full_name == 'unspecified': continue
          key = [osrel.short_name, arch.name, catrel.name]
          catalogs.append(key)
    return cjson.encode(catalogs)


class RestSvr4CatalogData(object):

  def GET(self, md5_sum):
    try:
      cat_gen_data = models.CatalogGenData.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound("RestSvr4CatalogData for %r not found" % md5_sum)
    simple_data = {
        'deps': cjson.decode(cat_gen_data.deps),
        'i_deps': cjson.decode(cat_gen_data.i_deps),
        'pkginfo_name': cat_gen_data.pkginfo_name,
        'pkgname': cat_gen_data.pkgname,
    }
    response = cjson.encode(simple_data)
    web.header('Content-Length', str(len(response)))
    return response


def GetCatalogEntries(catrel_name, arch_name, osrel_name):
  """Returns a list of CatalogEntry tuples."""
  try:
    sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
  except sqlobject.main.SQLObjectNotFound:
    raise web.notfound()
  rows = list(models.GetCatalogGenerationResult(sqo_osrel, sqo_arch, sqo_catrel))
  def MakeCatalogEntry(row):
    catalogname = row[0]
    desc = SanitizeDescription(catalogname, row[8])
    i_deps = cjson.decode(row[7])
    i_deps_str = FormatPkginstList(i_deps)
    deps_with_desc = cjson.decode(row[6])
    deps = [x[0] for x in deps_with_desc if x[0].startswith('CSW')]
    deps_str = FormatPkginstList(deps)
    entry = representations.CatalogEntry(
        catalogname=row[0],  # 0
        version=row[1],      # 1
        pkgname=row[2],      # 2
        basename=row[3],     # 3
        md5_sum=row[4],      # 4
        size=row[5],         # 5 # This needs to be an int in JSON
        deps=deps_str,       # 6
        category="none",     # 7
        i_deps=i_deps_str,   # 8
        desc=desc,           # 9
    )
    return entry
  entries_list = [MakeCatalogEntry(row) for row in rows]
  return entries_list


class CatalogForGenerationAsDicts(object):

  def GET(self, catrel_name, arch_name, osrel_name):
    """A list of tuples, aligning with the catalog format.

    catalogname version_string pkgname
    basename md5_sum size deps category i_deps
    """
    entries_list = GetCatalogEntries(catrel_name, arch_name, osrel_name)
    response_list = []
    for entry in entries_list:
      response_list.append(entry._asdict())
    response = cjson.encode(response_list)
    web.header('Content-Length', str(len(response)))
    return response


class CatalogTiming(object):

  def GET(self, catrel_name, arch_name, osrel_name):
    """A list of tuples, aligning with the catalog format.

    catalogname version_string pkgname
    basename md5_sum size deps category i_deps
    """
    try:
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    rows = list(models.GetCatalogGenerationResult(sqo_osrel, sqo_arch, sqo_catrel))
    # Change this to return a list of dicts
    def MakeCatalogTimingEntry(row):
      catalogname = row[0]
      desc = SanitizeDescription(catalogname, row[8])
      i_deps = tuple(cjson.decode(row[7]))
      deps_with_desc = cjson.decode(row[6])
      deps = tuple(x[0] for x in deps_with_desc if x[0].startswith('CSW'))
      entry = representations.CatalogTimingEntry(
        catalogname=catalogname,  # 0
        version=row[1],      # 1
        pkgname=row[2],      # 2
        basename=row[3],     # 3
        md5_sum=row[4],      # 4
        size=row[5],         # 5 # This needs to be an int in JSON
        deps=deps,           # 6
        category="none",     # 7
        i_deps=i_deps,       # 8
        desc=desc,           # 9
        maintainer=row[9],
        mtime=row[10].isoformat(),
        inserted_on=row[11].isoformat(),
        inserted_by=row[12],
      )
      return entry
    rows = [MakeCatalogTimingEntry(x)._asdict() for x in rows]
    response = cjson.encode(rows)
    web.header('Content-Length', str(len(response)))
    return response


debugme = False
if debugme:
  web.webapi.internalerror = web.debugerror

app = web.application(urls, globals())

applogger = logging.getLogger('pkgdb')
applogger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler(filename=LOG_FILE_TMPL)
log_handler.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(
    '%(process)d %(levelname)s %(asctime)s '
    '%(filename)s:%(lineno)d %(funcName)s: %(message)s')
log_handler.setFormatter(log_formatter)
applogger.addHandler(log_handler)


def app_wrapper(app):
  applogger.debug('Connecting to the database')
  web_lib.ConnectToDatabase()
  return app


if __name__ == '__main__':
  if debugme:
    logging.basicConfig(level=logging.DEBUG)
  app.run()
else:
  application = app_wrapper(app).wsgifunc()
  # application = app.wsgifunc()
  # from paste.exceptions.errormiddleware import ErrorMiddleware
  # application = ErrorMiddleware(application, debug=debugme)
