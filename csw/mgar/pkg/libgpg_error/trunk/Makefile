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

PACKAGES += CSWgpgerr
CATALOGNAME_CSWgpgerr = gpgerr
SPKG_DESC_CSWgpgerr = Transitional package as contents moved to CSWlibgpg-error and CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgpgerr = CSWgpg-error CSWlibgpg-error0
CHECKPKG_OVERRIDES_CSWgpgerr += surplus-dependency|CSWgpg-error
CHECKPKG_OVERRIDES_CSWgpgerr += surplus-dependency|CSWlibgpg-error0
PKGFILES_CSWgpgerr = NOFILES
ARCHALL_CSWgpgerr = 1

PACKAGES += CSWgpg-error
CATALOGNAME_CSWgpg-error = gpg_error
SPKG_DESC_CSWgpg-error = Tools for libgpg-error.so
RUNTIME_DEP_PKGS_CSWgpg-error = CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgpg-error += CSWggettextrt

PACKAGES += CSWlibgpg-error0
CATALOGNAME_CSWlibgpg-error0 = libgpg_error0
SPKG_DESC_CSWlibgpg-error0 = GNU gpg related library providing libgpg-error.so.0
PKGFILES_CSWlibgpg-error0 = $(call baseisadirs,$(libdir),libgpg-error\.so\.0(\.\d+)*)

PACKAGES += CSWlibgpg-error-dev
CATALOGNAME_CSWlibgpg-error-dev = libgpg_error_dev
SPKG_DESC_CSWlibgpg-error-dev = Development files for libgpg-error.so
PKGFILES_CSWlibgpg-error-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibgpg-error-dev += $(sharedstatedir)/common-lisp/.*
RUNTIME_DEP_PKGS_CSWlibgpg-error-dev += CSWlibgpg-error0

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.gnupg.org/download/

RUNTIME_DEP_PKGS = CSWggettextrt

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

TEST_TARGET = check

include gar/category.mk
