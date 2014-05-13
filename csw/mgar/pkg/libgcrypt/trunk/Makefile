NAME = libgcrypt
VERSION = 1.6.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU libgcrypt
define BLURB
  Libgcrypt is GNU's basic cryptographic library
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libgcrypt/
DISTFILES  = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.gnupg.org/related_software/libraries.en.htmGARCOMPILER = GCC4

BUILD_DEP_PKGS = CSWlibgpg-error-dev CSWlibgpg-error0

PACKAGES += CSWlibgcrypt-dev
SPKG_DESC_CSWlibgcrypt-dev = Development files
PKGFILES_CSWlibgcrypt-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgcrypt-dev += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibgcrypt-dev += $(BUILD_DEP_PKGS)
RUNTIME_DEP_PKGS_CSWlibgcrypt-dev += CSWlibgcrypt-utils

PACKAGES += CSWlibgcrypt20
CATALOGNAME_CSWlibgcrypt20 = libgcrypt20
PKGFILES_CSWlibgcrypt20 += $(call baseisadirs,$(libdir),libgcrypt\.so\.20\.0\.1)
PKGFILES_CSWlibgcrypt20 += $(call baseisadirs,$(libdir),libgcrypt\.so\.20(\.\d+)*)
SPKG_DESC_CSWlibgcrypt20 += $(DESCRIPTION), libgcrypt.so.20
RUNTIME_DEP_PKGS_CSWlibgcrypt20 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgcrypt20 += CSWlibgpg-error0$(BUILD_DEP_PKGS)

PACKAGES += CSWlibgcrypt-utils
SPKG_DESC_CSWlibgcrypt-utils = Utility prograRUNTIME_DEP_PKGS_CSWlibgcrypt-utils += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWlibgcrypt-utils += CSWlibgpg-error0
# PKGFILES is catchall
OBSOLETED_BY_CSWlibgcrypt-utils = CSWgcrypt
CATALOGNAME_CSWgcrypt = libgcrypt_stub

BUILD64 = 1
ISAEXECBUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARmd64-as-feature-detection
CONFIGURE_ARGS += --disable-asm

# Make some old bits of code happy
# http://mail-index.netbsd.org/tech-pkg/2004/08/19/0010.html
# https://www.choon.net/forum/read.php?21,794684
EXTRA_CFLAGS_sparc = -DLONGLONG_STANDALONE

EXTRA_CFLAGS = $(EXTRA_CFLAGS_$(GARCH))

include gar/category.mk
