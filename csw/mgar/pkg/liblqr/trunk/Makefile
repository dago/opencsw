NAME = liblqr
VERSION = 0.4.1
CATEGORIES = lib

DESCRIPTION = A seam-carving C/C++ library called Liquid Rescale.
define BLURB
endef

MASTER_SITES = http://liblqr.wikidot.com/local--files/en%3Adownload-page/
DISTNAME = $(NAME)-1-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# Otherwise the inline functions are not exported and are missing during linkage
PATCHFILES += inline.diff

# The compilation succeeds on Solaris 9 without any of these, disable for now.
#PATCHFILES += examples.diff
#PATCHFILES += lqr_carver.c.diff

# New glib2 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://liblqr.wikidot.com/

PACKAGES += CSWliblqr1-0
SPKG_DESC_CSWliblqr1-0 = A seam-carving C/C++ library called Liquid Rescale, liblqr-1.so.0
PKGFILES_CSWliblqr1-0 += $(call pkgfiles_lib,liblqr-1.so.0)
RUNTIME_DEP_PKGS_CSWliblqr1-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWliblqr1-0 += CSWlibglib2-0-0
OBSOLETED_BY_CSWliblqr1-0 += CSWliblqr

PACKAGES += CSWliblqr-dev
SPKG_DESC_CSWliblqr-dev += Development files for liblqr-1.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliblqr-dev += CSWliblqr1-0
OBSOLETED_BY_CSWliblqr-dev += CSWliblqrdevel
CATALOGNAME_CSWliblqrdevel = liblqr_devel_stub

BUILD64 = 1

include gar/category.mk
