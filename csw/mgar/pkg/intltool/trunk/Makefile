GARNAME = intltool
MAJOR_VER = 0.40
MINOR_VER = 5
GARVERSION = $(MAJOR_VER).$(MINOR_VER)
GNOME_SUBV = $(MAJOR_VER)
CATEGORIES = utils

DESCRIPTION =  A collection of tools for internationalization
define BLURB
  The intltool package is a set of tools for translating the contents of data files using the gettext translation framework.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWintltool,)

#No tests
TEST_SCRIPTS =

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
