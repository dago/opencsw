#!/opt/csw/bin/python2.6

# A webpy application to allow HTTP access to the checkpkg database.

import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", ".."))

import base64
import web
import sqlobject
import cjson
from lib.python import models
from lib.python import configuration
from lib.python import checkpkg_lib
from lib.python import package_stats
from lib.python import opencsw
from lib.python import common_constants
import datetime
import hashlib
import logging


urls = (
  r'/', 'Index',
  r'/srv4/', 'Srv4List',
  r'/srv4/([0-9a-f]{32})/', 'Srv4Detail',
  # We only accept submissions into unstable.
  # /catalogs/unstable/sparc/SunOS5.9/<md5-sum>/
  r'/catalogs/([^/]+)/([^/]+)/([^/]+)/([0-9a-f]{32})/', 'Srv4CatalogAssignment',
)

# render = web.template.render('templates/')
render = web.template.render('/home/maciej/src/pkgdb_web/templates/')

OPENCSW_ROOT = "/home/mirror/opencsw-official"
ALLPKGS_DIR = os.path.join(OPENCSW_ROOT, "allpkgs")
CAN_UPLOAD_TO_CATALOGS = frozenset([
    "unstable",
    "kiel",
    "bratislava",
    "beanie",
])

def ConnectToDatabase():
  configuration.SetUpSqlobjectConnection()


class Index(object):
  def GET(self):
    return "It works!\n"

class Srv4List(object):
  def POST(self):
    messages = []
    configuration.SetUpSqlobjectConnection()
    x = web.input(srv4_file={})
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
          SaveToAllpkgs(basename, x['srv4_file'].value)
      except sqlobject.main.SQLObjectNotFound, e:
        messages.append("File %s not found in the db." % data_md5_sum)
    else:
      save_attempt = False
    messages.append({
        "received_md5": data_md5_sum,
        "declared_md5": declared_md5_sum,
        "save_attempt": save_attempt,
    })
    return cjson.encode(messages)


class Srv4Detail(object):
  def GET(self, md5_sum):
    """Allows to verify whether a given srv4 file exists."""
    configuration.SetUpSqlobjectConnection()
    srv4 = None
    try:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      raise web.notfound()
    # Verifying whether the package exists in allpkgs.
    basename_in_allpkgs = os.path.join(ALLPKGS_DIR, srv4.basename)
    if not os.path.exists(basename_in_allpkgs):
      raise web.notfound()
    # Verify the hash; the file might already exist with the same filename,
    # but different content.
    hash = hashlib.md5()
    with open(basename_in_allpkgs) as fd:
      hash.update(fd.read())
    if not md5_sum == hash.hexdigest():
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
    configuration.SetUpSqlobjectConnection()
    sqo_osrel, sqo_arch, sqo_catrel = models.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
    srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
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
    configuration.SetUpSqlobjectConnection()
    if catrel_name not in CAN_UPLOAD_TO_CATALOGS:
      # Updates via web are allowed only for the unstable catalog.
      # We should return an error message instead.
      raise web.forbidden('Not allowed to upload to %s' % catrel_name)
    try:
      if arch_name == 'all':
        raise checkpkg_lib.CatalogDatabaseError(
            "There is no 'all' catalog, cannot proceed.")
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      parsed_basename = opencsw.ParsePackageFileName(srv4.basename)
      if parsed_basename["vendortag"] != "CSW":
        raise checkpkg_lib.CatalogDatabaseError(
            "Package vendor tag is %s instead of CSW."
            % parsed_basename["vendortag"])
      if not srv4.registered:
        # Package needs to be registered for releases
        stats = srv4.GetStatsStruct()
        # This can throw CatalogDatabaseError if the db user doesn't have
        # enough permissions.
        package_stats.PackageStats.ImportPkg(stats, True)
        srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
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

      # Retrieving logged in user name from the HTTP environment.
      # This does not work on the buildfarm. :-(
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
        sqlobject.dberrors.OperationalError), e:
      web.header(
          'Content-type',
          'application/x-vnd.opencsw.pkg;type=error-message')
      response = cjson.encode({
        "error_message": unicode(e),
      })
      web.header('Content-Length', len(response))
      raise web.notacceptable(data=response)

  def DELETE(self, catrel_name, arch_name, osrel_name, md5_sum):
    configuration.SetUpSqlobjectConnection()
    try:
      if osrel_name not in common_constants.OS_RELS:
        self.ReturnError(
            "%s is not one of %s (OS releases)"
            % (osrel_name, common_constants.OS_RELS))
      if osrel_name in common_constants.OBSOLETE_OS_RELS and catrel_name == 'unstable':
        self.ReturnError(
            "package deletions from an obsolete OS release such as %s "
            "are not allowed" % osrel_name)
      srv4_to_remove = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      c = checkpkg_lib.Catalog()
      c.RemoveSrv4(srv4_to_remove, osrel_name, arch_name, catrel_name)
    except (
        sqlobject.main.SQLObjectNotFound,
        sqlobject.dberrors.OperationalError), e:
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


def SaveToAllpkgs(basename, data):
  """Saves a file to allpkgs."""
  target_path = os.path.join(ALLPKGS_DIR, basename)
  fd = None
  try:
    try:
      os.unlink(target_path)
    except OSError, e:
      # It's okay if we can't unlink the file
      pass
    fd = os.open(target_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0644)
    os.write(fd, data)
  except IOError, e:
    if fd:
      os.close(fd)


web.webapi.internalerror = web.debugerror

app = web.application(urls, globals())
# main = app.wsgifunc()
application = app.wsgifunc()
from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(application, debug=True)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  app.run()
