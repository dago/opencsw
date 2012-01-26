NAME = intltool
MAJOR_VER = 0.40
MINOR_VER = 6
VERSION = $(MAJOR_VER).$(MINOR_VER)
GNOME_SUBV = $(MAJOR_VER)
CATEGORIES = utils
GARTYPE = v2
ARCHALL_CSWintltool = 1

DESCRIPTION =  A collection of tools for internationalization
define BLURB
  The intltool package is a set of tools for translating the contents of data files using the gettext translation framework.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWintltool = CSWperl CSWpmxmlparser

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
