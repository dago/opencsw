GARNAME = apg
GARVERSION = 2.2.3
CATEGORIES = utils

DESCRIPTION = Automated Password Generator
define BLURB
endef

MASTER_SITES = http://www.adel.nursat.kz/apg/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWapg)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
