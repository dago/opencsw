# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dconf
VERSION = 0.5.1
GARTYPE = v2

DESCRIPTION = low-level configuration system for glib
define BLURB
  dconf is a low-level configuration system. Its main purpose is to
  provide a backend to GSettings on platforms that dont already have
  configuration storage systems.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
GARCOMPILER = GNU

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_INC = $(prefix)/include/gtk-2.0
EXTRA_INC += $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/pango-1.0
EXTRA_INC += $(prefix)/lib/gtk-2.0/include/
EXTRA_INC += $(prefix)/include/gdk-pixbuf-2.0/
EXTRA_INC += $(prefix)/include/atk-1.0/

BUILD_DEP_PKGS += CSWlibdbusdev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWgtk2devel

RUNTIME_DEP_PKGS += CSWlibgio2-0-0
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWlibdbus

PACKAGES += CSWdconf
SPKG_DESC_CSWdconf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWdconf += CSWlibdconf0

PACKAGES += CSWlibdconf0
SPKG_DESC_CSWlibdconf0 = $(DESCRIPTION), library
PKGFILES_CSWlibdconf0 += $(call pkgfiles_lib,libdconf.so)

PACKAGES += CSWlibdconf-dev
SPKG_DESC_CSWlibdconf-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibdconf-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibdconf-dev += $(call baseisadirs,$(datadir),vala/vapi/dconf\.deps)
PKGFILES_CSWlibdconf-dev += $(call baseisadirs,$(datadir),vala/vapi/dconf\.vapi)
RUNTIME_DEP_PKGS_CSWlibdconf-dev += CSWlibdconf0

PATCHFILES += 0001-Use-statvfs-for-checking-filesystem-type.patch
PATCHFILES += 0002-Remove-linker-flags-remove-c89-request.patch
PATCHFILES += 0003-Add-gio-includes.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += CFLAGS="-std=c99 -D__EXTENSIONS__"

include gar/category.mk

