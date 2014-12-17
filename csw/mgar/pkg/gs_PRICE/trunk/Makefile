# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = PRICE
VERSION = 1.2.0
GARTYPE = v2

DESCRIPTION = Image viewing and filtering program
define BLURB
  Raster image viewing, manipulation, filtering and enhancement program based on GNUstep. Capable of opening several documents at once and running high quality filters on them.
endef

MASTER_SITES = http://downloads.sourceforge.net/project/price/PRICE%20source/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWPRICE += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWPRICE += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWPRICE += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWPRICE += CSWgnustep-back

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
SKIPTEST ?= 1

include gar/category.mk

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) &&. $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
