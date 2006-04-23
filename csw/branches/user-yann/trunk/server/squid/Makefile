GARNAME = squid
GARVERSION = 2.5.STABLE5
CATEGORIES = server

SPKG_PKGNAME = CSWsquid
SPKG_BITNAME = squid

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and Windows platforms.
endef

MASTER_SITES = http://www.squid-cache.org/Versions/v2/2.5/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --enable-removal-policies="heap lru"
CONFIGURE_ARGS += --enable-cache-digests
CONFIGURE_ARGS += --enable-dlmalloc
CONFIGURE_ARGS += --enable-underscores
CONFIGURE_ARGS += --disable-internal-dns

TEST_TARGET = check

include ../category.mk
