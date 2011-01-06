NAME = libevent
VERSION = 2.0.10
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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-stable.tar.gz

PACKAGES += CSWlibevent2-0-5
CATALOGNAME_CSWlibevent2-0-5 = libevent2_0_5
SPKG_DESC_CSWlibevent2-0-5 = Event notification library 2.0, libevent*-2.0.so.5
RUNTIME_DEP_PKGS_CSWlibevent2-0-5 += CSWosslrt


PACKAGES += CSWlibevent-devel
CATALOGNAME_CSWlibevent-devel = libevent_devel
SPKG_DESC_CSWlibevent-devel = Development files for libevent 2.0
RUNTIME_DEP_PKGS_CSWlibevent-devel += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWlibevent-devel += CSWpython

VENDOR_URL = http://www.monkey.org/~provos/libevent/
LICENSE = LICENSE

# We don't need it and if defined the test breaks
NOISALIST = 1
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS  = $(DIRPATHS) 

TEST_TARGET = verify

PKGFILES_CSWlibevent2-0-5 = $(PKGFILES_RT)

# These will go away after package release as the files have been moved from CSWlibevent to *-devel
CHECKPKG_OVERRIDES_CSWlibevent-devel += file-collision

# The package name guessing has a bug, overwrite for now.
CHECKPKG_OVERRIDES_CSWlibevent2-0-5 += shared-lib-pkgname-mismatch

include gar/category.mk

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
