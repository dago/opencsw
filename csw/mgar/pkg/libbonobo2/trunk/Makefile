GARNAME = libbonobo
GARVERSION = 2.24.2
CATEGORIES = gnome

DESCRIPTION = GNOME component and compound document system
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
