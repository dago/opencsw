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


BASE_URL = "http://buildfarm.opencsw.org/releases/"


class Error(Exception):
  pass


class RestCommunicationError(Error):
  pass


class Srv4Uploader(object):

  def __init__(self, filenames, debug=False):
    self.filenames = filenames
    self.md5_by_filename = {}
    self.debug = debug

  def Upload(self):
    for filename in self.filenames:
      self._UploadFile(filename)

  def _GetFileMd5sum(self, filename):
    if filename not in self.md5_by_filename:
      logging.debug("_GetFileMd5sum(%s): Reading the file", filename)
      with open(filename, "rb") as fd:
        hash = hashlib.md5()
        hash.update(fd.read())
        md5_sum = hash.hexdigest()
        self.md5_by_filename[filename] = md5_sum
    return self.md5_by_filename[filename]

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
    osrel = file_metadata['osrel']
    arch = file_metadata['arch']
    # Implementing backward compatibility.  A package for SunOS5.x is also
    # inserted into SunOS5.(x+n) for n=(0, 1, ...)
    for idx, known_osrel in enumerate(common_constants.OS_RELS):
      if osrel == known_osrel:
        osrels = common_constants.OS_RELS[idx:]
    if arch == 'all':
      archs = ('sparc', 'i386')
    else:
      archs = (arch,)
    for arch in archs:
      for osrel in osrels:
        self._InsertIntoCatalog(filename, arch, osrel, file_metadata)

  def _InsertIntoCatalog(self, filename, arch, osrel, file_metadata):
    logging.info("_InsertIntoCatalog(%s, %s, %s)", repr(arch), repr(osrel), repr(filename))
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
    c.setopt(pycurl.URL, str(url))
    c.setopt(pycurl.PUT, 1)
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
    if self.debug:
      logging.debug("*** Headers")
      logging.debug(h.getvalue())
      logging.debug("*** Data")
      logging.debug(d.getvalue())
    logging.info("Response: %s", d.getvalue())
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
    if self.debug:
      logging.debug("*** Headers")
      logging.debug(h.getvalue())
      logging.debug("*** Data")
      logging.debug(d.getvalue())
    successful = http_code >= 200 and http_code <= 299
    metadata = None
    if successful:
      metadata = json.loads(d.getvalue())
    return successful, metadata

  def _PostFile(self, filename):
    logging.info("_PostFile(%s)", repr(filename))
    md5_sum = self._GetFileMd5sum(filename)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    c.setopt(pycurl.URL, BASE_URL + "srv4/")
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
      raise RestCommunicationError("HTTP code: %s" % http_code)


if __name__ == '__main__':
  parser = optparse.OptionParser()
  parser.add_option("-d", "--debug",
      dest="debug",
      default=False, action="store_true")
  options, args = parser.parse_args()
  print "args:", args
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  uploader = Srv4Uploader(args, debug=options.debug)
  uploader.Upload()
