# $Id$
#
# Defines models for package database.

import logging
import sqlobject
import os.path
from sqlobject import sqlbuilder
import cPickle

class DataSource(sqlobject.SQLObject):
  """Represents: a /var/sadm/install/contents file, or CSW catalog.

  - "filesystem"
  - "catalog"
  """
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class CatalogReleaseType(sqlobject.SQLObject):
  "Unstable, testing, stable."
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class CatalogRelease(sqlobject.SQLObject):
  "Release names: potato, etc."
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  type = sqlobject.ForeignKey('CatalogReleaseType', notNone=True)

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

  def ObfuscatedEmail(self):
    username, domain = self.email.split("@")
    username = username[:-3] + "..."
    return "@".join((username, domain))

  def __unicode__(self):
    return u"%s <%s>" % (
        self.full_name or "Maintainer full name unknown",
        self.ObfuscatedEmail())

class Host(sqlobject.SQLObject):
  "Hostname, as returned by socket.getfqdn()"
  fqdn = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  arch = sqlobject.ForeignKey('Architecture', notNone=True)

class CswConfig(sqlobject.SQLObject):
  option_key = sqlobject.UnicodeCol(length=255, unique=True)
  float_value = sqlobject.FloatCol(default=None)
  int_value = sqlobject.IntCol(default=None)
  str_value = sqlobject.UnicodeCol(default=None)

class Pkginst(sqlobject.SQLObject):
  pkgname = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  catalogname = sqlobject.UnicodeCol(default=None)
  pkg_desc = sqlobject.UnicodeCol(default=None)
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
  basename = sqlobject.UnicodeCol(length=255, notNone=True)
  path = sqlobject.UnicodeCol(notNone=True, length=900)
  line = sqlobject.UnicodeCol(notNone=True, length=900)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  srv4_file = sqlobject.ForeignKey('Srv4FileStats')
  basename_idx = sqlobject.DatabaseIndex('basename')

  def __unicode__(self):
    return u"File: %s" % os.path.join(self.path, self.basename)

class Srv4FileStatsBlob(sqlobject.SQLObject):
  """Holds pickled data structures.

  This table holds potentially large amounts of data (>1MB per row),
  and is separated to make Srv4FileStats lighter.  Sometimes, we don't
  need to retrieve the heavy pickled data if we want to read just a few
  text fields.
  """
  pickle = sqlobject.BLOBCol(notNone=True, length=(2**24))
  srv4_file = sqlobject.SingleJoin('Srv4FileStats')


class Srv4FileStats(sqlobject.SQLObject):
  """Represents a srv4 file.

  It focuses on the stats, but it can as well represent just a srv4 file.
  """
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  basename = sqlobject.UnicodeCol(notNone=True)
  catalogname = sqlobject.UnicodeCol(notNone=True)
  # The data structure can be missing - necessary for fake SUNW
  # packages.
  data_obj = sqlobject.ForeignKey('Srv4FileStatsBlob', notNone=False)
  filename_arch = sqlobject.ForeignKey('Architecture', notNone=True)
  latest = sqlobject.BoolCol(notNone=True)
  maintainer = sqlobject.ForeignKey('Maintainer', notNone=False)
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True, length=32)
  size = sqlobject.IntCol()
  mtime = sqlobject.DateTimeCol(notNone=False)
  os_rel = sqlobject.ForeignKey('OsRelease', notNone=True)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  registered = sqlobject.BoolCol(notNone=True)
  use_to_generate_catalogs = sqlobject.BoolCol(notNone=True)
  rev = sqlobject.UnicodeCol(notNone=False)
  stats_version = sqlobject.IntCol(notNone=True)
  version_string = sqlobject.UnicodeCol(notNone=True)
  in_catalogs = sqlobject.MultipleJoin(
          'Srv4FileInCatalog',
          joinColumn='srv4file_id')
  files = sqlobject.MultipleJoin('CswFile',
          joinColumn='id')

  def DeleteAllDependentObjects(self):
    data_obj = self.data_obj
    self.data_obj = None
    if data_obj:
      # It could be already missing
      data_obj.destroySelf()
    self.RemoveAllCswFiles()
    self.RemoveAllCheckpkgResults()
    self.RemoveOverrides()

  def RemoveAllCswFiles(self):
    # Removing existing files, using sqlbuilder to use sql-level
    # mechanisms without interacting with Python.
    # http://www.mail-archive.com/sqlobject-discuss@lists.sourceforge.net/msg00520.html
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CswFile.sqlmeta.table,
          CswFile.q.srv4_file==self)))

  def GetOverridesResult(self):
    return CheckpkgOverride.select(CheckpkgOverride.q.srv4_file==self)

  def GetErrorTagsResult(self, os_rel, arch, catrel):
    return CheckpkgErrorTag.select(
        sqlobject.AND(
            CheckpkgErrorTag.q.srv4_file==self,
            CheckpkgErrorTag.q.os_rel==os_rel,
            CheckpkgErrorTag.q.arch==arch,
            CheckpkgErrorTag.q.catrel==catrel))

  def RemoveCheckpkgResults(self, os_rel, arch, catrel):
    logging.debug("%s: RemoveCheckpkgResults(%s, %s, %s)",
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
    logging.debug("%s: RemoveAllCheckpkgResults()", self)
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CheckpkgErrorTag.sqlmeta.table,
          CheckpkgErrorTag.q.srv4_file==self)))

  def RemoveOverrides(self):
    logging.debug("%s: RemoveOverrides()", self)
    sqlobject.sqlhub.processConnection.query(
        sqlobject.sqlhub.processConnection.sqlrepr(sqlbuilder.Delete(
          CheckpkgOverride.sqlmeta.table,
          CheckpkgOverride.q.srv4_file==self)))

  def __unicode__(self):
    return (
        u"Package: %s-%s, %s"
        % (self.catalogname, self.version_string, self.arch.name))

  def GetStatsStruct(self):
    return cPickle.loads(str(self.data_obj.pickle))


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
  pkgname = sqlobject.UnicodeCol(default=None)
  tag_name = sqlobject.UnicodeCol(notNone=True)
  tag_info = sqlobject.UnicodeCol(default=None)
  msg = sqlobject.UnicodeCol(default=None)
  # To cache results from checkpkg
  overridden = sqlobject.BoolCol(default=False)
  # The same package might have different sets of errors for different
  # catalogs or Solaris releases.
  os_rel = sqlobject.ForeignKey('OsRelease', notNone=True)
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  catrel = sqlobject.ForeignKey('CatalogRelease', notNone=True)

  def __unicode__(self):
    return u"Error: %s %s %s" % (self.pkgname, self.tag_name, self.tag_info)


class CheckpkgOverride(sqlobject.SQLObject):
  # Overrides don't need to contain catalog parameters.
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkgname = sqlobject.UnicodeCol(default=None)
  tag_name = sqlobject.UnicodeCol(notNone=True)
  tag_info = sqlobject.UnicodeCol(default=None)

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
  uniqueness_idx = sqlobject.DatabaseIndex(
          'arch', 'osrel', 'catrel', 'srv4file',
          unique=True)

  def __unicode__(self):
    return (
        u"%s is in catalog %s %s %s"
        % (self.srv4file,
           self.arch.name,
           self.osrel.full_name,
           self.catrel.name))


class Srv4DependsOn(sqlobject.SQLObject):
  """Models dependencies."""
  srv4_file = sqlobject.ForeignKey('Srv4FileStats', notNone=True)
  pkginst = sqlobject.ForeignKey('Pkginst', notNone=True)
  dep_uniq_idx = sqlobject.DatabaseIndex(
      'srv4_file', 'pkginst')
