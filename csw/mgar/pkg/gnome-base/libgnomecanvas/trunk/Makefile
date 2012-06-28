NAME = libgnomecanvas
VERSION = 2.30.3
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNOME Canvas Lib
define BLURB
  The libgnomecanvas package contains the GNOME canvas library. It is an engine
  for structured graphics and one of the essential GNOME libraries.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWlibgnomecanvas2-0
SPKG_DESC_CSWlibgnomecanvas2-0 = GNOME 2 canvas library, libgnomecanvas-2.so.0
PKGFILES_CSWlibgnomecanvas2-0 += $(call pkgfiles_lib,libgnomecanvas-2.so.0)
PKGFILES_CSWlibgnomecanvas2-0 += $(sharedstatedir)/locale/.*
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomecanvas2-0 += CSWlibatk1-0-0
OBSOLETED_BY_CSWlibgnomecanvas2-0 += CSWlibgnomecanvas

PACKAGES += CSWlibgnomecanvas-dev
SPKG_DESC_CSWlibgnomecanvas-dev = Development files for libgnomecanvas-2.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgnomecanvas-dev += CSWlibgnomecanvas2-0

LICENSE = COPYING.LIB

BUILD64_LIBS_ONLY = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
