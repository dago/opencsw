# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = libarchive
VERSION = 2.8.3
CATEGORIES = lib

DESCRIPTION = C library for reading and writing various archive formats
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# This is already in trunk from r2347:
#   <http://code.google.com/p/libarchive/source/diff?spec=svn2396&r=2347&format=side&path=/trunk/cpio/test/test_owner_parse.c>
PATCHFILES = 0001-Check-against-gids-0-and-1-for-root-on-Solaris.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://code.google.com/p/libarchive/

DEP_PKGS = CSWxz CSWbzip2 CSWiconv CSWlibxml2 CSWzlib CSWosslrt

EXTRA_INC = $(includedir)/cryptopp

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
