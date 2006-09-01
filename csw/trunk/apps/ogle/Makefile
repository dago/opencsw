GARNAME = ogle
GARVERSION = 0.9.2
CATEGORIES = apps

DESCRIPTION = opensource DVD player with DVD menu support
define BLURB
  opensource DVD player with DVD menu support
endef

MASTER_SITES = http://www.dtek.chalmers.se/groups/dvd/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWogle,)

PATCHFILES = solaris-audio.diff

CONFIGURE_ARGS = $(DIRPATHS)

ENABLE_TEST=0

include ../category.mk
