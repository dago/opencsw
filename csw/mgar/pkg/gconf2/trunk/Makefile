GARNAME = gconf2
GNOME_PROJ = GConf
GARVERSION = 2.28.0
CATEGORIES = lib

DESCRIPTION = GNOME configuration database system
define BLURB
  GConf is a system for storing application preferences. It is intended
  for user preferences; not configuration of something like Apache, or
  arbitrary data storage.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTNAME = GConf-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://projects.gnome.org/gconf/

CONFIGURE_ARGS  = $(DIRPATHS)

BUILD64 = 1
NO_ISAEXEC = 1

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
