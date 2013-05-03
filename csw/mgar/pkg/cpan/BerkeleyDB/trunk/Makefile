NAME = BerkeleyDB
VERSION = 0.51
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PMQS

DESCRIPTION = BerkeleyDB Module
define BLURB
  Includes BerkeleyDB, BerkeleyDB::Btree, BerkeleyDB::Hash
endef

DISTFILES = COPYING

PACKAGES = CSWpmberkeleydb
CATALOGNAME = pm_berkeleydb

PATCHFILES  = CSWpmberkeleydb.config.in.diff
PATCHFILES += 0001-scan.pl-path.patch

NOISALIST = 1
EXTRA_LIB = /opt/csw/bdb48/lib

RUNTIME_DEP_PKGS = CSWbdb48

# Catalog name correct for Perl module.
CHECKPKG_OVERRIDES_CSWpmberkeleydb += catalogname-does-not-match-pkgname|pkgname=CSWpmberkeleydb|catalogname=pm_berkeleydb|expected-catalogname=pmberkeleydb

include gar/category.mk
