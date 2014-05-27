# $Id$

NAME = ghostscript
VERSION = 9.14
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PostScript and PDF interpreter
define BLURB
endehttp://downloads.ghostscript.com/public/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += map.ghostscript$(# See for details https://www.opencsw.org/mantis/view.php?id=4913
#PATCHFILES += 0001-Use-ksh-and-GNU-sed-as-reported-in-4913.patch

VENDOR_URL = http://www.ghostscript.com

LICENSE = LICENSE

GARCOMPILER = GCC4

LINKER_MAPS ?= -M "$(abspath $(WORKDIR)/map.ghostscript)"PST Many more missing
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWlibjbig2dec-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpaper-dev
BUILD_DEP_PKGS += CSWlibcairo2inFOREIGN_PACKAGES += CSWlibgs8inPACKAGES += CSWghostscript
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


PACKAGES += CSWghostscript-dev
SPKG_DESC_CSWghostscript-dev = Development files for ghostscript and libgs.so.9
PKGFILES_CSWghostscript-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWghostscript-dev += CSWlibgs9

###
# Needed for the Solaris ld bug
ifeq ($(shell /usr/bin/uname -p),sparc)
RUNTIME_DEP_PKGS_CSWghostscript += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibgs9 += CSWlibk5crypto3
endif
###

REINPLACEMENTS += fontpath
REINPLACE_MATCH_fontpath = /usr/share/cups/fonts
REINPLACE_WITH_fontpath = $(sharedstatedir)/cups/fonts
REINPLACE_FILES_fontpath += cups/gstopxl.in

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

# The arguments used for libijs
CONFIGURE_ARGS_ijs  = $(DIRPATHS)
CONFIGURE_ARGS_ijs += --enable-shared
CONFIGURE_ARGS_ijs += --disable-static

# We want the shared library
BUILD_ARGS += so

# This is needed because libidn.so and libpaper.so are not linked with LDFLAGS set
BUILD_ARGS += XTRALIBS="$(strip $(LINKER_FLAGS))"

TEST_ARGS += XTRALIBS="$(strip $(LINKER_FLAGS))"

INSTALL_ARGS += soinstall

include gar/category.mkinpost-extract:
	# http://www.linuxfromscratch.org/blfs/view/svn/pst/gs.html
	gsed -i 's/ZLIBDIR=src/ZLIBDIR=$$includedir/' $(WORKSRC)/configure.ac $(WORKSRC)/configure
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

post-configure:
	# Specific for libijs
	cd $(WORKSRC)/ijs && ./autogen.sh
	cd $(WORKSRC)/ijs && \
		/usr/bin/env -i $(CONFIGURE_ENV) PWD=$(abspath $(WORKSRC)/ijs) \
		./configure $(CONFIGURE_ARGS_ijs)
	@$(MAKECOOKIE)

post-build:
	# Specific for libijs
	cd $(WORKSRC)/ijs && \
		 /usr/bin/env -i $(BUILD_ENV) $(MAKE) MAKEFLAGS= $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(OBJDIR) $(BUILD_ARGS_ijs)
	@$(MAKECOOKIE)

post-install:
	# Specific for libijs
	cd $(WORKSRC)/ijs && \
		/usr/bin/env -i $(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) $(foreach TTT,$(INSTALL_OVERRIDE_VARS),$(TTT)="$(INSTALL_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(INSTALL_OVERRIDE_DIRS),$(TTT)="$(DESTDIR)$($(TTT))") -C $(OBJDIR) $(INSTALL_ARGS_ijs) install
	@$(MAKECOOKIE)
