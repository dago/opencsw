GARNAME      = libcairo
GARVERSION   = 1.8.6
CATEGORIES   = lib

DESCRIPTION  = The Cairo 2D Graphics Library
define BLURB
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System, Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTNAME      = cairo-$(GARVERSION)
DISTFILES     = $(DISTNAME).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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

PREREQUISITE_PKGS = CSWrenderdev

REQUIRED_PKGS_CSWlibcairo      = CSWfconfig
REQUIRED_PKGS_CSWlibcairo     += CSWftype2
REQUIRED_PKGS_CSWlibcairo     += CSWlibxrender
REQUIRED_PKGS_CSWlibcairo     += CSWpixman
REQUIRED_PKGS_CSWlibcairo     += CSWpng
REQUIRED_PKGS_CSWlibcairo     += CSWzlib
REQUIRED_PKGS_CSWlibcairo     += CSWlibrsvg
REQUIRED_PKGS_CSWlibcairo     += CSWexpat
REQUIRED_PKGS_CSWlibcairo     += CSWiconv
REQUIRED_PKGS_CSWlibcairo     += CSWlibx11
REQUIRED_PKGS_CSWlibcairo     += CSWlibxcb
REQUIRED_PKGS_CSWlibcairo     += CSWxcbutil

REQUIRED_PKGS_CSWlibcairodevel = CSWlibcairo
REQUIRED_PKGS_CSWlibcairodoc   = 

ARCHALL_CSWlibcairodoc = 1

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests --enable-xlib=yes --enable-xlib-xrender=yes --enable-ft=yes --with-x 
CONFIGURE_ARGS += --enable-png=yes --enable-ps=yes --enable-pdf=yes --enable-svg=yes --enable-xcb=yes
CONFIGURE_ARGS += --enable-gtk-doc --enable-test-surfaces=yes 

include gar/category.mk
