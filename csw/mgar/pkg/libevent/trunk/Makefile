NAME = libevent
VERSION = 1.4.14b
CATEGORIES = lib

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://www.monkey.org/~provos/
DISTNAME = $(NAME)-$(VERSION)-stable
DISTFILES = $(DISTNAME).tar.gz

# From http://www.monkey.org/~provos/libevent/LICENSE
DISTFILES += LICENSE
LICENSE = LICENSE

PACKAGES += CSWlibevent1-4-2
SPKG_DESC_CSWlibevent1-4-2 = Event notification library, libevent-1.4.so.2
PKGFILES_CSWlibevent1-4-2 = $(PKGFILES_RT)
OBSOLETED_BY_CSWlibevent1-4-2 += CSWlibevent

# This is a unified lib package
CHECKPKG_OVERRIDES_CSWlibevent1-4-2 += shared-lib-pkgname-mismatch

VENDOR_URL = http://www.monkey.org/~provos/libevent/

BUILD64 = 1

TEST_TARGET = verify

include gar/category.mk

# For "make" to be GNU make
PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
