NAME = BerkeleyDB
VERSION = 0.43
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PMQS

DESCRIPTION = BerkeleyDB module
define BLURB
  Includes BerkeleyDB, BerkeleyDB::Btree, BerkeleyDB::Hash
endef

DISTFILES = COPYING

PACKAGES = CSWpmberkeleydb
CATALOGNAME = pm_berkeleydb

PATCHFILES = CSWpmberkeleydb.config.in.diff

NOISALIST = 1
EXTRA_LIB = /opt/csw/bdb48/lib

RUNTIME_DEP_PKGS = CSWbdb48

include gar/category.mk
