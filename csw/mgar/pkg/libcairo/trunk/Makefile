NAME      = libcairo
VERSION   = 1.8.8
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

PACKAGES = CSWlibcairo CSWlibcairodevel CSWlibcairodoc
CATALOGNAME_CSWlibcairo      = libcairo
CATALOGNAME_CSWlibcairodevel = libcairo_devel
CATALOGNAME_CSWlibcairodoc   = libcairo_doc

SPKG_DESC_CSWlibcairo 		= $(DESCRIPTION)
SPKG_DESC_CSWlibcairodevel 	= $(DESCRIPTION) development package
SPKG_DESC_CSWlibcairodoc 	= $(DESCRIPTION) documentation

PKGFILES_CSWlibcairodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibcairodevel += $(docdir)/libcairo_devel/.*
PKGFILES_CSWlibcairodoc    = $(sharedstatedir)/gtk-doc.*
PKGFILES_CSWlibcairodoc   += $(docdir)/libcairo_doc/.*

BUILD_DEP_PKGS += CSWlibxrenderdevel CSWkbproto CSWrenderproto
BUILD_DEP_PKGS += CSWlibspectre 

RUNTIME_DEP_PKGS_CSWlibcairo      = CSWfconfig
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWftype2
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWpixman
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWpng
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWzlib
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWexpat
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWiconv
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWlibxcb
RUNTIME_DEP_PKGS_CSWlibcairo     += CSWxcbutil

RUNTIME_DEP_PKGS_CSWlibcairodevel = CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibcairodoc   = 

ARCHALL_CSWlibcairodoc = 1

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
# We want libcairo to be linked with Xrender from $(prefix)/X11/lib not
# $(prefix)/lib since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
# imagediff in testsuite needs -lsocket
EXTRA_LDFLAGS = -lsocket -lnsl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-full-testing --enable-xlib=yes --enable-xlib-xrender=yes --enable-ft=yes --with-x 
CONFIGURE_ARGS += --enable-png=yes --enable-ps=yes --enable-pdf=yes --enable-svg=yes --enable-xcb=yes
CONFIGURE_ARGS += --enable-gtk-doc --enable-test-surfaces=yes 
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

# configure have problems with non-gnu utilities
PATH := /opt/csw/gnu:$(PATH)
