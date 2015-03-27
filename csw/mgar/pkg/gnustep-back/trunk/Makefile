# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnustep-back
VERSION = 0.24.0
GARTYPE = v2

DESCRIPTION = GNUstep-core back
define BLURB
  GNUstep-core, backend dependent part of GNUstep AppKit.
endef

MASTER_SITES = ftp://ftp.gnustep.org/pub/gnustep/core/
DISTFILES  = $(DISTNAME).tar.gz

#EXTRA_MODULATORS = GRAPHICS
#MODULATIONS_graphics = xlib cairo

BUILD_DEP_PKGS += CSWgmake
BUILD_DEP_PKGS += CSWgcc4objc
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWgnustep-make
BUILD_DEP_PKGS += CSWgnustep-base
BUILD_DEP_PKGS += CSWgnustep-gui


RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-make
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-base
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWgnustep-gui
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibxft2
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWmesa
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibobjc4


#for cairo:
BUILD_DEP_PKGS += CSWlibcairo-dev
#for cairo, add these. Perhaps these hould be pulled in by other packages
BUILD_DEP_PKGS += CSWfontconfig-dev
RUNTIME_DEP_PKGS_CSWgnustep-back += CSWlibcairo2
#DEP_PKGS_GRAPHICS_cairo += CSWlibcairo2

#overrides
CHECKPKG_OVERRIDES_CSWgnustep-back += surplus-dependency|CSWgnustep-gui
CHECKPKG_OVERRIDES_CSWgnustep-back += surplus-dependency|CSWgnustep-base
CHECKPKG_OVERRIDES_CSWgnustep-back += surplus-dependency|CSWgnustep-make


#this is by bundle design
CHECKPKG_OVERRIDES_CSWgnustep-back += shared-library-missing-dot-so|file=opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024

#we do not care about placement
CHECKPKG_OVERRIDES_CSWgnustep-back += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-back += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/gpbs|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWgnustep-back += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWgnustep-back += binary-architecture-does-not-match-placement|file=opt/csw/GNUstep/System/Tools/gpbs|arch_id=3|arch_name=i386


#we do not link directly yet
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libGL.so.1
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libXcursor.so.1
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libXext.so.0
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libXmu.so.4
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libXrender.so.1
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libcairo.so.2
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Tools/gpbs|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Tools/gpbs|is|not|directly|bound|to|soname|libgnustep-base.so.1.24
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Tools/gpbs|is|not|directly|bound|to|soname|libgnustep-gui.so.0.24
CHECKPKG_OVERRIDES_CSWgnustep-back += no-direct-binding|/opt/csw/GNUstep/System/Tools/gpbs|is|not|directly|bound|to|soname|libobjc.so.4
CHECKPKG_OVERRIDES_CSWgnustep-back += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024
CHECKPKG_OVERRIDES_CSWgnustep-back += soname-not-found|libgnustep-gui.so.0.24|is|needed|by|opt/csw/GNUstep/System/Tools/gpbs
CHECKPKG_OVERRIDES_CSWgnustep-back += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Tools/gpbs
CHECKPKG_OVERRIDES_CSWgnustep-back += soname-not-found|libgnustep-base.so.1.24|is|needed|by|opt/csw/GNUstep/System/Library/Bundles/libgnustep-back-024.bundle/libgnustep-back-024

#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-sparc
PACKAGING_PLATFORMS += solaris10-i386

#we absolutely need GCC for Objective-C support. The only alternative in the future would be clang
GARCOMPILER = GNU

# now special targets for configure, build and install so that we can source
# GNUstep.sh before
CONFIGURE_SCRIPTS = sourcegs
BUILD_SCRIPTS = sourcegs
INSTALL_SCRIPTS = sourcegs

# Disable test scripts for now
TEST_SCRIPTS = 
SKIPTEST ?= 1

CONFIGURE_ARGS = $(DIRPATHS)

#CONFIGURE_ARGS_GRAPHICS_xlib += --enable-graphics=xlib
#CONFIGURE_ARGS_GRAPHICS_cairo += --enable-graphics=cairo
CONFIGURE_ARGS += --enable-graphics=cairo 

include gar/category.mk

configure-sourcegs:
	 $(CONFIGURE_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) ; ./configure $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)

build-sourcegs:
	$(BUILD_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE)
	@$(MAKECOOKIE)

install-sourcegs:
	$(INSTALL_ENV) && . $(BUILD_PREFIX)/GNUstep/System/Library/Makefiles/GNUstep.sh && cd $(WORKSRC) && $(MAKE) install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)

test-none :
	@$(MAKECOOKIE)
