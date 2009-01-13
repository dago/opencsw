GARNAME = libgpg-error
GARVERSION = 1.7
CATEGORIES = lib

DESCRIPTION = GNU gpg related library
define BLURB
  Libgpg-error is a small library with error codes and descriptions
  shared by most GnuPG related software.
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libgpg-error/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgpgerr,)

SPKG_SOURCEURL = http://www.gnupg.org/download/

REQUIRED_PKGS = CSWiconv CSWggettext

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
