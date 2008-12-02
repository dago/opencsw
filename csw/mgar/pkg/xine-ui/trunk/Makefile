GARNAME = xine-ui
GARVERSION = 0.99.4
CATEGORIES = gnome

DESCRIPTION = Xine media player user interface.
define BLURB
    # Blurb goes here
endef

SF_PROJ = xine
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LIBDEPS = lib/xine-lib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
