# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Terminal
VERSION = 0.9.8
GARTYPE = v2

DESCRIPTION = GNUstep Terminal emulator
define BLURB
  GNUstep Terminal emulator, providing also Terminal services.
endef

MASTER_SITES = http://savannah.nongnu.org/download/gap/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWgnustep-base
BUILD_DEP_PKGS += CSWgnustep-gui
BUILD_DEP_PKGS += CSWgnustep-back

RUNTIME_DEP_PKGS_CSWTerminal += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWTerminal += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWTerminal += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWTerminal += CSWgnustep-back


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
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) &&$(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
