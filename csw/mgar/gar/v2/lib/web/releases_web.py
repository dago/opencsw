#!/opt/csw/bin/python2.6

# A webpy application to allow HTTP access to the checkpkg database.

import web
import sqlobject
import json
from lib.python import models
from lib.python import configuration
from lib.python import pkgdb
from lib.python import checkpkg_lib
from lib.python import package_stats
import datetime
import os
import os.path
import hashlib

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

OPENCSW_ROOT = "/home/mirror/opencsw-future"
ALLPKGS_DIR = os.path.join(OPENCSW_ROOT, "allpkgs")

def ConnectToDatabase():
  configuration.SetUpSqlobjectConnection()


class Index(object):
  def GET(self):
    return "It works!\n"

class Srv4List(object):
  def POST(self):
    configuration.SetUpSqlobjectConnection()
    x = web.input(srv4_file={})
    # x['srv4_file'].filename
    # x['srv4_file'].value
    # x['srv4_file'].file.read()
    web.header(
        'Content-type',
        'application/x-vnd.opencsw.pkg;type=upload-results')
    hash = hashlib.md5()
    # hash.update(x['srv4_file'].file.read())
    hash.update(x['srv4_file'].value)
    data_md5_sum = hash.hexdigest()
    declared_md5_sum = x['md5_sum']
    basename = x['basename']
    save_attempt = False
    if declared_md5_sum == data_md5_sum:
      srv4 = models.Srv4FileStats.selectBy(md5_sum=data_md5_sum).getOne()
      if srv4.use_to_generate_catalogs:
        SaveToAllpkgs(basename, x['srv4_file'].value)
        save_attempt = True
    else:
      save_attempt = False
    response_data = {
        "received_md5": data_md5_sum,
        "declared_md5": declared_md5_sum,
        "save_attempt": save_attempt,
    }
    return json.dumps(response_data)


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
    return json.dumps(response_data)


class Srv4CatalogAssignment(object):
  def GET(self, catrel_name, arch_name, osrel_name):
    """See if that package is in that catalog."""
    configuration.SetUpSqlobjectConnection()
    sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
        osrel_name, arch_name, catrel_name)
    srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
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
    return json.dumps(response_data)

  def PUT(self, catrel_name, arch_name, osrel_name, md5_sum):
    """Adds package to a catalog.

    When pycurl calls this function, it often hangs, waiting.  A fix for that
    is to add the 'Content-Length' header.  However, it sometimes still gets
    stuck and I don't know why.
    """
    code_version = "0x02"
    configuration.SetUpSqlobjectConnection()
    if catrel_name != 'unstable':
      # Updates via web are allowed only for the unstable catalog.
      # We should return an error message instead.
      raise web.notfound()
    try:
      if arch_name == 'all':
        raise checkpkg_lib.CatalogDatabaseError("Cannot add to 'all' catalog.")
      srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      if not srv4.registered:
        # Package needs to be registered for releases
        stats = srv4.GetStatsStruct()
        # This can throw CatalogDatabaseError if the db user doesn't have
        # enough permissions.
        package_stats.PackageStats.ImportPkg(stats, True)
        srv4 = models.Srv4FileStats.selectBy(md5_sum=md5_sum).getOne()
      c = checkpkg_lib.Catalog()
      # See if there already is a package with that catalogname.
      sqo_osrel, sqo_arch, sqo_catrel = pkgdb.GetSqoTriad(
          osrel_name, arch_name, catrel_name)
      res = c.GetConflictingSrv4ByCatalognameResult(
          srv4, srv4.catalogname,
          sqo_osrel, sqo_arch, sqo_catrel)
      if res.count() == 1:
        # Removing old version of the package from the catalog
        for pkg_in_catalog in res:
          srv4_to_remove = pkg_in_catalog.srv4file
          c.RemoveSrv4(srv4_to_remove, osrel_name, arch_name, catrel_name)
      c.AddSrv4ToCatalog(srv4, osrel_name, arch_name, catrel_name)
      web.header(
          'Content-type',
          'application/x-vnd.opencsw.pkg;type=catalog-update')
      response = json.dumps([
        u"Added to catalog %s %s %s" % (catrel_name, arch_name, osrel_name),
        u"%s" % srv4.basename,
        u"code_version" + str(code_version),
      ])
      web.header('Content-Length', len(response))
      return response
    except (
        checkpkg_lib.CatalogDatabaseError,
        sqlobject.dberrors.OperationalError), e:
      web.header(
          'Content-type',
          'application/x-vnd.opencsw.pkg;type=error-message')
      response = json.dumps({
        "error_message": unicode(e),
        "code_version": code_version,
      })
      web.header('Content-Length', len(response))
      return response


def SaveToAllpkgs(basename, data):
  """Saves a file to allpkgs."""
  target_path = os.path.join(ALLPKGS_DIR, basename)
  fd = None
  try:
    fd = os.open(target_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0644)
    os.write(fd, data)
  except IOError, e:
    if fd:
      os.close(fd)


web.webapi.internalerror = web.debugerror

app = web.application(urls, globals(), autoreload=False)
main = app.wsgifunc()

if __name__ == "__main__":
  app.run()
