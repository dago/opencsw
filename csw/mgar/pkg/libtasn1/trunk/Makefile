GARNAME = libtasn1
GARVERSION = 2.1
CATEGORIES = lib

DESCRIPTION = GNU ASN1 library
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS =

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

TEST_TARGET = check

include gar/category.mk

