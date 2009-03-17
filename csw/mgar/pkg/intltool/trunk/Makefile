GARNAME = intltool
MAJOR_VER = 0.40
MINOR_VER = 6
GARVERSION = $(MAJOR_VER).$(MINOR_VER)
GNOME_SUBV = $(MAJOR_VER)
CATEGORIES = utils

DESCRIPTION =  A collection of tools for internationalization
define BLURB
  The intltool package is a set of tools for translating the contents of data files using the gettext translation framework.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_TARGET = check

REQUIRED_PKGS_CSWintltool = CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
