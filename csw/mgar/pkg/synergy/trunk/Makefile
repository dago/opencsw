GARNAME = synergy
GARVERSION = 1.3.1
CATEGORIES = apps

DESCRIPTION = Synergy lets you easily share a single mouse and keyboard between multiple computer
define BLURB
endef

GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc3

SF_PROJ = $(GARNAME)2
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = synergy-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsynergy,depend)

PATCHFILES = missing-fonts.diff

CONFIGURE_ARGS = --prefix=$(prefix) --x-libraries=/usr/openwin/lib --x-includes=/usr/X/include

TEST_SCRIPTS =

include gar/category.mk
