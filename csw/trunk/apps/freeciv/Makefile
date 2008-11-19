GARNAME = freeciv
GARVERSION = 2.1.6
CATEGORIES = apps

DESCRIPTION = a free turn-based multiplayer strategy game
define BLURB
Freeciv is a Free and Open Source empire-building strategy game inspired by the history of human civilization. The game commences in prehistory and your mission is to lead your tribe from the stone age to the space age...
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWfreeciv, depend prototype )

GARCOMPILER = GNU

PATCHFILES = dataio.c.diff

TEST_SCRIPTS =

CONFIGURE_ARGS = LDFLAGS='-L/opt/csw/lib -lm'
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-included-gettext

include ../category.mk
