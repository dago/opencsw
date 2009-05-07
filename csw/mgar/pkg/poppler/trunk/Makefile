GARNAME = poppler
GARVERSION = 0.10.6
CATEGORIES = lib

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

REQUIRED_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2
REQUIRED_PKGS += CSWjpeg CSWlibxml2 CSWzlib

SPKG_SOURCEURL = http://poppler.freedesktop.org/

include gar/category.mk
