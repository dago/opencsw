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
RUNTIME_DEP_PKGS_CSWTerminal += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWTerminal += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWTerminal += CSWlibobjc4

#we do override because we depend on them
CHECKPKG_OVERRIDES_CSWTerminal += surplus-dependency|CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWTerminal += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWTerminal += surplus-dependency|CSWgnustep-back
CHECKPKG_OVERRIDES_CSWTerminal += surplus-dependency|CSWgnustep-make

# we don't direcly bind right now
CHECKPKG_OVERRIDES_CSWTerminal += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWTerminal += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWTerminal += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWTerminal += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|is|not|directly|bound|to|soname|libiconv.so.2
CHECKPKG_OVERRIDES_CSWTerminal += no-direct-binding|/opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|is|not|directly|bound|to|soname|libobjc.so.4

#known placement overrides since we use bundles
CHECKPKG_OVERRIDES_CSWTerminal += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal|arch_id=18|arch_name=sparcv8+

#others
CHECKPKG_OVERRIDES_CSWTerminal += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal
CHECKPKG_OVERRIDES_CSWTerminal += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/Local/Applications/Terminal.app/Terminal


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
