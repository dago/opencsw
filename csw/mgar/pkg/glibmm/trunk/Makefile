GARNAME = glibmm
GARVERSION = 2.20.0
CATEGORIES = lib

DESCRIPTION = C++ interface to glib2
define BLURB
endef

SPKG_DESC_CSWglibmm_rt    = C++ interface to glib2 runtime libs
SPKG_DESC_CSWglibmm_devel = C++ interface to glib2 development files

#REQUIRED_PKGS = CSWggettextrt CSWiconv

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)
MAKE = gmake
EXTRA_CONFIGURE_EXPORTS = MAKE

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_TARGET = check

include gar/category.mk
