NAME = kdesdk
CATEGORIES = kde
GARTYPE = v2

DESCRIPTION = Software Development Kit for KDE (gcc3)
define BLURB
  LONG DESCRIPTION
endef

DISTFILES += $(call admfiles,CSWkdesdkgcc,)

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@echo " ==> $(NAME) build disabled"
	@true

#include gar/category.mk
