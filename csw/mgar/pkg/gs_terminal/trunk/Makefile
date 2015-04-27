# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Terminal
VERSION = 0.9.8
GARTYPE = v2
PACKAGES += CSWgs-terminal

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

RUNTIME_DEP_PKGS_CSWgs-terminal += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWgnustep-back
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgs-terminal += CSWlibobjc4

#we do override because we depend on them
CHECKPKG_OVERRIDES_CSWgs-terminal += surplus-dependency|CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWgs-terminal += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWgs-terminal += surplus-dependency|CSWgnustep-back
CHECKPKG_OVERRIDES_CSWgs-terminal += surplus-dependency|CSWgnustep-make

# we don't direcly bind right now, this also means soname doesn't get found
CHECKPKG_OVERRIDES_CSWgs-terminal += no-direct-binding
CHECKPKG_OVERRIDES_CSWgs-terminal += soname-not-found

#known placement overrides since we use bundles
CHECKPKG_OVERRIDES_CSWgs-terminal += binary-architecture-does-not-match-placement


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
