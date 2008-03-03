GARNAME = koffice
GARVERSION = 1.5.1
CATEGORIES = kde

DESCRIPTION = KDE Web Development Environment (gcc3)
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = $(KDE_ROOT)/$(KDE_DIST)/$(GARNAME)-$(GARVERSION)/src/
#DISTFILES   += Templates, addons, etc...
DISTFILES   += $(call admfiles,CSWkofficegcc,)
DISTFILES   += $(call admfiles,CSWkofficeaddons,)

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
