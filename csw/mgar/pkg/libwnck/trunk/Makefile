GARNAME = libwnck
GARVERSION = 2.29.92
CATEGORIES = lib

DESCRIPTION = Library used for writing pagers and tasks lists
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://ftp.gnome.org/pub/GNOME/sources/libwnck/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# Problem: Requested 'gtk+-2.0 >= 2.19.7' but version of GTK+ is 2.16.5

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# Needed for GNU gettext
PATH := /opt/csw/gnu:$(PATH)
