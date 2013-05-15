# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dconf
VERSION = 0.5.1
GARTYPE = v2

DESCRIPTION = Low-level configuration system for glib
define BLURB
  dconf is a low-level configuration system. Its main purpose is to
  provide a backend to GSettings on platforms that dont already have
  configuration storage systems.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2
GARCOMPILER = GNU
# g-ir-scanner chokes on linking an uninstalled library if LINKER_IGNORE isn't reset,
# it invokes gcc directly for linking
LINKER_IGNORE =
REINPLACE_USRSHARE += editor/dconf-model.c

# for xproto
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# the package Makefile fails to add these to the header search path
EXTRA_INC = $(prefix)/include/gtk-2.0
EXTRA_INC += $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/pango-1.0
EXTRA_INC += $(prefix)/lib/gtk-2.0/include/
EXTRA_INC += $(prefix)/include/gdk-pixbuf-2.0/
EXTRA_INC += $(prefix)/include/atk-1.0/

BUILD_DEP_PKGS += CSWlibdbus-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev

# Add more dependencies as suggested by Laurent Blume
BUILD_DEP_PKGS_CSWdconf-editor += CSWlibfreetype-dev
BUILD_DEP_PKGS_CSWdconf-editor += CSWfconfig-dev
BUILD_DEP_PKGS_CSWdconf-editor += CSWlibgtk2-dev
BUILD_DEP_PKGS_CSWdconf-editor += CSWsunx11devel
BUILD_DEP_PKGS_CSWdconf-editor += CSWlibpcre-dev
BUILD_DEP_PKGS_CSWdconf-editor += CSWlibpng-dev

# as suggested by checkpkg
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibintl8
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibdconf0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWpango
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWdconf-editor += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibdconf0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibdconf0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibdconf0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibdconf0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibdconf0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWdconf += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWdconf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWdconf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWdconf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWdconf += CSWlibgio2-0-0

PACKAGES += CSWlibdconf-dev
SPKG_DESC_CSWlibdconf-dev = $(DESCRIPTION), development files
PKGFILES_CSWlibdconf-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibdconf-dev += $(call baseisadirs,$(datadir),vala/vapi/dconf\.deps)
PKGFILES_CSWlibdconf-dev += $(call baseisadirs,$(datadir),vala/vapi/dconf\.vapi)
RUNTIME_DEP_PKGS_CSWlibdconf-dev += CSWlibdconf0

PACKAGES += CSWlibdconf0
SPKG_DESC_CSWlibdconf0 = $(DESCRIPTION), library
PKGFILES_CSWlibdconf0 += $(call pkgfiles_lib,libdconf.so.0)

PACKAGES += CSWdconf-editor
SPKG_DESC_CSWdconf-editor = $(DESCRIPTION), configuration editor
PKGFILES_CSWdconf-editor += $(bindir)/dconf-editor

PACKAGES += CSWdconf
SPKG_DESC_CSWdconf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWdconf += CSWlibdconf0
# PKGFILES is catchall

PATCHFILES += 0001-Use-statvfs-for-checking-filesystem-type.patch
PATCHFILES += 0002-Remove-linker-flags-remove-c89-request.patch
PATCHFILES += 0003-Add-gio-includes.patch
PATCHFILES += 0000-Replace-posix_fallocate-with-ftruncate.patch
PATCHFILES += 0006-mkdtemp-replacement.patch

CONFIGURE_ARGS = $(DIRPATHS)
# package must be compiled in C99 mode; add __EXTENSIONS__ so the headers expose
# all interfaces that go beyong C99, cf man standards.5
EXTRA_CFLAGS += -std=c99 -D__EXTENSIONS__

# see above comment for LINKER_IGNORE
CHECKPKG_OVERRIDES_CSWdconf += soname-unused
CHECKPKG_OVERRIDES_CSWdconf-editor += soname-unused
CHECKPKG_OVERRIDES_CSWlibdconf0 += soname-unused

include gar/category.mk

