# $Id$
NAME = gdal
VERSION = 1.8.0
CATEGORIES = lib

DESCRIPTION = Geospatial Data Abstraction Library
define BLURB
GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.
endef

GARTYPE = v2-defaultchange

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-libtiff=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)

include gar/category.mk
