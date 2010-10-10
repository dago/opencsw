#!/usr/bin/env python2.6

import cPickle
import os
import re

import catalog
import database
import package
import overrides
import models as m
import tag

PACKAGE_STATS_VERSION = 9L

class PackageStats(database.DatabaseClient):
  """Collects stats about a package and saves it.

  TODO: Maintain a global database connection instead of creating one for each
  instantiated object.
  TODO: Store overrides in a separate table for performance.
  """

  def __init__(self, srv4_pkg, stats_basedir=None, md5sum=None, debug=False):
    super(PackageStats, self).__init__(debug=debug)
    self.srv4_pkg = srv4_pkg
    self.md5sum = md5sum
    self.dir_format_pkg = None
    self.all_stats = {}
    self.stats_basedir = stats_basedir
    self.db_pkg_stats = None
    if not self.stats_basedir:
      home = os.environ["HOME"]
      parts = [home, ".checkpkg", "stats"]
      self.stats_basedir = os.path.join(*parts)
    self.InitializeSqlobject()

  def GetPkgchkData(self):
    ret, stdout, stderr = self.srv4_pkg.GetPkgchkOutput()
    data = {
        'return_code': ret,
        'stdout_lines': stdout.splitlines(),
        'stderr_lines': stderr.splitlines(),
    }
    return data

  def GetMd5sum(self):
    if not self.md5sum:
      self.md5sum = self.srv4_pkg.GetMd5sum()
    return self.md5sum

  def GetDbObject(self):
    if not self.db_pkg_stats:
      md5_sum = self.GetMd5sum()
      res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
      if not res.count():
        # TODO: Change this bit to throw an exception if the object is not
        # found.
        return None
      else:
        self.db_pkg_stats = res.getOne()
    return self.db_pkg_stats


  def StatsExist(self):
    """Checks if statistics of a package exist.

    Returns:
      bool
    """
    pkg_stats = self.GetDbObject()
    if not pkg_stats:
      return False
    if pkg_stats.stats_version != PACKAGE_STATS_VERSION:
      pkg_stats.destroySelf()
    else:
      return True
    return False

  def GetDirFormatPkg(self):
    if not self.dir_format_pkg:
      self.dir_format_pkg = self.srv4_pkg.GetDirFormatPkg()
    return self.dir_format_pkg

  def GetMtime(self):
    return self.srv4_pkg.GetMtime()

  def _MakeDirP(self, dir_path):
    """mkdir -p equivalent.

    http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    """
    try:
      os.makedirs(dir_path)
    except OSError, e:
      if e.errno == errno.EEXIST:
        pass
      else:
        raise

  def GetBinaryDumpInfo(self):
    dir_pkg = self.GetDirFormatPkg()
    # Binaries. This could be split off to a separate function.
    # man ld.so.1 for more info on this hack
    env = copy.copy(os.environ)
    env["LD_NOAUXFLTR"] = "1"
    binaries_dump_info = []
    for binary in dir_pkg.ListBinaries():
      binary_abs_path = os.path.join(dir_pkg.directory, "root", binary)
      binary_base_name = os.path.basename(binary)
      args = [DUMP_BIN, "-Lv", binary_abs_path]
      dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE, env=env)
      stdout, stderr = dump_proc.communicate()
      ret = dump_proc.wait()
      binary_data = ParseDumpOutput(stdout)
      binary_data["path"] = binary
      binary_data["base_name"] = binary_base_name
      binaries_dump_info.append(binary_data)
    return binaries_dump_info

  def GetBasicStats(self):
    dir_pkg = self.GetDirFormatPkg()
    basic_stats = {}
    basic_stats["stats_version"] = PACKAGE_STATS_VERSION
    basic_stats["pkg_path"] = self.srv4_pkg.pkg_path
    basic_stats["pkg_basename"] = os.path.basename(self.srv4_pkg.pkg_path)
    basic_stats["parsed_basename"] = opencsw.ParsePackageFileName(
        basic_stats["pkg_basename"])
    basic_stats["pkgname"] = dir_pkg.pkgname
    basic_stats["catalogname"] = dir_pkg.GetCatalogname()
    basic_stats["md5_sum"] = self.GetMd5sum()
    return basic_stats

  def GetOverrides(self):
    dir_pkg = self.GetDirFormatPkg()
    override_list = dir_pkg.GetOverrides()
    def OverrideToDict(override):
      return {
        "pkgname":  override.pkgname,
        "tag_name":  override.tag_name,
        "tag_info":  override.tag_info,
      }
    overrides_simple = [OverrideToDict(x) for x in override_list]
    return overrides_simple

  def GetLddMinusRlines(self):
    """Returns ldd -r output."""
    dir_pkg = self.GetDirFormatPkg()
    binaries = dir_pkg.ListBinaries()
    ldd_output = {}
    for binary in binaries:
      binary_abspath = os.path.join(dir_pkg.directory, "root", binary)
      # this could be potentially moved into the DirectoryFormatPackage class.
      # ldd needs the binary to be executable
      os.chmod(binary_abspath, 0755)
      args = ["ldd", "-r", binary_abspath]
      ldd_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = ldd_proc.communicate()
      retcode = ldd_proc.wait()
      if retcode:
        logging.error("%s returned an error: %s", args, stderr)
      ldd_info = []
      for line in stdout.splitlines():
        ldd_info.append(self._ParseLddDashRline(line))
      ldd_output[binary] = ldd_info
    return ldd_output

  def GetDefinedSymbols(self):
    """Returns text symbols (i.e. defined functions) for packaged ELF objects

    To do this we parse output lines from nm similar to the following. "T"s are
    the definitions which we are after.

      0000104000 D _lib_version
      0000986980 D _libiconv_version
      0000000000 U abort
      0000097616 T aliases_lookup
    """
    dir_pkg = self.GetDirFormatPkg()
    binaries = dir_pkg.ListBinaries()
    defined_symbols = {}

    for binary in binaries:
      binary_abspath = os.path.join(dir_pkg.directory, "root", binary)
      # Get parsable, ld.so.1 relevant SHT_DYNSYM symbol information
      args = ["/usr/ccs/bin/nm", "-p", "-D", binary_abspath]
      nm_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = nm_proc.communicate()
      retcode = nm_proc.wait()
      if retcode:
        logging.error("%s returned an error: %s", args, stderr)
        continue
      nm_out = stdout.splitlines()

      defined_symbols[binary] = []
      for line in nm_out:
        sym = self._ParseNmSymLine(line)
        if not sym:
          continue
        if sym['type'] not in ("T", "D", "B"):
          continue
        defined_symbols[binary].append(sym['name'])

    return defined_symbols

  def _ParseNmSymLine(self, line):
    re_defined_symbol =  re.compile('[0-9]+ [ABDFNSTU] \S+')
    m = re_defined_symbol.match(line)
    if not m:
      return None
    fields = line.split()
    sym = { 'address': fields[0], 'type': fields[1], 'name': fields[2] }
    return sym

  def CollectStats(self, force=False):
    """Lazy stats collection."""
    if force or not self.StatsExist():
      return self._CollectStats()
    return self.ReadSavedStats()

  def _CollectStats(self):
    """The list of variables needs to be synchronized with the one
    at the top of this class.
    """
    dir_pkg = self.GetDirFormatPkg()
    logging.debug("Collecting %s package statistics.", repr(dir_pkg.pkgname))
    override_dicts = self.GetOverrides()
    pkg_stats = {
        "binaries": dir_pkg.ListBinaries(),
        "binaries_dump_info": self.GetBinaryDumpInfo(),
        "depends": dir_pkg.GetDependencies(),
        "isalist": GetIsalist(),
        "overrides": override_dicts,
        "pkgchk": self.GetPkgchkData(),
        "pkginfo": dir_pkg.GetParsedPkginfo(),
        "pkgmap": dir_pkg.GetPkgmap().entries,
        "bad_paths": dir_pkg.GetFilesContaining(BAD_CONTENT_REGEXES),
        "basic_stats": self.GetBasicStats(),
        "files_metadata": dir_pkg.GetFilesMetadata(),
        "mtime": self.GetMtime(),
    }
    pkgname = pkg_stats["basic_stats"]["pkgname"]
    # Getting sqlobject representations.
    try:
      pkginst = m.Pkginst.select(m.Pkginst.q.pkgname==pkgname).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      pkginst = m.Pkginst(pkgname=pkgname)
    try:
      res = m.Architecture.select(
          m.Architecture.q.name==pkg_stats["pkginfo"]["ARCH"])
      arch = res.getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      arch = m.Architecture(name=pkg_stats["pkginfo"]["ARCH"])
    parsed_basename = pkg_stats["basic_stats"]["parsed_basename"]
    os_rel_name = parsed_basename["osrel"]
    try:
      os_rel = m.OsRelease.select(
          m.OsRelease.q.short_name==os_rel_name).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      os_rel = m.OsRelease(short_name=os_rel_name, full_name=os_rel_name)
    try:
      maint_email = pkg_stats["pkginfo"]["EMAIL"]
      maintainer = m.Maintainer.select(
          m.Maintainer.q.email==maint_email).getOne()
    except sqlobject.main.SQLObjectNotFound, e:
      logging.debug(e)
      maintainer = m.Maintainer(email=maint_email)

    # If there are any previous records of the same pkginst, arch and os_rel,
    # we're marking them as not-latest.
    # This assumes that the packages are examined in a chronological order.
    res = m.Srv4FileStats.select(sqlobject.AND(
        m.Srv4FileStats.q.pkginst==pkginst,
        m.Srv4FileStats.q.arch==arch,
        m.Srv4FileStats.q.os_rel==os_rel))
    for obj in res:
      obj.latest = False

    rev=None
    if "revision_info" in parsed_basename:
      if "REV" in parsed_basename["revision_info"]:
        rev = parsed_basename["revision_info"]["REV"]
    # Creating the object in the database.
    db_pkg_stats = m.Srv4FileStats(
        md5_sum=self.GetMd5sum(),
        pkginst=pkginst,
        catalogname=pkg_stats["basic_stats"]["catalogname"],
        stats_version=PACKAGE_STATS_VERSION,
        os_rel=os_rel,
        arch=arch,
        basename=pkg_stats["basic_stats"]["pkg_basename"],
        maintainer=maintainer,
        latest=True,
        version_string=parsed_basename["full_version_string"],
        rev=rev,
        mtime=self.GetMtime(),
        data=cPickle.dumps(pkg_stats))
    # Inserting overrides as rows into the database
    for override_dict in override_dicts:
      o = m.CheckpkgOverride(srv4_file=db_pkg_stats,
                             **override_dict)

    # The ldd -r reporting breaks on bigger packages during yaml saving.
    # It might work when yaml is disabled
    # self.DumpObject(self.GetLddMinusRlines(), "ldd_dash_r")
    # This check is currently disabled, let's save time by not collecting
    # these data.
    # self.DumpObject(self.GetDefinedSymbols(), "defined_symbols")
    # This one should be last, so that if the collection is interrupted
    # in one of the previous runs, the basic_stats.pickle file is not there
    # or not updated, and the collection is started again.

    logging.debug("Statistics of %s have been collected.", repr(dir_pkg.pkgname))
    return pkg_stats

  def GetAllStats(self):
    if not self.all_stats and self.StatsExist():
      self.all_stats = self.ReadSavedStats()
    elif not self.all_stats:
      self.all_stats = self.CollectStats()
    return self.all_stats

  def GetSavedOverrides(self):
    if not self.StatsExist():
      raise PackageError("Package stats not ready.")
    pkg_stats = self.GetDbObject()
    res = m.CheckpkgOverride.select(m.CheckpkgOverride.q.srv4_file==pkg_stats)
    override_list = []
    for db_override in res:
      d = {
          'pkgname': db_override.pkgname,
          'tag_name': db_override.tag_name,
          'tag_info': db_override.tag_info,
      }
      override_list.append(overrides.Override(**d))
    return override_list

  def GetSavedErrorTags(self):
    pkg_stats = self.GetDbObject()
    res = m.CheckpkgErrorTag.select(m.CheckpkgErrorTag.q.srv4_file==pkg_stats)
    tag_list = [tag.CheckpkgTag(x.pkgname, x.tag_name, x.tag_info, x.msg)
                for x in res]
    return tag_list

  def ReadSavedStats(self):
    if not self.all_stats:
      md5_sum = self.GetMd5sum()
      res = m.Srv4FileStats.select(m.Srv4FileStats.q.md5_sum==md5_sum)
      self.all_stats = cPickle.loads(str(res.getOne().data))
    return self.all_stats

  def _ParseLddDashRline(self, line):
    found_re = r"^\t(?P<soname>\S+)\s+=>\s+(?P<path_found>\S+)"
    symbol_not_found_re = (r"^\tsymbol not found:\s(?P<symbol>\S+)\s+"
                           r"\((?P<path_not_found>\S+)\)")
    only_so = r"^\t(?P<path_only>\S+)$"
    version_so = (r'^\t(?P<soname_version_not_found>\S+) '
                  r'\((?P<lib_name>\S+)\) =>\t \(version not found\)')
    stv_protected = (r'^\trelocation \S+ symbol: (?P<relocation_symbol>\S+): '
                     r'file (?P<relocation_path>\S+): '
                     r'relocation bound to a symbol '
                     r'with STV_PROTECTED visibility$')
    sizes_differ = (r'^\trelocation \S+ sizes differ: '
                    r'(?P<sizes_differ_symbol>\S+)$')
    sizes_info = (r'^\t\t\(file (?P<sizediff_file1>\S+) size=(?P<size1>0x\w+); '
                  r'file (?P<sizediff_file2>\S+) size=(?P<size2>0x\w+)\)$')
    sizes_one_used = (r'^\t\t(?P<sizediffused_file>\S+) size used; '
                      r'possible insufficient data copied$')
    common_re = (r"(%s|%s|%s|%s|%s|%s|%s|%s)"
                 % (found_re, symbol_not_found_re, only_so, version_so,
                    stv_protected, sizes_differ, sizes_info, sizes_one_used))
    m = re.match(common_re, line)
    response = {}
    if m:
      d = m.groupdict()
      if "soname" in d and d["soname"]:
        # it was found
        response["state"] = "OK"
        response["soname"] = d["soname"]
        response["path"] = d["path_found"]
        response["symbol"] = None
      elif "symbol" in d and d["symbol"]:
        response["state"] = "symbol-not-found"
        response["soname"] = None
        response["path"] = d["path_not_found"]
        response["symbol"] = d["symbol"]
      elif d["path_only"]:
        response["state"] = "OK"
        response["soname"] = None
        response["path"] = d["path_only"]
        response["symbol"] = None
      elif d["soname_version_not_found"]:
        response["state"] = "version-not-found"
        response["soname"] = d["soname_version_not_found"]
        response["path"] = None
        response["symbol"] = None
      elif d["relocation_symbol"]:
        response["state"] = 'relocation-bound-to-a-symbol-with-STV_PROTECTED-visibility'
        response["soname"] = None
        response["path"] = d["relocation_path"]
        response["symbol"] = d["relocation_symbol"]
      elif d["sizes_differ_symbol"]:
        response["state"] = 'sizes-differ'
        response["soname"] = None
        response["path"] = None
        response["symbol"] = d["sizes_differ_symbol"]
      elif d["sizediff_file1"]:
        response["state"] = 'sizes-diff-info'
        response["soname"] = None
        response["path"] = "%s %s" % (d["sizediff_file1"], d["sizediff_file2"])
        response["symbol"] = None
      elif d["sizediffused_file"]:
        response["state"] = 'sizes-diff-one-used'
        response["soname"] = None
        response["path"] = "%s" % (d["sizediffused_file"])
        response["symbol"] = None
      else:
        raise StdoutSyntaxError("Could not parse %s with %s"
                                % (repr(line), common_re))
    else:
      raise StdoutSyntaxError("Could not parse %s with %s"
                              % (repr(line), common_re))
    return response


def StatsListFromCatalog(file_name_list, catalog_file_name=None, debug=False):
  packages = [package.CswSrv4File(x, debug) for x in file_name_list]
  if catalog_file_name:
    catalog_obj = catalog.OpencswCatalog(catalog_file_name)
    md5s_by_basename = catalog_obj.GetDataByBasename()
    for pkg in packages:
      basename = os.path.basename(pkg.pkg_path)
      # It might be the case that a file is present on disk, but missing from
      # the catalog file.
      if basename in md5s_by_basename:
        pkg.md5sum = md5s_by_basename[basename]["md5sum"]
  stats_list = [PackageStats(pkg) for pkg in packages]
  return stats_list
