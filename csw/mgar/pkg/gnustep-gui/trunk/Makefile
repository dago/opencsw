# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-gui
VERSION = 0.24.0
GARTYPE = v2

DESCRIPTION = GNUstep-core gui
define BLURB
  GNUstep-core gui framework, which provides all AppKit classes except the backend dependent. Necessary for all graphical and application-oriented development.
endef

BUILD_DEP_PKGS = CSWgmake CSWgcc4objc
DEP_PKGS = CSWgnustep-make CSWgnustep-base

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

# now special targets for configure, build and install so that we can source
# GNUstep.sh before
CONFIGURE_SCRIPTS = sourcegs
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = none
SKIPTEST = 1


CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

configure-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
