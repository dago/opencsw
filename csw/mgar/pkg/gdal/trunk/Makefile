# $Id$
NAME = gdal
VERSION = 1.8.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Geospatial Data Abstraction Library
define BLURB
GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Force-the-use-of-CSWbash.patch

PACKAGES += CSWgdal 
CATALOGNAME_CSWgdal = gdal
SPKG_DESC_CSWgdal = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgdal1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWgdal += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgdal += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWgdal += CSWjasper
RUNTIME_DEP_PKGS_CSWgdal += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdal += CSWlibidn11
RUNTIME_DEP_PKGS_CSWgdal += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWgdal += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWgdal += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdal += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWgdal += CSWlibz1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibpq5
RUNTIME_DEP_PKGS_CSWgdal += CSWlibmysqlclient15

PACKAGES += CSWlibgdal1
CATALOGNAME_CSWlibgdal1 = libgdal1
SPKG_DESC_CSWlibgdal1 += Geospatial Data Abstraction Library, libgdal.so.1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWjasper
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibpq5
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibgcc-s1
PKGFILES_CSWlibgdal1 += $(call baseisadirs,$(libdir),libgdal\.so\.1\.15\.0)
PKGFILES_CSWlibgdal1 += $(call baseisadirs,$(libdir),libgdal\.so\.1(\.\d+)*)

PACKAGES += CSWgdal-dev
CATALOGNAME_CSWgdal-dev = gdal_dev
SPKG_DESC_CSWgdal-dev += Geospatial Data Abstraction Library, development files
RUNTIME_DEP_PKGS_CSWgdal-dev += CSWlibgdal1
PKGFILES_CSWgdal-dev += $(PKGFILES_DEVEL) /opt/csw/bin/gdal-config

GARCOMPILER = GNU

# c++ libraries, so move things around a bit
libdir = $(abspath /opt/csw/gxx/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-libtiff=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mysql=/opt/csw/bin/mysql_config
CONFIGURE_ARGS += --with-sqlite3=$(prefix)

# doesn't have tests?
TEST_TARGET = 

LICENSE = LICENSE.TXT

EXTRA_LIB += /opt/csw/postgresql/lib

include gar/category.mk

ifeq ($(GARCH),sparc)
CONFIGURE_ARGS += --with-pg=/opt/csw/postgresql/bin/sparcv8/pg_config
else
CONFIGURE_ARGS += --with-pg=/opt/csw/postgresql/bin/pg_config
endif

# to avoid the __sync_fetch_and_add4 issue (must be after including category)
ARCHFLAGS_GCC4_sparcvv8 = -m32
