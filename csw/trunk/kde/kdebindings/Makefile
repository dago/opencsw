GARNAME = kdebindings
GARVERSION = 3.5.0
CATEGORIES = kde

DESCRIPTION = Key bindings for KDE (gcc3)
define BLURB
  LONG DESCRIPTION
endef

DISTFILES += $(call admfiles,CSWkdebindingsgcc,depend)

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@echo " ==> $(GARNAME) build disabled"
	@true

#include ../category.mk
