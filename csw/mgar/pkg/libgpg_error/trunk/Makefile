NAME = libgpg-error
VERSION = 1.10
CATEGORIES = lib

DESCRIPTION = GNU gpg related library
define BLURB
  Libgpg-error is a small library with error codes and descriptions
  shared by most GnuPG related software.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libgpg-error/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES += CSWgpg-error
CATALOGNAME_CSWgpg-error = gpg_error
SPKG_DESC_CSWgpg-error = Tools for libgpg-error.so
RUNTIME_DEP_PKGS_CSWgpg-error = CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgpg-error += CSWlibintl8
OBSOLETED_BY_CSWgpg-error = CSWgpgerr
CATALOGNAME_CSWgpgerr = libgpg_error_stub

PACKAGES += CSWlibgpg-error0
CATALOGNAME_CSWlibgpg-error0 = libgpg_error0
SPKG_DESC_CSWlibgpg-error0 = GNU gpg related library, libgpg-error.so.0
PKGFILES_CSWlibgpg-error0 += $(call pkgfiles_lib,libgpg-error.so.0)
PKGFILES_CSWlibgpg-error0 += .*/libgpg-error.mo
RUNTIME_DEP_PKGS_CSWlibgpg-error0 += CSWlibintl8
OBSOLETED_BY_libgpg-error0 = CSWgpgerr

PACKAGES += CSWlibgpg-error-dev
CATALOGNAME_CSWlibgpg-error-dev = libgpg_error_dev
SPKG_DESC_CSWlibgpg-error-dev = Development files for libgpg-error.so.0
PKGFILES_CSWlibgpg-error-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibgpg-error-dev += $(sharedstatedir)/common-lisp/.*
RUNTIME_DEP_PKGS_CSWlibgpg-error-dev += CSWlibgpg-error0

VENDOR_URL = http://www.gnupg.org/download/

RUNTIME_DEP_PKGS = CSWggettextrt

BUILD64_LIBS_ONLY = 1

include gar/category.mk
