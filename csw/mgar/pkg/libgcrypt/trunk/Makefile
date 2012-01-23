NAME = libgcrypt
VERSION = 1.5.0
CATEGORIES = lib

DESCRIPTION = GNU libgcrypt
define BLURB
  Libgcrypt is GNU's basic cryptographic library
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libgcrypt/
DISTFILES  = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.gnupg.org/related_software/libraries.en.html#lib-libgcrypt

BUILD_DEP_PKGS = CSWlibgpg-error-dev

PACKAGES += CSWlibgcrypt11
SPKG_DESC_CSWlibgcrypt11 = GNU libgcrypt, libgcrypt.so.11
PKGFILES_CSWlibgcrypt11 += $(call pkgfiles_lib,libgcrypt.so.11)
RUNTIME_DEP_PKGS_CSWlibgcrypt11 += CSWlibgpg-error0

PACKAGES += CSWlibgcrypt-dev
SPKG_DESC_CSWlibgcrypt-dev = Development files for libgcrypt.so.11
PKGFILES_CSWlibgcrypt-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgcrypt-dev += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgcrypt-dev += $(BUILD_DEP_PKGS)

PACKAGES += CSWlibgcrypt-utils
SPKG_DESC_CSWlibgcrypt-utils = Utility programs for libgcrypt
# PKGFILES is catchall
OBSOLETED_BY_CSWlibgcrypt-utils = CSWgcrypt
CATALOGNAME_CSWgcrypt = libgcrypt_stub

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-asm

include gar/category.mk
