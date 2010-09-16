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
BUILD64 = 1

## Needed for "Large file support" in NetCDF
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

## non-redistributable libs in /opt/SUNWspro
GARCOMPILER = GCC3

DEBUG_PACKAGING = 1
## Add GCC4 lib dir to CFLAGS and friends because gcc3core_rt puts it's 
## libgcc_s.so in /opt/csw/lib and this breaks the build in all sorts of weird 
## places.
## Rationale: Automake keeps wanting to put /opt/csw/lib in the front of the 
## -L options during the linking phase, so the GCC3 libgcc_s gets pulled in 
## first and an unresolved symbol error occurs. By adding to the 
## CFLAGS/FFLAGS/FCFLAGS/CXXFLAGS, it is pulled in before AM_LDFLAGS in the 
## linking stage in most automake-generated Makefiles. Ugly hack but it works.
##
## Adding -dalign to *FLAGS in attempt to fix bus error in nf_test/ftst_vars4
## in fuction nf_put_vlen_element
#EXTRA_CFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
#EXTRA_FFLAGS= -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
#EXTRA_FCFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
#EXTRA_CXXFLAGS = -L/opt/csw/gcc4/lib/$(MM_LIBDIR) -dalign
## OPT_FLAGS_GCC = -O2 -pipe
include gar/category.mk

## During the 32-bit sparc build, the C++ bindings were barfing with an error 
## about undefined symbol __sync_fetch_and_add_4 in libnetcdf_c++
## Per http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
## replacing -march=v8 with -m32 seems to solve the problem
ARCHFLAGS_GCC4_sparcv8 = -m32 -mcpu=v8
