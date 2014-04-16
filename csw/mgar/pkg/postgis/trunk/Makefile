# $Id$
NAME = postgis
VERSION = 2.1.1
GARTYPE = v2

DESCRIPTION = Spatial and Geographic objects for PostgreSQL
define BLURB
  PostGIS is a spatial database extender for PostgreSQL object-relational database. It
  adds support for geographic objects allowing location queries to be run in SQL. 
endef

GARCOMPILER = GNU

PATCHFILES += 0000-Use-stdarg.h-only-if-__STDC__-is-defined-to-1.patch

MASTER_SITES = http://download.osgeo.org/postgis/source/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES  = CSWpostgis
SPKG_DESC_CSWpostgis = PostGIS - Spatial and Geographic objects for PostgreSQL
RUNTIME_DEP_PKGS_CSWpostgis  = CSWliblwgeom2-1-1
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibz1
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibproj0
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpostgis += CSWperl
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibpq5
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibgdal1
RUNTIME_DEP_PKGS_CSWpostgis += CSWlibgeos-c1
# Required by sparc packages
CHECKPKG_OVERRIDES_CSWpostgis += surplus-dependency|CSWlibz1

PACKAGES += CSWliblwgeom2-1-1
SPKG_DESC_CSWliblwgeom2-1-1 = PostGIS, liblwgeom library
PKGFILES_CSWliblwgeom2-1-1 = $(call pkgfiles_lib,liblwgeom-2.1.1.so)
RUNTIME_DEP_PKGS_CSWliblwgeom2-1-1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWliblwgeom2-1-1 += CSWlibproj0
RUNTIME_DEP_PKGS_CSWliblwgeom2-1-1 += CSWlibgeos-c1
CHECKPKG_OVERRIDES_CSWliblwgeom2-1-1 += soname-equals-filename|file=/opt/csw/lib/sparcv9/liblwgeom-2.1.1.so
CHECKPKG_OVERRIDES_CSWliblwgeom2-1-1 += soname-equals-filename|file=/opt/csw/lib/amd64/liblwgeom-2.1.1.so
CHECKPKG_OVERRIDES_CSWliblwgeom2-1-1 += soname-equals-filename|file=/opt/csw/lib/liblwgeom-2.1.1.so


PACKAGES += CSWliblwgeom-dev
SPKG_DESC_CSWliblwgeom-dev = PostGIS, liblwgeom header files
PKGFILES_CSWliblwgeom-dev = include/.*

EXTRA_LINKER_FLAGS = -lm
EXTRA_CFLAGS = -std=c99 -D__EXTENSIONS__

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

# Tests require a working postgres installation with a user having
# permission to create databases. Further, we would need a 32bit and
# 64bit database server.
SKIPTEST = 1

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)
