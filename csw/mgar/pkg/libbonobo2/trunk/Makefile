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

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check


CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
