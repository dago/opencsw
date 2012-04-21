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

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

