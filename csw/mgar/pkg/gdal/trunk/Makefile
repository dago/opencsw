# $Id$
NAME = gdal
VERSION = 1.8.0
CATEGORIES = lib

DESCRIPTION = Geospatial Data Abstraction Library
define BLURB
GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.
endef

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Force-the-use-of-CSWbash.patch

PACKAGES += CSWgdal 
CATALOGNAME_CSWgdal = gdal
SPKG_DESC_CSWgdal = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgdal1
RUNTIME_DEP_PKGS_CSWgdal += CSWcurlrt
RUNTIME_DEP_PKGS_CSWgdal += CSWexpat
RUNTIME_DEP_PKGS_CSWgdal += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgdal += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgdal += CSWgiflibrt
RUNTIME_DEP_PKGS_CSWgdal += CSWhdf5rt
RUNTIME_DEP_PKGS_CSWgdal += CSWjasper
RUNTIME_DEP_PKGS_CSWgdal += CSWjpeg
RUNTIME_DEP_PKGS_CSWgdal += CSWlibcares2
RUNTIME_DEP_PKGS_CSWgdal += CSWlibidn11
RUNTIME_DEP_PKGS_CSWgdal += CSWlibnetcdf6
RUNTIME_DEP_PKGS_CSWgdal += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWgdal += CSWoldaprt
RUNTIME_DEP_PKGS_CSWgdal += CSWosslrt
RUNTIME_DEP_PKGS_CSWgdal += CSWpng
RUNTIME_DEP_PKGS_CSWgdal += CSWtiff
RUNTIME_DEP_PKGS_CSWgdal += CSWzlib

PACKAGES += CSWlibgdal1
CATALOGNAME_CSWlibgdal1 = libgdal1
SPKG_DESC_CSWlibgdal1 += Geospatial Data Abstraction Library, libgdal.so.1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWcurlrt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWexpat
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWgiflibrt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWjasper
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWjpeg
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibcares2
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibnetcdf6
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWpng
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWtiff
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWzlib
PKGFILES_CSWlibgdal1 += $(call baseisadirs,$(libdir),libgdal\.so\.1\.15\.0)
PKGFILES_CSWlibgdal1 += $(call baseisadirs,$(libdir),libgdal\.so\.1(\.\d+)*)

PACKAGES += CSWgdal-dev
CATALOGNAME_CSWgdal-dev = gdal_dev
SPKG_DESC_CSWgdal-dev += Geospatial Data Abstraction Library, development files
RUNTIME_DEP_PKGS_CSWgdal-dev += CSWlibgdal1
PKGFILES_CSWgdal-dev += $(PKGFILES_DEVEL)

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-libtiff=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mysql=/opt/csw/mysql5/bin/mysql_config
CONFIGURE_ARGS += --with-pg=/opt/csw/postgresql/bin/sparcv8/pg_config
CONFIGURE_ARGS += --with-sqlite3=$(prefix)

# doesn't have tests?
TEST_TARGET = 

LICENSE = LICENSE.TXT

include gar/category.mk
