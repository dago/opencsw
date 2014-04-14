# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = postgis
VERSION = 2.1.1
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

GARCOMPILER = GNU

PATCHFILES += 0000-Use-stdarg.h-only-if-__STDC__-is-defined-to-1.patch

MASTER_SITES = http://download.osgeo.org/postgis/source/
DISTFILES  = $(DISTNAME).tar.gz

EXTRA_LINKER_FLAGS = -lm
EXTRA_CFLAGS = -std=c99 -D__EXTENSIONS__
EXTRA_TEST_ENV = GDAL_DATA=/opt/csw/share/gdal-data

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

include gar/category.mk

