GARNAME = gconf2
GNOME_PROJ = GConf
GARVERSION = 2.28.1
CATEGORIES = gnome

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

BUILD64 = 1
NOISAEXEC = 1

TEST_TARGET = check

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc


include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
