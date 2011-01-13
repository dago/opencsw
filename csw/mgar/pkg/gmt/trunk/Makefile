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


BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWnetcdf-devel CSWnetcdf

PACKAGES += CSWgmt
CATALOGNAME_CSWgmt = gmt
SPKG_DESC_CSWgmt = Generic Mapping Tools
RUNTIME_DEP_PKGS_CSWgmt += CSWlibnetcdf6
RUNTIME_DEP_PKGS_CSWgmt += CSWsunmath

PACKAGES += CSWgmt-doc
CATALOGNAME_CSWgmt-doc = gmt_doc
SPKG_DESC_CSWgmt-doc = Documentation for GMT
PKGFILES_CSWgmt-doc += /opt/csw/share/doc/gmt
PKGFILES_CSWgmt-doc += /opt/csw/share/doc/gmt/.*


## GMT Includes no unit tests
TEST_SCRIPTS =

## GMT doesn't use the GNU convention for unpacked tarballs
#WORKSRC = $(WORKDIR)/GMT$(VERSION)
DISTNAME = GMT$(GMT_VERSION)

## Arguments passed to the ./configure script. Configure ignores the various
## environment variables so we have to pass CFLAGS and friends
CONFIGURE_ARGS += NETCDF_LIB=$(libdir)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)"
CONFIGURE_ARGS += LDFLAGS="$(LDFLAGS)"
CONFIGURE_ARGS += CXXFLAGS="$(CXXFLAGS)"
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-mex
#CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-netcdf=/opt/csw


## Attempt to build this 64-bit
BUILD64 = 1

GARCOMPILER = GCC4

#DEBUG_PACKAGING = 1

INSTALL_ARGS = install-all

LICENSE = LICENSE.TXT
include gar/category.mk
