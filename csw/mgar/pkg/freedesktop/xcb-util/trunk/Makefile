# $Id$

GARNAME = xcb-util
GARVERSION = 0.3.6
CATEGORIES = x11

DESCRIPTION = The XCB utility library
define BLURB
endef

MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

BUILD_DEP_PKGS = CSWgnulinks
RUNTIME_DEP_PKGS = CSWlibxcb
PACKAGES = CSWxcbutil

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CATALOGNAME = xcbutil

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES += xcb_size_hints_set_win_gravity-prototype.patch

include gar/category.mk

# We need GNU gm4 as m4
PATH := /opt/csw/gnu:$(PATH)
