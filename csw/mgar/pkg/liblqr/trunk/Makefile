GARNAME = liblqr
GARVERSION = 0.4.1
CATEGORIES = lib

DESCRIPTION = A seam-carving C/C++ library called Liquid Rescale.
define BLURB
endef

MASTER_SITES = http://liblqr.wikidot.com/local--files/en:download-page/
DISTNAME = $(GARNAME)-1-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

PACKAGES = CSWliblqr CSWliblqrdevel
CATALOGNAME_CSWliblqr = liblqr
CATALOGNAME_CSWliblqrdevel = liblqr_devel

SPKG_DESC_CSWliblqr += A seam-carving C/C++ library called Liquid Rescale
SPKG_DESC_CSWliblqrdevel += A seam-carving C/C++ library called Liquid Rescale - developer package

RUNTIME_DEP_PKGS_CSWliblqr += CSWggettextrt
RUNTIME_DEP_PKGS_CSWliblqr += CSWglib2
RUNTIME_DEP_PKGS_CSWliblqrdevel += CSWliblqr

PKGFILES_CSWliblqrdevel = $(PKGFILES_DEVEL)

# Some symbols seems to be missing for some strange reason
CHECKPKG_OVERRIDES_CSWliblqr += symbol-not-found|liblqr-1.so.0.3.1
CHECKPKG_OVERRIDES_CSWliblqr += symbol-not-found|liblqr-1.so.0.3.1

SPKG_SOURCEURL = http://liblqr.wikidot.com/

#LICENSE = flashpix.h

#DOCFILES = AUTHORS ChangeLog NEWS README

UFILES_REGEX = $(GARNAME)-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)

STRIP_LIBTOOL=1

TEST_TARGET = check

BUILD64 = 1

include gar/category.mk
