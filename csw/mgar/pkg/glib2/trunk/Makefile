GARNAME = glib
GARVERSION = 2.18.4
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES  = $(call admfiles,CSWglib2,)
DISTFILES += $(call admfiles,CSWglib2devel,)
DISTFILES += $(GARNAME)-$(GARVERSION).tar.bz2

#See gnome bug 569889
PATCHFILES = gtkdoc-rebase.patch

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

PKGFILES_CSWglib2  = $(PKGFILES_RT)
PKGFILES_CSWglib2 += /opt/csw/share/locale/.*

include gar/category.mk
