# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Zipper
VERSION = 1.5
GARTYPE = v2

DESCRIPTION = GNUstep graphical archive tool (zip, tar, ...)
define BLURB
  GNUstep tool to inspect and extract  various archives by wrapping existing shell tools (tar, zip, lha...) and create archives through Services from the Workspace.
endef

MASTER_SITES = http://savannah.nongnu.org/download/gap/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWZipper += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWZipper += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWZipper += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWZipper += CSWgnustep-back
RUNTIME_DEP_PKGS_CSWZipper += CSWgtar
RUNTIME_DEP_PKGS_CSWZipper += SUNWzip


#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

# now special targets for build and install so that we can source
# GNUstep.sh before
# configure is skipped
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = 
SKIPTEST ?= 1

include gar/category.mk

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
