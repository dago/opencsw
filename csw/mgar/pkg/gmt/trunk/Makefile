# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GMT_VERSION = 4.5.3

NAME = gmt
VERSION = $(GMT_VERSION)
CATEGORIES = apps
DESCRIPTION = Generic Mapping Tools
define BLURB
  GMT is an open source collection of ~60 tools for manipulating geographic and Cartesian data sets (including filtering, trend fitting, gridding, projecting, etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging from simple x-y plots via contour maps to artificially illuminated surfaces and 3-D perspective views. GMT supports ~30 map projections and transformations and comes with support data such as GSHHS coastlines, rivers, and political boundaries. GMT is developed and maintained by Paul Wessel and Walter H. F. Smith with help from a global set of volunteers, and is supported by the National Science Foundation. It is released under the GNU General Public License. 
endef

##
## Upstream URL that should show up in the VENDOR field as well as on
## http://opencsw.org/packages/<packagename>.
SPKG_SOURCEURL = http://gmt.soest.hawaii.edu/
##
## Whitespace-separated list of URLs to download the source package from.
## There are presets: $(SF_MIRRORS), $(GNU_MIRRORS) and $(GOOGLE_MIRROR).
MASTER_SITES = ftp://ftp.iris.washington.edu/pub/gmt/ ftp://ftp.soest.hawaii.edu/gmt/ ftp://gd.tuwien.ac.at/pub/gmt/

DISTFILES  = GMT$(GMT_VERSION)_doc.tar.bz2 \
	     GMT$(GMT_VERSION)_share.tar.bz2 \
	     GMT$(GMT_VERSION)_src.tar.bz2 \
	     GMT$(GMT_VERSION)_suppl.tar.bz2
UFILES_REGEX = GMT(\d+(?:\.\d+)*)_(.*).tar.gz


RUNTIME_DEP_PKGS = CSWnetcdf CSWgmtcoast
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

## GMT Includes no unit tests
TEST_SCRIPTS =

## GMT doesn't use the GNU convention for unpacked tarballs
#WORKSRC = $(WORKDIR)/GMT$(VERSION)
DISTNAME = GMT$(GMT_VERSION)

## Arguments passed to the ./configure script. Configure ignores the various
## environment variables so we have to pass CFLAGS and friends
CONFIGURE_ARGS = $(DIRPATHS) \
		 --disable-mex \
		 --enable-shared \
		 --enable-netcdf=/opt/csw

CONFIGURE_ENV += NETCDF_LIB=$(libdir)
CONFIGURE_ENV += CFLAGS="$(CFLAGS)"
CONFIGURE_ENV += LDFLAGS="$(LDFLAGS)"
CONFIGURE_ENV += CXXFLAGS="$(CXXFLAGS)"
## Attempt to build this 64-bit
BUILD64 = 1

## Although NetCDF is built with GCC3, GMT Seems to build fine with GCC4
GARCOMPILER = GCC4

DEBUG_PACKAGING = 1

## Checkpkg whines about this, but GMT really needs it's coastline files in
## order to make a map of any real substance
CHECKPKG_OVERRIDES_CSWgmt += surplus-dependency|CSWgmtcoast

INSTALL_ARGS = install-all

## Gar's license file finding routine isn't aware of how to find files when WORKSRC has been redefined, so we need to put the license file somewhere that it can find.
#post-install-modulated:
#	@cp $(WORKSRC)/LICENSE.TXT $(WORKDIR)/COPYING
LICENSE = LICENSE.TXT
include gar/category.mk
