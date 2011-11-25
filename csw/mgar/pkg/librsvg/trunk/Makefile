NAME = librsvg
VERSION = 2.34.0
CATEGORIES = lib

DESCRIPTION = Scalable Vector Graphics library
define BLURB
 This is librsvg - A high performance SVG rendering library associated with the Gnome Project.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

# Upstream develops on gcc only 
PATCHFILES += pdiff.patch
PATCHFILES += perceptualdiff.patch

VENDOR_URL = http://librsvg.sourceforge.net 

LICENSE = COPYING.LIB

PACKAGES += CSWlibrsvg2-2
SPKG_DESC_CSWlibrsvg2-2 = Scalable Vector Graphics library, librsvg-2.so.2
PKGFILES_CSWlibrsvg2-2 += $(call pkgfiles_lib,librsvg-2.so.2)
OBSOLETED_BY_CSWlibrsvg2-2  = CSWlibrsvg
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWpango
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWpng
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibgsf
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWglib2

PACKAGES += CSWlibrsvg-dev
SPKG_DESC_CSWlibrsvg-dev = Development files for librsvg-2.so.2
PKGFILES_CSWlibrsvg-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibrsvg-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWgtk2devel
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibcairo-dev

PACKAGES += CSWrsvg
SPKG_DESC_CSWrsvg += SVG to raster image conversion utility
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrsvg += CSWpng
RUNTIME_DEP_PKGS_CSWrsvg += CSWftype2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibcairo
RUNTIME_DEP_PKGS_CSWrsvg += CSWgtk2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibatk
RUNTIME_DEP_PKGS_CSWrsvg += CSWpango
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibcroco
RUNTIME_DEP_PKGS_CSWrsvg += CSWfconfig
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibgsf
RUNTIME_DEP_PKGS_CSWrsvg += CSWglib2

PACKAGES += CSWlibrsvg-gnome
PKGFILES_CSWlibrsvg-gnome = $(libdir)/gtk-2.0/.*
SPKG_DESC_CSWlibrsvg-gnome += Scalable Vector Graphics library - Gnome module
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWpango
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWpng
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWftype2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgsf
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWglib2

BUILD_DEP_PKGS += CSWlibxml2-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes --enable-static=no

# Won't work until libgsf-1 is 64bit
# BUILD64 = 1

STRIP_LIBTOOL = 1

include gar/category.mk
