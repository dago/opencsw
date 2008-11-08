GARNAME = freeciv
GARVERSION = 2.0.10
CATEGORIES = apps

DESCRIPTION = a free turn-based multiplayer strategy game
define BLURB
  Players of the Civilization® series by Microprose® should feel at home, since one aim of Freeciv is to have optional modes (called rulesets) with compatible rules.

Freeciv is maintained by an international team of coders and enthusiasts, and is easily one of the most fun and addictive network games out there!

That also means it has very extensive multilanguage support, something rare in games. 
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWfreeciv, depend )

GARCOMPILER = GNU

PATCHFILES = dataio.c.diff

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
