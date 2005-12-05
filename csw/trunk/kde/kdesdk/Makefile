GARNAME = kdesdk
GARVERSION = 3.5.0
CATEGORIES = kde

DESCRIPTION = Software Development Kit for KDE (gcc3)
define BLURB
  LONG DESCRIPTION
endef

DISTFILES += $(call admfiles,CSWkdesdkgcc,depend)

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@echo " ==> $(GARNAME) build disabled"
	@true

#include ../category.mk
