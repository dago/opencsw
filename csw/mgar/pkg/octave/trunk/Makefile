NAME = octave
VERSION = 3.2.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The GNU Octave language for numerical computations
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

