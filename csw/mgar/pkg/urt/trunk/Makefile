NAME = urt
VERSION = 3.1b1
DISTVERSION = 3.1.b.1
CATEGORIES = lib

DESCRIPTION = Utah Raster Toolkit containing RLE encoding
define BLURB
endef

# It is hard to find the sources nowadays
SF_PROJ = gnuwin32
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(DISTVERSION)-2-src.zip

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-2-src.zip

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
