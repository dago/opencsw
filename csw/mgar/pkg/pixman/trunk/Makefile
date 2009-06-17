GARNAME      = pixman
GARVERSION   = 0.15.12
CATEGORIES   = lib

DESCRIPTION = The pixel-manipulation library for X and cairo
define BLURB
endef

MASTER_SITES = http://www.cairographics.org/releases/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Same as from gar/x11/categories/x11/category.mk
EXTRA_CFLAGS = -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
EXTRA_CXXFLAGS = -xlibmil -xlibmopt -features=tmplife -norunpath

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-gtk

include gar/category.mk
