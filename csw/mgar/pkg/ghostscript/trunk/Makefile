# $Id$

NAME = ghostscript
VERSION = 9.04
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PostScript and PDF interpreter
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWgs
CATALOGNAME_CSWgs = ghostscript
SPKG_DESC_CSWgs = PostScript and PDF interpreter


RUNTIME_DEP_PKGS_CSWgs += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgs += CSWlibz1
RUNTIME_DEP_PKGS_CSWgs += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWgs += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgs += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWgs += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgs += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgs += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWgs += CSWlibidn11
RUNTIME_DEP_PKGS_CSWgs += CSWlibk5crypto3

RUNTIME_DEP_PKGS_CSWgs += CSWfconfig
RUNTIME_DEP_PKGS_CSWgs += CSWgnutls
RUNTIME_DEP_PKGS_CSWgs += CSWgtk2
RUNTIME_DEP_PKGS_CSWgs += CSWjpeg
RUNTIME_DEP_PKGS_CSWgs += CSWpango
RUNTIME_DEP_PKGS_CSWgs += CSWperl
RUNTIME_DEP_PKGS_CSWgs += CSWgsfonts
RUNTIME_DEP_PKGS_CSWgs += CSWjbig2dec

# I'm dubious about this one. Maybe unnecessary?
# RUNTIME_DEP_PKGS_CSWgs += CSWlibcairo

CHECKPKG_OVERRIDES_CSWgs += surplus-dependency|CSWperl
# Fonts are definitely necessary.
CHECKPKG_OVERRIDES_CSWgs += surplus-dependency|CSWgsfonts

# Only docs and man pages.
CHECKPKG_OVERRIDES_CSWgs += file-with-bad-content
# Historical reasons.
CHECKPKG_OVERRIDES_CSWgs += catalogname-does-not-match-pkgname|pkgname=CSWgs|catalogname=ghostscript|expected-catalogname=gs

# Pending release of libpaper
#RUNTIME_DEP_PKGS_CSWgs += CSWlibpaper

# CHECKPKG_OVERRIDES_CSWgs += symbol-not-found|gsc
# CHECKPKG_OVERRIDES_CSWgs += symbol-not-found|gsx

SPKG_SOURCEURL = http://www.ghostscript.com

LICENSE = LICENSE

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1

# PATCHFILES += 0001-Support-libjpeg7.patch
PATCHFILES += 0002-Rearrange-compiler-flags.patch
PATCHFILES += 0003-Change-gcc-flags-to-sun.patch
# PATCHFILES += 0004-PLATFORM-is-used-by-GAR.patch
PATCHFILES += 0005-Fix-pathes-according-to-old-package.patch
# PATCHFILES += 0006-Fix-dynamic-link-flag.patch
PATCHFILES += 0007-libidn-needs-L-opt-csw-lib.patch
PATCHFILES += 0008-Wrong-place-in-configure.patch

# Not until libcupsimage.so libcups.so libkrb5.so libk5crypto.so
# libcom_err.so libkrb5support.so are 64-bit

# EXTRA_INC = $(prefix)/X11/include
# EXTRA_LIB = $(prefix)/X11/lib
# EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
# We want to be linked with Xrender from $(prefix)/X11/lib not
# $(prefix)/lib since the latter is linked to /usr/openwin/lib/libX11.so.4
# EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

# EXTRA_BUILD_ISAS = sparcv8plus+vis pentium_pro+mmx

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic
CONFIGURE_ARGS += --enable-cups
CONFIGURE_ARGS += --with-fontpath=$(datadir)/ghostscript/fonts
# CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
# CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib

# This fails due to ghostscript using PLATFORM for internal use which gets set
# by GAR
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk

# BUILD_ARGS = std so
# INSTALL_ARGS = install install-so

# Use CSW build packages instead of bundled stuff
pre-configure-$(MODULATION):
	@(echo "~~~ Removing bundled binaries ~~~")
	rm -rf $(WORKSRC)/jpeg
	rm -rf $(WORKSRC)/jbig2dec
#	@rm -rf $(WORKSRC)/jasper
