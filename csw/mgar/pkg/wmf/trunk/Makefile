NAME = wmf
VERSION = 0.2.8.4
CATEGORIES = lib

DESCRIPTION = Library and tools for manipulating Windows metafiles
define BLURB
	libwmf is a library for reading vector images in Microsoft's native Windows 
	Metafile Format (WMF) and for either (a) displaying them in, e.g., an X 
	window; or (b) converting them to more standard/open file formats such as, 
	e.g., the W3C's XML-based Scaleable Vector Graphic (SVG) format. 
endef

SF_PROJ = wvware
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = libwmf-$(VERSION).tar.gz
DISTNAME = libwmf-$(VERSION)

SPKG_SOURCEURL = http://wvware.sourceforge.net

PACKAGES = CSWwmf CSWlibwmf CSWlibwmfdevel CSWlibwmfdoc CSWwmffonts CSWlibwmfgtk
CATALOGNAME_CSWwmf = wmf
CATALOGNAME_CSWlibwmf = libwmf
CATALOGNAME_CSWlibwmfdevel = libwmf_devel
CATALOGNAME_CSWlibwmfdoc = libwmf_doc
CATALOGNAME_CSWlibwmfgtk = libwmf_gtk
CATALOGNAME_CSWwmffonts = wmf_fonts

SPKG_DESC_CSWwmf += Library and tools for manipulating Windows metafiles
SPKG_DESC_CSWlibwmf += Library and tools for manipulating Windows metafiles - runtime package
SPKG_DESC_CSWlibwmfdevel += Library and tools for manipulating Windows metafiles - developer package
SPKG_DESC_CSWlibwmfdoc += Library and tools for manipulating Windows metafiles - documentation
SPKG_DESC_CSWlibwmfgtk += Library and tools for manipulating Windows metafiles - GTK loader
SPKG_DESC_CSWwmffonts += Library and tools for manipulating Windows metafiles - fonts

RUNTIME_DEP_PKGS_CSWwmf += CSWftype2 
RUNTIME_DEP_PKGS_CSWwmf += CSWjpeg CSWlibx11 CSWpng CSWzlib
RUNTIME_DEP_PKGS_CSWwmf += CSWwmffonts CSWlibwmf
RUNTIME_DEP_PKGS_CSWwmf += CSWiconv
RUNTIME_DEP_PKGS_CSWwmf += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibwmf += CSWwmffonts
RUNTIME_DEP_PKGS_CSWlibwmf += CSWftype2
RUNTIME_DEP_PKGS_CSWlibwmf += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibwmf += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibwmf += CSWpng
RUNTIME_DEP_PKGS_CSWlibwmf += CSWzlib
RUNTIME_DEP_PKGS_CSWlibwmf += CSWiconv
RUNTIME_DEP_PKGS_CSWlibwmf += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibwmfdevel += CSWlibwmf
RUNTIME_DEP_PKGS_CSWlibwmfdoc += 
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWlibwmf
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWglib2
RUNTIME_DEP_PKGS_CSWlibwmfgtk += CSWgtk2
RUNTIME_DEP_PKGS_CSWwmffonts += 

BUILD_DEP_PKGS += CSWgtk2devel

PKGFILES_CSWlibwmf = $(PKGFILES_RT)
PKGFILES_CSWlibwmfdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibwmfdoc = $(sharedstatedir)/doc/.*
PKGFILES_CSWlibwmfgtk = $(libdir).*/io-wmf.so
PKGFILES_CSWwmffonts = $(sharedstatedir)/libwmf/fonts/.*

ARCHALL_CSWlibwmfdoc = 1
ARCHALL_CSWwmffonts = 1

CHECKPKG_OVERRIDES_CSWlibwmf += symbol-not-found|libwmf-0.2.so.7.1.0
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|io-wmf.so
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|wmf2gd
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|wmf2x
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|wmf2fig
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|wmf2svg
CHECKPKG_OVERRIDES_CSWwmf += symbol-not-found|wmf2eps

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10501
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x
#CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-libxml2=$(prefix)
CONFIGURE_ARGS += --with-freetype=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-sys-gd=$(prefix)
CONFIGURE_ARGS += --with-sysfontmap=$(datadir)/fonts/fontmap
#CONFIGURE_ARGS += --with-xtrafontmap=
CONFIGURE_ARGS += --with-gsfontmap=$(datadir)/ghostscript/Resource/Init/Fontmap.GS
CONFIGURE_ARGS += --with-gsfontdir=$(datadir)/ghostscript/fonts
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
