GARNAME = memcached
GARVERSION = 1.1.12
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

# Pilfered code from OpenSolaris cmd/ssh/libopenbsd-compat
DISTFILES   += daemon.c daemon.h
PATCHFILES  += solaris.diff

DEPENDS += lib/libevent

CONFIGURE_ARGS  = $(DIRPATHS)

# No test suite
ENABLE_TEST = 0

include ../category.mk

post-extract:
	@for file in daemon.c daemon.h ; do \
		mv $(WORKDIR)/$$file $(WORKSRC) ; \
	done
	$(DONADA)
	@$(MAKECOOKIE)

