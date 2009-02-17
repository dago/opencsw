GARNAME = glib
GARVERSION = 2.18.4
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

PACKAGES = CSWglib2 CSWglib2devel
CATALOGNAME_CSWglib2 = glib2
CATALOGNAME_CSWglib2devel = glib2_devel
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
SPKG_DESC_CSWglib2devel = Low level core compatibility library for GTK+ and GNOME development

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

#See gnome bug 569889
PATCHFILES = gtkdoc-rebase.patch
#See http://defect.opensolaris.org/bz/show_bug.cgi?id=3366 for discussion on:
PATCHFILES += glib-typedetect.patch
PATCHFILES += checksum-test.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --enable-static
CONFIGURE_ARGS += --disable-gtk-doc

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

REQUIRED_PKGS_CSWglib2 = CSWggettext CSWiconv CSWsunmath
REQUIRED_PKGS_CSWglib2devel = CSWglib2 CSWggettext CSWiconv

TEST_TARGET =

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

PKGFILES_CSWglib2  = $(PKGFILES_RT)
PKGFILES_CSWglib2 += /opt/csw/share/locale/.*

include gar/category.mk
