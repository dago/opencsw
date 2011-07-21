NAME = xz
VERSION = 5.0.3
CATEGORIES = utils

DESCRIPTION = XZ Utils is free data compression software with high compression ratio
define BLURB
  XZ Utils is free general-purpose data compression software with high compression
  ratio. XZ Utils were written for POSIX-like systems (GNU/Linux, *BSDs, etc.), but
  also work on some not-so-POSIX systems like Windows. XZ is based on the LZMA2
  algorithm. The implementation is much more heavywight than lzip.
endef

MASTER_SITES = http://tukaani.org/xz/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES += CSWxz
SPKG_DESC_CSWxz = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWxz += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxz += CSWliblzma5
OBSOLETED_BY_CSWxz += CSWlzma

PACKAGES += CSWliblzma5
SPKG_DESC_CSWliblzma5 = LZMA compression library, liblzma.so.5
PKGFILES_CSWliblzma5 += $(call pkgfiles_lib,liblzma.so.5)

PACKAGES += CSWliblzma-dev
SPKG_DESC_CSWliblzma-dev = Development Files for liblzma.so.5
PKGFILES_CSWliblzma-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWliblzma-dev += $(docdir)/xz/examples/.*
PKGFILES_CSWliblzma-dev += $(docdir)/xz/.*-file-format.txt
RUNTIME_DEP_PKGS_CSWliblzma-dev += CSWliblzma5

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
# This test fails as SOS12 cc is not real c99 (stdbool.h is missing)
# but nonetheless SOS12 works fine
CONFIGURE_ARGS += ac_cv_prog_cc_c99=

include gar/category.mk
