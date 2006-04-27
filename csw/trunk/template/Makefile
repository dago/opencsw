GARNAME = SDL
GARVERSION = 1.2.9
CATEGORIES = lib

DESCRIPTION = Simple DirectMedia Layer library
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = http://www.libsdl.org/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpackage,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
