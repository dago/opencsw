GARNAME = xcb-util
GARVERSION = 0.3.5
CATEGORIES = x11

DESCRIPTION = The XCB utility library
define BLURB
endef

MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS = CSWgnulinks
REQUIRED_PKGS = CSWlibxcb
PACKAGES = CSWxcbutil

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CATALOGNAME = xcbutil

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

#EXTRA_CFLAGS = -D__solaris__

include gar/category.mk

# We need GNU gm4 as m4
PATH := /opt/csw/gnu:$(PATH)
