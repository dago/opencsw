# $Id$
#
NAME = grass
VERSION = 6.4.2
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Geographic Resources Analysis Support System
define BLURB
Commonly referred to as GRASS, this is free Geographic Information System (GIS) software used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization. GRASS is currently used in academic and commercial settings around the world, as well as by many governmental agencies and environmental consulting companies. GRASS is an official project of the Open Source Geospatial Foundation.
endef

# libgdal is 10+ only
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = http://grass.osgeo.org/grass64/source/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWgdal-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWproj-dev
# for nad2bin
BUILD_DEP_PKGS += CSWproj

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-postgres
CONFIGURE_ARGS += --with-readline
CONFIGURE_ARGS += --with-mysql-includes=$(prefix)/include/mysql
CONFIGURE_ARGS += --with-gdal=/opt/csw/bin/gdal-config
CONFIGURE_ARGS += --with-geos=/opt/csw/bin/geos-config
CONFIGURE_ARGS += --with-python=/opt/csw/bin/python-config
CONFIGURE_ARGS += --with-proj-share=/opt/csw/share/proj

include gar/category.mk

