# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ProjectCenter
VERSION = 0.6.1
GARTYPE = v2

DESCRIPTION = GNUstep IDE
define BLURB
  GNUstep IDE for creating Tools and Applications with Makefile generation.
endef

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/dev-apps/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

CHECKPKG_OVERRIDES_CSWProjectCenter += CSWgnustep-make
CHECKPKG_OVERRIDES_CSWProjectCenter += CSWgnustep-base
CHECKPKG_OVERRIDES_CSWProjectCenter += CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWProjectCenter += CSWgnustep-back

PATCHFILES += 0001-solaris-fix.patch

#overrides
CHECKPKG_OVERRIDES_CSWgnustep-base += surplus-dependency|CSWgnustep-make

#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc

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
SKIPTEST = ?1

include gar/category.mk

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) &&. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
