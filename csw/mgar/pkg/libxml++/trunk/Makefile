# $Id$
NAME = libxml++
VERSION = 2.30.1
CATEGORIES = lib

DESCRIPTION = C++ wrapper for the libxml XML parser library
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_CONFIGURE_EXPORTS = MAKE
MAKE = gmake

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
