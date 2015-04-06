# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = FTP
VERSION = 0.5
GARTYPE = v2

DESCRIPTION = GNUstep FTP client
define BLURB
  Graphical, compact FTP client for GNUstep. 
endef

MASTER_SITES = http://savannah.nongnu.org/download/gap/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgmake 
BUILD_DEP_PKGS += CSWgcc4objc

RUNTIME_DEP_PKGS_CSWFTP += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWFTP += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWFTP += CSWgnustep-gui 
RUNTIME_DEP_PKGS_CSWFTP += CSWgnustep-back
RUNTIME_DEP_PKGS_CSWFTP += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWFTP += CSWlibobjc4

#we know about these, but they are needed at runtime
CHECKPKG_OVERRIDES_CSWFTP += surplus-dependency|CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWFTP += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWFTP += surplus-dependency|CSWgnustep-back
CHECKPKG_OVERRIDES_CSWFTP += surplus-dependency|CSWgnustep-make

#these are due to our bundles
CHECKPKG_OVERRIDES_CSWFTP += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/Local/Applications/FTP.app/FTP|arch_id=18|arch_name=sparcv8+

#we do not directly bind
CHECKPKG_OVERRIDES_CSWFTP += no-direct-binding|/opt/csw/GNUstep/Local/Applications/FTP.app/FTP|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWFTP += no-direct-binding|/opt/csw/GNUstep/Local/Applications/FTP.app/FTP|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWFTP += no-direct-binding|/opt/csw/GNUstep/Local/Applications/FTP.app/FTP|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWFTP += no-direct-binding|/opt/csw/GNUstep/Local/Applications/FTP.app/FTP|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWFTP += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/Local/Applications/FTP.app/FTP
CHECKPKG_OVERRIDES_CSWFTP += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/Local/Applications/FTP.app/FTP


#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

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
