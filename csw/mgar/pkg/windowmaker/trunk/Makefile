# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = windowmaker
VERSION = 0.95.5
GARTYPE = v2

DESCRIPTION = X11 window manager
define BLURB
  A classic windowmanager with the NeXT and OpenStep look. Fast and low on
  resources, it is optimal for every serous user! It is the recommended
  window manager for GNUstep.
endef

#PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386efine BLURB
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GNU

MASTER_SITES = http://windowmaker.org/pub/source/release/
DISTNAME = WindowMaker-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-add-__progname.patch
PATCHFILES += 0002-use-wconfig-in-wxpaste-because-of-__progname.patch

EXTRA_INC = /opt/csw/X11/include

EXTRA_LINKER_FLAGS = -lrt

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWlibwings2
PKGFILES_CSWlibwings2 += $(call baseisadirs,$(libdir),libWINGs\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibwings2 += $(DESCRIPTION), libWINGs.so.2
RUNTIME_DEP_PKGS_CSWlibwings2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibwings2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibwings2 += CSWlibwraster3
RUNTIME_DEP_PKGS_CSWlibwings2 += CSWlibwutil2
RUNTIME_DEP_PKGS_CSWlibwin += CSWlibxrender

PACKAGES += CSWlibwutil2
PKGFILES_CSWlibwutil2 += $(call baseisadirs,$(libdir),libWUtil\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibwutil2 += $(DESCRIPTION), libWUtil.so.2
RUNTIME_DEP_PKGS_CSWlibwutil2 += CSWlibgcc-s1
# Not investigated.
CHECKPKG_OVERRIDES_CSWlibwutil2 += file-with-bad-content|/usr/local|root/opt/csw/lib/libWUtil.so.2.0.0

PACKAGES += CSWlibwraster3
PKGFILES_CSWlibwraster3 += $(call baseisadirs,$(libdir),libwraster\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibwraster3 += $(DESCRIPTION), libwraster.so.3
RUNTIME_DEP_PKGS_CSWlibtiff5er3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwraster3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwraster3 += CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibwrasterRUNTIME_DEP_PKGS_CSWlibwraster3 += CSWlibpng16-16
RUNTIME_DEP_PKGS_CSWlibwraster3 += CSWlibxpm4r3 += CSWlibgcc-s1

PACKAGES += CSWwindowmaker-dev
SPKG_DESC_CSWwindowmaker-dev += $(DESCRIPTION), development files
PKGFILES_CSWwindowmaker-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWwindowmaker-dev += CSWlibwutil2
RUNTIME_DEP_PKGS_CSWwindowmaker-dev += CSWlibwraster3
RUNTIME_DEP_PKGS_CSWwindowmaker-deRUNTIME_DEP_PKGS_CSWwindowmaker-dev += CSWwindowmakerev += CSWlibwings2

PACKAGES += CSWwindowmaker
SPKG_DESC_CSWwindowmaker = $(DESCRIPTION)
OBSOLETED_BY_CSWwindowmaker = CSWwmaker
INCOMPATIBLE_PKGS_CSWwindowmaker = CSWwmaker
RUNTIME_DEP_PKGS_CSWwindo-wmaker += CSWemacscommon
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibwings2
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibwraster3
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibwutil2
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibxft2
RUNTIME_DEP_PKGS_CSWperl
RUNTIME_DEP_PKGS_CSWwindowmaker += CSWlibgcc-s1

# Documentation
CHECKPKG_OVERRIDES_CSWwindowmaker += file-with-bad-content

# Main library file
CHECKPKG_OVERRIDES_CSWwindowmaker += shared-lib-pkgname-mismatch|file=opt/csw/lib/libWMaker.so.1.0.1|soname=libWMaker.so.1|pkgname=CSWwindowmaker|expected=CSWlibwmaker1e-with-bad-content

include gar/category.mk

post-configure-modulated:
	gpatch -i $(abspath $(FILEDIR))/0001-add-__progname.patch -p1 -d $(WORKSRC