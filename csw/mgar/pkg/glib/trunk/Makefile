GARNAME = glib
GARVERSION = 1.3.15
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists.
endef

PACKAGES = CSWglib CSWglibdevel
CATALOGNAME_CSWglib2 = glib
CATALOGNAME_CSWglib2devel = glib2devel
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
SPKG_DESC_CSWglib2devel = Low level core compatibility library for GTK+ and GNOME development

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

#PATCHFILES  = glib-typedetect.patch
#PATCHFILES += checksum-test.patch
#PATCHFILES += gsize.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv
#CONFIGURE_ARGS += --enable-static

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

#REQUIRED_PKGS_CSWglib2 = CSWggettextrt CSWiconv
#REQUIRED_PKGS_CSWglib2devel = CSWglib2 CSWggettextrt CSWiconv

TEST_TARGET = check

#provided by iconv
#MERGE_EXCLUDE_FILES = .*/charset.alias

#PKGFILES_CSWglib2  = $(PKGFILES_RT)
#PKGFILES_CSWglib2 += /opt/csw/share/locale/.*

include gar/category.mk
