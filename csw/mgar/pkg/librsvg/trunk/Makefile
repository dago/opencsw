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
PKGFILES_CSWlibrsvg-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibrsvg2-2
OBSOLETED_BY_CSWlibrsvg-dev = CSWlibrsvgdevel
CATALOGNAME_CSWlibrsvgdevel = librsvg_devel_stub

PACKAGES += CSWlibrsvg-doc
SPKG_DESC_CSWlibrsvg-doc = Documentation for librsvg
PKGFILES_CSWlibrsvg-doc = $(sharedstatedir)/gtk-doc/.*
ARCHALL_CSWlibrsvg-doc = 1
OBSOLETED_BY_CSWlibrsvg-doc = CSWlibrsvgdoc
CATALOGNAME_CSWlibrsvgdoc = librsvg_doc_stub

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

PACKAGES += CSWlibrsvggnome
CATALOGNAME_CSWlibrsvggnome = librsvg_gnome
PKGFILES_CSWlibrsvggnome = $(libdir)/gtk-2.0/.*
SPKG_DESC_CSWlibrsvggnome += Scalable Vector Graphics library - Gnome module
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWpango
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWpng
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWftype2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWlibgsf
RUNTIME_DEP_PKGS_CSWlibrsvggnome += CSWglib2

BUILD_DEP_PKGS += CSWlibxml2-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes --enable-static=no

# Won't work until libgsf-1 is 64bit
# BUILD64 = 1

STRIP_LIBTOOL = 1

include gar/category.mk
