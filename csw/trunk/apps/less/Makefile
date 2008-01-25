GARNAME = less
GARVERSION = 418
CATEGORIES = apps

DESCRIPTION = less
define BLURB
  less
endef

#MASTER_SITES = http://pkg-config.freedesktop.org/releases/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWless,depend)

PREREQUISITE_PKGS = CSWncurses CSWggettext

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include ../category.mk
