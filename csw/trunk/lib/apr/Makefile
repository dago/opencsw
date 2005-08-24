GARNAME = apr
GARVERSION = 1.0.0
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.gnusoft.net/apr/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads --enable-other-child

# APR Tests are very time consuming...
ENABLE_TEST = 0

include ../category.mk
