# $Id$

NAME = xcb-util
VERSION = 0.3.6
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = The XCB utility library
define BLURB
endef

SPKG_SOURCEDIR = http://xcb.freedesktop.org/XcbUtil/
MASTER_SITES = http://xcb.freedesktop.org/dist/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

RUNTIME_DEP_PKGS = CSWlibxcb
BUILD_DEP_PKGS = CSWgnulinks $(RUNTIME_DEP_PKGS)
PACKAGES = CSWxcbutil

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CATALOGNAME = xcbutil

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES += xcb_size_hints_set_win_gravity-prototype.patch

include gar/category.mk

# We need GNU gm4 as m4
PATH := /opt/csw/gnu:$(PATH)
