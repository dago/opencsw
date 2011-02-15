NAME      = libcairo
VERSION   = 1.10.2
CATEGORIES   = lib

DESCRIPTION  = The Cairo 2D Graphics Library
define BLURB
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System, Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTNAME      = cairo-$(VERSION)
DISTFILES     = $(DISTNAME).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibcairo
CATALOGNAME_CSWlibcairo = libcairo
SPKG_DESC_CSWlibcairo = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWlibcairo += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibcairo += CSWftype2
RUNTIME_DEP_PKGS_CSWlibcairo += CSWpixman
RUNTIME_DEP_PKGS_CSWlibcairo += CSWpng
RUNTIME_DEP_PKGS_CSWlibcairo += CSWzlib
RUNTIME_DEP_PKGS_CSWlibcairo += CSWexpat
RUNTIME_DEP_PKGS_CSWlibcairo += CSWiconv

PACKAGES += CSWlibcairodevel
CATALOGNAME_CSWlibcairodevel = libcairo_devel
SPKG_DESC_CSWlibcairodevel = $(DESCRIPTION) development package
PKGFILES_CSWlibcairodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibcairodevel += $(docdir)/libcairo_devel/.*
RUNTIME_DEP_PKGS_CSWlibcairodevel = CSWlibcairo

PACKAGES += CSWlibcairodoc
CATALOGNAME_CSWlibcairodoc = libcairo_doc
SPKG_DESC_CSWlibcairodoc = $(DESCRIPTION) documentation
PKGFILES_CSWlibcairodoc    = $(sharedstatedir)/gtk-doc.*
PKGFILES_CSWlibcairodoc   += $(docdir)/libcairo_doc/.*
ARCHALL_CSWlibcairodoc = 1

BUILD_DEP_PKGS = CSWlibspectre 

# imagediff in testsuite needs -lsocket
# EXTRA_LDFLAGS = -lsocket -lnsl

# We don't need it and if defined linking breaks if an old Cairo is installed
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

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

include gar/category.mk

# configure has problems with non-gnu utilities
PATH := /opt/csw/gnu:$(PATH)
