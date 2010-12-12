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

PACKAGES = CSWgpgerr
CATALOGNAME = libgpg_error

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.gnupg.org/download/

RUNTIME_DEP_PKGS = CSWggettextrt

BUILD64 = 1
NOISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
