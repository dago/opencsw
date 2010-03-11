# $Id$

GARNAME = poppler
GARVERSION = 0.12.4
CATEGORIES = lib

DESCRIPTION = Poppler is a PDF rendering library based on the xpdf-3.0 code base
define BLURB
endef

SPKG_SOURCEURL = http://poppler.freedesktop.org/
MASTER_SITES = http://poppler.freedesktop.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES += missing-includes.patch

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS += CSWfconfig
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWjpeg
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWzlib

include gar/category.mk
