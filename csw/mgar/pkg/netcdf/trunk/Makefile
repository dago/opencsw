# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = netcdf
GARVERSION = 4.1.1
CATEGORIES = lib
DESCRIPTION = machine-independent data formats for array-oriented scientific data
SPKG_SOURCEURL = http://www.unidata.ucar.edu/software/netcdf/
MASTER_SITES = http://www.unidata.ucar.edu/downloads/netcdf/ftp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = COPYRIGHT
RUNTIME_DEP_PKGS = CSWcurlrt CSWhdf5rt CSWgcc3g77rt CSWzlib CSWgcc3corert \
		   CSWoldaprt CSWlibcares CSWlibidn CSWgcc3g++rt CSWosslrt

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWtetex CSWgcc3g77
## CFLAGS AND LDFLAGS are necessary due to problems with the fortran bindings when
## building 64-bit
BUILD_ARGS = CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" FFLAGS="$(FFLAGS)" FCFLAGS="$(FCFLAGS)"

CONFIGURE_ARGS = $(DIRPATHS) \
		 --enable-netcdf-4 \
		 --enable-dap \
		 --enable-ncgen4 \
		 --enable-shared \
		 --enable-separate-fortran \
		 --enable-cxx4 \
		 --enable-docs-install \
		 --enable-udunits \
		 --disable-logging \
		 --with-hdf5=/opt/csw \
		 --with-zlib=/opt/csw

## 64 bit build fails in fortran binding tests
## Disabling 64 bit builds until we can tweak GAR to handle Fortran  & ARCH
BUILD64 = 0

## Needed for "Large file support" in NetCDF
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

## Can't use Sun Studio with shared libs:
##  * non-redistributable libs in /opt/SUNWspro prevent Sun Studio
## Can't use GCC4
##  * C++ is way broken for 32-bit Sparc
##    During the 32-bit sparc build, the C++ bindings were barfing with an error
##    about undefined symbol __sync_fetch_and_add_4 in libnetcdf_c++
##    http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
##  * Fortran to C bindings fail test on 64-bit sparc
GARCOMPILER = GCC3

DEBUG_PACKAGING = 1
include gar/category.mk
