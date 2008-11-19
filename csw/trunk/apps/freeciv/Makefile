### BUILD.NOTES
#
#   need to patch C99.m4 file to remove check for stdint.h
#   Need to find all header files that have stdint.h and replace
#   with inttypes.h 


GARNAME = freeciv
GARVERSION = 2.1.6
CATEGORIES = apps

DESCRIPTION = a free turn-based multiplayer strategy game
define BLURB
Freeciv is a Free and Open Source empire-building strategy game inspired by the history of human civilization. The game commences in prehistory and your mission is to lead your tribe from the stone age to the space age...
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWfreeciv, depend )

GARCOMPILER = GNU

PATCHFILES = dataio.c.diff

TEST_SCRIPTS =

CONFIGURE_ARGS = LDFLAGS=-lm
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-nls

include ../category.mk
