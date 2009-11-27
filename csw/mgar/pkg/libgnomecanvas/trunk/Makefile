GARNAME = libgnomecanvas
GARVERSION = 2.26.0
CATEGORIES = lib

DESCRIPTION = GNOME Canvas Lib
define BLURB
  The libgnomecanvas package contains the GNOME canvas library. It is an engine
  for structured graphics and one of the essential GNOME libraries.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)

BUILD64 = 1
NO_ISAEXEC = 1

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
