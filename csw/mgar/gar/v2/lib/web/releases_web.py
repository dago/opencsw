#!/opt/csw/bin/python2.6
# coding=utf-8

# A webpy application to allow HTTP access to the checkpkg database.

import sys
import os

import base64
import cjson
import datetime
import hashlib
import logging
import sqlobject
import tempfile
import web

from lib.python import checkpkg_lib
from lib.python import configuration
from lib.python import common_constants
from lib.python import errors
from lib.python import models
from lib.python import opencsw
from lib.python import relational_util
from lib.web import web_lib

from lib.web import web_lib

urls = (
  r'/', 'Index',
  r'/favicon\.ico', 'Favicon',
  r'/srv4/', 'Srv4List',
  r'/srv4/([0-9a-f]{32})/', 'Srv4Detail',
  # The 'relational' resource is a concept representing the state of the
  # package in the relational part of the database. Meanings:
  # PUT creates or updates relational entries
  # DELETE deletes them
  # GET returns some basic information (not too useful, maybe for checking)
  r'/svr4/([0-9a-f]{32})/db-level-1/', 'Srv4RelationalLevelOne',
  r'/svr4/([0-9a-f]{32})/db-level-2/', 'Srv4RelationalLevelTwo',
  r'/blob/([^/]+)/([0-9a-f]{32})/', 'JsonStorage',
  r'/catalogs/([^/]+)/([^/]+)/([^/]+)/([0-9a-f]{32})/', 'Srv4CatalogAssignment',
  r'/rpc/bulk-existing-svr4/', 'QueryExistingSvr4',
)

templatedir = os.path.join(os.path.dirname(__file__), "templates/")
render = web.template.render(templatedir)

config = configuration.GetConfig()
ALLPKGS_DIR = os.path.join(config.get("buildfarm", "opencsw_root"), "allpkgs")
CAN_UPLOAD_TO_CATALOGS = frozenset([
    "beanie",
    "bratislava",
    "dublin",
    "kiel",
    "unstable",
    "legacy",
])


class Index(object):

  def GET(self):
    return """<html><body>
    <p>OpenCSW RESTful interface of the package database.
    <a href=\"http://buildfarm.opencsw.org/pkgdb/\">Learn more</a>.
    </p></body></html>
    """


class Favicon(object):

  def GET(self):
    """To reduce the number of 404 messages in the logs."""
    return ""


class Srv4List(object):

  def POST(self):
    messages = []
    # The 'srv4_file={}' is necessary for the .filename attribute to work.
    # Reference: http://webpy.org/cookbook/fileupload
    x = web.input(srv4_file={})
    for field_name in ('srv4_file', 'md5_sum', 'basename'):
      if field_name not in x:
        raise web.badrequest('srv4_file not found')
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=upload-results')
    file_hash = hashlib.md5()
    # Don't read the whole file into memory at once, do it in small chunks.
    chunk_size = 2 * 1024 * 1024
    data = x['srv4_file'].file.read(chunk_size)
    while data:
      file_hash.update(data)
      data = x['srv4_file'].file.read(chunk_size)
    data_md5_sum = file_hash.hexdigest()
    declared_md5_sum = x['md5_sum']
    basename = x['basename']
    save_attempt = False
    if declared_md5_sum == data_md5_sum:
      save_attempt = True
      try:
        srv4 = models.Srv4FileStats.selectBy(md5_sum=data_md5_sum).getOne()
        if srv4.use_to_generate_catalogs:
          # FieldStorage by default unlinks the temporary local file as soon as
          # it's been opened. Therefore, we have to take care of writing data
          # to the target location in an atomic way.
          fd, tmp_filename = tempfile.mkstemp(dir=ALLPKGS_DIR)
          x['srv4_file'].file.seek(0)
          data = x['srv4_file'].file.read(chunk_size)
          while data:
            os.write(fd, data)
            data = x['srv4_file'].file.read(chunk_size)
          os.close(fd)
          target_path = os.path.join(ALLPKGS_DIR, basename)
          os.rename(tmp_filename, target_path)
          # Since mkstemp creates files with mode 0600 by default:
          os.chmod(target_path, 0644)
      except sqlobject.main.SQLObjectNotFound:
        messages.append("File %s not found in the db." % data_md5_sum)
    messages.append({
        "received_md5": data_md5_sum,
        "declared_md5": declared_md5_sum,
        "save_attempt": save_attempt,
    })
    return cjson.encode(messages)


class Srv4Detail(object):

  def GET(self, md5_sum):
    """Allows to verify whether a given srv4 file exists."""
    srv4 = None
    try:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound()
    # Verifying whether the package exists in allpkgs.
    basename_in_allpkgs = os.path.join(ALLPKGS_DIR, srv4.basename)
    if not os.path.exists(basename_in_allpkgs):
      raise web.notfound()
    # Verify the hash; the file might already exist with the same filename,
    # but different content.
    file_hash = hashlib.md5()
    # TODO: Do not read the whole file into memory at once.
    with open(basename_in_allpkgs) as fd:
      file_hash.update(fd.read())
    if md5_sum != file_hash.hexdigest():
      raise web.notfound()
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=srv4-details')
    send_filename = "srv4-exists-%s.txt" % md5_sum
    web.header('Content-Disposition',
               'attachment; filename=%s' % send_filename)
    response_data = {
        "md5_sum": srv4.md5_sum,
        "catalogname": srv4.catalogname,
        "basename": srv4.basename,
        "pkgname": srv4.pkginst.pkgname,
        "maintainer": unicode(srv4.maintainer),
        "arch": srv4.arch.name,
        "osrel": srv4.os_rel.short_name,
    }
    return cjson.encode(response_data)


class Srv4CatalogAssignment(object):

  def GET(self, catrel_name, arch_name, osrel_name):
    """See if that package is in that catalog."""
    sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
    try:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound as e:
      raise web.notfound("Object %s not found" % (md5_sum))
    logging.debug("Srv4CatalogAssignment::GET srv4: %s", srv4.basename)
    srv4_in_c = models.Srv4FileInCatalog.selectBy(
        osrel=sqo_osrel,
        arch=sqo_arch,
        catrel=sqo_catrel,
        srv4file=srv4)
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=srv4-catalog-assignment')
    response_data = {
        'srv': unicode(srv4),
    }
    return cjson.encode(response_data)

  def PUT(self, catrel_name, arch_name, osrel_name, md5_sum):
    """Adds package to a catalog.

    When pycurl calls this function, it often hangs, waiting.  A fix for that
    is to add the 'Content-Length' header.  However, it sometimes still gets
    stuck and I don't know why.
    """
    if catrel_name not in CAN_UPLOAD_TO_CATALOGS:
      # Updates via web are allowed only for the unstable catalog.
      # We should return an error message instead.
      # Sadly, we cannot return a response body due to webpy's API
      # limitation.
      raise web.forbidden()
    try:
      if arch_name == 'all':
        raise web.badrequest("There is no 'all' catalog, cannot proceed.")
      try:
        srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      except sqlobject.main.SQLObjectNotFound:
        try:
          srv4, _ = relational_util.StatsStructToDatabaseLevelOne(md5_sum)
        except errors.DataError as exc:
          logging.warning(exc)
          # TODO(maciej): Add the exception to the web.conflict() call.
          # webpy 0.37 apparently doesn't allow that.
          raise web.conflict()
      parsed_basename = opencsw.ParsePackageFileName(srv4.basename)
      if parsed_basename["vendortag"] not in ("CSW", "FAKE"):
        raise web.badrequest(
            "Package vendor tag is %s instead of CSW or FAKE."
            % parsed_basename["vendortag"])
      if not srv4.registered_level_two:
        relational_util.StatsStructToDatabaseLevelTwo(md5_sum, True)
        # Package needs to be registered for releases
        # This can throw CatalogDatabaseError if the db user doesn't have
        # enough permissions.
        # raise web.internalerror('Package not registered')
      c = checkpkg_lib.Catalog()
      sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
      # See if there already is a package with that catalogname.
      res = c.GetConflictingSrv4ByCatalognameResult(
          srv4, srv4.catalogname,
          sqo_osrel, sqo_arch, sqo_catrel)
      if res.count() == 1:
        # Removing old version of the package from the catalog
        for pkg_in_catalog in res:
          srv4_to_remove = pkg_in_catalog.srv4file
          c.RemoveSrv4(srv4_to_remove, osrel_name, arch_name, catrel_name)
      # See if there already is a package with that pkgname.
      res = c.GetConflictingSrv4ByPkgnameResult(
          srv4, srv4.pkginst.pkgname,
          sqo_osrel, sqo_arch, sqo_catrel)
      if res.count() == 1:
        # Removing old version of the package from the catalog
        for pkg_in_catalog in res:
          srv4_to_remove = pkg_in_catalog.srv4file
          c.RemoveSrv4(srv4_to_remove, osrel_name, arch_name, catrel_name)

      # This is set by basic HTTP auth.
      username = web.ctx.env.get('REMOTE_USER')

      c.AddSrv4ToCatalog(srv4, osrel_name, arch_name, catrel_name, who=username)
      web.header(
          'Content-type',
          'application/x-vnd.opencsw.pkg;type=catalog-update')
      response = cjson.encode([
        u"Added to catalog %s %s %s" % (catrel_name, arch_name, osrel_name),
        u"%s" % srv4.basename,
        u"%s" % srv4.md5_sum,
      ])
      web.header('Content-Length', len(response))
      return response
    except (
        checkpkg_lib.CatalogDatabaseError,
        sqlobject.dberrors.OperationalError) as exc:
      web.header(
          'Content-Type',
          'application/x-vnd.opencsw.pkg;type=error-message')
      response = cjson.encode({
        "error_message": unicode(exc),
      })
      web.header('Content-Length', str(len(response)))
      raise web.badrequest(response)

  def DELETE(self, catrel_name, arch_name, osrel_name, md5_sum):
    try:
      if osrel_name not in common_constants.OS_RELS:
        self.ReturnError(
            "%s is not one of %s (OS releases)"
            % (osrel_name, common_constants.OS_RELS))
      if (osrel_name in common_constants.OBSOLETE_OS_RELS
          and catrel_name == 'unstable'):
        self.ReturnError(
            "package deletions from an obsolete OS release such as %s "
            "are not allowed" % osrel_name)
      srv4_to_remove = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      c = checkpkg_lib.Catalog()
      c.RemoveSrv4(srv4_to_remove, osrel_name, arch_name, catrel_name)
      msg = ('Package %s / %s removed successfully'
             % (srv4_to_remove.basename, md5_sum))
      response = cjson.encode({'message': msg})
      web.header('Content-Length', len(response))
      return response

    except (
        sqlobject.main.SQLObjectNotFound,
        sqlobject.dberrors.OperationalError) as e:
      self.ReturnError("An error occurred: %s" % e)

  def ReturnError(self, message):
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=error-message')
    response = cjson.encode({
      "error_message": unicode(message),
    })
    web.header('Content-Length', len(response))
    raise web.notacceptable(data=response)


class JsonStorage(object):

  BLOB_CLASSES = {
      'pkgstats': models.Srv4FileStatsBlob,
      'elfdump': models.ElfdumpInfoBlob,
  }

  def GetBlobClass(self, tag):
    if tag not in self.BLOB_CLASSES:
      raise web.badrequest(cjson.encode(
        {'message': 'We do not store %r type objects.' % tag}))
    return self.BLOB_CLASSES[tag]


  def GetObject(self, blob_class, md5_sum):
    try:
      obj = blob_class.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound as e:
      raise web.notfound(cjson.encode(
        {'message': 'Object %s/%s not found.'
                    % (blob_class, md5_sum)}))
    return obj

  def GET(self, tag, md5_sum):
    BlobClass = self.GetBlobClass(tag)
    obj = self.GetObject(BlobClass, md5_sum)
    return obj.json

  def HEAD(self, tag, md5_sum):
    BlobClass = self.GetBlobClass(tag)
    c = BlobClass.selectBy(md5_sum=md5_sum).count()
    if c > 0:
      web.header('X-OpenCSW-Message', 'Data exists')
      return ''
    else:
      web.header('X-OpenCSW-Message', 'Data does not exist')
      raise web.notfound()

  def PUT(self, tag, md5_sum):
    BlobClass = self.GetBlobClass(tag)
    mime_type = 'application/json'
    # This sometimes fails with 'No space left' ‒ can be amended by
    # adding more swap, which in turn adds more space into the /tmp
    # directory. The issue is that /tmp resides (partly?) in the swap
    # area.
    x = web.input()
    if 'json_data' not in x:
      raise web.badrequest('Missing "json_data" in the request.')
    if 'md5_sum' not in x:
      raise web.badrequest('Missing "md5_sum" in the request.')
    if md5_sum != x['md5_sum']:
      raise web.badrequest('URL: %s, request: %s' % (md5_sum, x['md5_sum']))
    json_data = x['json_data']
    content_hash = hashlib.md5()
    content_hash.update(json_data)
    content_md5_sum = content_hash.hexdigest()
    try:
      obj = BlobClass(md5_sum=md5_sum, json=json_data, mime_type=mime_type,
                      content_md5_sum=content_md5_sum)
    except sqlobject.dberrors.DuplicateEntryError:
      # Saving/updating the new data (idempotence).
      #
      # This might throw a NotFound exception if the object was deleted
      # in the meantime. This kind of race condition is inherent to SQL,
      # so we'll let the exception propagate and fail the query.
      try:
        obj = self.GetObject(BlobClass, md5_sum)
        obj.mime_type = mime_type
        obj.content_md5_sum = content_md5_sum
        obj.json = json_data
        # sqlobject immediately saves the changes.
      except sqlobject.main.SQLObjectNotFound:
        raise web.internalerror('A race condition. Sorry, please retry.')
    return cjson.encode({'message': 'Save of %s successful.' % md5_sum})

  def DELETE(self, tag, md5_sum):
    BlobClass = self.GetBlobClass(tag)
    obj = self.GetObject(BlobClass, md5_sum)
    obj.destroySelf()
    return cjson.encode({'message': 'Delete successful.'})


class QueryExistingSvr4(object):
  """Bulk query the existence of stats of md5_sums.

  The same can be achieved by repeated calls to HEAD of the blob storage class,
  but this implementation is much faster.
  """

  def POST(self):
    form_data = web.input(query_data={})
    md5_sum_list = cjson.decode(form_data['query_data'])
    existing_stats = []
    missing_stats = []
    # Maybe there's a more effective way of doing this? For example, a single query?
    # But the list of md5 sums is usually long, e.g. 3k or 4k items.
    for md5 in md5_sum_list:
      stats_count = models.Srv4FileStatsBlob.selectBy(md5_sum=md5).count()
      if stats_count < 1:
        missing_stats.append(md5)
      else:
        existing_stats.append(md5)
    ret_payload = cjson.encode({
      'existing_stats': existing_stats,
      'missing_stats': missing_stats,
    })
    web.header('Content-Length', str(len(ret_payload)))
    return ret_payload


class Srv4RelationalLevelOne(object):
  """Registers the package: creates a set of relational database entries."""

  def PUT(self, md5_sum):
    try:
      relational_util.StatsStructToDatabaseLevelOne(md5_sum)
      response = cjson.encode({'message': 'Package registered to level 1'})
      web.header('Content-Length', str(len(response)))
      return response
    except errors.DataError as exc:
      raise web.notacceptable(exc)


class Srv4RelationalLevelTwo(object):
  """Registers the package: creates a set of relational database entries."""

  def PUT(self, md5_sum):
    url_data = web.input(use_in_catalogs='1')
    negative_values = (0, '0', 'False', 'false', 'No', 'no')
    use_in_catalogs = True
    if url_data['use_in_catalogs'] in negative_values:
      use_in_catalogs = False
    try:
      relational_util.StatsStructToDatabaseLevelTwo(
          md5_sum, use_in_catalogs=use_in_catalogs)
      response = cjson.encode({'message': 'Package registered to level 2'})
      web.header('Content-Length', str(len(response)))
      return response
    except errors.DataError as exc:
      raise web.notacceptable(exc)

  def HEAD(self, md5_sum):
    try:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound:
      raise web.notfound('Stats not in the database')
    if not srv4.registered_level_two:
      raise web.notfound('Stats in the db, but not registered')
    return ''

# web.webapi.internalerror = web.debugerror


app = web.application(urls, globals())

def app_wrapper(app):
  web_lib.ConnectToDatabase()
  logging.basicConfig(level=logging.DEBUG)
  return app.wsgifunc()


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  app.run()
else:
  application = app_wrapper(app)
  # application = app
  # from paste.exceptions.errormiddleware import ErrorMiddleware
  # application = ErrorMiddleware(application, debug=True)
