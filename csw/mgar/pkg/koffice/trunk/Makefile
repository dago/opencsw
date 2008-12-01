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
# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
