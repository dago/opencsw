#!/usr/bin/env python2.6
# coding=utf-8

import copy
import datetime
import hashlib
import itertools
import logging
import marshal
import os.path
import progressbar
import progressbar.widgets
import re
import sqlobject
import sys

from sqlobject import sqlbuilder

from lib.python import checkpkg_lib
from lib.python import common_constants
from lib.python import configuration
from lib.python import errors
from lib.python import fake_pkgstats_composer
from lib.python import models as m
from lib.python import mute_progressbar
from lib.python import opencsw
from lib.python import representations
from lib.python import rest
from lib.python import sharedlib_utils
from lib.python import shell
from lib.python import util

CONTENT_PKG_RE = r"^\*?(CSW|SUNW)[0-9a-zA-Z\-]?[0-9a-z\-]+$"
ALPHANUMERIC_RE = r"[0-9a-zA-Z]+"

class ParsingError(errors.Error):
  """Parsing has failed."""


class PackageError(errors.Error):
  """An problem with the package."""


class DataError(errors.Error):
  """Insonsistency in processed data."""


class OsIndexingBase(object):

  def _ChunkName(self, name):
    return "%s-%s.marshal" % (self._Basename(), name)

  def SaveChunk(self, name, data):
    fn = self._ChunkName(name)
    with open(fn, "w") as fd:
      logging.debug("Marshalling data to %r.", fn)
      marshal.dump(data, fd)

  def ChunkExists(self, name):
    fn = self._ChunkName(name)
    if os.path.exists(fn):
      logging.info("%s already exists.", fn)
      return True
    else:
      logging.info("%s does not exist.", fn)
      return False

  def LoadChunk(self, name):
    fn = self._ChunkName(name)
    with open(fn, "r") as fd:
      logging.debug("Loading chunk %r", fn)
      data = marshal.load(fd)
    return data

  def _Basename(self):
    return "system-idx-%s-%s" % (self.osrel, self.arch)


class Indexer(OsIndexingBase):

  """Indexer of /var/sadm/install/contents.

  Based on:
  http://docs.sun.com/app/docs/doc/816-5174/contents-4?l=en&a=view

  """

  def __init__(self, out_basename=None, infile_contents=None,
               infile_pkginfo=None, osrel=None, arch=None):
    super(Indexer, self).__init__()
    self.out_basename = out_basename
    self.infile_contents = infile_contents
    self.infile_pkginfo = infile_pkginfo
    self.osrel = osrel
    self.arch = arch
    if not self.infile_contents:
      self.infile_contents = common_constants.DEFAULT_INSTALL_CONTENTS_FILE
    if not self.osrel:
      self.osrel = self._GetOsrel()
    if not self.arch:
      self.arch = self._GetArch()
    if not self.out_basename:
      self.out_basename = self._Basename()
    logging.debug("Indexer(): infile_contents=%s, out_basename=%s, osrel=%s, arch=%s",
                  repr(self.infile_contents), repr(self.out_basename), repr(self.osrel),
                  repr(self.arch))
    assert self.out_basename is not None

  def _ParseSrv4PkginfoLine(self, line):
    fields = re.split(configuration.WS_RE, line)
    pkgname = fields[1]
    pkg_desc = u" ".join(fields[2:])
    return pkgname, pkg_desc

  def _ParseIpsPkgListLine(self, line):
    fields = re.split(configuration.WS_RE, line)
    pkgname = self._IpsNameToSrv4Name(fields[0])
    desc_field_start = 1
    # The optional publisher field is always between
    # parenthesis, we skip it if necessary
    if fields[desc_field_start].startswith("("):
      desc_field_start += 1
    pkg_desc = u" ".join(fields[desc_field_start:])
    return pkgname, pkg_desc

  def _ParseIpsPkgContentsLine(self, line):
    """Parses one line of "pkg contents" output

    Returns: A dictionary of fields, or None.
    """
    # we will map from IPS type to SVR4 type
    type_mapping  = { "link": "s", "hardlink": "l", "file": "f", "dir": "d" }

    parts = re.split(configuration.WS_RE, line.strip())
    if len(parts) < 4:
      raise ParsingError("Line does not have enough fields: %s"
                         % repr(parts))
    # paths are relative to "/" in pkg contents output
    f_path = "/" + parts[0]
    f_target = None
    try:
      f_type = type_mapping[parts[1]]
    except:
      raise ParsingError("Wrong file type: %s in %s"
                         % (repr(parts[1]), repr(line)))
    f_mode = None
    f_owner = None
    f_group = None
    f_pkgname = None
    pkgnames = [ self._IpsNameToSrv4Name(parts[2]) ]
    if f_type in ("s", "l"):
      f_target = parts[3]
    else:
      (f_mode, f_owner, f_group) = parts[3:6]

    return representations.PkgmapEntry(
        line=line,
        class_=None,
        mode=f_mode,
        owner=f_owner,
        group=f_group,
        path=f_path,
        target=f_target,
        type_=f_type,
        major=None,
        minor=None,
        size=None,
        cksum=None,
        modtime=None,
        pkgnames=pkgnames,
    )

  def _ParseSrv4PkgmapLine(self, line):
    """Parses one line of /var/sadm/install/contents.

    Returns: A dictionary of fields, or None.
    """
    if line.startswith("#"):
      return None
    parts = re.split(configuration.WS_RE, line.strip())
    # logging.debug("_ParsePkgmapLine(): %s", parts)
    if len(parts) < 4:
      raise ParsingError("Line does not have enough fields: %s"
                         % repr(parts))
    file_type = parts[1]
    f_path = None
    f_target = None
    f_type = None
    f_class = None
    f_major = None
    f_minor = None
    f_mode = None
    f_owner = None
    f_group = None
    f_size = None
    f_cksum = None
    f_modtime = None
    f_pkgname = None
    pkgnames = []
    if file_type == 's':
      # ftype s: path=rpath s class package
      #
      # Spotted in real life:
      # ['/opt/csw/man=share/man', 's', 'none', 'CSWschilybase',
      # 'CSWschilyutils', 'CSWstar', 'CSWcommon']
      (f_path_rpath, f_type, f_class) = parts[:3]
      pkgnames.extend(parts[3:])
      f_path, f_target = f_path_rpath.split("=")
    elif file_type == 'l':
      # ftype l: path l class package
      f_path, f_type, f_class, f_pkgname = parts
    elif file_type in ('d', 'x', 'p'):
      # ftype d: path d class mode owner group package(s)
      # ftype x: path x class mode owner group package
      f_path, f_type, f_class, f_mode, f_owner, f_group = parts[:6]
      pkgnames.extend(parts[6:])
    elif file_type == '?':
      # Does not follow the specfication.  A specimen:
      # /opt/csw/gcc3/lib/gcc/sparc-sun-solaris2.8/3.4.6/include
      # ? none CSWgcc3g77 CSWgcc3core
      logging.warning("File type of %s is '?', assuming it's a directory.",
                      parts[0])
      f_type = 'd'
      f_path, unused_type, f_class = parts[:3]
      pkgnames.extend(parts[3:])
    elif file_type in ('b', 'c'):
      # ftype b: path b class major minor mode owner group package
      # ftype c: path c class major minor mode owner group package
      (f_path, f_type, f_class, f_major, f_minor, f_mode, f_owner,
       f_group, f_pkgname) = parts
    elif file_type in ('f', 'v', 'e'):
      # ftype f: path f class mode owner group size cksum modtime package
      # ftype v: path v class mode owner group size cksum modtime package
      # ftype e: path e class mode owner group size cksum modtime package
      #
      # Spotted in real life:
      # ['/etc/.java/.systemPrefs/.system.lock', 'e', 'preserve',
      # '0644', 'root', 'bin', '0', '0', '1265116929', 'SUNWj6cfg',
      # 'SUNWj5cfg']
      (f_path, f_type, f_class, f_mode, f_owner, f_group, f_size,
          f_cksum, f_modtime) = parts[:9]
      pkgnames.extend(parts[9:])
    else:
      raise ParsingError("Wrong file type: %s in %s"
                         % (repr(file_type), repr(line)))
    if f_pkgname:
      pkgnames.append(f_pkgname)

    static_parts = parts[:9]
    dynamic_parts = parts[9:]
    # ['/usr/lib/sparcv9/libpthread.so.1', 'f', 'none', '0755', 'root',
    # 'bin', '41296', '28258', '1018129099', 'SUNWcslx']
    # line, class_, mode, owner, group, path, target, type_,
    # major, minor, size, cksum, modtime, pkgnames
    return representations.PkgmapEntry(
        line=line,
        class_=f_class,
        mode=f_mode,
        owner=f_owner,
        group=f_group,
        path=f_path,
        target=f_target,
        type_=f_type,
        major=f_major,
        minor=f_minor,
        size=f_size,
        cksum=f_cksum,
        modtime=f_modtime,
        pkgnames=pkgnames,
    )

  def _ParsePkgContents(self, stream, parser, show_progress):
    logging.debug("-> _ParsePkgContents()")
    parsed_lines = []
    c = itertools.count()
    # Progressbar stuff can go here.
    for line in stream:
      if show_progress:
        if not c.next() % 1000:
          sys.stdout.write(".")
          sys.stdout.flush()
      parsed_line = parser(line)
      # parsed_line might be None if line was a comment
      if parsed_line:
        # Cast to tuple for serializability.
        parsed_lines.append(tuple(parsed_line))
    if show_progress:
      sys.stdout.write("\n")
    logging.debug("<- _ParsePkgContents()")
    return parsed_lines

  def _GetUname(self, uname_option=None):
    args = ["uname"]
    if uname_option:
      args.append(uname_option)
    # TODO: Don't fork during unit tests
    ret, stdout, unused_stderr = shell.ShellCommand(args,
        allow_error=False)
    return stdout.strip()

  def _GetOsrel(self):
    osname = self._GetUname()
    osnumber = self._GetUname("-r")
    return osname + osnumber

  def _GetArch(self):
    return self._GetUname("-p")

  def IndexAndSave(self):
    # This function interacts with the OS.
    contents = None
    files_metadata = None
    show_progress = True

    if not self.ChunkExists("pkginfo"):
      srv4_pkginfos_stream = self._GetSrv4PkginfosStream()
      if self.osrel in common_constants.IPS_OS_RELS:
        ips_pkginfos_stream = self._GetIpsPkginfosStream()
      else:
        ips_pkginfos_stream = None
      pkginfo = self._ParsePkginfoOutput(srv4_pkginfos_stream,
                                         self._ParseSrv4PkginfoLine,
                                         show_progress)
      if ips_pkginfos_stream:
        pkginfo.update(self._ParsePkginfoOutput(ips_pkginfos_stream,
                                                self._ParseIpsPkgListLine,
                                                show_progress))
      self.SaveChunk("pkginfo", pkginfo)
    if not self.ChunkExists("contents"):
      srv4_pkgcontents_stream = self._GetSrv4PkgcontentStream()
      if self.osrel in common_constants.IPS_OS_RELS:
        ips_pkgcontents_stream = self._GetIpsPkgcontentStream()
      else:
        ips_pkgcontents_stream = None

      contents_stream = open(self.infile_contents, "r")
      contents = self._ParsePkgContents(contents_stream,
                                        self._ParseSrv4PkgmapLine,
                                        show_progress=False)
      if ips_pkgcontents_stream:
        contents += self._ParsePkgContents(ips_pkgcontents_stream,
                                           self._ParseIpsPkgContentsLine,
                                           show_progress)
      self.SaveChunk("contents", contents)
    if not self.ChunkExists("files_metadata"):
      if not contents:
        contents = self.LoadChunk("contents")
      # We don't need to index anything under /opt/csw.
      contents_namedtuple = [representations.PkgmapEntry._make(x)
                             for x in contents]
      fetch_metadata_for = [
          x for x in contents_namedtuple
          if not x.path.startswith("/opt/csw")]
      files_metadata = self._GetFilesMetadata(fetch_metadata_for)
      self.SaveChunk("files_metadata", files_metadata)
      del contents # Will it save any memory?
    if not self.ChunkExists("binaries_dump_info"):
      if not files_metadata:
        files_metadata = self.LoadChunk("files_metadata")
      # Changing from named tuples to tuples for marshalling.
      binaries_dump_info = (
          [tuple(x) for x in self._GetBinariesDumpInfo(files_metadata)])
      self.SaveChunk("binaries_dump_info", binaries_dump_info)

  def _GetSrv4PkgcontentStream(self):
    return open(self.infile_contents, "r")

  def _GetIpsPkgcontentStream(self):
    args = ["pkg", "contents", "-H", "-o",
            "path,action.name,pkg.name,target,mode,owner,group",
            "-t", "dir,file,hardlink,link"]
    ret, stdout, unused_stderr = shell.ShellCommand(args)
    return stdout.splitlines()

  def _GetSrv4PkginfosStream(self):
    """Calls pkginfo if file is not specified."""
    if self.infile_pkginfo:
      pkginfo_stream = open(self.infile_pkginfo, "r")
    else:
      args = ["pkginfo"]
      ret, stdout, stderr = shell.ShellCommand(args)
      pkginfo_stream = stdout.splitlines()
    return pkginfo_stream

  def _GetIpsPkginfosStream(self):
    args = ["pkg", "list", "-H", "-s"]
    ret, stdout, stderr = shell.ShellCommand(args)
    pkglist_stream = stdout.splitlines()
    return pkglist_stream

  def _ParsePkginfoOutput(self, pkginfo_stream, parser, unused_show_progress):
    """Parses information about packages

    Args:
      stream: Output from pkginfo, or the Solaris 11 equivalent
      parser: The parse method used to retrieve information from the stream
      unused_show_progress: Used to display a progress bar, which was removed.
    Returns:
      A dictionary from pkgnames to descriptions.
    """
    logging.debug("-> _ParsePkginfoOutput()")
    packages_by_pkgname = {}
    for line in pkginfo_stream:
      pkgname, pkg_desc = parser(line)
      packages_by_pkgname.setdefault(pkgname, pkg_desc)
    logging.debug("<- _ParsePkginfoOutput()")
    return packages_by_pkgname

  def _IpsNameToSrv4Name(self, ips_name):
    """Create a fake Srv4 pkgname from an ips pkgname."""
    return "SUNW" + "-".join(re.findall (ALPHANUMERIC_RE, ips_name))

  def _GetFilesMetadata(self, contents):
    logging.debug("_GetFilesMetadata()")
    file_magic = util.FileMagic()
    files_metadata = []
    counter = itertools.count()
    counter_max = len(contents)
    for d in contents:
      p = d.path
      iteration_number = counter.next()
      sys.stdout.write(
          "\r%06d / %06d %-60s"
          % (iteration_number, counter_max, p[:60]))
      sys.stdout.flush()
      file_info = util.GetFileMetadata(file_magic, "/", p)
      # The file_info variable can be empty; in which case we don't want
      # to store it.
      if file_info:
        # We need to cast the named tuple to a regular tuple, otherwise
        # it won't marshal.
        files_metadata.append(tuple(file_info))
    sys.stdout.write("\n")
    sys.stdout.flush()
    return files_metadata

  def _GetBinariesDumpInfo(self, files_metadata):
    binaries_dump_info = []
    for metadata_tuple in files_metadata:
      file_metadata = representations.FileMetadata._make(metadata_tuple)
      d = file_metadata._asdict()
      if sharedlib_utils.IsBinary(d, allow_missing=True):
        abs_path = d["path"]
        sys.stdout.write("\r%-78s" % (abs_path[:78]))
        sys.stdout.flush()
        binary_path = d["path"]
        # Need to strip off the leading slash.
        if binary_path.startswith("/"):
          binary_path = binary_path[1:]
        binaries_dump_info.append(
                util.GetBinaryDumpInfo(abs_path, binary_path))
    sys.stdout.write("\n")
    sys.stdout.flush()
    return binaries_dump_info

class InstallContentsImporter(OsIndexingBase):
  """Responsible for importing a serialized file into the database."""

  def __init__(self, osrel, arch, debug=False):
    super(InstallContentsImporter, self).__init__()
    self.osrel = osrel
    self.arch = arch
    self.pkginst_cache = {}
    config = configuration.GetConfig()
    self.rest_client = rest.RestClient(
        pkgdb_url=config.get('rest', 'pkgdb'),
        releases_url=config.get('rest', 'releases'),
        debug=debug)

  def _RemoveSystemPackagesFromCatalog(self, data):
    # TODO(maciej): Move this functionality to the server side.
    sqo_osrel, sqo_arch = self._GetSqoOsrelAndArch(data["osrel"], data["arch"])
    # We need to delete assignments from only the system packages, not
    # the CSW packages.
    result = m.Srv4FileInCatalog.select(
        sqlobject.AND(
          m.Srv4FileInCatalog.q.arch==sqo_arch,
          m.Srv4FileInCatalog.q.osrel==sqo_osrel))
    for catalog_assignment in result:
      if not catalog_assignment.srv4file.use_to_generate_catalogs:
        catalog_assignment.destroySelf()

  def ImportData(self, data, show_progress=False, include_prefixes=None):
    logging.debug('Cleaning the catalogs.')
    self._RemoveSystemPackagesFromCatalog(data)
    logging.debug('Composing fake packages.')
    pkgstats_list = self._ComposePkgstats(data)
    catalogs_to_insert_to = common_constants.DEFAULT_CATALOG_RELEASES
    logging.info('Inserting system packages into %s.'
                 % ' '.join(catalogs_to_insert_to))
    pbar = self._GetPbar(show_progress)
    pbar.maxval = len(pkgstats_list)
    pbar.start()
    for i, pkgstats in enumerate(pkgstats_list):
      md5_sum = pkgstats['basic_stats']['md5_sum']
      if not self.rest_client.BlobExists('pkgstats', md5_sum):
        self.rest_client.SaveBlob('pkgstats', md5_sum, pkgstats)
      if not self.rest_client.IsRegisteredLevelTwo(md5_sum):
        self.rest_client.RegisterLevelTwo(md5_sum, use_in_catalogs=False)
      # We need to import these into the regular catalogs.
      # TODO(maciej): Solve the problem of adding a new catalog. All
      # these have to be imported again.
      for catalog_release in catalogs_to_insert_to:
        self.rest_client.AddSvr4ToCatalog(catalog_release, data['arch'],
                                          data['osrel'], md5_sum)
      pbar.update(i)
    pbar.finish()

  def _GetSqoOsrelAndArch(self, osrel, arch):
    # TODO(maciej): Remove when _RemoveSystemPackagesFromCatalog uses
    # REST.
    sqo_osrel = m.OsRelease.selectBy(short_name=osrel).getOne()
    sqo_arch = m.Architecture.selectBy(name=arch).getOne()
    return sqo_osrel, sqo_arch

  def _GetPbar(self, show_progress):
    if show_progress:
      pbar = progressbar.ProgressBar(widgets=[
        progressbar.widgets.Percentage(),
        ' ',
        progressbar.widgets.ETA(),
        ' ',
        progressbar.widgets.Bar()
      ])
    else:
      pbar = mute_progressbar.MuteProgressBar()
    return pbar

  def SanitizeInstallContentsPkgname(self, pkgname):
    # Some install/contents line add ":none" to package names.  For
    # example: "BOstdenv:none". Some lines prefix packages with
    # stars: "*BOstdenv" or tilde: "~BOstdenv".
    #
    # Other specimen:
    # SUNWjhrt:j3link
    pkgname_orig = pkgname
    pkgname = pkgname.split(":")[0]
    for c in ('*', '~', '!'):
      pkgname = pkgname.lstrip(c)
    return pkgname

  def _SkipPrefix(self, pkgname, include_prefixes):
    skip_pkgname = False
    for prefix in common_constants.OWN_PKGNAME_PREFIXES:
      if pkgname.startswith(prefix):
        skip_pkgname = True
        break
    if include_prefixes:
      for prefix_to_include in include_prefixes:
        if pkgname.startswith(prefix_to_include):
          skip_pkgname = False
          break
    return skip_pkgname

  def _ComposePkgstats(self, data, include_prefixes=None, show_progress=True):
    logging.debug("_ComposePkgstats()")
    osrel = data["osrel"]
    arch = data["arch"]
    contents = data["contents"]
    files_metadata = [representations.FileMetadata._make(x)
                      for x in data["files_metadata"]]
    logging.debug("Creating an in-memory index of files metadata (mime types)")
    metadata_by_file_name = dict(
        (x.path, x) for x in files_metadata)
    catalog = checkpkg_lib.Catalog()
    srv4_files_to_catalog = set()
    cleaned_pkgs = set()
    pkgs_by_pkgname = {}
    pbar = self._GetPbar(show_progress)
    progressbar_divisor = int(len(contents) / 1000)
    if progressbar_divisor < 1:
      progressbar_divisor = 1
    update_period = 1L
    pbar.maxval = len(contents)
    pbar.start()
    count = itertools.count()
    plc = fake_pkgstats_composer.PkgstatsListComposer(osrel, arch)
    # Create a new class responsible for creating pkgstats lists.
    # We might potentially run out of memory here.
    for pkgmap_tuple in contents:
      pkgmap_entry = representations.PkgmapEntry._make(pkgmap_tuple)
      logging.debug("Pkgmap entry: %r", pkgmap_entry)
      for pkgname in pkgmap_entry.pkgnames:
        pkgname = self.SanitizeInstallContentsPkgname(pkgname)
        if not self._SkipPrefix(pkgname, include_prefixes):
          # This is a little messy. Some pkgmap_entry objects are the
          # /opt/csw ones which don't have the metadata collected.
          # We have to skip them.
          if pkgmap_entry.path not in metadata_by_file_name:
            continue
          plc.AddPkgname(pkgname)
          plc.AddFile(pkgname,
                      pkgmap_entry,
                      metadata_by_file_name[pkgmap_entry.path],
                      None, None)
      i = count.next()
      if not i % update_period and (i / progressbar_divisor) <= pbar.maxval:
        pbar.update(i / progressbar_divisor)
    pbar.finish()
    return plc.GetPkgstats()

  def Import(self, show_progress):
    # Maybe the data will fit in memory.
    pkginfo = self.LoadChunk("pkginfo")
    contents = self.LoadChunk("contents")
    files_metadata = self.LoadChunk("files_metadata")
    binaries_dump_info = self.LoadChunk("binaries_dump_info")
    self.ImportData({
      "pkginfo": pkginfo,
      "contents": contents,
      "files_metadata": files_metadata,
      "binaries_dump_info": binaries_dump_info,
      "osrel": self.osrel,
      "arch": self.arch,
    }, show_progress=show_progress)
