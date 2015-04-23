# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Zipper
VERSION = 1.5
GARTYPE = v2
PACKAGES += CSWgs-zipper

DESCRIPTION = GNUstep graphical archive tool (zip, tar, ...)
define BLURB
  GNUstep tool to inspect and extract  various archives by wrapping existing shell tools (tar, zip, lha...) and create archives through Services from the Workspace.
endef

MASTER_SITES = http://savannah.nongnu.org/download/gap/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWgs-zipper += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWlibobjc4
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWgnustep-back
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWgtar
RUNTIME_DEP_PKGS_CSWgs-zipper += CSWzip

#we depend on these packages at runtime
# we want at least two archivers to be present, zip and gnu tar. Others are optional
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWgtar
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWzip
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWgnustep-back
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWgnustep-make
CHECKPKG_OVERRIDES_CSWgs-zipper += surplus-dependency|CSWgnustep-gui



#overrides
CHECKPKG_OVERRIDES_CSWgs-zipper += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper
CHECKPKG_OVERRIDES_CSWgs-zipper += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper
CHECKPKG_OVERRIDES_CSWgs-zipper += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgs-zipper += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgs-zipper += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgs-zipper += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/Local/Applications/Zipper.app/Zipper|arch_id=18|arch_name=sparcv8+


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
