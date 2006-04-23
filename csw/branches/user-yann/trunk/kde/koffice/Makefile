GARNAME = koffice
GARVERSION = 1.4.2
CATEGORIES = kde

DESCRIPTION = KDE Web Development Environment (gcc3)
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = $(KDE_ROOT)/$(GARNAME)-$(GARVERSION)/src/
#DISTFILES   += Templates, addons, etc...
DISTFILES   += $(call admfiles,CSWkofficegcc,)
DISTFILES   += $(call admfiles,CSWkofficeaddons,)

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
