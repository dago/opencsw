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

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibgif-dev

RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibpng3
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgnustep-gui += CSWlibgif4

#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc

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
	$(CONFIGURE_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
