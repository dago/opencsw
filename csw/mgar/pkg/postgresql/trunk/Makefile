GARNAME = package
GARVERSION = 1.0
CATEGORIES = category

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpackage,)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
