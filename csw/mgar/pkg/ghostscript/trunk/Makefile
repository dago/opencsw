GARNAME = ghostscript
GARVERSION = 8.70
CATEGORIES = apps

DESCRIPTION = Ghostscript, a PostScript and PDF interpreter for previewing, conversion and printing
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://www.ghostscript.com

LICENSE = COPYING

REQUIRED_PKGS += 

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

#PATCHFILES += 0001-Support-libjpeg7.patch
PATCHFILES += 0002-Rearrange-compiler-flags.patch
PATCHFILES += 0003-Change-gcc-flags-to-sun.patch

#BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib

include gar/category.mk

pre-configure-$(MODULATION):
	@(echo "~~~ Removing bundled jpeglib ~~~")
	@rm -rf $(WORKSRC)/jpeg
#	@rm -rf $(WORKSRC)/jasper
