# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gorm
VERSION = 1.2.20
GARTYPE = v2

DESCRIPTION = GNUstep graphical interface builder
define BLURB
  GORM (Graphical Object Relationship Modeller) is GNUstep Interface Builder equivalent to build graphically interface files.
endef

BUILD_DEP_PKGS = CSWgmake CSWgcc4objc
DEP_PKGS = CSWgnustep-make CSWgnustep-base CSWgnustep-gui CSWgnustep-back

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/dev-apps/
DISTFILES  = $(DISTNAME).tar.gz

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
TEST_SCRIPTS = none
SKIPTEST = 1

include gar/category.mk

build-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
