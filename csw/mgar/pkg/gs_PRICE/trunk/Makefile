# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = PRICE
VERSION = 1.2.0
GARTYPE = v2

PACKAGES += CSWgs-price

DESCRIPTION = Image viewing and filtering program
define BLURB
  Raster image viewing, manipulation, filtering and enhancement program based on GNUstep. Capable of opening several documents at once and running high quality filters on them.
endef

MASTER_SITES = http://downloads.sourceforge.net/project/price/PRICE%20source/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWgs-price += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgs-price += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgs-price += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWgs-price += CSWgnustep-back
RUNTIME_DEP_PKGS_CSWgs-price += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgs-price += CSWlibobjc4

#overrides, we know we need these!
CHECKPKG_OVERRIDES_CSWgs-price += surplus-dependency|CSWgnustep-make
CHECKPKG_OVERRIDES_CSWgs-price += surplus-dependency|CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWgs-price += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWgs-price += surplus-dependency|CSWgnustep-back

#known GNUstep app bundle overrides
CHECKPKG_OVERRIDES_CSWgs-price += no-direct-binding|/opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgs-price += no-direct-binding|/opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgs-price += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE
CHECKPKG_OVERRIDES_CSWgs-price += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE
CHECKPKG_OVERRIDES_CSWgs-price += no-direct-binding|/opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWgs-price += no-direct-binding|/opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|is|not|directly|bound|to|soname|libgnustep-base.so.1.24

#known placement problems
CHECKPKG_OVERRIDES_CSWgs-price += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgs-price += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/Local/Applications/PRICE.app/PRICE|arch_id=3|arch_name=i386


#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386


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
