NAME = oniguruma
VERSION = 5.9.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A regular expression library
define BLURB
  Oniguruma is a regular expressions library.
  The characteristics of this library is that different character encoding 
  for every regular expression object can be specified. 
  (supported APIs: GNU regex, POSIX and Oniguruma native)
endef

MASTER_SITES = http://www.geocities.jp/kosako3/oniguruma/archive/
DISTNAME = onig-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.geocities.jp/kosako3/oniguruma/

PACKAGES += CSWlibonig2
SPKG_DESC_CSWlibonig2 = Oniguruma is a regular expression library, libonig.so.2
PKGFILES_CSWlibonig2 += $(call pkgfiles_lib,libonig.so.2)
OBSOLETED_BY_CSWlibonig2 += CSWoniguruma

PACKAGES += CSWlibonig-dev
SPKG_DESC_CSWlibonig-dev = Development files for libonig.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibonig-dev += CSWlibonig2

BUILD64_LIBS_ONLY = 1

include gar/category.mk
