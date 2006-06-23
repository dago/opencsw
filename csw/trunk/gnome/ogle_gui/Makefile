GARNAME = ogle_gui
GARVERSION = 0.9.2
CATEGORIES = gnome

DESCRIPTION = Ogle graphical user interface
define BLURB
Ogle graphical user interface
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle_gui, depend prototype)

GARCOMPILER ?= GNU

CONFIGURE_ARGS = $(DIRPATHS)

ENABLE_TEST = 0

include ../category.mk
