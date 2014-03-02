#!/usr/bin/env python2.6

from StringIO import StringIO
import anydbm
import cjson
import getpass
import httplib
import logging
import os
import pycurl
import re
import urllib
import urllib2
import httplib

# Reading or writing via HTTP can be flaky at times. Since all REST calls are
# idempotent, it's safe to repeat a failed query.
from lib.python import retry_decorator

from lib.python import configuration
from lib.python import errors
from lib.python import shell


DEFAULT_TRIES = 5
DEFAULT_RETRY_DELAY = 10


class ArgumentError(errors.Error):
  """Wrong arguments passed."""


class RestCommunicationError(errors.Error):
  """An error during REST request processing."""


class RestClient(object):

  def __init__(self, pkgdb_url, releases_url,
               username=None, password=None, debug=False):
    self.pkgdb_url = pkgdb_url
    self.releases_url = releases_url
    self.username = username
    self.password = password
    self.debug = debug

  def ValidateMd5(self, md5_sum):
    if not re.match(r'^[0-9a-f]{32}$', md5_sum):
      raise ArgumentError('Passed argument is not a valid md5 sum: %r' % md5_sum)

  @retry_decorator.Retry(tries=DEFAULT_TRIES, exceptions=(RestCommunicationError, httplib.BadStatusLine))
  def GetPkgByMd5(self, md5_sum):
    self.ValidateMd5(md5_sum)
    url = self.pkgdb_url + "/srv4/%s/" % md5_sum
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
    self.ValidateMd5(md5_sum)
    return self.GetBlob('pkgstats', md5_sum)

  @retry_decorator.Retry(tries=DEFAULT_TRIES, exceptions=(RestCommunicationError, httplib.BadStatusLine))
  def GetCatalogData(self, md5_sum):
    self.ValidateMd5(md5_sum)
    url = self.pkgdb_url + "/srv4/%s/catalog-data/" % md5_sum
    try:
      data = urllib2.urlopen(url).read()
      return cjson.decode(data)
    except urllib2.HTTPError as e:
      logging.warning("Could not fetch catalog data for %r: %r", url, e)
      raise

  def GetMaintainerByMd5(self, md5_sum):
    self.ValidateMd5(md5_sum)
    pkg = self.GetPkgByMd5(md5_sum)
    if not pkg:
      pkg = {"maintainer_email": "Unknown"}
    return {
        "maintainer_email": pkg["maintainer_email"],
    }

  def GetCatalogList(self):
    url = self.releases_url + "/catalogs/"
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetCatalog(self, catrel, arch, osrel):
    if not catrel:
      raise ArgumentError("Missing catalog release.")
    url = (
        self.pkgdb_url
        + "/catalogs/%s/%s/%s/?quick=true" % (catrel, arch, osrel))
    logging.debug("GetCatalog(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return cjson.decode(data)
    except urllib2.HTTPError as e:
      logging.warning("%s -- %s", url, e)
      return None

  def Srv4ByCatalogAndCatalogname(self, catrel, arch, osrel, catalogname):
    """Returns a srv4 data structure or None if not found."""
    url = self.pkgdb_url + (
        "/catalogs/%s/%s/%s/catalognames/%s/"
        % (catrel, arch, osrel, catalogname))
    logging.debug("Srv4ByCatalogAndCatalogname(): GET %s", url)
    # The server is no longer returning 404 when the package is absent.  If
    # a HTTP error code is returned, we're letting the application fail.
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def Srv4ByCatalogAndPkgname(self, catrel, arch, osrel, pkgname):
    """Returns a srv4 data structure or None if not found."""
    url = self.pkgdb_url + (
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
      c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
      c.setopt(pycurl.USERPWD, "%s:%s" % (self.username, self.password))
    else:
      logging.debug("User and password not set, not using HTTP AUTH")
    return c

  def RemoveSvr4FromCatalog(self, catrel, arch, osrel, md5_sum):
    url = (
        "%s/catalogs/%s/%s/%s/%s/"
        % (self.releases_url, catrel, arch, osrel, md5_sum))
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

  def _CurlPut(self, url, data):
    """Makes a PUT request, potentially uploading data.

    Some pieces of information left from a few debugging sessions:

    The UPLOAD option must not be set or upload will not work.
    c.setopt(pycurl.UPLOAD, 1)

    This would disable the chunked encoding, but the problem only appears
    when the UPLOAD option is set.
    c.setopt(pycurl.HTTPHEADER, ["Transfer-encoding:"])
    """
    for key, value in data:
      assert isinstance(value, basestring), (value, type(value))
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.CUSTOMREQUEST, "PUT")
    if data:
      c.setopt(pycurl.POST, 1)
      c.setopt(pycurl.HTTPPOST, data)
    else:
      # This setting would make the client hang indefinitely.
      # c.setopt(pycurl.PUT, 1)
      pass
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    # The empty Expect: header fixes the HTTP 417 error on the buildfarm,
    # related to the use of squid as a proxy (squid only supports HTML/1.0).
    c.setopt(pycurl.HTTPHEADER, ["Expect:"])
    c = self._SetAuth(c)
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    logging.debug(
        "curl getinfo: %s %s",
        http_code,
        c.getinfo(pycurl.EFFECTIVE_URL))
    c.close()
    if http_code >= 400 and http_code <= 599:
      if not self.debug:
        # In debug mode, all headers are printed to screen, and we aren't
        # interested in the response body.
        logging.fatal("Response: %s %s", http_code, d.getvalue())
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))
    else:
      logging.debug("Response: %s %s", http_code, d.getvalue())
    return http_code

  @retry_decorator.Retry(tries=DEFAULT_TRIES, delay=DEFAULT_RETRY_DELAY,
                         exceptions=(RestCommunicationError, pycurl.error))
  def AddSvr4ToCatalog(self, catrel, arch, osrel, md5_sum):
    self.ValidateMd5(md5_sum)
    url = (
        "%s/catalogs/%s/%s/%s/%s/"
        % (self.releases_url, catrel, arch, osrel, md5_sum))
    logging.debug("AddSvr4ToCatalog: %s", url)
    return self._CurlPut(url, [])

  @retry_decorator.Retry(tries=DEFAULT_TRIES, delay=DEFAULT_RETRY_DELAY,
                         exceptions=(RestCommunicationError, pycurl.error))
  def SaveBlob(self, tag, md5_sum, data):
    url = self.releases_url + "/blob/%s/%s/" % (tag, md5_sum)
    logging.debug("SaveBlob(%s, %s): url=%r", tag, md5_sum, url)
    json_data = cjson.encode(data)
    logging.debug("JSON data size: %.1fKB", len(json_data) / 1024)
    return self._CurlPut(url, [
      ('json_data', json_data),
      ('md5_sum', md5_sum),
    ])

  @retry_decorator.Retry(tries=DEFAULT_TRIES, delay=DEFAULT_RETRY_DELAY,
                         exceptions=(RestCommunicationError, pycurl.error))
  def GetBlob(self, tag, md5_sum):
    url = self.releases_url + "/blob/%s/%s/" % (tag, md5_sum)
    logging.debug('GetBlob() url=%r', url)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
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
    logging.debug("HTTP code: %s", http_code)
    if http_code == 401:
      raise RestCommunicationError("Received HTTP code {0}".format(http_code))
    successful = (http_code >= 200 and http_code <= 299)
    metadata = None
    if successful:
      metadata = cjson.decode(d.getvalue())
    else:
      logging.warning("Blob %r for %r was not found in the database"
                      % (tag, md5_sum))
    return metadata

  def _HttpHeadRequest(self, url):
    """Make a HTTP HEAD request and return the http code."""
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.NOPROGRESS, 1)
    c.setopt(pycurl.NOBODY, 1)
    c.setopt(pycurl.HEADER, 1)
    c = self._SetAuth(c)
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    c.close()
    return http_code

  @retry_decorator.Retry(tries=DEFAULT_TRIES, delay=DEFAULT_RETRY_DELAY,
                         exceptions=(RestCommunicationError, pycurl.error))
  def BlobExists(self, tag, md5_sum):
    url = self.releases_url + "/blob/%s/%s/" % (tag, md5_sum)
    logging.debug('BlobExists(): HEAD %r' % url)
    http_code = self._HttpHeadRequest(url)
    if http_code == 404:
      logging.debug("Stats for %s don't exist" % md5_sum)
      return False
    elif http_code == 200:
      logging.debug('Stats for %s do exist' % md5_sum)
      return True
    else:
      raise RestCommunicationError(
          "URL HEAD %r HTTP code: %d"
          % (url, http_code))

  def _RPC(self, url, query_struct):
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.POST, 1)
    data = [
        ('query_data', cjson.encode(query_struct)),
    ]
    c.setopt(pycurl.HTTPPOST, data)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    # The empty Expect: header fixes the HTTP 417 error on the buildfarm,
    # related to the use of squid as a proxy (squid only supports HTML/1.0).
    c.setopt(pycurl.HTTPHEADER, ["Expect:"])
    c = self._SetAuth(c)
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    logging.debug("curl getinfo: %s %s", http_code, c.getinfo(pycurl.EFFECTIVE_URL))
    c.close()
    if http_code >= 400 and http_code < 600:
      if not self.debug:
        # In debug mode, all headers are printed to screen, and we aren't
        # interested in the response body.
        logging.fatal("Response: %s %s", http_code, d.getvalue())
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))
    else:
      d.seek(0)
      display_response = d.read(100)
      if d.len > 100:
        display_response += " (...)"
      logging.debug('Response: HTTP %d %r', http_code, display_response)

    return cjson.decode(d.getvalue())

  def BulkQueryStatsExistence(self, md5_sum_list):
    url = self.releases_url + "/rpc/bulk-existing-svr4/"
    return self._RPC(url, md5_sum_list)

  def RegisterLevelOne(self, md5_sum):
    self.ValidateMd5(md5_sum)
    url = self.releases_url + "/svr4/%s/db-level-1/" % md5_sum
    return self._CurlPut(url, [])

  @retry_decorator.Retry(tries=DEFAULT_TRIES, delay=DEFAULT_RETRY_DELAY,
                         exceptions=(RestCommunicationError, pycurl.error))
  def IsRegisteredLevelTwo(self, md5_sum):
    self.ValidateMd5(md5_sum)
    url = self.releases_url + '/svr4/%s/db-level-2/' % md5_sum
    http_code = self._HttpHeadRequest(url)
    if http_code == 404:
      return False
    elif http_code == 200:
      return True
    else:
      raise RestCommunicationError("URL %r HTTP code: %d"
                                   % (url, http_code))

  def RegisterLevelTwo(self, md5_sum, use_in_catalogs=True):
    self.ValidateMd5(md5_sum)
    url = self.releases_url + '/svr4/%s/db-level-2/' % md5_sum
    if use_in_catalogs:
      url += '?use_in_catalogs=1'
    else:
      url += '?use_in_catalogs=0'
    return self._CurlPut(url, [])

  def GetCatalogForGeneration(self, catrel, arch, osrel):
    url = (self.pkgdb_url + "/catalogs/%s/%s/%s/for-generation/"
           % (catrel, arch, osrel))
    logging.debug("GetCatalogForGeneration(): url=%r", url)
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetBasenamesByCatalogAndDir(self, catrel, arch, osrel, basedir):
    url = (
        self.pkgdb_url
        + "/catalogs/%s/%s/%s/pkgnames-and-paths-by-basedir?%s"
           % (catrel, arch, osrel, urllib.urlencode({'basedir': basedir})))
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetPathsAndPkgnamesByBasename(self, catrel, arch, osrel, basename):
    url = (
        self.pkgdb_url
        + "/catalogs/%s/%s/%s/pkgnames-and-paths-by-basename?%s"
           % (catrel, arch, osrel, urllib.urlencode({'basename': basename})))
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetCatalogTimingInformation(self, catrel, arch, osrel):
    url = (
      self.pkgdb_url
      + "/catalogs/%s/%s/%s/timing/" % (catrel, arch, osrel))
    data = urllib2.urlopen(url).read()
    return cjson.decode(data)

  def GetSrv4FileMetadataForReleases(self, md5_sum):
    """I have no idea what I was thinking when I wrote this.

    This function seems to be looking for the existence of package stats.

    Returns:
      a tuple: (successful_fetch, metadata)
    """
    logging.debug("_GetSrv4FileMetadata(%s)", repr(md5_sum))
    url = self.releases_url + "/srv4/" + md5_sum + "/"
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
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
    logging.debug("HTTP code: %s", http_code)
    if http_code == 401:
      raise RestCommunicationError("Received HTTP code {0}".format(http_code))
    successful = (http_code >= 200 and http_code <= 299)
    metadata = None
    if successful:
      metadata = cjson.decode(d.getvalue())
    else:
      logging.debug("Metadata for %s were not found in the database" % repr(md5_sum))
    return successful, metadata

  def PostFile(self, filename, md5_sum):
    logging.info("Uploading %s" % repr(filename))
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    url = self.releases_url + "/srv4/"
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.POST, 1)
    c = self._SetAuth(c)
    post_data = [
        ('srv4_file', (pycurl.FORM_FILE, filename)),
        ('submit', 'Upload'),
        ('md5_sum', md5_sum),
        ('basename', os.path.basename(filename)),
    ]
    c.setopt(pycurl.HTTPPOST, post_data)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.setopt(pycurl.HTTPHEADER, ["Expect:"]) # Fixes the HTTP 417 error
    if self.debug:
      c.setopt(c.VERBOSE, 1)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    c.close()
    if self.debug:
      logging.debug("*** Headers")
      logging.debug(h.getvalue())
      logging.debug("*** Data")
      logging.debug(d.getvalue())
    logging.debug("File POST http code: %s", http_code)
    if http_code >= 400 and http_code <= 499:
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))


class CachedPkgstats(object):
  """Class responsible for holding and caching package stats.

  Wraps RestClient and provides a caching layer.
  """

  def __init__(self, filename, rest_client):
    self.filename = filename
    self.d = anydbm.open("%s.db" % self.filename, "c")
    config = configuration.GetConfig()
    self.rest_client = rest_client
    self.deps = anydbm.open("%s-deps.db" % self.filename, "c")

  def __del__(self):
    self.d.close()

  def GetPkgstats(self, md5):
    pkgstats = None
    if str(md5) in self.d:
      serialized_data = self.d[md5]
      try:
        return cjson.decode(serialized_data)
      except (TypeError, cjson.DecodeError) as e:
        logging.fatal('A problem with %r: %r', md5, e)
        del self.d[md5]
    if not pkgstats:
      pkgstats = self.rest_client.GetPkgstatsByMd5(md5)
      self.d[md5] = cjson.encode(pkgstats)
    return pkgstats

  def GetDeps(self, md5):
    if str(md5) in self.deps:
      return cjson.decode(self.deps[md5])
    else:
      data = self.rest_client.GetCatalogData(md5)
      self.deps[md5] = cjson.encode(data)
      return data


def GetUsernameAndPassword():
  username = os.environ["LOGNAME"]
  password = None
  authfile = os.path.join('/etc/opt/csw/releases/auth', username)
  try:
    with open(authfile, 'r') as af:
      password = af.read().strip()
  except IOError as e:
    logging.debug("Error reading %s: %s", authfile, e)

  if password is None:
    # This part is specific to OpenCSW buildfarm.
    args = ['ssh', '-o BatchMode=yes', '-o StrictHostKeyChecking=no', 'login', 'cat', authfile]
    ret_code, stdout, stderr = shell.ShellCommand(args)
    if not ret_code:
      password = stdout.strip()
    else:
      logging.debug('Failed running %r', args)

  if password is None:
    logging.warning(
        'Could not find password for user %r. '
        'Falling back to getpass.getpass().', username)
    password = getpass.getpass("{0}'s pkg release password> ".format(username))

  return username, password
