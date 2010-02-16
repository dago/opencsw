GARNAME = wmf
GARVERSION = 0.2.8.4
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
DISTFILES  = libwmf-$(GARVERSION).tar.gz
DISTNAME = libwmf-$(GARVERSION)

SPKG_SOURCEURL = http://wvware.sourceforge.net

PACKAGES = CSWwmf CSWlibwmfdevel CSWlibwmfdoc CSWwmffonts CSWlibwmf
CATALOGNAME_CSWwmf = wmf
CATALOGNAME_CSWlibwmf = libwmf
CATALOGNAME_CSWlibwmfdevel = libwmf_devel
CATALOGNAME_CSWlibwmfdoc = wmf_doc
CATALOGNAME_CSWwmffonts = wmf_fonts

SPKG_DESC_CSWwmf += Library and tools for manipulating Windows metafiles
SPKG_DESC_CSWlibwmf += Library and tools for manipulating Windows metafiles - runtime package
SPKG_DESC_CSWlibwmfdevel += Library and tools for manipulating Windows metafiles - developer package
SPKG_DESC_CSWlibwmfdoc += Library and tools for manipulating Windows metafiles - documentation
SPKG_DESC_CSWwmffonts += Library and tools for manipulating Windows metafiles - fonts

RUNTIME_DEP_PKGS_CSWwmf += CSWexpat CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
RUNTIME_DEP_PKGS_CSWwmf += CSWjpeg CSWlibx11 CSWpng CSWzlib
RUNTIME_DEP_PKGS_CSWwmf += CSWwmffonts CSWlibwmf
RUNTIME_DEP_PKGS_CSWlibwmf += CSWwmffonts
RUNTIME_DEP_PKGS_CSWlibwmf += CSWexpat
RUNTIME_DEP_PKGS_CSWlibwmf += CSWftype2
RUNTIME_DEP_PKGS_CSWlibwmf += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibwmf += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibwmf += CSWpng
RUNTIME_DEP_PKGS_CSWlibwmf += CSWzlib
RUNTIME_DEP_PKGS_CSWlibwmfdevel += CSWlibwmf
RUNTIME_DEP_PKGS_CSWlibwmfdoc += CSWwmf
RUNTIME_DEP_PKGS_CSWwmffonts += 

BUILD_DEP_PKGS += CSWgtk2devel

PKGFILES_CSWlibwmf = $(PKGFILES_RT)
PKGFILES_CSWlibwmfdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibwmfdoc = $(sharedstatedir)/doc/.*
PKGFILES_CSWwmffonts = $(sharedstatedir)/libwmf/fonts/.*

ARCHALL_CSWwmfdoc = 1
ARCHALL_CSWwmffonts = 1

CHECKPKG_OVERRIDES += CSWlibwmf|symbol-not-found|libwmf-0.2.so.7.1.0
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|io-wmf.so
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|wmf2gd
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|wmf2x
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|wmf2fig
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|wmf2svg
CHECKPKG_OVERRIDES += CSWwmf|symbol-not-found|wmf2eps

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10501
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

STRIP_LIBTOOL = 1

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)
