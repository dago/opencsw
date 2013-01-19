#!/opt/csw/bin/python2.6

# A webpy application to allow HTTP access to the checkpkg database.

import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", ".."))

import cjson
import json
import logging
import pprint
import sqlobject
import web

from lib.python import models
from lib.python import configuration
from lib.python import pkgdb
from lib.python import checkpkg_lib
import datetime
from sqlobject import sqlbuilder

connected_to_db = False

urls_html = (
  r'/', 'index',
  r'/srv4/', 'Srv4List',
  r'/srv4/([0-9a-f]{32})/', 'Srv4Detail',
  r'/srv4/([0-9a-f]{32})/files/', 'Srv4DetailFiles',
  r'/catalogs/', 'CatalogList',
  r'/catalogs/([\w-]+)-(sparc|i386)-(SunOS[^-]+)/', 'CatalogDetail',
  r'/maintainers/', 'MaintainerList',
  r'/maintainers/(\d+)/', 'MaintainerDetail',
  r'/maintainers/(\d+)/checkpkg/', 'MaintainerCheckpkgReport',
  r'/error-tags/', 'ErrorTagList',
  r'/error-tags/([^/]+)/', 'ErrorTagDetail',
  r'/catalognames/', 'CatalognameList',
  r'/catalognames/([^/]+)/', 'Catalogname',
)
urls_rest = (
  r'/rest/catalogs/', 'RestCatalogList',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/', 'Catalogs',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgname-by-filename',
      'PkgnameByFilename',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgnames-and-paths-by-basename',
      'PkgnamesAndPathsByBasename',
  # Query by catalog release, arch, OS release and catalogname
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/catalognames/([^/]+)/', 'Srv4ByCatAndCatalogname',
  r'/rest/catalogs/([^/]+)/(sparc|i386)/(SunOS[^/]+)/pkgnames/([^/]+)/', 'Srv4ByCatAndPkgname',
  r'/rest/maintainers/([0-9]+)/', 'RestMaintainerDetail',
  r'/rest/srv4/([0-9a-f]{32})/', 'RestSrv4Detail',
  r'/rest/srv4/([0-9a-f]{32})/files/', 'RestSrv4DetailFiles',
  r'/rest/srv4/([0-9a-f]{32})/pkg-stats/', 'RestSrv4FullStats',
)
urls = urls_html + urls_rest

templatedir = os.path.join(os.path.dirname(__file__), "templates/")
render = web.template.render(templatedir)


# TODO(maciej): Convert this extension to cjson.
class PkgStatsEncoder(json.JSONEncoder):
  """Maps frozensets to lists."""
  def default(self, obj):
    if isinstance(obj, frozenset):
      # Python 2.6 doesn't have the dictionary comprehension
      # return {x: None for x in obj}
      return list(obj)
    if isinstance(obj, datetime.datetime):
      return obj.isoformat()
    return json.JSONEncoder.default(self, obj)


def ConnectToDatabase():
  """Connect to the database only if necessary.

  One problem with this approach might be that if the connection is lost, the
  script will never try to reconnect (unless it's done by the ORM).
  """
  global connected_to_db
  if not connected_to_db:
    configuration.SetUpSqlobjectConnection()
    connected_to_db = True


class index(object):
  def GET(self):
    return render.index()


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
    pkgstats_raw = (
      "As of January 2013, the stats stored are so big that "
      "processing them can take several minutes before they "
      "can be served. Disabling until a proper solution "
      "is in place.")
    # pkgstats_raw = pprint.pformat(pkg.GetStatsStruct())
    if pkg.arch.name == 'all':
      archs = models.Architecture.select(models.Architecture.q.name!='all')
    else:
      archs = [pkg.arch]
    for catrel in catrels:
      for arch in archs:
        for osrel in osrels:
          tags = pkg.GetErrorTagsResult(osrel, arch, catrel)
          key = (osrel, arch, catrel)
          tags = list(tags)
          tags_by_cat[key] = tags
          tags_and_catalogs.append((osrel, arch, catrel, tags))
    return render.Srv4Detail(pkg, overrides, tags_by_cat, all_tags,
        tags_and_catalogs, pkgstats_raw)


class Catalogname(object):
  def GET(self, catalogname):
    try:
      pkgs = models.Srv4FileStats.selectBy(
          catalogname=catalogname,
          registered=True).orderBy('mtime')
      return render.Catalogname(catalogname, pkgs)
    except sqlobject.main.SQLObjectNotFound, e:
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
            models.Srv4FileStats.q.registered==True),
          orderBy=models.Srv4FileStats.q.catalogname)))
      return render.CatalognameList(rows)
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
    archs = models.Architecture.select()
    osrels = models.OsRelease.select()
    catrels = models.CatalogRelease.select()
    catalogs = []
    for catrel in catrels:
      for arch in archs:
        if arch.name in ('all'): continue
        for osrel in osrels:
          if osrel.full_name == 'unspecified': continue
          # tags = pkg.GetErrorTagsResult(osrel, arch, catrel)
          key = (osrel, arch, catrel)
          # tags_by_cat[key] = list(tags)
          catalogs.append(key)
    return render.CatalogList(catalogs)


class CatalogDetail(object):
  def GET(self, catrel_name, arch_name, osrel_name):
    cat_name = " ".join((catrel_name, arch_name, osrel_name))
    sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
    pkgs = models.GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel)
    return render.CatalogDetail(cat_name, pkgs)


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
          models.Srv4FileStats.q.registered==True,
        ),
    ).orderBy('basename')
    return render.MaintainerDetail(maintainer, pkgs)


class RestMaintainerDetail(object):
  def GET(self, id):
    maintainer = models.Maintainer.selectBy(id=id).getOne()
    return cjson.encode(maintainer.GetRestRepr())


class MaintainerCheckpkgReport(object):
  def GET(self, id):
    maintainer = models.Maintainer.selectBy(id=id).getOne()
    pkgs = models.Srv4FileStats.select(
        sqlobject.AND(
          models.Srv4FileStats.q.maintainer==maintainer,
          models.Srv4FileStats.q.registered==True,
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
          models.Srv4FileStats.q.registered==True,
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


class Catalogs(object):
  def GET(self, catrel_name, arch_name, osrel_name):
    sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
    pkgs = list(models.GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel))
    user_data = web.input(quick='')
    quick = (user_data.quick == "true")
    if not len(pkgs):
      raise web.notfound()
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=srv4-list')
    pkgs_data = [p.GetRestRepr(quick)[1] for p in pkgs]
    return cjson.encode(pkgs_data)


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
    except sqlobject.main.SQLObjectNotFound, e:
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
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=pkgname-list')
    web.header('Content-Disposition',
               'attachment; filename=%s' % send_filename)
    return cjson.encode(data)


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
      pkg = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    data_structure = pkg.GetStatsStruct()
    web.header('Content-type', 'application/x-vnd.opencsw.pkg;type=pkg-stats')
    return json.dumps(data_structure, cls=PkgStatsEncoder)


class Srv4ByCatAndCatalogname(object):

  def GET(self, catrel_name, arch_name, osrel_name, catalogname):
    """Get a srv4 reference by catalog ane catalogname."""
    configuration.SetUpSqlobjectConnection()
    try:
      sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
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
      mimetype, data = srv4.GetRestRepr()
      web.header('Content-type', mimetype)
      web.header('Access-Control-Allow-Origin', '*')
      return cjson.encode(data)
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    except sqlobject.dberrors.OperationalError, e:
      raise web.internalerror(e)


class Srv4ByCatAndPkgname(object):

  def GET(self, catrel_name, arch_name, osrel_name, pkgname):
    """Get a srv4 reference by catalog ane pkgname."""
    configuration.SetUpSqlobjectConnection()
    sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
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


web.webapi.internalerror = web.debugerror


def app_wrapper():
  ConnectToDatabase()
  app = web.application(urls, globals())
  logging.basicConfig(level=logging.DEBUG)
  return app.wsgifunc()

application = app_wrapper()


if __name__ == "__main__":
  app.run()
