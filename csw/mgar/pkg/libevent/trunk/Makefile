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
CATALOGNAME_CSWlibevent1-4-2 = libevent1_4_2
SPKG_DESC_CSWlibevent1-4-2 = Event notification library, libevent-1.4.so.2
PKGFILES_CSWlibevent1-4-2 = $(PKGFILES_RT)

PACKAGES += CSWlibevent
CATALOGNAME_CSWlibevent = libevent
SPKG_DESC_CSWlibevent = Legacy package as contents moved to soname-specific packages
RUNTIME_DEP_PKGS_CSWlibevent = CSWlibevent1-4-2
ARCHALL_CSWlibevent = 1
PKGFILES_CSWlibevent = NOFILES

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-stable.tar.gz

SPKG_SOURCEURL = http://www.monkey.org/~provos/libevent/

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS  = $(DIRPATHS) 

TEST_TARGET = verify

# This is a legacy dependancy
CHECKPKG_OVERRIDES_CSWlibevent += surplus-dependency|CSWlibevent1-4-2

# This is a bug in checkpkg, remove after fixing
CHECKPKG_OVERRIDES_CSWlibevent1-4-2 += shared-lib-pkgname-mismatch

include gar/category.mk

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
