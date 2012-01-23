NAME = libevent
VERSION = 2.0.16
CATEGORIES = lib

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://github.com/downloads/libevent/libevent/
DISTNAME = $(NAME)-$(VERSION)-stable
DISTFILES += $(DISTNAME).tar.gz

# This is the same fix as reported in
#   http://sourceforge.net/tracker/?func=detail&aid=3452589&group_id=50884&atid=461322
PATCHFILES += 0001-Do-not-return-value-in-void-function.patch

VENDOR_URL = http://www.monkey.org/~provos/libevent/
LICENSE = LICENSE

BUILD_DEP_PKGS += CSWossldevel

PACKAGES += CSWlibevent2-0-5
SPKG_DESC_CSWlibevent2-0-5 = Event notification library 2.0, libevent-2.0.so.5
PKGFILES_CSWlibevent2-0-5 = $(call pkgfiles_lib,libevent-2.0.so.5)

PACKAGES += CSWlibevent-core2-0-5
SPKG_DESC_CSWlibevent-core2-0-5 = Event notification library 2.0, libevent_core-2.0.so.5
PKGFILES_CSWlibevent-core2-0-5 = $(call pkgfiles_lib,libevent_core-2.0.so.5)

PACKAGES += CSWlibevent-extra2-0-5
SPKG_DESC_CSWlibevent-extra2-0-5 = Event notification library 2.0, libevent_extra-2.0.so.5
PKGFILES_CSWlibevent-extra2-0-5 = $(call pkgfiles_lib,libevent_extra-2.0.so.5)

PACKAGES += CSWlibevent-openssl2-0-5
SPKG_DESC_CSWlibevent-openssl2-0-5 = Event notification library 2.0, libevent_openssl-2.0.so.5
PKGFILES_CSWlibevent-openssl2-0-5 = $(call pkgfiles_lib,libevent_openssl-2.0.so.5)
RUNTIME_DEP_PKGS_CSWlibevent-openssl2-0-5 += CSWosslrt

PACKAGES += CSWlibevent-pthreads2-0-5
SPKG_DESC_CSWlibevent-pthreads2-0-5 = Event notification library 2.0, libevent_pthreads-2.0.so.5
PKGFILES_CSWlibevent-pthreads2-0-5 = $(call pkgfiles_lib,libevent_pthreads-2.0.so.5)

PACKAGES += CSWlibevent-dev
SPKG_DESC_CSWlibevent-dev = Development files for libevent*-2.0.so.5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-core2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-extra2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-openssl2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-dev += CSWlibevent-pthreads2-0-5
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

BUILD64_LIBS_ONLY = 1

TEST_TARGET = verify

# This is a unified package with all libraries in there
CHECKPKG_OVERRIDES_CSWlibevent2-0-5 += shared-lib-pkgname-mismatch

include gar/category.mk

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
