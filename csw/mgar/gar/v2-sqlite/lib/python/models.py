# $Id$
#
# Defines models for package database.

import sqlobject

class DataSource(sqlobject.SQLObject):
  "Represents: a /var/sadm/install/contents file, or CSW catalog."
  name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class OsVersion(sqlobject.SQLObject):
  "Short name: 5.9, long name: Solaris 9"
  short_name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)
  full_name = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)

class Architecture(sqlobject.SQLObject):
  "One of: 'sparc', 'x86'."
  name = sqlobject.UnicodeCol(length=40, unique=True, notNone=True)

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


class CswPackage(sqlobject.SQLObject):
  pkgname = sqlobject.UnicodeCol(length=255, unique=True, notNone=True)
  catalogname = sqlobject.UnicodeCol(default=None)
  pkg_desc = sqlobject.UnicodeCol(default=None)

class CswFile(sqlobject.SQLObject):
  basename = sqlobject.UnicodeCol(length=255, notNone=True)
  path = sqlobject.UnicodeCol(notNone=True)
  line = sqlobject.UnicodeCol(notNone=True)
  basename_idx = sqlobject.DatabaseIndex('basename')
