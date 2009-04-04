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

LICENSE = COPYING

REQUIRED_PKGS += CSWexpat CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWjpeg
REQUIRED_PKGS += CSWpng CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10501
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-configure-modulated:
	@(echo "~~~ Fixing Libtool ~~~")
	@$(FILEDIR)/fixme.sh $(WORKSRC)
	$(DONADA)
