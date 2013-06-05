# $Id$

NAME = ghostscript
VERSION = 8.71
GARTYPE = v2

DESCRIPTION = PostScript and PDF interpreter
define BLURB
endef

DISTFILES += libgs.so.8.71-i386
DISTFILES += libgs.so.8.71-sparc
DISTFILES += libgs.so.8.71-sparcv8plus+vis2
DISTFILES += LICENSE

VENDOR_URL = http://www.ghostscript.com

LICENSE = LICENSE

# Legacy lib still in use
PACKAGES += CSWlibgs8
SPKG_DESC_CSWlibgs8 = Ghostscript library, libgs.so.8
PKGFILES_CSWlibgs8 += $(call pkgfiles_lib,libgs.so.8)
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWsunmath
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibjbig2dec0
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibcups2
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgs8 += CSWlibk5crypto3

# This is old and we won't change it any more
CHECKPKG_OVERRIDES_CSWlibgs8 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgs8 += file-with-bad-content

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS =

include gar/category.mk

post-install-isa-sparcv8plus:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -m 0644 $(WORKDIR)/libgs.so.8.71-sparc $(DESTDIR)$(libdir)/libgs.so.8.71
	gln -s libgs.so.8.71 $(DESTDIR)$(libdir)/libgs.so.8
	ginstall -d $(DESTDIR)$(libdir)/sparcv8plus+vis2
	ginstall -m 0644 $(WORKDIR)/libgs.so.8.71-sparcv8plus+vis2 $(DESTDIR)$(libdir)/sparcv8plus+vis2/libgs.so.8.71
	gln -s libgs.so.8.71 $(DESTDIR)$(libdir)/sparcv8plus+vis2/libgs.so.8
	@$(MAKECOOKIE)

post-install-isa-pentium_pro:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -m 0644 $(WORKDIR)/libgs.so.8.71-i386 $(DESTDIR)$(libdir)/libgs.so.8.71
	gln -s libgs.so.8.71 $(DESTDIR)$(libdir)/libgs.so.8
	@$(MAKECOOKIE)
	

