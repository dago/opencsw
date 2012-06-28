# $Id$
NAME = gdal
VERSION = 1.9.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Geospatial Data Abstraction Library
define BLURB
GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GNU

MASTER_SITES = http://download.osgeo.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Force-use-of-double-data-type-before-checking-for-is.patch
PATCHFILES += 0002-apply-patch-from-upstream-to-handle-building-with-a-.patch
PATCHFILES += 0003-Cast-inbuf-parameter-to-iconv-call-to-work-with-Sun-.patch
PATCHFILES += 0004-Ensure-that-__FUNCTION__-is-mapped-to-__func__-when-.patch
PATCHFILES += 0005-Pass-proper-types-to-std-make_pair-to-satisfy-Sun-St.patch
#PATCHFILES += 0001-Force-the-use-of-CSWbash.patch

BUILD_DEP_PKGS += CSWgeos-dev

PACKAGES += CSWgdal 
CATALOGNAME_CSWgdal = gdal
SPKG_DESC_CSWgdal = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgif4
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgeos-c1
RUNTIME_DEP_PKGS_CSWgdal += CSWlibgdal1-gxx
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

PACKAGES += CSWlibgdal1-gxx
OBSOLETED_BY_CSWlibgdal1-gxx = CSWlibgdal1
CATALOGNAME_CSWlibgdal1-gxx = libgdal1_gxx
SPKG_DESC_CSWlibgdal1-gxx += Geospatial Data Abstraction Library, libgdal.so.1
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWjasper
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibpq5
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgdal1-gxx += CSWlibgeos-c1
PKGFILES_CSWlibgdal1-gxx += $(call baseisadirs,$(libdir),libgdal\.so\.1\.15\.0)
PKGFILES_CSWlibgdal1-gxx += $(call baseisadirs,$(libdir),libgdal\.so\.1(\.\d+)*)

PACKAGES += CSWgdal-dev
CATALOGNAME_CSWgdal-dev = gdal_dev
SPKG_DESC_CSWgdal-dev += Geospatial Data Abstraction Library, development files
RUNTIME_DEP_PKGS_CSWgdal-dev += CSWlibgdal1-gxx
PKGFILES_CSWgdal-dev += $(PKGFILES_DEVEL) /opt/csw/bin/gdal-config

libdir = $(abspath /opt/csw/gxx/lib/$(MM_LIBDIR))
includedir = /opt/csw/gxx/include

# enable use of __func__ as required by patch 0004
ifneq ($(GARCOMPILER),GNU)
EXTRA_CXXFLAGS += -features=extensions
endif

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libz=$(prefix)
CONFIGURE_ARGS += --with-png=$(prefix)
CONFIGURE_ARGS += --with-libtiff=$(prefix)
CONFIGURE_ARGS += --with-jpeg=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mysql=/opt/csw/bin/mysql_config
CONFIGURE_ARGS += --with-sqlite3=$(prefix)
CONFIGURE_ARGS += --with-pg=/opt/csw/bin/pg_config

# doesn't have tests?
TEST_TARGET = 

LICENSE = LICENSE.TXT

EXTRA_LIB += /opt/csw/postgresql/lib
EXTRA_LDFLAGS += -L$(libdir) -R$(libdir)

include gar/category.mk




# to avoid the __sync_fetch_and_add4 issue (must be after including category)
ARCHFLAGS_GCC4_sparcvv8 = -m32
