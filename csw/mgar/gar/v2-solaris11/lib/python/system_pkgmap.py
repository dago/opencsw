#!/usr/bin/env python2.6
# coding=utf-8

import re
import configuration as c
import subprocess
import logging
import common_constants
import cPickle
import itertools
import progressbar
import models as m
import sqlobject
import hashlib
import opencsw
import package_stats
import datetime
import os.path
import mute_progressbar
import checkpkg_lib
import sys

CONTENT_PKG_RE = r"^\*?(CSW|SUNW)[0-9a-zA-Z\-]?[0-9a-z\-]+$"
ALPHANUMERIC_RE = r"[0-9a-zA-Z]+"

class Error(Exception):
  pass


class ParsingError(Error):
  pass


class SubprocessError(Error):
  pass


class OldLocalDatabaseManager(object):
  """Detects if local database is up to date, and re-populates it."""

  def __init__(self):
    super(LocalDatabaseManager, self).__init__()
    self.initialized = False

  def InitializeDatabase(self):
    """Establishing the connection to the database."""
    need_to_create_tables = False
    db_path = self.GetDatabasePath()
    checkpkg_dir = os.path.join(os.environ["HOME"], self.CHECKPKG_DIR)
    if not os.path.exists(db_path):
      logging.info("Building the  cache database %s.", self.system_pkgmap_files)
      logging.info("The cache will be kept in %s.", db_path)
      if not os.path.exists(checkpkg_dir):
        logging.debug("Creating %s", checkpkg_dir)
        os.mkdir(checkpkg_dir)
      need_to_create_tables = True
    self.InitializeRawDb()
    self.InitializeSqlobject()
    if not self.IsDatabaseGoodSchema():
      logging.info("Old database schema detected.")
      raise SetupError("Checkpkg database does not have the right schema.\n"
                       "Updates of the database no longer happen within "
                       "checkpkg.")
      self.PurgeDatabase(drop_tables=True)
      need_to_create_tables = True
    if need_to_create_tables:
      self.CreateTables()
      self.PerformInitialDataImport()
    if not self.IsDatabaseUpToDate():
      raise SetupError("Checkpkg database is not up to date.\n"
                       "Updates of the database no longer happen within "
                       "checkpkg.")
      self.ClearTablesForUpdates()
      self.RefreshDatabase()
    self.initialized = True


class Indexer(object):

  """Indexer of /var/sadm/install/contents.

  Based on:
  http://docs.sun.com/app/docs/doc/816-5174/contents-4?l=en&a=view

  """

  def __init__(self, outfile=None, infile_contents=None, infile_pkginfo=None,
               osrel=None, arch=None):
    self.outfile = outfile
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
    if not self.outfile:
      self.outfile = ("install-contents-%s-%s.pickle"
                      % (self.osrel, self.arch))
    logging.debug("Indexer(): infile_contents=%s, outfile=%s, osrel=%s, arch=%s",
                  repr(self.infile_contents), repr(self.outfile), repr(self.osrel),
                  repr(self.arch))

  def _ParseSrv4PkginfoLine(self, line):
    fields = re.split(c.WS_RE, line)
    pkgname = fields[1]
    pkg_desc = u" ".join(fields[2:])
    return pkgname, pkg_desc

  def _ParseIpsPkgListLine(self, line):
    fields = re.split(c.WS_RE, line)
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

    parts = re.split(c.WS_RE, line.strip())
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

    d = {
        "path": f_path,
        "target": f_target,
        "type": f_type,
        "mode": f_mode,
        "owner": f_owner,
        "group": f_group,
        "pkgnames": pkgnames,
        "line": line,
    }
    return d

  def _ParseSrv4PkgmapLine(self, line):
    """Parses one line of /var/sadm/install/contents.

    Returns: A dictionary of fields, or None.
    """
    if line.startswith("#"):
      return None
    parts = re.split(c.WS_RE, line.strip())
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
    d = {
        "path": f_path,
        "target": f_target,
        "type": f_type,
        "class": f_class,
        "major": f_major,
        "minor": f_minor,
        "mode": f_mode,
        "owner": f_owner,
        "group": f_group,
        "size": f_size,
        "cksum": f_cksum,
        "modtime": f_modtime,
        "pkgnames": pkgnames,
        "line": line,
    }
    return d

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
      d = parser(line)
      # d might be None if line was a comment
      if d:
        parsed_lines.append(d)
    if show_progress:
      sys.stdout.write("\n")
    logging.debug("<- _ParsePkgContents()")
    return parsed_lines

  def _GetUname(self, uname_option=None):
    args = ["uname"]
    if uname_option:
      args.append(uname_option)
    # TODO: Don't fork during unit tests
    uname_proc = subprocess.Popen(args,
                                  stdout=subprocess.PIPE)
    stdout, stderr = uname_proc.communicate()
    ret = uname_proc.wait()
    if ret:
      raise SubprocessError("Running uname has failed.")
    return stdout.strip()

  def _GetOsrel(self):
    osname = self._GetUname()
    osnumber = self._GetUname("-r")
    return osname + osnumber

  def _GetArch(self):
    return self._GetUname("-p")

  def GetDataStructure(self, srv4_pkgcontent_stream, srv4_pkginfo_stream, 
                       ips_pkgcontent_stream, ips_pkginfo_stream,
                       osrel, arch, show_progress=False):
    """Gets the data structure to be pickled.

    Does not interact with the OS.
    """
    data = {
        "osrel": osrel,
        "arch": arch,
        "contents": self._ParsePkgContents(srv4_pkgcontent_stream, self._ParseSrv4PkgmapLine, show_progress),
        "pkginfo": self._ParsePkgInfos(srv4_pkginfo_stream, self._ParseSrv4PkginfoLine, show_progress),
    }
    if ips_pkginfo_stream and ips_pkgcontent_stream:
      data["contents"].append(self._ParsePkgContents(ips_pkgcontent_stream, self._ParseIpsPkgContentsLine, show_progress))
      data["pkginfo"].update(self._ParsePkgInfos(ips_pkgcontent_stream, self._ParseIpsPkgListLine, show_progress))

    return data

  def Index(self, show_progress=False):
    # This function interacts with the OS.
    srv4_pkgcontents_stream = self._GetSrv4PkgcontentStream()
    srv4_pkginfos_stream = self._GetSrv4PkginfosStream()

    if self.osrel in common_constants.IPS_OS_RELS:
      ips_pkgcontents_stream = self._GetIpsPkgcontentStream()
      ips_pkginfos_stream = self._GetIpsPkginfosStream()
    else: 
      ips_pkgcontents_stream = None
      ips_pkginfos_stream = None
      
    data = self.GetDataStructure(srv4_pkgcontents_stream, srv4_pkginfos_stream, 
                                 ips_pkgcontents_stream, ips_pkginfos_stream, 
                                 self.osrel, self.arch, show_progress)
    return data

  def IndexAndSave(self):
    # This function interacts with the OS.
    data = self.Index()
    out_fd = open(self.outfile, "w")
    logging.debug("IndexAndSave(): pickling the data.")
    cPickle.dump(data, out_fd, cPickle.HIGHEST_PROTOCOL)
    logging.debug("IndexAndSave(): pickling done.")

  def _GetSrv4PkgcontentStream(self):
    return (open(self.infile_contents, "r"))

  def _GetIpsPkgcontentStream(self):
    args = ["pkg", "contents", "-H", "-o",
            "path,action.name,pkg.name,target,mode,owner,group",
            "-t", "dir,file,hardlink,link"]
    pkg_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = pkg_proc.communicate()
    ret = pkg_proc.wait()
    return stdout.splitlines()

  def _GetSrv4PkginfosStream(self):
    """Calls pkginfo if file is not specified."""
    if self.infile_pkginfo:
      pkginfo_stream = open(self.infile_pkginfo, "r")
    else:
      args = ["pkginfo"]
      pkginfo_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
      stdout, stderr = pkginfo_proc.communicate()
      ret = pkginfo_proc.wait()
      pkginfo_stream = stdout.splitlines()
    
    return pkginfo_stream

  def _GetIpsPkginfosStream(self):
    args = ["pkg", "list", "-H", "-s"]
    pkg_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = pkg_proc.communicate()
    ret = pkg_proc.wait()
    pkglist_stream = stdout.splitlines()
    return pkglist_stream

  def _ParsePkgInfos(self, stream, parser, unused_show_progress):
    """Parses informations about packages

    Args:
      stream: A stream that contains informations about packages
      parser: The parse method used to retrieve information from the stream
      unused_show_progress: Used to display a progress bar, which was removed.
    Returns:
      A dictionary from pkgnames to descriptions.
    """
    logging.debug("-> _ParsePkgInfos()")
    packages_by_pkgname = {}
    for line in stream:
      pkgname, pkg_desc = parser(line)
      packages_by_pkgname.setdefault(pkgname, pkg_desc)
    logging.debug("<- _ParsePkgInfos()")
    return packages_by_pkgname

  def _IpsNameToSrv4Name(self, ips_name):
    """Create a fake Srv4 pkgname from an ips pkgname."""
    return "SUNW" + "-".join(re.findall (ALPHANUMERIC_RE, ips_name))

class InstallContentsImporter(object):
  """Responsible for importing a pickled file into the database."""

  def __init__(self):
    self.pkginst_cache = {}
    self.fake_srv4_cache = {}

  def _ImportPackages(self, data):
    logging.debug("_ImportPackages()")
    for pkgname, pkg_desc in data["pkginfo"].iteritems():
      sqo_pkg = None
      try:
        sqo_pkg = m.Pkginst.select(
            m.Pkginst.q.pkgname==pkgname).getOne()
      except sqlobject.main.SQLObjectNotFound, e:
        sqo_pkg = m.Pkginst(pkgname=pkgname,
                            pkg_desc=pkg_desc)
      self.pkginst_cache[pkgname] = sqo_pkg

  def _GetPkginst(self, pkgname):
    if pkgname not in self.pkginst_cache:
      logging.debug("_GetPkginst(): getting %s", repr(pkgname))
      sqo_pkg = m.Pkginst.select(
          m.Pkginst.q.pkgname==pkgname).getOne()
      self.pkginst_cache[pkgname] = sqo_pkg
    return self.pkginst_cache[pkgname]

  def _RemoveSystemPackagesFromCatalog(self, data):
    sqo_osrel, sqo_arch = self._GetSqoOsrelAndArch(data["osrel"], data["arch"])
    res = m.Srv4FileStats.select(
        sqlobject.AND(
          m.Srv4FileStats.q.use_to_generate_catalogs==False,
          m.Srv4FileStats.q.arch==sqo_arch,
          m.Srv4FileStats.q.os_rel==sqo_osrel))
    for sqo_srv4 in res:
      for srv4_in_cat in sqo_srv4.in_catalogs:
        srv4_in_cat.destroySelf()

  def ImportFromFile(self, in_fd, show_progress=False):
    logging.debug("Unpickling data")
    data = cPickle.load(in_fd)
    self.ImportData(data, show_progress)

  def ImportData(self, data, show_progress=False, include_prefixes=None):
    logging.debug("Cleaning the catalogs.")
    self._RemoveSystemPackagesFromCatalog(data)
    logging.debug("Importing packages.")
    self._ImportPackages(data)
    logging.debug("Importing files.")
    self._ImportFiles(data, include_prefixes, show_progress=show_progress)

  def _GetFakeMaintainer(self):
    fake_email = "fake@example.com"
    fake_name = "Placeholder for an external maintainer"
    try:
      sqo_maintainer = m.Maintainer.select(
          m.Maintainer.q.email==fake_email).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      sqo_maintainer = m.Maintainer(
          email=fake_email,
          full_name=fake_name)
    return sqo_maintainer

  def _GetSqoOsrelAndArch(self, osrel, arch):
    sqo_osrel = m.OsRelease.select(
        m.OsRelease.q.short_name==osrel).getOne()
    sqo_arch = m.Architecture.select(
        m.Architecture.q.name==arch).getOne()
    return sqo_osrel, sqo_arch

  def _GetFakeSrv4(self, pkgname, osrel, arch):
    """Retrieves or creates a fake srv4 object."""
    key = (pkgname, osrel, arch)
    if key not in self.fake_srv4_cache:
      sqo_pkginst = self._GetPkginst(pkgname)
      fake_srv4_md5 = self.ComposeFakeSrv4Md5(pkgname, osrel, arch)
      sqo_osrel, sqo_arch = self._GetSqoOsrelAndArch(osrel, arch)
      # logging.debug("_GetFakeSrv4(%s, %s, %s), %s",
      #               pkgname, osrel, arch, fake_srv4_md5)
      try:
        sqo_srv4 = m.Srv4FileStats.select(
            m.Srv4FileStats.q.md5_sum==fake_srv4_md5).getOne()
      except sqlobject.main.SQLObjectNotFound, e:
        catalogname = opencsw.PkgnameToCatName(pkgname)
        maintainer = self._GetFakeMaintainer()
        sqo_srv4 = m.Srv4FileStats(
            arch=sqo_arch,
            basename=("%s-fake_version" % catalogname),
            catalogname=catalogname,
            data_obj=None,
            use_to_generate_catalogs=False,
            filename_arch=sqo_arch,
            latest=True,
            maintainer=maintainer,
            md5_sum=fake_srv4_md5,
            mtime=datetime.datetime.now(),
            os_rel=sqo_osrel,
            pkginst=sqo_pkginst,
            registered=True,
            rev="fake_rev",
            stats_version=package_stats.PACKAGE_STATS_VERSION,
            version_string="fake_version",
            size=0)
      self.fake_srv4_cache[key] = sqo_srv4
    return self.fake_srv4_cache[key]

  def _ImportFiles(self, data, include_prefixes=None, show_progress=False):
    logging.debug("_ImportFiles()")
    osrel = data["osrel"]
    arch = data["arch"]
    contents = data["contents"]
    catalog = checkpkg_lib.Catalog()
    srv4_files_to_catalog = set()
    # The progressbar library doesn't like handling larger numbers
    # It displays up to 99% if we feed it a maxval in the range of hundreds of
    # thousands.
    progressbar_divisor = int(len(contents) / 1000)
    if progressbar_divisor < 1:
      progressbar_divisor = 1
    update_period = 1L
    count = itertools.count()
    if show_progress:
      pbar = progressbar.ProgressBar()
    else:
      pbar = mute_progressbar.MuteProgressBar()
    pbar.maxval = len(contents) / progressbar_divisor
    pbar.start()
    cleaned_pkgs = set()
    logging.debug("Content leghts: %s", len(contents))
    for d in contents:
      i = count.next()
      if not i % update_period and (i / progressbar_divisor) <= pbar.maxval:
        pbar.update(i / progressbar_divisor)
      for pkgname in d["pkgnames"]:
        pkgname = self.SanitizeInstallContentsPkgname(pkgname)
        # If a package is a packge of our own,
        # it should not be imported that way; own packages should be
        # only managed by adding them to specific catalogs.
        skip_pkgname = False
        for prefix in common_constants.OWN_PKGNAME_PREFIXES:
          if pkgname.startswith(prefix):
            skip_pkgname = True
            break
        # Prefix whilelist - whitelisted prefixes win.
        if include_prefixes:
          for prefix_to_include in include_prefixes:
            if pkgname.startswith(prefix_to_include):
              skip_pkgname = False
              break
        if skip_pkgname:
          continue
        # We'll create one file instance for each package
        try:
          sqo_srv4 = self._GetFakeSrv4(pkgname, osrel, arch)
        except sqlobject.main.SQLObjectNotFound, e:
          print d
          raise
        if sqo_srv4 not in cleaned_pkgs:
          sqo_srv4.RemoveAllCswFiles()
          cleaned_pkgs.add(sqo_srv4)
        sqo_pkginst = self._GetPkginst(pkgname)
        f_path, f_basename = os.path.split(d["path"])
        # This is really slow (one run ~1h), but works.
        # To speed it up, raw SQL + cursor.executemany() could be used, but
        # there's a incompatibility between MySQL and sqlite drivers:
        # MySQL:  INSERT ... VALUES (%s, %s, %s);
        # sqlite: INSERT ... VALUES (?, ?, ?);
        # For now, using the sqlobject ORM which is slow, but at least
        # handles compatibility issues.
        csw_file = m.CswFile(pkginst=sqo_pkginst,
            line=d["line"], path=f_path, basename=f_basename,
            srv4_file=sqo_srv4)
        srv4_files_to_catalog.add(sqo_srv4)
    pbar.finish()
    logging.debug(
        "Registering all the fake srv4 files in all catalogs.")
    for sqo_srv4 in srv4_files_to_catalog:
      for sqo_catrel in m.CatalogRelease.select():
        catalog.AddSrv4ToCatalog(
            sqo_srv4, osrel, arch, sqo_catrel.name)

  def ComposeFakeSrv4Md5(self, pkgname, osrel, arch):
    """Returns a fake md5 sum of a fake srv4 package.

    For the purposes of fake srv4 packages for SUNW stuff.
    """
    key = pkgname + osrel + arch
    md5_sum = hashlib.md5(key).hexdigest()
    return md5_sum

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
    # logging.debug("d['pkgnames']: %s → %s", pkgname_orig, pkgname)
    return pkgname
