NAME = plib
VERSION = 1.8.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A Suite of Portable Game Libraries
define BLURB
endef

MASTER_SITES = http://plib.sourceforge.net/dist/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://plib.sourceforge.net

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

# This library contains only static libs, so it is more like a developer library
MERGE_EXCLUDE_STATICLIBS =

include gar/category.mk
