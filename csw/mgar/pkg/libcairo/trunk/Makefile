NAME = cairo
VERSION = 1.10.2
CATEGORIES = lib

DESCRIPTION = The Cairo 2D Graphics Library
define BLURB
  Cairo is a 2D graphics library with support for multiple output devices.
  Currently supported output targets include the X Window System, Quartz, Win32,
  image buffers, PostScript, PDF, and SVG file output. Experimental backends
  include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES = http://www.cairographics.org/releases/
DISTFILES = $(DISTNAME).tar.gz 

# Apply patch until this is fixed:
#   https://bugs.freedesktop.org/show_bug.cgi?id=37916
PATCHFILES += 0001-Use-detected-EGREP-instead-of-generic-grep.patch

PACKAGES += CSWlibcairo2
SPKG_DESC_CSWlibcairo2 = The Cairo 2D Graphics Library, libcairo.so.2
PKGFILES_CSWlibcairo2 = $(call pkgfiles_lib,libcairo.so.2)
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWpng
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibcairo2 += CSWlibpixman1-0
OBSOLETED_BY_CSWlibcairo2 = CSWlibcairo

PACKAGES += CSWlibcairo-script-interpreter2
SPKG_DESC_CSWlibcairo-script-interpreter2 = The Cairo 2D Graphics Library, libcairo-script-interpreter.so.2
PKGFILES_CSWlibcairo-script-interpreter2 = $(call pkgfiles_lib,libcairo-script-interpreter.so.2)
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWpng
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibcairo-script-interpreter2 += CSWlibpixman1-0
OBSOLETED_BY_CSWlibcairo-script-interpreter2 = CSWlibcairo

PACKAGES += CSWlibcairo-gobject2
SPKG_DESC_CSWlibcairo-gobject2 = The Cairo 2D Graphics Library, libcairo-gobject.so.2
PKGFILES_CSWlibcairo-gobject2 = $(call pkgfiles_lib,libcairo-gobject.so.2)
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWpng
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWlibcairo-gobject2 += CSWglib2
OBSOLETED_BY_CSWlibcairo-gobject2 = CSWlibcairo

PACKAGES += CSWlibcairo-dev
SPKG_DESC_CSWlibcairo-dev = Development files for libcairo.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibcairo-dev += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibcairo-dev += CSWlibcairo-script-interpreter2
RUNTIME_DEP_PKGS_CSWlibcairo-dev += CSWlibcairo-gobject2
# This is important or pkgconfig on cairo will fail
RUNTIME_DEP_PKGS_CSWlibcairo-dev += CSWlibpixman-dev
OBSOLETED_BY_CSWlibcairo-dev = CSWlibcairodevel
CATALOGNAME_CSWlibcairodevel = libcairo_devel_stub

PACKAGES += CSWlibcairo-doc
SPKG_DESC_CSWlibcairo-doc = $(DESCRIPTION) documentation
PKGFILES_CSWlibcairo-doc += $(sharedstatedir)/gtk-doc.*
ARCHALL_CSWlibcairo-doc = 1
OBSOLETED_BY_CSWlibcairo-doc = CSWlibcairodoc
CATALOGNAME_CSWlibcairodoc = libcairo_doc_stub

# We do NOT want -L/opt/csw/lib in there as the pathes are detected properly and this disturbs libtool later on
LINKER_FLAGS =

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-full-testing
CONFIGURE_ARGS += --enable-xlib=yes
CONFIGURE_ARGS += --enable-xlib-xrender=yes
CONFIGURE_ARGS += --enable-ft=yes
CONFIGURE_ARGS += --with-x 
CONFIGURE_ARGS += --enable-png=yes
CONFIGURE_ARGS += --enable-ps=yes
CONFIGURE_ARGS += --enable-pdf=yes
CONFIGURE_ARGS += --enable-svg=yes
CONFIGURE_ARGS += --enable-xcb=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --enable-test-surfaces=yes 

# Use custom lroundf at least on Solaris 9 as it does not provide its own
CONFIGURE_ARGS += --disable-some-floating-point

# This is broken due to missing stdint.h and use of setenv(3c)
CONFIGURE_ARGS += --enable-trace=no

# There are many source tests failing
SKIPTEST ?= 1

include gar/category.mk

# configure has problems with non-gnu utilities
PATH := /opt/csw/gnu:$(PATH)
