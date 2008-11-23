GARNAME = PACKAGE
GARVERSION = 1.0
CATEGORIES = CATEGORY

DESCRIPTION = BRIEF DESCRIPTION
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpackage,)

CONFIGURE_ARGS = $(DIRPATHS)

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@true

#include gar/category.mk
