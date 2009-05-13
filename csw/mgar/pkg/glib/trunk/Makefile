GARNAME = glib
# Most applications bind to libglib-1.2.so.0, so stick to 1.2.x for the moment
GARVERSION = 1.2.10
#GARVERSION = 1.3.15
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists.
endef

SPKG_DESC_CSWglib2 = Utility library commonly associated with GNOME programs

REQUIRED_PKGS = CSWggettextrt CSWiconv

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# glib 1.x doesn't seem to be 64 bit clean
#BUILD64 = 1
#NO_ISAEXEC = 1

# Only needed for 1.3.x
#EXTRA_BUILD_EXPORTS = SGML_CATALOG_FILES
#SGML_CATALOG_FILES = $(sysconfdir)/sgml/catalog

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

include gar/category.mk
