# $Id$
#
# Defines models for package database.

import sqlobject

class DataSource(sqlobject.SQLObject):
  """Represents: a /var/sadm/install/contents file, or CSW catalog.

  - "local"
  - "catalog"
  """
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class OsRelease(sqlobject.SQLObject):
  "Short name: SunOS5.9, long name: Solaris 9"
  short_name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)
  full_name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class Architecture(sqlobject.SQLObject):
  "One of: 'sparc', 'x86'."
  name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)

class Maintainer(sqlobject.SQLObject):
  """The maintainer of the package, identified by the e-mail address."""
  email = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  full_name = sqlobject.UnicodeCol(length=255, default=None)

class Host(sqlobject.SQLObject):
  "Hostname, as returned by socket.getfqdn()"
  fqdn = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  arch = sqlobject.ForeignKey('Architecture')

class CswConfig(sqlobject.SQLObject):
  option_key = sqlobject.UnicodeCol(length=255, unique=True)
  # float_value = sqlobject.DecimalCol(size=12, precision=3, default=None)
  float_value = sqlobject.FloatCol(default=None)
  int_value = sqlobject.IntCol(default=None)
  str_value = sqlobject.UnicodeCol(default=None)

class Pkginst(sqlobject.SQLObject):
  pkgname = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  catalogname = sqlobject.UnicodeCol(default=None)
  pkg_desc = sqlobject.UnicodeCol(default=None)

class CswFile(sqlobject.SQLObject):
  basename = sqlobject.UnicodeCol(length=255, notNone=True)
  path = sqlobject.UnicodeCol(notNone=True)
  line = sqlobject.UnicodeCol(notNone=True)
  basename_idx = sqlobject.DatabaseIndex('basename')

class Srv4FileStats(sqlobject.SQLObject):
  """Represents a srv4 file."""
  md5_sum = sqlobject.UnicodeCol(notNone=True, unique=True)
  pkginst = sqlobject.ForeignKey('Pkginst')
  stats_version = sqlobject.IntCol(notNone=True)
  catalogname = sqlobject.UnicodeCol(notNone=True)
  basename = sqlobject.UnicodeCol(notNone=True)
  arch = sqlobject.ForeignKey('Architecture', notNone=True)
  os_rel = sqlobject.ForeignKey('OsRelease', notNone=True)
  maintainer = sqlobject.ForeignKey('Maintainer')
  data = sqlobject.UnicodeCol(notNone=True)
  latest = sqlobject.BoolCol(notNone=True)
  version_string = sqlobject.UnicodeCol(notNone=True)
  rev = sqlobject.UnicodeCol(notNone=False)
  mtime = sqlobject.DateTimeCol(notNone=False)

class CheckpkgOverride(sqlobject.SQLObject):
  srv4_file = sqlobject.ForeignKey('Srv4FileStats')
  pkgname = sqlobject.UnicodeCol(default=None)
  tag_name = sqlobject.UnicodeCol(notNone=True)
  tag_info = sqlobject.UnicodeCol(default=None)

class CheckpkgErrorTag(sqlobject.SQLObject):
  srv4_file = sqlobject.ForeignKey('Srv4FileStats')
  pkgname = sqlobject.UnicodeCol(default=None)
  tag_name = sqlobject.UnicodeCol(notNone=True)
  tag_info = sqlobject.UnicodeCol(default=None)
  msg = sqlobject.UnicodeCol(default=None)
