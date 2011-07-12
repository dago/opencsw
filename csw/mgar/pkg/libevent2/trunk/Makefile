NAME = libevent
VERSION = 2.0.12
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
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.monkey.org/~provos/libevent/
LICENSE = LICENSE

BUILD_DEP_PKGS += CSWossldevel

PACKAGES += CSWlibevent2-0-5
SPKG_DESC_CSWlibevent2-0-5 = Event notification library 2.0, libevent*-2.0.so.5
PKGFILES_CSWlibevent2-0-5 = $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWlibevent2-0-5 += CSWosslrt

PACKAGES += CSWlibevent-dev
SPKG_DESC_CSWlibevent-dev = Development files for libevent*-2.0.so.5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWpython
OBSOLETED_BY_CSWlibevent-dev += CSWlibevent-devel

# We don't need it and if defined the test breaks
NOISALIST = 1
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

# Pass incudes via CFLAGS until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=3361614&group_id=50884&atid=461322
CPPFLAGS =
EXTRA_CFLAGS += $(INCLUDE_FLAGS)

BUILD64 = 1

TEST_TARGET = verify

# This is a unified package with all libraries in there
CHECKPKG_OVERRIDES_CSWlibevent2-0-5 += shared-lib-pkgname-mismatch

include gar/category.mk

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
