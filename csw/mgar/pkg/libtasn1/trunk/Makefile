GARNAME = libtasn1
GARVERSION = 1.7
CATEGORIES = lib

DESCRIPTION = GNU ASN1 library
define BLURB
endef

MASTER_SITES = http://ftp.gnu.org/pub/gnu/gnutls/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibtasn1,)

PATCHFILES = patch-stdint.diff

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS =

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

TEST_TARGET = check

include gar/category.mk

