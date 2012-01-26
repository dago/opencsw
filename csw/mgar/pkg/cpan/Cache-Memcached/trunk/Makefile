NAME = Cache-Memcached
VERSION = 1.29
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DORMANDO

DESCRIPTION = Client library for memcached
define BLURB
	This is the Perl API for memcached, a distributed memory cache daemon. More
	information is available at: http://www.danga.com/memcached/
endef

DISTFILES += COPYING

PACKAGES = CSWpm-cache-memcached
CATALOGNAME_CSWpm-cache-memcached = pm_cache_memcached
SPKG_DESC_CSWpm-cache-memcached = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-cache-memcached = CSWpmcachememcached
CATALOGNAME_CSWpmcachememcached = pm_cachememcached

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmstringcrc32

include gar/category.mk
