NAME = libmatio
VERSION = 1.3.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = An ISO C library for reading and writing Matlab MAT files
define BLUECTRB
endef

SF_PROJ = matio
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include