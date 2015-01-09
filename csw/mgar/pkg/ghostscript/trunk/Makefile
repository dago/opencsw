# $Id$

NAME = ghostscript
VERSION = 9.15
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PostScript and PDF interpreter
define BLURB
endehttp://downloads.ghostscript.com/public/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.ghostscript.com

LICENSE = LICENSE

GARCOMPILER = GCC4PST Many more missing
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWlibjbig2dec-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpaper-dev
BUILD_DEP_PKGS += CSWlibcairo-devinFOREIGN_PACKAGES += CSWlibgs8inPACKAGES += CSWghostscript
SPKG_DESC_CSWghostscript = PostScript and PDF interpreter
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibgs9
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibz1
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibtiff5
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
RUNTIME_DEP_PKGS_CSWghostscript += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWghostscript-sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWghostscript += $(RUNTIME_DEP_PKGS_CSWghostscript-$(GARCH))

# These are probably ok
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/unix-lpr.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/unix-lpr.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/unix-lpr.sh  
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/lprsetup.sh
CHECKPKG_OVERRIDES_CSWghostscript += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/unix-lpr.sh

# This was the old package
OBSOLETED_BY_CSWghostscript += CSWgs
CATALOGNAME_CSWgs = ghostscript_stub
# We need this as legacy packages still depend on CSWgs to include libgs.so.8
RUNTIME_DEP_PKGS_CSWgs += CSWlibgs8
CHECKPKG_OVERRIDES_CSWgs += surplus-dependency|CSWlibgs8

PRESERVECONF += $(sysconfdir)/cups/gstoraster.convs

PACKAGES += CSWlibgs9
SPKG_DESC_CSWlibgs9 = Ghostscript library, libgs.so.9
PKGFILES_CSWlibgs9 += $(call pkgfiles_lib,libgs.so.9)
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibjbig2dec0
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibpaper1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWlibgs9-sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgs9 += $(RUNTIME_DEP_PKGS_CSWlibgs9-$(GARCH))

PACKAGES += CSWghostscript-dev
SPKG_DESC_CSWghostscript-dev = Development files for ghostscript and libgs.so.9
# This remove all the .so symlinks for PKGFILES_DEVEL
# so only the right ones can be re-added, and the versioned .so used
# in the package above
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWghostscript-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWghostscript-dev += $(call baseisadirs,$(libdir),libgs\.so)
RUNTIME_DEP_PKGS_CSWghostscript-dev += CSWlibgs9
RUNTIME_DEP_PKGS_CSWghostscript-dev += CSWghostscript

# This is for cups/gstoraster.c which doesn't seem to honour --with-fontpath
EXTRA_CPPFLAGS += -DCUPS_FONTPATH=\\\"$(datadir)/ghostscript/fonts\\\"

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic
CONFIGURE_ARGS += --with-fontpath=$(datadir)/ghostscript/fonts
CONFIGURE_ARGS += --with-system-libtiff

# pentium_pro does not have SSE2 and the detection does not work
CONFIGURE_ARGS-32-i386 += --disable-sse2
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL)-$(GARCH))

# This makes debugging much easier, remove for production
CONFIGURE_ARGS-DBG += --disable-compile-inits
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GARFLAVOR))

# We do not bootstrap and compile libijs any more as Ghostscript statically compiles
# against the local ijs sources and the libijs library is not useful. See for details
#   http://bugs.ghostscript.com/show_bug.cgi?id=695692

# We want the shared library
BUILD_ARGS += so

INSTALL_ARGS += soinstall

include gar/category.mk

# Remove local versions of libraies we want to link against system-wide
post-extract:
	rm -rf $(WORKSRC)/lcms2
	rm -rf $(WORKSRC)/zlib
	rm -rf $(WORKSRC)/jpeg
	rm -rf $(WORKSRC)/openjpeg
	rm -rf $(WORKSRC)/tiff
	rm -rf $(WORKSRC)/jbig2dec
	rm -rf $(WORKSRC)/libpng
	rm -rf $(WORKSRC)/freetype
	rm -rf $(WORKSRC)/expat
	@$(MAKECOOKIE)

