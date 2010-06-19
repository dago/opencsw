GARNAME = apr-util
GARVERSION = 1.3.9
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWapr CSWiconv CSWsqlite3rt CSWunixodbc CSWexpat
#RUNTIME_DEP_PKGS += CSWbdb48

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
#not yet
#CONFIGURE_ARGS += --with-berkeley-db=$(prefix)/bdb48
CONFIGURE_ARGS += --without-freetds --without-sqlite2

BUILD64 = 1
STRIP_LIBTOOL = 1

CHECKPKG_OVERRIDES_CSWapr-util += pkginfo-bad-catalogname|apr-util
CHECKPKG_OVERRIDES_CSWapr-util += rev-tag-missing-in-filename
CHECKPKG_OVERRIDES_CSWapr-util += osrel-tag-not-specified
CHECKPKG_OVERRIDES_CSWapr-util += filename-version-does-not-match-pkginfo-version|filename=util|pkginfo=1.3.9,REV=2010.06.19

include gar/category.mk
