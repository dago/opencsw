NAME = ogle_gui
VERSION = 0.9.2
GARTYPE = v1
CATEGORIES = gnome

DESCRIPTION = gtk user interface for Ogle DVD player 
define BLURB
A gtk graphical user interface for Ogle DVD player
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle_gui, depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER ?= GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
