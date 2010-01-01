GARNAME = libgcrypt
GARVERSION = 1.4.5
CATEGORIES = lib

DESCRIPTION = GNU libgcrypt
define BLURB
  Libgcrypt is GNU's basic cryptographic library
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libgcrypt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWgcrypt
CATALOGNAME = libgcrypt

SPKG_SOURCEURL = http://www.gnupg.org/related_software/libraries.en.html#lib-libgcrypt

REQUIRED_PKGS = CSWgpgerr

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-asm

TEST_TARGET = check

include gar/category.mk
