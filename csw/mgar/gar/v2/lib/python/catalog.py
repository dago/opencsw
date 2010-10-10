#!/usr/bin/env python2.6

import re

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

  def __init__(self, file_name):
    self.file_name = file_name
    self.by_basename = None
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
            r"(?P<none_thing_1>\S+)"
            # An optional empty field.
            r"("
              r"\s+"
              # none\n'
              r"(?P<none_thing_2>\S+)"
            r")?"
            r"$"
        ),
    ]
    cline_re_list = [re.compile(x) for x in cline_re_str_list]
    matched = False
    d = None
    for cline_re in cline_re_list:
      m = cline_re.match(line)
      if m:
        d = m.groupdict()
        matched = True
        if not d:
          raise CatalogLineParseError("Parsed %s data is empty" % repr(line))
    if not matched:
      raise CatalogLineParseError("No regexes matched %s" % repr(line))
    return d

  def _GetCatalogData(self, fd):
    catalog_data = []
    for line in fd:
      try:
        parsed = self._ParseCatalogLine(line)
        catalog_data.append(parsed)
      except CatalogLineParseError, e:
        logging.debug("Could not parse %s, %s", repr(line), e)
    return catalog_data

  def GetCatalogData(self):
    if not self.catalog_data:
      fd = open(self.file_name, "r")
      self.catalog_data = self._GetCatalogData(fd)
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
