GARNAME      = libcairo
GARVERSION   = 1.8.10
CATEGORIES   = lib

DESCRIPTION  = The Cairo 2D Graphics Library
define BLURB
  Cairo is a 2D graphics library with support for multiple output devices.
  Currently supported output targets include the X Window System, Quartz,
  Win32, image buffers, PostScript, PDF, and SVG file output. Experimental
  backends include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTNAME      = cairo-$(GARVERSION)
DISTFILES     = $(DISTNAME).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibcairo CSWlibcairodevel CSWlibcairodoc
# PACKAGES += CSWcxlibcairo CSWcxlibcairodevel
CATALOGNAME_CSWlibcairo      = libcairo
CATALOGNAME_CSWlibcairodevel = libcairo_devel
CATALOGNAME_CSWlibcairodoc   = libcairo_doc
CATALOGNAME_CSWcxlibcairo    = cx_libcairo
CATALOGNAME_CSWcxlibcairodevel = cx_libcairo_devel

SPKG_DESC_CSWlibcairo 		= $(DESCRIPTION)
SPKG_DESC_CSWlibcairodevel 	= $(DESCRIPTION) development package
SPKG_DESC_CSWlibcairodoc 	= $(DESCRIPTION) documentation
SPKG_DESC_CSWcxlibcairo 	= $(DESCRIPTION) (bound against OpenCSW X11)
SPKG_DESC_CSWcxlibcairodevel 	= $(DESCRIPTION) development package (bound against OpenCSW X11)

#BUILD_DEP_PKGS = CSWlibxrenderdevel CSWkbproto CSWrenderproto CSWlibspectre 
BUILD_DEP_PKGS = CSWlibxrenderdevel CSWlibspectre 

RUNTIME_DEP_PKGS_CSWlibcairo      = CSWfconfig CSWftype2 CSWpixman CSWpng CSWzlib CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibcairodevel = CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibcairodoc   = 
RUNTIME_DEP_PKGS_CSWcxlibcairo    = CSWftype2 CSWpixman CSWlibxrender CSWlibxcb CSWxcbutil CSWzlib CSWpng CSWfconfig CSWlibx11
RUNTIME_DEP_PKGS_CSWcxlibcairodevel = CSWcxlibcairo CSWlibxrenderdevel CSWlibxcbdevel CSWlibx11devel

EXTRA_MODULATORS = X11
#MODULATIONS_X11 = sunwx11 cswx11
MODULATIONS_X11 = sunwx11 

BUILD64 = 1

EXTRA_INC_cswx11 = $(prefix)/X11/include
EXTRA_LIB_cswx11 = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS_cswx11 = $(prefix)/X11/lib

EXTRA_INC = $(EXTRA_INC_$(X11)
EXTRA_LIB = $(EXTRA_LIB_$(X11)
EXTRA_PKG_CONFIG_DIRS = $(EXTRA_PKG_CONFIG_DIRS_$(X11))

# We want libcairo to be linked with Xrender from $(prefix)/X11/lib not
# $(prefix)/lib since the latter is linked to /usr/openwin/lib/libX11.so.4
#EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
#EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
# imagediff in testsuite needs -lsocket
EXTRA_LDFLAGS = -lsocket -lnsl

prefix_cswx11 = $(BUILD_PREFIX)/X11
prefix = $(or $(prefix_$(X11)),$(BUILD_PREFIX))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-full-testing --enable-xlib=yes --enable-ft=yes --with-x 
CONFIGURE_ARGS += --enable-png=yes --enable-ps=yes --enable-pdf=yes --enable-svg=yes
CONFIGURE_ARGS += --enable-gtk-doc --enable-test-surfaces=yes 

CONFIGURE_ARGS_sunwx11 += --x-includes=/usr/openwin/include
CONFIGURE_ARGS_sunwx11 += --x-libraries=$(abspath /usr/openwin/lib/$(MM_LIBDIR))
CONFIGURE_ARGS_sunwx11 += --enable-xcb=no
CONFIGURE_ARGS_cswx11 += --x-includes=$(prefix)/include
CONFIGURE_ARGS_cswx11 += --x-libraries=$(abspath $(prefix)/lib/$(MM_LIBDIR))
CONFIGURE_ARGS_cswx11 += --enable-xlib-xrender=yes --enable-xcb=yes
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(X11))

MERGE_SCRIPTS_isa-default-x11-sunwx11 = copy-all
MERGE_SCRIPTS_isa-default64-x11-sunwx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-sunwx11 = $(libdir)
MERGE_SCRIPTS_isa-default-x11-cswx11 = copy-only
MERGE_DIRS_isa-default-x11-cswx11 = $(libdir) $(includedir)
MERGE_SCRIPTS_isa-default64-x11-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-cswx11 = $(libdir)

PKGFILES_CSWlibcairodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibcairodevel += $(docdir)/libcairo_devel/.*
PKGFILES_CSWlibcairodoc    = $(sharedstatedir)/gtk-doc.*
PKGFILES_CSWlibcairodoc   += $(docdir)/libcairo_doc/.*
PKGFILES_CSWcxlibcairo     = $(call baseisadirs,/opt/csw/X11/lib,[^/]*\.so(\.\d+)*)
PKGFILES_CSWcxlibcairodevel = $(call baseisadirs,/opt/csw/X11/lib,pkgconfig(/.*)?)
PKGFILES_CSWcxlibcairodevel += /opt/csw/X11/include/.*

ARCHALL_CSWlibcairodoc = 1

CHECKPKG_OVERRIDES_CSWlibcairodevel += surplus-dependency|CSWlibcairo
CHECKPKG_OVERRIDES_CSWcxlibcairodevel += surplus-dependency|CSWlibx11devel
CHECKPKG_OVERRIDES_CSWcxlibcairodevel += surplus-dependency|CSWcxlibcairo
CHECKPKG_OVERRIDES_CSWcxlibcairodevel += surplus-dependency|CSWlibxcbdevel
CHECKPKG_OVERRIDES_CSWcxlibcairodevel += surplus-dependency|CSWlibxrenderdevel

include gar/category.mk

# configure have problems with non-gnu utilities
PATH := /opt/csw/gnu:$(PATH)
