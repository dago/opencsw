NAME = libgnome
VERSION = 2.32.1
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = The main GNOME library

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = COPYING.LIB

PACKAGES += CSWlibgnome2-0
SPKG_DESC_CSWlibgnome2-0 = The main GNOME library, libgnome-2.so.0
PKGFILES_CSWlibgnome2-0 += $(call pkgfiles_lib,libgnome-2.so.0)
PKGFILES_CSWlibgnome2-0 += $(sharedstatedir)/locale/.*
PKGFILES_CSWlibgnome2-0 += $(sysconfdir)/.*
PKGFILES_CSWlibgnome2-0 += $(call baseisadirs,$(libdir),bonobo/.*)
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgnome2-0 += CSWlibbonobo2
OBSOLETED_BY_CSWlibgnome2-0 += CSWlibgnome

PACKAGES += CSWlibgnome-dev
SPKG_DESC_CSWlibgnome-dev = Development files for libgnome-2.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibgnome-dev += CSWlibgio2-0-0

# These are just docs
CHECKPKG_OVERRIDES_CSWlibgnome-dev += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/libgnome/libgnome-gnome-program.html
CHECKPKG_OVERRIDES_CSWlibgnome-dev += file-with-bad-content|/usr/share|root/opt/csw/share/gtk-doc/html/libgnome/libgnome-gnome-sound.html

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-canberra

include gar/category.mk

# For GNU gettext
PATH := /opt/csw/gnu:$(PATH)
