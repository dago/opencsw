NAME = liblqr
VERSION = 0.4.1
CATEGORIES = lib

DESCRIPTION = A seam-carving C/C++ library called Liquid Rescale.
define BLURB
endef

MASTER_SITES = http://liblqr.wikidot.com/local--files/en:download-page/
DISTNAME = $(NAME)-1-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

PACKAGES = CSWliblqr CSWliblqrdevel
CATALOGNAME_CSWliblqr = liblqr
CATALOGNAME_CSWliblqrdevel = liblqr_devel

SPKG_DESC_CSWliblqr += $(DESCRIPTION)
SPKG_DESC_CSWliblqrdevel += $(DESCRIPTION) - developer package

RUNTIME_DEP_PKGS_CSWliblqr += CSWggettextrt
RUNTIME_DEP_PKGS_CSWliblqr += CSWglib2
RUNTIME_DEP_PKGS_CSWliblqrdevel += CSWliblqr

PKGFILES_CSWliblqrdevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://liblqr.wikidot.com/

DOCFILES = AUTHORS BUGS COPYING COPYING.LESSER ChangeLog NEWS README TODO

UFILES_REGEX = $(NAME)-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

PATCHFILES += inline.diff
PATCHFILES += examples.diff
PATCHFILES += lqr_carver.c.diff

CONFIGURE_ARGS  = $(DIRPATHS)

STRIP_LIBTOOL=1

TEST_TARGET = check

BUILD64 = 1

include gar/category.mk
