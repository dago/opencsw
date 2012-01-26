NAME = ghostscript
VERSION = 8.70
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Ghostscript, a PostScript and PDF interpreter for previewing, conversion and printing
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWgs
CATALOGNAME_CSWgs = ghostscript
SPKG_DESC_CSWgs = Ghostscript, a PostScript and PDF interpreter for previewing, conversion and printing

RUNTIME_DEP_PKGS_CSWgs += CSWfconfig CSWjpeg CSWlibcairo CSWgsfonts
RUNTIME_DEP_PKGS_CSWgs += CSWftype2 CSWggettextrt CSWglib2 CSWgnutls CSWgtk2
RUNTIME_DEP_PKGS_CSWgs += CSWkrb5lib CSWlibatk CSWlibcups CSWpango CSWperl CSWzlib
RUNTIME_DEP_PKGS_CSWgs += CSWjbig2dec
# Pending release of libpaper
#RUNTIME_DEP_PKGS_CSWgs += CSWlibpaper

CHECKPKG_OVERRIDES_CSWgs += symbol-not-found|gsc
CHECKPKG_OVERRIDES_CSWgs += symbol-not-found|gsx

SPKG_SOURCEURL = http://www.ghostscript.com

LICENSE = LICENSE

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

#PATCHFILES += 0001-Support-libjpeg7.patch
PATCHFILES += 0002-Rearrange-compiler-flags.patch
PATCHFILES += 0003-Change-gcc-flags-to-sun.patch
PATCHFILES += 0004-PLATFORM-is-used-by-GAR.patch
PATCHFILES += 0005-Fix-pathes-according-to-old-package.patch
PATCHFILES += 0006-Fix-dynamic-link-flag.patch

# Not until libcupsimage.so libcups.so libkrb5.so libk5crypto.so
# libcom_err.so libkrb5support.so are 64-bit

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
# We want to be linked with Xrender from $(prefix)/X11/lib not
# $(prefix)/lib since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro+mmx

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic
CONFIGURE_ARGS += --enable-cups
CONFIGURE_ARGS += --with-fontpath=$(datadir)/ghostscript/fonts
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib

# This fails due to ghostscript using PLATFORM for internal use which gets set
# by GAR
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

BUILD_ARGS = std so
INSTALL_ARGS = install install-so

# Use CSW build packages instead of bundled stuff
pre-configure-$(MODULATION):
	@(echo "~~~ Removing bundled stuff ~~~")
	@rm -rf $(WORKSRC)/jpeg
	@rm -rf $(WORKSRC)/jbig2dec
#	@rm -rf $(WORKSRC)/jasper
