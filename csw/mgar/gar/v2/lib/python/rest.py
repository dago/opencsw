#!/usr/bin/env python2.6

import cjson
import gdbm
import logging
import urllib2

DEFAULT_URL = "http://buildfarm.opencsw.org"


class Error(Exception):
  """Generic error."""


class ArgumentError(Error):
  """Wrong arguments passed."""


class RestClient(object):

  PKGDB_APP = "/pkgdb/rest"

  def __init__(self, rest_url=DEFAULT_URL):
    self.rest_url = rest_url

  def GetPkgByMd5(self, md5_sum):
    url = self.rest_url + self.PKGDB_APP + "/srv4/%s/" % md5_sum
    logging.debug("GetPkgByMd5(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return cjson.decode(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      if e.code == 404:
        # Code 404 is fine, it means that the package with given md5 does not
        # exist.
        return None
      else:
        # Other HTTP errors are should be thrown.
        raise

  def GetPkgstatsByMd5(self, md5_sum):
    url = self.rest_url + self.PKGDB_APP + "/srv4/%s/pkg-stats/" % md5_sum
    logging.debug("GetPkgstatsByMd5(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return cjson.decode(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      if e.code == 404:
        # Code 404 is fine, it means that the package with given md5 does not
        # exist.
        return None
      else:
        # Other HTTP errors are should be thrown.
        raise

  def GetMaintainerByMd5(self, md5_sum):
    pkg = self.GetPkgByMd5(md5_sum)
    if not pkg:
      pkg = {"maintainer_email": "Unknown"}
    return {
        "maintainer_email": pkg["maintainer_email"],
    }

  def GetCatalog(self, catrel, arch, osrel):
    if not catrel:
      raise ArgumentError("Missing catalog release.")
    url = self.rest_url + self.PKGDB_APP + "/catalogs/%s/%s/%s/?quick=true" % (catrel, arch, osrel)
    logging.debug("GetCatalog(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return cjson.decode(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      return None

  def Srv4ByCatalogAndCatalogname(self, catrel, arch, osrel, catalogname):
    """Returns a srv4 data structure or None if not found."""
    url = self.rest_url + self.PKGDB_APP + (
        "/catalogs/%s/%s/%s/catalognames/%s/"
        % (catrel, arch, osrel, catalogname))
    logging.debug("Srv4ByCatalogAndCatalogname(): GET %s", url)
    # The server is no longer returning 404 when the package is absent.  If
    # a HTTP error code is returned, we're letting the application fail.
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)


class CachedPkgstats(object):
  """Class responsible for holding and caching package stats.

  Wraps RestClient and provides a caching layer.
  """

  def __init__(self, filename):
    self.filename = filename
    self.d = gdbm.open(filename, "c")
    self.rest_client = RestClient()
    self.local_cache = {}

  def GetPkgstats(self, md5):
    if md5 in self.local_cache:
      return self.local_cache[md5]
    elif str(md5) in self.d:
      return cjson.decode(self.d[md5])
    else:
      pkgstats = self.rest_client.GetPkgstatsByMd5(md5)
      self.d[md5] = cjson.encode(pkgstats)
      self.local_cache[md5] = pkgstats
      return pkgstats
