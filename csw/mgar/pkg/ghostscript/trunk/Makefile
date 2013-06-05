# $Id$

NAME = ghostscript
VERSION = 9.07
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PostScript and PDF interpreter
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VENDOR_d|gsx

SPKG_SOURCEURL = http://www.ghostscript.com

LICENSE = LICENSE

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPST Many more missing
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWlibjbig2dec-dev
BUILD_DEP_PKGS += CSWfconfig-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpaper-dev
BUILD_DEP_PKGS += CSWlibcairo2inFOREIGN_PACKAGES += CSWlibgs8inPACKAGES += CSWghostscript
SPKG_DESC_CSWghostscript = PostScript and PDF interpreter
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgs9
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibz1
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibcups2
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibjbig2dec0 
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibidn11 
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibpaper1
RUNTIME_DEP_PKGS_CSWghostscript += CSWemacs-common
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgtk-x11-2-0-0

# These are probably ok
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/unix-lpr.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/unix-lpr.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/unix-lpr.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/unix-lpr.sh

CHECKPKG_OVERRIDES_CSWghostscript += missing-dependency|CSWemacs-common

# This was the old package
OBSOLETED_BY_CSWghostscript += CSWgs
CATALOGNAME_CSWgs = ghostscript_stub
# We need this as legacy packages still depend on CSWgs to include libgs.so.8
RUNTIME_DEP_PKGS_CSWgs += CSWlibgs8
CHECKPKG_OVERRIDES_CSWgs += surplus-dependency|CSWlibgs8

PACKAGES += CSWlibgs9
SPKG_DESC_CSWlibgs9 = Ghostscript library, libgs.so.9
PKGFILES_CSWlibgs9 += $(call pkgfiles_lib,libgs.so.9)
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibjbig2dec0
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibpaper1

PACKAGES += CSWghostscript-dev
SPKG_DESC_CSWghostscript-dev = Development files for ghostscript and libgs.so.9
PKGFILES_CSWghostscript-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWghostscript-dev += CSWlibgs9

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic
CONFIGURE_ARGS += --with-fontpath=$(datadir)/ghostscript/fonts
CONFIGURE_ARGS += --enable-cups

# pentium_pro does not have SSE2 and the detection does not work
CONFIGURE_ARGS-32-i386 += --disable-sse2
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL)-$(GARCH))

# We want the shared library
BUILD_ARGS += so

# This is needed because libidn.so and libpaper.so are not linked with LDFLAGS set
BUILD_ARGS += XTRALIBS="$(strip $(LINKER_FLAGS))"

TEST_ARGS += XTRALIBS="$(strip $(LINKER_FLAGS))"

INSTALL_ARGS += soinstall

include gar/category.mkinpost-extract:
	@# Ghostscript 9.07 depends on API not released in the current lcms2 2.4
	@#   https://bugzilla.redhat.com/show_bug.cgi?id=912307
	@#   http://list-archives.org/2013/02/14/gs-devel-ghostscript-com/ghostscript-9-07-and-ghostpdl-9-07/f/6061272699
	#rm -rf $(WORKSRC)/lcms2
	rm -rf $(WORKSRC)/zlib
	rm -rf $(WORKSRC)/jpeg
	rm -rf $(WORKSRC)/tiff
	rm -rf $(WORKSRC)/jbig2dec
	rm -rf $(WORKSRC)/libpng
	rm -rf $(WORKSRC)/freetype
	@$(MAKECOOKIE)
	
