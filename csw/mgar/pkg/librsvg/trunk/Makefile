NAME = librsvg
VERSION = 2.36.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Scalable Vector Graphics library
define BLURB
 This is librsvg - A high performance SVG rendering library associated with the Gnome Project.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  =xzDISTNAME).tar.bz2

# Upstream develops on gcc only 
PATCHFILES += pdiff.patch
PATCHFILES += perceptualdiff.patch

s://wiki.gnome.org/LibRsvg

LICENSE = COPYING.LIB

GARCOMPILER = GCC4NSPKG_CONFIG_PATH=/opt/csw/lib/pkgconfigNSE = COPYING.LIB

# We need the new glib only available on Solaris 10
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# TBD: There are more missing
BUILD_DEP_PKGS +BUILD_DEP_PKGS += CSWlibpng16KGS += CSWlibxml2-dev

PACKAGES += CSWlibrsvg2-2
SPKG_DESC_CSWlibrsvg2-2 = Scalable Vector Graphics library, librsvg-2.so.2
PKGFILES_CSWlibrsvg2-2 += $(call pkgfiles_lib,librsvg-2.so.2)
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 +=RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibgdk-pixbuf2-2 +=RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibpangocairo1-0-0
= CSWlibglib2-0-0
OBSOLETED_BY_CSWlibrsvg2-2  = CSWlibrsvg

PACKAGES += CSWlibrsvg-dev
SPKG_DESC_CSWlibrsvg-dev = Development files for librsvg-2.so.2
PKGFILES_CSWlibrsvg-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibrsvg-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWllibgtk2-devv += CSWgtk2devel
RUNTIME_DEP_PKGS_CSWlibrsvg-dev += CSWlibcairo-dev

PACKAGES += CSWrsvg
SPKG_DESC_CSWrsvg += SVG to raster image conversion utility
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_cairo2SWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_Cdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibgcc-s1+= CSWlibgio2-0-0

PACKAGES += CSWlibrsvg-gnome
SPKG_DESC_CSWlibrsvg-gnome += Scalable Vector Graphics library - Gnome module
PKGFILES_CSWlibrsvg-gnome += $(call baseisadirs,$(libdir),gtk-2.0/.*)
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgtk-x11-nome +RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgmodule2-0-0

###
# Needed for the Solaris ld bug
ifeq ($(shell /usr/bin/uname -p),sparc)
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibpng16-16
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibcroco
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg-gnome += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibpng16-16
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibcroco
RUNTIME_DEP_PKGS_CSWrsvg += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrsvg2-2 += CSWlibpng16-16
endif
###+= CSWlibgio2-0-0

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared=yes --enabat fails on sparc
CONFIGURE_ARGS += --enable-introspections --enable-static=no
# This causes an configure abort
CONFIGURE_ARGS += --disable-Bsymbolic

BUILD64 = 1
ISAEXEC = 1

ST# https://bugzilla.gnome.org/show_bug.cgi?id=694649
SKIPTEST 1

STRIP_LIBTOOL = 1

EXTRA_MERGE_DIRS_isa-extra = $(bindir)

include