#!/usr/bin/env python2.6

"""csw_upload_pkg.py - uploads packages to the database.

POST using pycurl code example taken from:
http://pycurl.cvs.sourceforge.net/pycurl/pycurl/tests/test_post2.py?view=markup
"""

from StringIO import StringIO
import pycurl
import logging
import optparse
import hashlib
import os.path
import opencsw
import json
import common_constants
import socket
import rest
import struct_util


BASE_URL = "http://buildfarm.opencsw.org/releases/"
DEFAULT_CATREL = "unstable"
USAGE = """%prog [ options ] <pkg1> [ <pkg2> [ ... ] ]

Uploads a set of packages to the unstable catalog in opencsw-future.

- When an ARCH=all package is sent, it's added to both sparc and i386 catalogs
- When a SunOS5.x package is sent, it's added to catalogs SunOS5.x,
  SunOS5.(x+1), up to SunOS5.11, but only if there are no packages specific to
  5.10 (and/or 5.11).
- If a package update is sent, the tool uses catalogname to identify the
  package it's supposed to replace

The --remove option affects the same catalogs as the regular use, except that
it removes assignments of a given package to catalogs, instead of adding them.

The --os-release flag makes %prog only insert the package to catalog with the
given OS release.

For more information, see:
http://wiki.opencsw.org/automated-release-process#toc0
"""

class Error(Exception):
  pass


class RestCommunicationError(Error):
  pass


class PackageCheckError(Error):
  """A problem with the package."""


class DataError(Error):
  """Unexpected data found."""


class Srv4Uploader(object):

  def __init__(self, filenames, os_release=None, debug=False):
    self.filenames = filenames
    self.md5_by_filename = {}
    self.debug = debug
    self._rest_client = rest.RestClient()
    self.os_release = os_release

  def Upload(self):
    for filename in self.filenames:
      parsed_basename = opencsw.ParsePackageFileName(
          os.path.basename(filename))
      if parsed_basename["vendortag"] != "CSW":
        raise PackageCheckError(
            "Package vendor tag is %s instead of CSW."
            % parsed_basename["vendortag"])
      self._UploadFile(filename)

  def Remove(self):
    for filename in self.filenames:
      self._RemoveFile(filename)

  def _RemoveFile(self, filename):
    md5_sum = self._GetFileMd5sum(filename)
    file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
    osrel = file_metadata['osrel']
    arch = file_metadata['arch']
    catalogs = self._MatchSrv4ToCatalogs(
        filename, DEFAULT_CATREL, arch, osrel, md5_sum)
    for unused_catrel, cat_arch, cat_osrel in catalogs:
      self._RemoveFromCatalog(filename, cat_arch, cat_osrel, file_metadata)

  def _RemoveFromCatalog(self, filename, arch, osrel, file_metadata):
    md5_sum = self._GetFileMd5sum(filename)
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    # TODO: Move this bit to a separate class (RestClient)
    url = (
        "%scatalogs/unstable/%s/%s/%s/"
        % (BASE_URL, arch, osrel, md5_sum))
    logging.debug("DELETE @ URL: %s %s", type(url), url)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
    c.setopt(pycurl.HTTPHEADER, ["Expect:"]) # Fixes the HTTP 417 error
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
    if http_code >= 400 and http_code <= 499:
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))

  def _GetFileMd5sum(self, filename):
    if filename not in self.md5_by_filename:
      logging.debug("_GetFileMd5sum(%s): Reading the file", filename)
      with open(filename, "rb") as fd:
        hash = hashlib.md5()
        hash.update(fd.read())
        md5_sum = hash.hexdigest()
        self.md5_by_filename[filename] = md5_sum
    return self.md5_by_filename[filename]

  def _MatchSrv4ToCatalogs(self, filename,
                           catrel, srv4_arch, srv4_osrel,
                           md5_sum):
    """Compile a list of catalogs affected by the given file.

    If it's a 5.9 package, it can be matched to 5.9, 5.10 and 5.11.  However,
    if there already are specific 5.10 and/or 5.11 versions of the package,
    don't overwrite them.
    """
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    osrels = None
    for idx, known_osrel in enumerate(common_constants.OS_RELS):
      if srv4_osrel == known_osrel:
        osrels = common_constants.OS_RELS[idx:]
    assert osrels, "OS releases not found"
    if srv4_arch == 'all':
      archs = ('sparc', 'i386')
    else:
      archs = (srv4_arch,)
    catalogname = parsed_basename["catalogname"]
    catalogs = []
    for arch in archs:
      for osrel in osrels:
        logging.debug("%s %s %s", catrel, arch, osrel)
        srv4_in_catalog = self._rest_client.Srv4ByCatalogAndCatalogname(
            catrel, arch, osrel, catalogname)
        if not srv4_in_catalog or srv4_in_catalog["osrel"] == srv4_osrel:
          # The same architecture as our package, meaning that we can insert
          # the same architecture into the catalog.
          if (not self.os_release
              or (self.os_release and osrel == self.os_release)):
            catalogs.append((catrel, arch, osrel))
        else:
          if self.os_release and osrel == self.os_release:
            catalogs.append((catrel, arch, osrel))
          logging.debug(
              "Catalog %s %s %s has another version of %s.",
              catrel, arch, osrel, catalogname)
    return tuple(catalogs)

  def _UploadFile(self, filename):
    md5_sum = self._GetFileMd5sum(filename)
    file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
    if file_in_allpkgs:
      logging.debug("File %s already uploaded.", filename)
    else:
      logging.debug("Uploading %s.", filename)
      self._PostFile(filename)
    file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
    logging.debug("file_metadata %s", repr(file_metadata))
    if not file_metadata:
      logging.error(
          "File metadata was not found in the database.  "
          "This happens when the package you're trying to upload was never "
          "unpacked and imported into the database.  "
          "To fix the problem, run checkpkg against your package and try "
          "importing again.")
      raise DataError("file_metadata is empty: %s" % repr(file_metadata))
    osrel = file_metadata['osrel']
    arch = file_metadata['arch']
    catalogs = self._MatchSrv4ToCatalogs(
        filename, DEFAULT_CATREL, arch, osrel, md5_sum)
    for unused_catrel, cat_arch, cat_osrel in catalogs:
      self._InsertIntoCatalog(filename, cat_arch, cat_osrel, file_metadata)

  def _InsertIntoCatalog(self, filename, arch, osrel, file_metadata):
    logging.info(
        "_InsertIntoCatalog(%s, %s, %s)",
        repr(arch), repr(osrel), repr(filename))
    md5_sum = self._GetFileMd5sum(filename)
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    logging.debug("parsed_basename: %s", parsed_basename)
    url = (
        "%scatalogs/unstable/%s/%s/%s/"
        % (BASE_URL, arch, osrel, md5_sum))
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
    if http_code >= 400 and http_code <= 499:
      if not self.debug:
        # In debug mode, all headers are printed to screen, and we aren't
        # interested in the response body.
        logging.fatal("Response: %s %s", http_code, d.getvalue())
      raise RestCommunicationError("%s - HTTP code: %s" % (url, http_code))
    else:
      logging.info("Response: %s %s", http_code, d.getvalue())
    return http_code

  def _GetSrv4FileMetadata(self, md5_sum):
    logging.debug("_GetSrv4FileMetadata(%s)", repr(md5_sum))
    url = BASE_URL + "srv4/" + md5_sum + "/"
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.WRITEFUNCTION, d.write)
    c.setopt(pycurl.HEADERFUNCTION, h.write)
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
    successful = http_code >= 200 and http_code <= 299
    metadata = None
    if successful:
      metadata = json.loads(d.getvalue())
    else:
      logging.info("Data for %s not found" % repr(md5_sum))
    return successful, metadata

  def _PostFile(self, filename):
    logging.info("_PostFile(%s)", repr(filename))
    md5_sum = self._GetFileMd5sum(filename)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    url = BASE_URL + "srv4/"
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.POST, 1)
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


if __name__ == '__main__':
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug",
      dest="debug",
      default=False, action="store_true")
  parser.add_option("--remove",
      dest="remove",
      default=False, action="store_true",
      help="Remove packages from catalogs instead of adding them")
  parser.add_option("--os-release",
      dest="os_release",
      help="If specified, only uploads to the specified OS release.")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  logging.debug("args: %s", args)
  hostname = socket.gethostname()
  if not hostname.startswith('login'):
    logging.warning("This script is meant to be run on the login host.")
  os_release = options.os_release
  if os_release:
    os_release = struct_util.OsReleaseToLong(os_release)
  uploader = Srv4Uploader(args,
                          os_release=os_release,
                          debug=options.debug)
  if options.remove:
    uploader.Remove()
  else:
    uploader.Upload()
