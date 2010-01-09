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

PACKAGES = CSWwmf CSWwmfdevel CSWwmfdoc
CATALOGNAME_CSWwmf = wmf
CATALOGNAME_CSWwmfdevel = wmf_devel
CATALOGNAME_CSWwmfdoc = wmf_doc

SPKG_DESC_CSWwmf += Library and tools for manipulating Windows metafiles
SPKG_DESC_CSWwmfdevel += Library and tools for manipulating Windows metafiles - developer package
SPKG_DESC_CSWwmfdoc += Library and tools for manipulating Windows metafiles - documentation

REQUIRED_PKGS_CSWwmf += CSWexpat CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
REQUIRED_PKGS_CSWwmf += CSWjpeg CSWlibx11 CSWpng CSWzlib
REQUIRED_PKGS_CSWwmfdevel += CSWwmf
REQUIRED_PKGS_CSWwmfdoc += CSWwmf

PKGFILES_CSWwmfdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWwmfdoc = $(sharedstatedir)/doc/.*

ARCHALL_CSWwmfdoc = 1

BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10501
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

STRIP_LIBTOOL = 1

include gar/category.mk
PATH := /opt/csw/gnu:$(PATH)
