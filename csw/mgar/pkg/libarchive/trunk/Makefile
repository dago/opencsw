# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = libarchive
GARVERSION = 2.8.3
CATEGORIES = lib

DESCRIPTION = C library for reading and writing various archive formats
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://code.google.com/p/libarchive/

DEP_PKGS = CSWxz CSWbzip2 CSWiconv CSWlibxml2 CSWzlib CSWosslrt

EXTRA_INC = $(includedir)/cryptopp

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
