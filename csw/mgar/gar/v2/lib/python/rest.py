#!/usr/bin/env python2.6

import os
from StringIO import StringIO
import cjson
import gdbm
import logging
import urllib2
import pycurl

DEFAULT_URL = "http://buildfarm.opencsw.org"
RELEASES_APP = "/releases"

class Error(Exception):
  """Generic error."""


class ArgumentError(Error):
  """Wrong arguments passed."""


class RestCommunicationError(Error):
  """An error during REST request processing."""


class RestClient(object):

  PKGDB_APP = "/pkgdb/rest"

  def __init__(self, rest_url=DEFAULT_URL, username=None, password=None,
      debug=False):
    self.rest_url = rest_url
    self.username = username
    self.password = password
    self.debug = debug

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

  def GetCatalogList(self):
    url = self.rest_url + self.PKGDB_APP + "/catalogs/"
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetCatalog(self, catrel, arch, osrel):
    if not catrel:
      raise ArgumentError("Missing catalog release.")
    url = (
        self.rest_url
        + self.PKGDB_APP
        + "/catalogs/%s/%s/%s/?quick=true" % (catrel, arch, osrel))
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

  def Srv4ByCatalogAndPkgname(self, catrel, arch, osrel, pkgname):
    """Returns a srv4 data structure or None if not found."""
    url = self.rest_url + self.PKGDB_APP + (
        "/catalogs/%s/%s/%s/pkgnames/%s/"
        % (catrel, arch, osrel, pkgname))
    logging.debug("Srv4ByCatalogAndPkgname(): GET %s", url)
    # The server is no longer returning 404 when the package is absent.  If
    # a HTTP error code is returned, we're letting the application fail.
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def _SetAuth(self, c):
    """Set basic HTTP auth options on given Curl object."""
    if self.username:
      logging.debug("Using basic AUTH for user %s", self.username)
      c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
      c.setopt(pycurl.USERPWD, "%s:%s" % (self.username, self.password))
    else:
      logging.debug("User and password not set, not using HTTP AUTH")
    return c

  def RemoveSvr4FromCatalog(self, catrel, arch, osrel, md5_sum):
    url = (
        "%s%s/catalogs/%s/%s/%s/%s/"
        % (self.rest_url,
           RELEASES_APP,
           catrel, arch, osrel,
           md5_sum))
    logging.debug("DELETE @ URL: %s %s", type(url), url)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.setopt(pycurl.HTTPHEADER, ["Expect:"]) # Fixes the HTTP 417 error
    c = self._SetAuth(c)
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    logging.debug(
        "DELETE curl getinfo: %s %s %s",
        type(http_code),
        http_code,
        c.getinfo(pycurl.EFFECTIVE_URL))
    c.close()
    if not (http_code >= 200 and http_code <= 299):
      raise RestCommunicationError(
          "%s - HTTP code: %s, content: %s"
          % (url, http_code, d.getvalue()))

  def AddSvr4ToCatalog(self, catrel, arch, osrel, md5_sum):
    url = (
        "%s%s/catalogs/%s/%s/%s/%s/"
        % (self.rest_url,
           RELEASES_APP,
           catrel,
           arch,
           osrel,
           md5_sum))
    logging.debug("URL: %s %s", type(url), url)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    # Bogus data to upload
    s = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.PUT, 1)
    c.setopt(pycurl.UPLOAD, 1)
    c.setopt(pycurl.INFILESIZE_LARGE, s.len)
    c.setopt(pycurl.READFUNCTION, s.read)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.setopt(pycurl.HTTPHEADER, ["Expect:"]) # Fixes the HTTP 417 error
    c = self._SetAuth(c)
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    logging.debug(
        "curl getinfo: %s %s %s",
        type(http_code),
        http_code,
        c.getinfo(pycurl.EFFECTIVE_URL))
    c.close()
    # if self.debug:
    #   logging.debug("*** Headers")
    #   logging.debug(h.getvalue())
    #   logging.debug("*** Data")
    if http_code >= 400 and http_code <= 599:
      if not self.debug:
        # In debug mode, all headers are printed to screen, and we aren't
        # interested in the response body.
        logging.fatal("Response: %s %s", http_code, d.getvalue())
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))
    else:
      logging.debug("Response: %s %s", http_code, d.getvalue())
    return http_code


class CachedPkgstats(object):
  """Class responsible for holding and caching package stats.

  Wraps RestClient and provides a caching layer.
  """

  def __init__(self, filename):
    self.filename = filename
    self.d = gdbm.open("%s.db" % self.filename, "c")
    self.rest_client = RestClient()
    self.local_cache = {}
    self.deps = gdbm.open("%s-deps.db" % self.filename, "c")

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

  def GetDeps(self, md5):
    if str(md5) in self.deps:
      return cjson.decode(self.deps[md5])
    else:
      pkgstats = self.GetPkgstats(md5)
      data = {"deps": pkgstats["depends"],
              "pkgname": pkgstats["basic_stats"]["pkgname"]}
      self.deps[md5] = cjson.encode(data)
      return data

def GetUsernameAndPassword():
  username = os.environ["LOGNAME"]
  password = None
  authfile = os.path.join('/etc/opt/csw/releases/auth', username)
  try:
    with open(authfile, 'r') as af:
      password = af.read().strip()
  except IOError, e:
    logging.warning("Error reading %s: %s", authfile, e)
    password = getpass.getpass("{0}'s pkg release password> ".format(username))
  return username, password
