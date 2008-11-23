GARNAME = ogle_gui
GARVERSION = 0.9.2
CATEGORIES = gnome

DESCRIPTION = gtk user interface for Ogle DVD player 
define BLURB
A gtk graphical user interface for Ogle DVD player
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle_gui, depend prototype)

GARCOMPILER ?= GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
