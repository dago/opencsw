# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-back
VERSION = 0.24.0
GARTYPE = v2

DESCRIPTION = GNUstep-core back
define BLURB
  GNUstep-core, backend dependent part of GNUstep AppKit.
endef

#EXTRA_MODULATORS = GRAPHICS
#MODULATIONS_graphics = xlib cairo

BUILD_DEP_PKGS = SUNWxorg-headers CSWgmake CSWgcc4objc CSWlibfreetype-dev
DEP_PKGS = CSWgnustep-make CSWgnustep-base CSWgnustep-gui CSWlibfreetype6

BUILD_DEP_PKGS += CSWlibcairo-dev
DEP_PKGS += CSWlibcairo2
#DEP_PKGS_GRAPHICS_cairo += CSWlibcairo2

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

#CONFIGURE_ARGS_GRAPHICS_xlib += --enable-graphics=xlib
#CONFIGURE_ARGS_GRAPHICS_cairo += --enable-graphics=cairo
CONFIGURE_ARGS +== $(DIRPATHS) --enable-graphics=cairo

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
