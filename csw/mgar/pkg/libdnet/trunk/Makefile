# $Id$
NAME = libdnet
VERSION = 1.12
CATEGORIES = lib
GARTYPE = v2

# ! .so extension missing http://code.google.com/p/libdnet/issues/detail?id=18
# An idea:
#   http://www.v7w.com/debian/libtool-missing_so.html
#   http://www.v7w.com/debian/libtool-updating.html

DESCRIPTION = A simplified, portable interface to several low-level networking routines
define BLURB
endef

VENDOR_URL = http://code.google.com/p/libdnet/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
