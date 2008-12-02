GARNAME = memcached
GARVERSION = 1.2.2
CATEGORIES = net

DESCRIPTION = distributed memory object caching system
define BLURB
  memcached is a high-performance, distributed memory object caching system,
  generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load.
endef

MASTER_SITES = http://www.danga.com/memcached/dist/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWmemcached,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

DEPENDS += lib/libevent

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dependency-tracking
CONFIGURE_ARGS += --with-libevent=$(prefix)

# No test suite
TEST_SCRIPTS =

include gar/category.mk

