# $Id$
NAME = libdbi-drivers
VERSION = 0.8.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Drivers for the libdbi database abstraction layer
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
