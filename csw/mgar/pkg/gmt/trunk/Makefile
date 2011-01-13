# Copyright 2011 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GMT_VERSION = 4.5.5

NAME = gmt
VERSION = $(GMT_VERSION)
CATEGORIES = apps
DESCRIPTION = Generic Mapping Tools
define BLURB
  GMT is an open source collection of ~60 tools for manipulating geographic and Cartesian data sets (including filtering, trend fitting, gridding, projecting, etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging from simple x-y plots via contour maps to artificially illuminated surfaces and 3-D perspective views. GMT supports ~30 map projections and transformations and comes with support data such as GSHHS coastlines, rivers, and political boundaries. GMT is developed and maintained by Paul Wessel and Walter H. F. Smith with help from a global set of volunteers, and is supported by the National Science Foundation. It is released under the GNU General Public License. 
endef

SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
MASTER_SITES += ftp://ftp.iris.washington.edu/pub/gmt/
MASTER_SITES += ftp://ftp.soest.hawaii.edu/gmt/
MASTER_SITES += ftp://gd.tuwien.ac.at/pub/gmt/

DISTFILES += GMT$(GMT_VERSION)_doc.tar.bz2
DISTFILES += GMT$(GMT_VERSION)_share.tar.bz2
DISTFILES += GMT$(GMT_VERSION)_src.tar.bz2
DISTFILES += GMT$(GMT_VERSION)_suppl.tar.bz2
UFILES_REGEX = GMT(\d+(?:\.\d+)*)_(.*).tar.gz


RUNTIME_DEP_PKGS = CSWnetcdf 
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWnetcdf-devel

## GMT Includes no unit tests
TEST_SCRIPTS =

## GMT doesn't use the GNU convention for unpacked tarballs
#WORKSRC = $(WORKDIR)/GMT$(VERSION)
DISTNAME = GMT$(GMT_VERSION)

## Arguments passed to the ./configure script. Configure ignores the various
## environment variables so we have to pass CFLAGS and friends
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-mex
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-netcdf=/opt/csw

CONFIGURE_ENV += NETCDF_LIB=$(libdir)
CONFIGURE_ENV += CFLAGS="$(CFLAGS)"
CONFIGURE_ENV += LDFLAGS="$(LDFLAGS)"
CONFIGURE_ENV += CXXFLAGS="$(CXXFLAGS)"

## Attempt to build this 64-bit
BUILD64 = 1

GARCOMPILER = GCC4

#DEBUG_PACKAGING = 1

INSTALL_ARGS = install-all

LICENSE = LICENSE.TXT
include gar/category.mk
