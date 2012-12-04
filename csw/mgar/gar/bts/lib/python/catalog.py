#!/usr/bin/env python2.6

import os
import re
import logging
import opencsw


class Error(Exception):
  pass


class CatalogLineParseError(Error):
  pass


class OpencswCatalogBuilder(object):

  def __init__(self, product_dir, catalog_dir):
    self.product_dir = product_dir
    self.catalog_dir = catalog_dir

  def Run(self):
    pkg_dirs = os.listdir(self.product_dir)
    for pkg_dir in pkg_dirs:
      pkg_path = os.path.join(self.product_dir, pkg_dir)
      pkginfo_path = os.path.join(pkg_path, "pkginfo")
      if (os.path.isdir(pkg_path)
            and
          os.path.exists(pkginfo_path)):
        if not self.Srv4Exists(pkg_path):
          pkg = None
          tmpdir = None
          try:
            tmpdir = tempfile.mkdtemp(prefix="sunw-pkg-")
            logging.debug("Copying %s to %s", repr(pkg_path), repr(tmpdir))
            tmp_pkg_dir = os.path.join(tmpdir, pkg_dir)
            shutil.copytree(pkg_path, tmp_pkg_dir, symlinks=True)
            pkg = DirectoryFormatPackage(tmp_pkg_dir)
            # Replacing NAME= in the pkginfo, setting it to the catalog name.
            pkg.ResetNameProperty()
            pkg.ToSrv4(self.catalog_dir)
          except IOError, e:
            logging.warn("%s has failed: %s", pkg_path, e)
          finally:
            if pkg:
              del(pkg)
            if os.path.exists(tmpdir):
              shutil.rmtree(tmpdir)
        else:
          logging.warn("srv4 file for %s already exists, skipping", pkg_path)
      else:
        logging.warn("%s is not a directory.", pkg_path)


  def Srv4Exists(self, pkg_dir):
    pkg = DirectoryFormatPackage(pkg_dir)
    srv4_name = pkg.GetSrv4FileName()
    srv4_name += ".gz"
    srv4_path = os.path.join(self.catalog_dir, srv4_name)
    result = os.path.exists(srv4_path)
    logging.debug("Srv4Exists(%s) => %s, %s", pkg_dir, repr(srv4_path), result)
    return result


class OpencswCatalog(object):
  """Represents a catalog file."""

  def __init__(self, fd):
    self.fd = fd
    self.by_basename = None
    self.by_catalogname = None
    self.catalog_data = None

  def _ParseCatalogLine(self, line):
    cline_re_str_list = [
        (
            r"^"
            # tmux
            r"(?P<catalogname>\S+)"
            r"\s+"
            # 1.2,REV=2010.05.17
            r"(?P<version>\S+)"
            r"\s+"
            # CSWtmux
            r"(?P<pkgname>\S+)"
            r"\s+"
            # tmux-1.2,REV=2010.05.17-SunOS5.9-sparc-CSW.pkg.gz
            r"(?P<file_basename>\S+)"
            r"\s+"
            # 145351cf6186fdcadcd169b66387f72f
            r"(?P<md5sum>\S+)"
            r"\s+"
            # 214091
            r"(?P<size>\S+)"
            r"\s+"
            # CSWcommon|CSWlibevent
            r"(?P<deps>\S+)"
            r"\s+"
            # none
            r"(?P<category>\S+)"
            # An optional empty field.
            r"("
              r"\s+"
              # none\n'
              r"(?P<i_deps>\S+)"
            r")?"
            r"$"
        ),
    ]
    cline_re_list = [re.compile(x) for x in cline_re_str_list]
    matched = False
    d = None
    def SplitPkgList(pkglist):
      if not pkglist:
        pkglist = ()
      elif pkglist == "none":
        pkglist = ()
      else:
        pkglist = tuple(pkglist.split("|"))
      return pkglist
    for cline_re in cline_re_list:
      m = cline_re.match(line)
      if m:
        d = m.groupdict()
        matched = True
        if not d:
          raise CatalogLineParseError("Parsed %s data is empty" % repr(line))
        d["deps"] = SplitPkgList(d["deps"])
        d["i_deps"] = SplitPkgList(d["i_deps"])
    if not matched:
      raise CatalogLineParseError("No regexes matched %s" % repr(line))
    return d

  def _GetCatalogData(self, fd):
    catalog_data = []
    for line in fd:
      if not line.strip(): continue
      if line.startswith("#"): continue
      if line.startswith("-----BEGIN PGP SIGNED"): continue
      if line.startswith("Hash: "): continue
      if line.startswith("-----BEGIN PGP SIGNATURE"): break
      try:
        parsed = self._ParseCatalogLine(line)
        catalog_data.append(parsed)
      except CatalogLineParseError, e:
        logging.debug("Could not parse %s, %s", repr(line), e)
    return catalog_data

  def GetCatalogData(self):
    if not self.catalog_data:
      self.catalog_data = self._GetCatalogData(self.fd)
    return self.catalog_data

  def GetDataByBasename(self):
    if not self.by_basename:
      self.by_basename = {}
      cd = self.GetCatalogData()
      for d in cd:
        if "file_basename" not in d:
          logging.error("%s is missing the file_basename field", d)
        self.by_basename[d["file_basename"]] = d
    return self.by_basename

  def GetDataByCatalogname(self):
    if not self.by_catalogname:
      self.by_catalogname = {}
      cd = self.GetCatalogData()
      for d in cd:
        if "catalogname" not in d:
          logging.error("%s is missing the catalogname field", d)
        if d["catalogname"] in self.by_catalogname:
          logging.warning("Catalog name %s is duplicated!", d["catalogname"])
        self.by_catalogname[d["catalogname"]] = d
    return self.by_catalogname


class CatalogComparator(object):

  def GetCatalogDiff(self, cat_a, cat_b):
    """Returns a difference between two catalogs.

    Catalogs need to be represented either as a OpencswCatalog() object, or as
    a dictionary, as returned by OpencswCatalog.GetDataByCatalogname().
    """
    if type(cat_a) == dict:
      bc_a = cat_a
    else:
      bc_a = cat_a.GetDataByCatalogname()
    if type(cat_b) == dict:
      bc_b = cat_b
    else:
      bc_b = cat_b.GetDataByCatalogname()
    cn_a = set(bc_a)
    cn_b = set(bc_b)
    new_catalognames = cn_b.difference(cn_a)
    removed_catalognames = cn_a.difference(cn_b)
    same_catalognames = cn_b.intersection(cn_a)
    # Looking for updated catalognames
    updated_catalognames = set()
    for catalogname in same_catalognames:
      if bc_a[catalogname]["version"] != bc_b[catalogname]["version"]:
        updated_catalognames.add(catalogname)
    new_pkgs = [bc_b[x] for x in new_catalognames]
    removed_pkgs = [bc_a[x] for x in removed_catalognames]
    def UpdateData(_bc_a, _bc_b, catalogname):
      a = bc_a[x]
      b = bc_b[x]
      cmp_result = opencsw.CompareVersions(
          a["version"],
          b["version"])
      if cmp_result < 0:
        direction = "upgrade"
      else:
        direction = "downgrade"
      return {
          "from": a,
          "to": b,
          "type": self.DiffType(a, b),
          "direction": direction,
      }
    updated_pkgs = [UpdateData(bc_a, bc_b, x) for x in updated_catalognames]
    return new_pkgs, removed_pkgs, updated_pkgs

  def DiffType(self, a, b):
    va = opencsw.ParseVersionString(a["version"])
    vb = opencsw.ParseVersionString(b["version"])
    if va[0] == vb[0]:
      return "revision"
    else:
      return "version"
