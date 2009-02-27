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

LICENSE = COPYING

REQUIRED_PKGS += CSWexpat CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWjpeg
REQUIRED_PKGS += CSWpng CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check
include gar/category.mk
