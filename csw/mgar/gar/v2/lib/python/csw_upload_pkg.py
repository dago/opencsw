#!/opt/csw/bin/python2.6

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
import subprocess
import file_set_checker
import sys
import getpass


BASE_URL = "http://buildfarm.opencsw.org"
RELEASES_APP = "/releases"
DEFAULT_CATREL = "unstable"
USAGE = """%prog [ options ] <file1.pkg.gz> [ <file2.pkg.gz> [ ... ] ]

Uploads a set of packages to the unstable catalog in opencsw-future.

- When an architecture-independent package is uploaded, it gets added to both
	sparc and i386 catalogs

- When a SunOS5.x package is sent, it's added to catalogs SunOS5.x,
  SunOS5.(x+1), up to SunOS5.11, but only if there are no packages specific to
  5.10 (and/or 5.11).

- If a package update is sent, the tool uses both the catalogname and the
	pkgname to identify the package it's updating. For example, you might upload
	foo_stub/CSWfoo and mean to replace foo/CSWfoo with it.

The --os-release flag makes %prog only insert the package to catalog with the
given OS release.

= General considerations =

This tool operates on a database of packages and a package file store. It
modifies a number of package catalogs, a cartesian product of:

  {legacy,dublin,unstable}x{sparc,i386}x{5.8,5.9.5.10,5.11}

This amounts to 3x2x4 = 24 package catalogs total.

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


class WorkflowError(Error):
  """Unexpected state of workflow, e.g. expected element not found."""


class Srv4Uploader(object):

  def __init__(self, filenames, rest_url, os_release=None, debug=False,
      output_to_screen=True,
      username=None, password=None):
    super(Srv4Uploader, self).__init__()
    if filenames:
      filenames = self.SortFilenames(filenames)
    self.filenames = filenames
    self.md5_by_filename = {}
    self.debug = debug
    self.os_release = os_release
    self.rest_url = rest_url
    self._rest_client = rest.RestClient(self.rest_url)
    self.output_to_screen = output_to_screen
    self.username = username
    self.password = password

  def _SetAuth(self, c):
    """Set basic HTTP auth options on given Curl object."""
    if self.username:
      logging.debug("Using basic AUTH for user %s", self.username)
      c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
      c.setopt(pycurl.USERPWD, "%s:%s" % (self.username, self.password))
    else:
      logging.debug("User and password not set, not using HTTP AUTH")
    return c

  def _ImportMetadata(self, filename):
    md5_sum = self._GetFileMd5sum(filename)
    metadata = self._rest_client.GetPkgByMd5(md5_sum)
    if metadata:
      # Metadata are already in the database.
      return
    logging.warning("%s (%s) is not known to the database.", filename, md5_sum)
    bin_dir = os.path.dirname(__file__)
    pkgdb_executable = os.path.join(bin_dir, "pkgdb")
    assert os.path.exists(pkgdb_executable), (
        "Could not find %s. Make sure that the pkgdb executable is "
        "available \n"
        "from the same directory as csw-upload-pkg." % pkgdb_executable)
    args = [pkgdb_executable, "importpkg"]
    if self.debug:
      args.append("--debug")
    args.append(filename)
    ret = subprocess.call(args)
    if ret:
      raise OSError("An error occurred when running %s." % args)
    # Verify that the import succeeded
    metadata = self._rest_client.GetPkgByMd5(md5_sum)
    if not metadata:
      raise WorkflowError(
          "Metadata of %s could not be imported into the database."
          % filename)


  def Upload(self):
    do_upload = True
    planned_modifications = []
    metadata_by_md5 = {}
    if self.output_to_screen:
      print "Processing %s file(s). Please wait." % (len(self.filenames),)
    for filename in self.filenames:
      self._ImportMetadata(filename)
      md5_sum = self._GetFileMd5sum(filename)
      file_in_allpkgs, file_metadata = self._GetSrv4FileMetadata(md5_sum)
      if file_in_allpkgs:
        logging.debug("File %s already uploaded.", filename)
      else:
        if do_upload:
          logging.debug("Uploading %s.", filename)
          self._PostFile(filename)
          # Querying the database again, this time the data should be
          # there
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
      metadata_by_md5[md5_sum] = file_metadata
      catalogs = self._MatchSrv4ToCatalogs(
          filename, DEFAULT_CATREL, arch, osrel, md5_sum)
      for unused_catrel, cat_arch, cat_osrel in catalogs:
        planned_modifications.append(
            (filename, md5_sum,
             arch, osrel, cat_arch, cat_osrel))
    # The plan:
    # - Create groups of files to be inserted into each of the catalogs
    # - Invoke checkpkg to check every target catalog
    checkpkg_sets = self._CheckpkgSets(planned_modifications)
    checks_successful = self._RunCheckpkg(checkpkg_sets)
    if checks_successful:
      if self.output_to_screen:
        print "All checks successful. Proceeding."
      for arch, osrel in sorted(checkpkg_sets):
        for filename, md5_sum in checkpkg_sets[(arch, osrel)]:
          file_metadata = metadata_by_md5[md5_sum]
          self._InsertIntoCatalog(filename, arch, osrel, file_metadata)

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

    Args:
      filename: string, base file name of the srv4 stream file
      catrel: string denoting catalog release, usually 'unstable'
      srv4_arch: string, denoting srv4 file architecture (sparc, i386 or all)
      srv4_osrel: string, OS release of the package, e.g. 'SunOS5.9'
      md5_sum: string, md5 sum of the srv4 file

    Returns:
      A tuple of tuples, where each tuple is: (catrel, arch, osrel)
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
    # This part of code quickly became complicated and should probably be
    # rewritten.  However, it is unit tested, so all the known cases are
    # handled as intended.
    catalogs = []
    first_cat_osrel_seen = None
    for arch in archs:
      for osrel in osrels:
        logging.debug("%s %s %s", catrel, arch, osrel)
        cat_key = (catrel, arch, osrel)
        srv4_in_catalog = self._rest_client.Srv4ByCatalogAndCatalogname(
            catrel, arch, osrel, catalogname)
        if srv4_in_catalog:
          logging.debug("Catalog %s %s contains version %s of the %s package",
                        arch, osrel, srv4_in_catalog["osrel"], catalogname)
        else:
          logging.debug(
              "Catalog %s %s does not contain any version of the %s package.",
              arch, osrel, catalogname)
        if not first_cat_osrel_seen:
          if srv4_in_catalog:
            first_cat_osrel_seen = srv4_in_catalog["osrel"]
          else:
            first_cat_osrel_seen = srv4_osrel
          logging.debug("Considering %s the base OS to match",
                        first_cat_osrel_seen)
        if (not srv4_in_catalog
            or srv4_in_catalog["osrel"] == srv4_osrel
            or srv4_in_catalog["osrel"] == first_cat_osrel_seen):
          # The same architecture as our package, meaning that we can insert
          # the same architecture into the catalog.
          if (not self.os_release
              or (self.os_release and osrel == self.os_release)):
            catalogs.append(cat_key)
        else:
          if self.os_release and osrel == self.os_release:
            logging.debug("OS release specified and matches %s.", osrel)
            catalogs.append(cat_key)
          else:
            logging.debug(
                "Not matching %s %s package with %s containing a %s package",
                catalogname,
                srv4_osrel, osrel, srv4_in_catalog["osrel"])
          logging.debug(
              "Catalog %s %s %s has another version of %s.",
              catrel, arch, osrel, catalogname)
    return tuple(catalogs)

  def _InsertIntoCatalog(self, filename, arch, osrel, file_metadata):
    logging.debug(
        "_InsertIntoCatalog(%s, %s, %s)",
        repr(arch), repr(osrel), repr(filename))
    print("Inserting %s (%s %s) into catalog %s %s %s"
          % (file_metadata["catalogname"],
             file_metadata["arch"],
             file_metadata["osrel"],
             DEFAULT_CATREL, arch, osrel))
    md5_sum = self._GetFileMd5sum(filename)
    basename = os.path.basename(filename)
    parsed_basename = opencsw.ParsePackageFileName(basename)
    logging.debug("parsed_basename: %s", parsed_basename)
    return rest_client.AddSvr4ToCatalog(catrel, arch, osrel, md5_sum)

  def _GetSrv4FileMetadata(self, md5_sum):
    logging.debug("_GetSrv4FileMetadata(%s)", repr(md5_sum))
    url = self.rest_url + RELEASES_APP + "/srv4/" + md5_sum + "/"
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
      metadata = json.loads(d.getvalue())
    else:
      logging.debug("Metadata for %s were not found in the database" % repr(md5_sum))
    return successful, metadata

  def _PostFile(self, filename):
    if self.output_to_screen:
      print "Uploading %s" % repr(filename)
    md5_sum = self._GetFileMd5sum(filename)
    c = pycurl.Curl()
    d = StringIO()
    h = StringIO()
    url = self.rest_url + RELEASES_APP + "/srv4/"
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

  def _CheckpkgSets(self, planned_modifications):
    """Groups packages according to catalogs.
    
    Used to determine groups of packages to check together, against
    a specific catalog.

    Args:
      A list of tuples

    Returns:
      A dictionary of tuples, indexed by (arch, osrel) tuples.
    """
    by_catalog = {}
    for fields in planned_modifications:
      filename, md5_sum, pkg_arch, pkg_osrel, cat_arch, cat_osrel = fields
      key = cat_arch, cat_osrel
      by_catalog.setdefault(key, [])
      by_catalog[key].append((filename, md5_sum))
    return by_catalog

  def SortFilenames(self, filenames):
    """Sorts filenames according to OS release.

    The idea is that in lexicographic sorting, SunOS5.9 is after
    SunOS5.10, while we want 5.9 to be first.
    """
    by_osrel = {}
    sorted_filenames = []
    for filename in filenames:
      basename = os.path.basename(filename)
      parsed_basename = opencsw.ParsePackageFileName(basename)
      by_osrel.setdefault(parsed_basename["osrel"], []).append(filename)
    for osrel in common_constants.OS_RELS:
      if osrel in by_osrel:
        for filename in by_osrel.pop(osrel):
          sorted_filenames.append(filename)
    if by_osrel:
      raise DataError("Unexpected architecture found in file list: %s."
                      % (repr(by_osrel),))
    return sorted_filenames

  def _RunCheckpkg(self, checkpkg_sets):
    bin_dir = os.path.dirname(__file__)
    checkpkg_executable = os.path.join(bin_dir, "checkpkg")
    assert os.path.exists(checkpkg_executable), (
        "Could not find %s. Make sure that the checkpkg executable is "
        "available \n"
        "from the same directory as csw-upload-pkg." % checkpkg_executable)
    checks_failed_for_catalogs = []
    args_by_cat = {}
    for arch, osrel in checkpkg_sets:
      print ("Checking %s package(s) against catalog %s %s %s"
             % (len(checkpkg_sets[(arch, osrel)]), DEFAULT_CATREL, arch, osrel))
      md5_sums = []
      basenames = []
      for filename, md5_sum in checkpkg_sets[(arch, osrel)]:
        md5_sums.append(md5_sum)
        basenames.append(os.path.basename(filename))
      # Not using the checkpkg Python API.  The reason is that checkpkg
      # requires the process calling its API to have an established
      # MySQL connection, while csw-upload-pkg does not, and it's better
      # if it stays that way.
      args_by_cat[(arch, osrel)] = [
          checkpkg_executable,
          "--catalog-release", DEFAULT_CATREL,
          "--os-release", osrel,
          "--architecture", arch,
      ] + md5_sums
      ret = subprocess.call(args_by_cat[(arch, osrel)] + ["--quiet"])
      if ret:
        checks_failed_for_catalogs.append(
            (arch, osrel, basenames)
        )
    if checks_failed_for_catalogs:
      print "Checks failed for catalogs:"
      for arch, osrel, basenames in checks_failed_for_catalogs:
        print "  - %s %s" % (arch, osrel)
        for basename in basenames:
          print "    %s" % basename
        print "To see errors, run:"
        print " ", " ".join(args_by_cat[(arch, osrel)])
      print ("Packages have not been submitted to the %s catalog."
             % DEFAULT_CATREL)
    return not checks_failed_for_catalogs


if __name__ == '__main__':
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-d", "--debug",
      dest="debug",
      default=False, action="store_true")
  parser.add_option("--os-release",
      dest="os_release",
      help="If specified, only uploads to the specified OS release.")
  parser.add_option("--rest-url",
      dest="rest_url",
      default=BASE_URL,
      help="Base URL for REST, e.g. %s" % BASE_URL)
  parser.add_option("--no-filename-check",
      dest="filename_check",
      default=True, action="store_false",
      help="Don't check the filename set (e.g. for a missing architecture)")
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

  if not args:
    parser.print_usage()
    sys.exit(1)

  # Check the file set.
  fc = file_set_checker.FileSetChecker()
  error_tags = fc.CheckFiles(args)
  if error_tags:
    print "There is a problem with the presented file list."
    for error_tag in error_tags:
      print "*", error_tag
    if options.filename_check:
      sys.exit(1)
    else:
      print "Continuing anyway."

  username, password = rest.GetUsernameAndPassword()
  uploader = Srv4Uploader(args,
                          options.rest_url,
                          os_release=os_release,
                          debug=options.debug,
                          username=username,
                          password=password)
  uploader.Upload()
