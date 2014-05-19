# $Id$
#
# Defines models for package database.

import cjson
import datetime
import logging
import os.path
import re
import sqlobject
from sqlobject import sqlbuilder

logger = logging.getLogger('opencsw.models')

def SanitizeDatetime(d):
  if isinstance(d, datetime.datetime):
    return d.isoformat()
  else:
    return d


class Error(Exception):
  """Generic error."""


class DataError(Error):
  """A problem with data in the database."""


class CatalogRelease(sqlobject.SQLObject):
  "Release names: potato, etc."
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

  def __unicode__(self):
    return u"Catalog release: %s" % self.name


class OsRelease(sqlobject.SQLObject):
  "Short name: SunOS5.9, long name: Solaris 9"
  short_name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)
  full_name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

  def __unicode__(self):
    return u"OS release: %s" % self.full_name


class Architecture(sqlobject.SQLObject):
  "One of: 'sparc', 'x86'."
  name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)

  def __unicode__(self):
    return u"Architecture: %s" % self.name


class Maintainer(sqlobject.SQLObject):
  """The maintainer of the package, identified by the e-mail address."""
  email = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  full_name = sqlobject.UnicodeCol(length=255, default=None)
  # TODO: Add more fields: status (active/retired/unregistered)
  # There are some emails that are just errors, it would be good to
  # distinguish emails that once were velid @opencsw.org addresses from pure
  # bugs, e.g. "someone@opencsw.or".

  def ObfuscatedEmail(self):
    if self.email:
      email = self.email.split("@")
    else:
      email = ["unknown"]
    if len(email) == 2:
      username, domain = email
      if len(domain) > 4:
        domain = domain[:4] + u'\u2026'
    else:
      username, domain = email[0], "no domain"
    return u'\u24b6'.join((username, domain))

  def __unicode__(self):
    return u"%s <%s>" % (
        self.full_name or "Maintainer full name unknown",
        self.ObfuscatedEmail())

  def Username(self):
    if '@' in self.email:
      return self.email.split('@')[0]
    else:
      return unicode(self)

  def GetRestRepr(self):
    return {
        'maintainer_email': self.email,
        'maintainer_full_name': self.full_name,
        'maintainer_id': self.id,
    }

class Host(sqlobject.SQLObject):
  "Hostname, as returned by socket.getfqdn()"
  fqdn = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  arch = sqlobject.ForeignKey('Architecture', notNone=True)


class CswConfig(sqlobject.SQLObject):
  option_key = sqlobject.UnicodeCol(length=255, unique=True)
  float_value = sqlobject.FloatCol(default=None)
  int_value = sqlobject.IntCol(default=None)
  str_value = sqlobject.UnicodeCol(default=None, length=250)


class Pkginst(sqlobject.SQLObject):
  pkgname = sqlobject.UnicodeCol(length=250, unique=True, notNone=True)
  catalogname = sqlobject.UnicodeCol(default=None, length=250)
  pkg_desc = sqlobject.UnicodeCol(default=None, length=250)
  srv4_files = sqlobject.MultipleJoin('Srv4FileStats')


class CswFile(sqlobject.SQLObject):
  """Represents a file in a catalog.

  There can be multiple files with the same basename and the same path,
  belonging to different packages.

  This class needs to also contain files from the operating system,
  coming from SUNW packages, for which we don't have the original srv4
  files.  (Even if we could, they are generally not accessible.)  They
  need to be specific to Solaris release and architecture, so we need
  a way to link CswFile with a specific catalog.

  Fake registered Srv4FileStats object would do, but we would have to
  ensure that they can't be associated with a catalog.  Also, we'd have
  to generate fake md5 sums for them.
  """
  class sqlmeta:
    # MySQL uses case-insensitive collation by default, which doesn't make sense
    # for file names. If the utf8_bin (or other case sensitive) collation is not
    # used, it reports e.g. Zcat and zcat as a file collision, while it really
    # isn't one.
    createSQL = {
        'mysql' : [
        'ALTER TABLE csw_file CONVERT TO CHARACTER SET utf8 '
        'COLLATE utf8_bin']
    }
  basename = sqlobject.UnicodeCol(length=255, notNone=True)
  path = sqlobject.UnicodeCol(notNone=True, length=900)
  line = sqlobject.UnicodeCol(notNone=True, length=900)
  # Symlinks don't have permissions on their own
  perm_user = sqlobject.UnicodeCol(notNone=False, length=255)
  perm_group = sqlobject.UnicodeCol(notNone=False, length=255)
  perm_mode = sqlobject.UnicodeCol(notNone=False, length=5)
  target = sqlobject.UnicodeCol(notNone=False, length=900)
  mimetype = sqlobject.UnicodeCol(notNone=False, length=255)
  machine = sqlobject.UnicodeCol(notNone=False, length=255)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  srv4_file = sqlobject.ForeignKey('Srv4FileStats')
  basename_idx = sqlobject.DatabaseIndex('basename')
  path_idx = sqlobject.DatabaseIndex('path')

  def FullPath(self):
    return os.path.join(self.path, self.basename)

  def __unicode__(self):
    return u"%s %s %s %s %s" % (self.perm_user, self.perm_group, self.perm_mode,
                                self.FullPath(), self.mimetype)


# Storing binary blobs. Caching is disabled for these blobs, because they tend
# to be large and we don't want them to stick around in the cache.
class Srv4FileStatsBlob(sqlobject.SQLObject):
  """Holds serialized data structures in JSON.

  This table holds potentially large amounts of data (>1MB per row),
  and is separated to make Srv4FileStats lighter.  Sometimes, we don't
  need to retrieve the heavy pickled data if we want to read just a few
  text fields.
  """
  class sqlmeta:
    cacheValues = False
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True, length=32)
  json = sqlobject.BLOBCol(notNone=True, length=(2**24))
  content_md5_sum = sqlobject.UnicodeCol(notNone=True, unique=False, length=32)
  mime_type = sqlobject.UnicodeCol(notNone=True, length=250)
  created_on = sqlobject.DateTimeCol(
      notNone=True,
      default=sqlobject.DateTimeCol.now)


class CatalogGenData(sqlobject.SQLObject):
  """Fields required to generate the catalog.

  Having this smaller table lets us avoid fetching the main big data
  structure.
  """
  deps = sqlobject.BLOBCol(notNone=True, length=(2 ** 14 - 1))
  i_deps = sqlobject.BLOBCol(notNone=True, length=(2 ** 14 - 1))
  pkginfo_name = sqlobject.BLOBCol(notNone=True, length=(2 ** 14 - 1))
  pkgname = sqlobject.UnicodeCol(default=None, length=250)
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True, length=32)


class ElfdumpInfoBlob(sqlobject.SQLObject):
  """Holds JSON with elfdump information for a package.

  Indexed by the md5 sum of the binary.
  """
  class sqlmeta:
    cacheValues = False
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True, length=32)
  json = sqlobject.BLOBCol(notNone=True, length=(2**24 - 1))
  content_md5_sum = sqlobject.UnicodeCol(notNone=True, unique=False, length=32)
  mime_type = sqlobject.UnicodeCol(notNone=True, length=250)


class Srv4FileStats(sqlobject.SQLObject):
  """Represents a srv4 file.

  It focuses on the stats, but it can as well represent just a srv4 file.
  """
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  basename = sqlobject.UnicodeCol(notNone=True, length=250)
  catalogname = sqlobject.UnicodeCol(notNone=True, length=250)
  filename_arch = sqlobject.ForeignKey('Architecture', notNone=True)
  maintainer = sqlobject.ForeignKey('Maintainer', notNone=False)
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True, length=32)
  size = sqlobject.IntCol()
  mtime = sqlobject.DateTimeCol(notNone=False)
  os_rel = sqlobject.ForeignKey('OsRelease', notNone=True)
  osrel_str = sqlobject.UnicodeCol(notNone=True, length=9) # "SunOS5.10"
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  pkginst_str = sqlobject.UnicodeCol(notNone=True, length=255)
  registered_level_one = sqlobject.BoolCol(notNone=True)
  registered_level_two = sqlobject.BoolCol(notNone=True)
  use_to_generate_catalogs = sqlobject.BoolCol(notNone=True)
  rev = sqlobject.UnicodeCol(notNone=False, length=250)
  stats_version = sqlobject.IntCol(notNone=True)
  version_string = sqlobject.UnicodeCol(notNone=True, length=250)
  bundle = sqlobject.UnicodeCol(length=250)
  in_catalogs = sqlobject.MultipleJoin(
          'Srv4FileInCatalog',
          joinColumn='srv4file_id')
  files = sqlobject.MultipleJoin('CswFile',
          joinColumn='id')
  catalog_idx = sqlobject.DatabaseIndex('catalogname')
  basename_idx = sqlobject.DatabaseIndex('basename')
  pkginst_idx = sqlobject.DatabaseIndex('pkginst')

  def __init__(self, *args, **kwargs):
    super(Srv4FileStats, self).__init__(*args, **kwargs)

  def __unicode__(self):
    return u'%s/%s, %s' % (self.pkginst.pkgname, self.catalogname, self.md5_sum)

  def __str__(self):
    return str(unicode(self))

  def DeleteAllDependentObjects(self):
    self.RemoveCatalogAssignments()
    self.RemoveAllCswFiles()
    self.RemoveAllCheckpkgResults()
    self.RemoveOverrides()
    self.RemoveDepends()
    self.RemoveIncompatibles()

  def RemoveAllCswFiles(self):
    # Removing existing files, using sqlbuilder to use sql-level
    # mechanisms without interacting with Python.
    # http://www.mail-archive.com/sqlobject-discuss@lists.sourceforge.net/msg00520.html
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CswFile.sqlmeta.table,
          CswFile.q.srv4_file==self)))

  def RemoveDepends(self):
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          Srv4DependsOn.sqlmeta.table,
          Srv4DependsOn.q.srv4_file==self)))

  def RemoveIncompatibles(self):
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          Srv4IncompatibleWith.sqlmeta.table,
          Srv4IncompatibleWith.q.srv4_file==self)))

  def RemoveCatalogAssignments(self):
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          Srv4FileInCatalog.sqlmeta.table,
          Srv4FileInCatalog.q.srv4file==self)))

  def GetOverridesResult(self):
    return CheckpkgOverride.select(CheckpkgOverride.q.srv4_file==self)

  def GetErrorTagsResult(self, os_rel, arch, catrel):
    assert arch.name != 'all', ("Asked for the 'all' architecture, this is not valid "
                                "for GetErrorTagsResult().")
    return CheckpkgErrorTag.select(
        sqlobject.AND(
            CheckpkgErrorTag.q.srv4_file==self,
            CheckpkgErrorTag.q.os_rel==os_rel,
            CheckpkgErrorTag.q.arch==arch,
            CheckpkgErrorTag.q.catrel==catrel))

  def RemoveCheckpkgResults(self, os_rel, arch, catrel):
    logger.debug("%s: RemoveCheckpkgResults(%s, %s, %s)",
                  self, os_rel, arch, catrel)
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CheckpkgErrorTag.sqlmeta.table,
          sqlobject.AND(
            CheckpkgErrorTag.q.srv4_file==self,
            CheckpkgErrorTag.q.os_rel==os_rel,
            CheckpkgErrorTag.q.arch==arch,
            CheckpkgErrorTag.q.catrel==catrel))))

  def RemoveAllCheckpkgResults(self):
    logger.debug("%s: RemoveAllCheckpkgResults()", self)
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CheckpkgErrorTag.sqlmeta.table,
          CheckpkgErrorTag.q.srv4_file==self)))

  def RemoveOverrides(self):
    logger.debug("%s: RemoveOverrides()", self)
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CheckpkgOverride.sqlmeta.table,
          CheckpkgOverride.q.srv4_file==self)))

  def GetUnicodeOrNone(self, s):
    """Tries to decode UTF-8.

    If the object does not decode as UTF-8, it's forced to do so, while
    ignoring any potential errors.

    Returns: a unicode object or a None type.
    """
    if s is None:
      return None
    if type(s) != unicode:
      try:
        s = unicode(s, 'utf-8')
      except UnicodeDecodeError, e:
        s = s.decode("utf-8", "ignore")
        s = s + u" (bad unicode detected)"
    return s

  def GetStatsStruct(self):
    pkg_stats_sqo = Srv4FileStatsBlob.selectBy(
        md5_sum=self.md5_sum).getOne()
    return cjson.decode(pkg_stats_sqo.json)

  def _GetBuildSource(self):
    data = self.GetStatsStruct()
    build_src = None
    if "OPENCSW_REPOSITORY" in data["pkginfo"]:
      build_src = data["pkginfo"]["OPENCSW_REPOSITORY"]
    return build_src

  def GetSvnUrl(self):
    build_src = self._GetBuildSource()
    svn_url = None
    if build_src:
      svn_url = re.sub(r'([^@]*).*', r'\1/Makefile', build_src)
    return svn_url

  def GetTracUrl(self):
    build_src = self._GetBuildSource()
    trac_url = None
    if build_src:
      trac_url = re.sub(
            r'https://gar.svn.(sf|sourceforge).net/svnroot/gar/([^@]+)@(.*)',
            r'http://sourceforge.net/apps/trac/gar/browser/\2/Makefile?rev=\3',
            build_src)
    return trac_url

  def GetVendorUrl(self):
    data = self.GetStatsStruct()
    vendor_url = None
    if "VENDOR" in data["pkginfo"]:
      vendor_url = re.split(r"\s+", data["pkginfo"]["VENDOR"])[0]
    return vendor_url

  def GetRestRepr(self, quick=False):
    mimetype = "application/x-vnd.opencsw.pkg;type=srv4-detail"
    # Slow subqueries, could be solved by caching in the db schema:
    #  - self.pkginst.pkgname
    #  - self.maintainer.full_name
    #  - self.maintainer_email
    #  - self.maintainer_id
    #  - GetVendorUrl unpickles the object (very slow)
    #  - GetSvnUrl unpickles the object (very slow)
    data = {
        'basename': self.basename,
        # For compatibility with the catalog parser from catalog.py
        'file_basename': self.basename,
        'catalogname': self.catalogname,
        'md5_sum': self.md5_sum,
        'mtime': SanitizeDatetime(self.mtime),
        'rev': self.rev,
        'size': self.size,
        'version_string': self.version_string,
        # For compatibility with the catalog parser from catalog.py
        'version': self.version_string,
        'osrel': self.osrel_str,
        'pkgname': self.pkginst_str,
    }
    if not quick:
      # These data are used by the package database integration
      data['arch'] = self.arch.name
      data['filename_arch'] = self.filename_arch.name
      data['maintainer_email'] = self.maintainer.email
      data['maintainer_full_name'] = self.maintainer.full_name
      data['maintainer_id'] = self.maintainer.id
      data['vendor_url'] = self.GetVendorUrl()
      data['repository_url'] = self.GetSvnUrl()
    return mimetype, data


class CheckpkgErrorTagMixin(object):

  def ToGarSyntax(self):
    """Presents the error tag using GAR syntax."""
    msg_lines = []
    if self.tag_info:
      tag_postfix = "|%s" % self.tag_info.replace(" ", "|")
    else:
      tag_postfix = ""
    msg_lines.append(u"CHECKPKG_OVERRIDES_%s += %s%s"
                     % (self.pkgname, self.tag_name, tag_postfix))
    return "\n".join(msg_lines)

  def __eq__(self, other):
    value = (
        self.pkgname == other.pkgname
          and
        self.tag_name == other.tag_name
          and
        self.tag_info == other.tag_info)
    return value


class CheckpkgErrorTag(CheckpkgErrorTagMixin, sqlobject.SQLObject):
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkgname = sqlobject.UnicodeCol(default=None, length=250)
  tag_name = sqlobject.UnicodeCol(notNone=True, length=250)
  tag_info = sqlobject.UnicodeCol(default=None, length=250)
  msg = sqlobject.UnicodeCol(default=None, length=250)
  # To cache results from checkpkg
  overridden = sqlobject.BoolCol(default=False)
  # The same package might have different sets of errors for different
  # catalogs or Solaris releases.
  os_rel = sqlobject.ForeignKey('OsRelease', notNone=True)
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  catrel = sqlobject.ForeignKey('CatalogRelease', notNone=True)

  def __unicode__(self):
    return (u"CheckpkgErrorTag: %s %s %s"
            % (self.pkgname, self.tag_name, self.tag_info))


class CheckpkgOverride(sqlobject.SQLObject):
  # Overrides don't need to contain catalog parameters.
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkgname = sqlobject.UnicodeCol(default=None, length=250)
  tag_name = sqlobject.UnicodeCol(notNone=True, length=250)
  tag_info = sqlobject.UnicodeCol(default=None, length=250)

  def __unicode__(self):
    return (u"Override: %s: %s %s" %
            (self.pkgname,
             self.tag_name,
             self.tag_info or ""))

  def DoesApply(self, tag):
    """Figures out if this override applies to the given tag."""
    basket_a = {}
    basket_b = {}
    if self.pkgname:
      basket_a["pkgname"] = self.pkgname
      basket_b["pkgname"] = tag.pkgname
    if self.tag_info:
      basket_a["tag_info"] = self.tag_info
      basket_b["tag_info"] = tag.tag_info
    basket_a["tag_name"] = self.tag_name
    basket_b["tag_name"] = tag.tag_name
    return basket_a == basket_b


class Srv4FileInCatalog(sqlobject.SQLObject):
  """Assignment of a particular srv4 file to a specific catalog.

  There could be one more layer, to which arch and osrel could be moved.
  But for now, it's going to be a not-normalized structure.
  """
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  osrel = sqlobject.ForeignKey('OsRelease', notNone=True)
  catrel = sqlobject.ForeignKey('CatalogRelease', notNone=True)
  srv4file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  created_on = sqlobject.DateTimeCol(
      notNone=True,
      default=sqlobject.DateTimeCol.now)
  created_by = sqlobject.UnicodeCol(length=50, notNone=True)
  uniqueness_idx = sqlobject.DatabaseIndex(
          'arch', 'osrel', 'catrel', 'srv4file',
          unique=True)

  def __unicode__(self):
    return (u"%s is in catalog %s %s %s"
            % (self.srv4file,
               self.arch.name, self.osrel.full_name, self.catrel.name))


class Srv4DependsOn(sqlobject.SQLObject):
  """Models dependencies."""
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  dep_uniq_idx = sqlobject.DatabaseIndex('srv4_file', 'pkginst')


class Srv4IncompatibleWith(sqlobject.SQLObject):
  """Models dependencies."""
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  dep_uniq_idx = sqlobject.DatabaseIndex('srv4_file', 'pkginst')


def GetCatPackagesResult(sqo_osrel, sqo_arch, sqo_catrel):
  join = [
      sqlbuilder.INNERJOINOn(None,
        Srv4FileInCatalog,
        Srv4FileInCatalog.q.srv4file==Srv4FileStats.q.id),
  ]
  res = Srv4FileStats.select(
      sqlobject.AND(
        Srv4FileInCatalog.q.osrel==sqo_osrel,
        Srv4FileInCatalog.q.arch==sqo_arch,
        Srv4FileInCatalog.q.catrel==sqo_catrel,
        Srv4FileStats.q.use_to_generate_catalogs==True,
      ),
      join=join,
  ).orderBy('catalogname')
  return res


def GetCatalogGenerationResult(sqo_osrel, sqo_arch, sqo_catrel):
  """Get rows with catalog results.

  CatalogEntry
  catalogname version pkgname basename md5_sum size deps category i_deps
  """
  join = [
      sqlbuilder.INNERJOINOn(None,
        Srv4FileInCatalog,
        Srv4FileInCatalog.q.srv4file==Srv4FileStats.q.id),
      sqlbuilder.INNERJOINOn(None,
        CatalogGenData,
        Srv4FileStats.q.md5_sum==CatalogGenData.q.md5_sum),
      sqlbuilder.INNERJOINOn(None,
        Maintainer,
        Srv4FileStats.q.maintainer==Maintainer.q.id),
  ]
  where = sqlbuilder.AND(
      Srv4FileInCatalog.q.osrel==sqo_osrel,
        Srv4FileInCatalog.q.arch==sqo_arch,
        Srv4FileInCatalog.q.catrel==sqo_catrel,
        Srv4FileStats.q.use_to_generate_catalogs==True,
  )
  select = sqlbuilder.Select(
      ['catalogname',    # 0
       'version_string', # 1
       'pkgname',        # 2
       'basename',       # 3
       'srv4_file_stats.md5_sum', # Hardcoded table name, is it portable?
       'size',           # 5
       'deps',           # 6
       'i_deps',         # 7
       'pkginfo_name',   # 8
       # The above columns are used to generate catalogs.
       # Additional columns can be added blow.
       # 'maintainer.id',  # 9
       'maintainer.email',  # 9
       'mtime',          # 10
       'created_on',     # 11
       'created_by',     # 12
      ],
      where=where,
      orderBy='catalogname',
      join=join)
  query = sqlobject.sqlhub.processConnection.sqlrepr(select)
  rows = sqlobject.sqlhub.processConnection.queryAll(query)
  return rows


def GetRecentlyBuiltPackages():
  join = [
      # sqlbuilder.INNERJOINOn(None,
      #   Srv4FileInCatalog,
      #   Srv4FileInCatalog.q.srv4file==Srv4FileStats.q.id),
      # sqlbuilder.INNERJOINOn(None,
      #   CatalogGenData,
      #   Srv4FileStats.q.md5_sum==CatalogGenData.q.md5_sum),
  ]
  where = sqlbuilder.AND(
        # Srv4FileStats.q.use_to_generate_catalogs==True,
  )
  select = sqlbuilder.Select(
      [
       'srv4_file_stats.md5_sum', # Hardcoded table name, is it portable?
       'srv4_file_stats.catalogname',
       # 'version_string',
       # 'pkgname',
       # 'basename',
       # 'size',
       # 'deps',
       # 'i_deps',
       # 'pkginfo_name',
       # The above columns are used to generate catalogs.
       # Additional columns can be added blow.
       'srv4_file_stats.maintainer_id',
       'srv4_file_stats.mtime',
       # 'created_on',
       # 'created_by',
       ],
      where=where,
      orderBy='-mtime',
      join=join,
      limit=30)
  query = sqlobject.sqlhub.processConnection.sqlrepr(select)
  rows = sqlobject.sqlhub.processConnection.queryAll(query)
  return rows


def GetSqoTriad(osrel, arch, catrel):
  sqo_osrel = OsRelease.selectBy(short_name=osrel).getOne()
  sqo_arch = Architecture.selectBy(name=arch).getOne()
  sqo_catrel = CatalogRelease.selectBy(name=catrel).getOne()
  return sqo_osrel, sqo_arch, sqo_catrel
