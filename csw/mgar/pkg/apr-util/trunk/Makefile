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

RUNTIME_DEP_PKGS = CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config

BUILD64 = 1
STRIP_LIBTOOL = 1

include gar/category.mk
