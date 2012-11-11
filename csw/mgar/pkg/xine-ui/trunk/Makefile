NAME = xine-ui
VERSION = 0.99.4
GARTYPE = v1
CATEGORIES = gnome

DESCRIPTION = Xine media player user interface.
define BLURB
    # Blurb goes here
endef

SF_PROJECT = xine
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LIBDEPS = lib/xine-lib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
