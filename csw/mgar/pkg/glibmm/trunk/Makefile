NAME = glibmm
VERSION = 2.22.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = C++ interface to glib2
define BLURB
endef

SPKG_DESC_CSWglibmm_rt    = C++ interface to glib2 runtime libs
SPKG_DESC_CSWglibmm_devel = C++ interface to glib2 development files

#RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)
MAKE = gmake
EXTRA_CONFIGURE_EXPORTS = MAKE

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

include gar/category.mk
