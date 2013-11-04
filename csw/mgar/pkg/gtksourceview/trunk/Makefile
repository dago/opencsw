NAME = gtksourceview
VERSION = 2.11.2
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = A text widget with features typical of a source code editor

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES += $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://live.gnome.org/GtkSourceView

PACKAGES += CSWlibgtksourceview2-0-0
SPKG_DESC_CSWlibgtksourceview2-0-0 = A text widget with features typical of a source code editor
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtksourceview2-0-0 += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibgtksourceview2-0-0 += CSWgtksourceview

# Harmless
CHECKPKG_OVERRIDES_CSWlibgtksourceview2-0-0 += soname-unused|libthread.so.1|is|needed|by|/opt/csw/lib/libgtksourceview-2.0.so.0.0.0|but|never|used
CHECKPKG_OVERRIDES_CSWlibgtksourceview2-0-0 += soname-unused|libthread.so.1|is|needed|by|/opt/csw/lib/sparcv9/libgtksourceview-2.0.so.0.0.0|but|never|used

PACKAGES += CSWlibgtksourceview-dev
SPKG_DESC_CSWlibgtksourceview-dev = Development files for libgtksourceview-2.0.so.0
PKGFILES_CSWlibgtksourceview-dev  += $(PKGFILES_DEVEL)
PKGFILES_CSWlibgtksourceview-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWlibgtksourceview-dev += CSWlibgtksourceview2-0-0

STRIP_LIBTOOL = 1

BUILD64 = 1

# Work around for old pango stuff:
#   http://lists.opencsw.org/pipermail/maintainers/2013-April/017892.html
EXTRA_CFLAGS += -DG_CONST_RETURN=const

# This is also deprecated
EXTRA_CFLAGS += -DG_UNICODE_COMBINING_MARK

EXTRA_CONFIGURE_EXPORTS += XGETTEXT MSGMERGE MSGFMT
CONFIGURE_ENV_XGETTEXT = $(bindir_install)/gxgettext
CONFIGURE_ENV_MSGMERGE = $(bindir_install)/gmsgmerge
CONFIGURE_ENV_MSGFMT = $(bindir_install)/gmsgfmt

CONFIGURE_ARGS += $(DIRPATHS)
# We are missing Gtk-2.0.gir
CONFIGURE_ARGS += --enable-introspection=no

# We probably don't have a display
SKIPTEST ?= 1

include gar/category.mk
