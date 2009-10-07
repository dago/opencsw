GARNAME = libmatio
GARVERSION = 1.3.3
CATEGORIES = lib

DESCRIPTION = An ISO C library for reading and writing Matlab MAT files
define BLURB
endef

SF_PROJ = matio
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include gar/category.mk
