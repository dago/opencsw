# $Id$
GARNAME = libxml++
GARVERSION = 2.30.1
CATEGORIES = lib

DESCRIPTION = C++ wrapper for the libxml XML parser library
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_CONFIGURE_EXPORTS = MAKE
MAKE = gmake

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
