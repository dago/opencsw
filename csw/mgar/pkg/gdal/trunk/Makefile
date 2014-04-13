# $Id$
NAME = gdal
VERSION = 1.9.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Geospatial Data Abstraction Library
define BLURB
GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GNU

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(of-CSWbash.patch

BUILD_DEP_PKGS += CSWgeos-dev

PACKAGES += CSWgdal 
CATALOGNAME_CSWgdal = gdal
SPKG_DESC_CSWgdal = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgif4
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgeos-c1
RUNTIME_DEP_PKGS_CSWgd= CSWlibgdal1-gxx
RUNTIME_DEP_PKGS_CSWgdal += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWgdal += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgdal += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWgdal += CSWjasper
RUNTIME_DEP_PKGS_CSWgdal += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdal += CSWlibidn11
RUNTIME_DEP_PKGS_CSWgdal += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWgdal += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWgdal += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdal += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWgdal += CSWlibz1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibpq5
RUNTIME_DEP_PKGS_CSWgdal += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWgdal += CSWlibiconv2

PACKAG
OBSOLETED_BY_CSWlibgdal1 = CSWlibgdal1-gxx
CATALOGNAME_CSWlibgdal1-gxx = libgdal1_gxx_stub
SPKG_DESC_CSWlibgdal1C_CSWlibgdal1-gxx += Geospatial Data Abstraction Library, libgdal.so.1
RUNTIME_DEP += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWjasper
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibpq5
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgdal1 += CSWlibgeos-c1
PKGFILES_CSWlibgdal1 += $(call baseisadirs,$(libdir),libgdal\.so\.1\.16\.0)
PKGFILES_CSWlibgdal1S_CSWlibgdal1-gxx += $(call baseisadirs,$(libdir),libgdal\.so\.1(\.\d+)*)

PACKAGES += CSWgdal-dev
CATALOGNAME_CSWgdal-dev = gdal_dev
SPKG_DESC_CSWgdal-dev += Geospatial Data Abstraction Library, development files
RUNTIME_DEP_PKGS_CSWgdal-d
PKGFILES_CSWgdal-dev += $(PKGFILES_DEVEL) /opt/csw/bin/gdal-config

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --datadir=$(datadir)/gdal-dataRGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-libtiff=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with# Fails w/
#  ld: fatal: file /lib/libc.so: version 'SUNW_1.22.5' is unavailable:
#        required by file /opt/csw/lib/libmysqlclient.so
#-expat=$(prefix)
CONFIGURE_ARGS$(bindir)/mysql_config
CONFIGURE_ARGS += --without-mysql
CONFIGURE_ARGS += --with-sqlite3=$(prefix)
CONFIGURE_ARGS += --with-pg=$(bindir)h-pg=/opt/csw/bin/pg_config

# doesn't have tests?
TEST_TARGET = 

LICENSE = LICDFLAGS += -L$(libdir) -R$(libdir)

include gar/category.mk
