GARNAME = octave
GARVERSION = 3.2.3
CATEGORIES = apps

DESCRIPTION = The GNU Octave language for numerical computations
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

