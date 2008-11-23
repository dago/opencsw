GARNAME = openal
GARVERSION = 0.0.8
CATEGORIES = lib

DESCRIPTION = openal - A 3D positional spatialized sound library (gcc3)
define BLURB
endef

MASTER_SITES = http://www.openal.org/openal_webstf/downloads/

DISTFILES  =$(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWopenal,depend)

PATCHFILES = al_main.diff

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-esd

include gar/category.mk

#pre-configure:
#	( cd $(WORKSRC) ; ./autogen.sh )
#	@$(MAKECOOKIE)
