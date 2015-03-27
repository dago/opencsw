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

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

#EXTRA_MODULATORS = GRAPHICS
#MODULATIONS_graphics = xlib cairo

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWgnustep-base
BUILD_DEP_PKGS += CSWgnustep-gui


RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibfreetype6

#for cairo:
BUILD_DEP_PKGS += CSWlibcairo-dev
#for cairo, add these. Perhaps these hould be pulled in by other packages
BUILD_DEP_PKGS += CSWfontconfig-dev
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibcairo2
#DEP_PKGS_GRAPHICS_cairo += CSWlibcairo2

#overrides
CHECKPKG_OVERRIDES_CSWgnustep-base += surplus-dependency|CSWgnustep-make

#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

# now special targets for configure, build and install so that we can source
# GNUstep.sh before
CONFIGURE_SCRIPTS = sourcegs
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = 
SKIPTEST ?= 1

CONFIGURE_ARGS = $(DIRPATHS)

#CONFIGURE_ARGS_GRAPHICS_xlib += --enable-graphics=xlib
#CONFIGURE_ARGS_GRAPHICS_cairo += --enable-graphics=cairo
CONFIGURE_ARGS += --enable-graphics=cairo $(DIRPATHS)

include gar/category.mk

configure-sourcegs:
	 $(CONFIGURE_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
