NAME = gegl
VERSION = 0.1.8
CATEGORIES = gnome

DESCRIPTION = A graph based image processing framework
define BLURB
endef

MASTER_SITES = http://ftp.gtk.org/pub/gegl/$(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')/
DISTFILES += $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Enforce-array-size-even-if-zero-length.patch
PATCHFILES += 0002-Keep-norunpath-during-linkage.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://gegl.org/

BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibrsvg-dev
BUILD_DEP_PKGS += CSWlibsdl-dev
BUILD_DEP_PKGS += CSWasciidoc
BUILD_DEP_PKGS += CSWlua

PACKAGES += CSWlibgegl0-1-0
SPKG_DESC_CSWlibgegl0-1-0 = A graph based image processing framework library, libgegl-0.1.so.0
PKGFILES_CSWlibgegl0-1-0 += $(call pkgfiles_lib,libgegl-0.1.so.0)
PKGFILES_CSWlibgegl0-1-0 += $(call baseisadirs,$(libdir),gegl-0.1/.*)
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibbabl0-1-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWjasper
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibrsvg2-2
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWilmbase
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWlibgegl0-1-0 += CSWlibgio2-0-0
OBSOLETED_BY_CSWlibgegl0-1-0 += CSWlibgegl

PACKAGES += CSWlibgegl-dev
SPKG_DESC_CSWlibgegl-dev = Development files for 
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgegl-dev += CSWlibgegl0-1-0

PACKAGES += CSWgegl
SPKG_DESC_CSWgegl = The gegl image processing utility
PKGFILES_CSWgegl += $(call baseisadirs,$(bindir),gegl)
RUNTIME_DEP_PKGS_CSWgegl += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgegl += CSWlibbabl0-1-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibgegl0-1-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgegl += CSWlibgmodule2-0-0

# There are zero-sized structs/unions used
EXTRA_CXXFLAGS += -features=extensions
EXTRA_CXXFLAGS += -features=zla -feat
EXTRA_CXXFLAGS += -norunpath

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS += $(RUNPATH_LINKER_FLAGS)

# librsvg is missing
BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

# For diff option --report-identical-files
PATH := /opt/csw/gnu:$(PATH)
