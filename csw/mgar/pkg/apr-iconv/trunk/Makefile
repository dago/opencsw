NAME = apr-iconv
VERSION = 1.2.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Apache Portable Runtime Utilities
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES  = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config

BUILD64_LIBS_ONLY = 1
STRIP_LIBTOOL = 1

include gar/category.mk
