# Copyright 2009,2010 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = netcdf
VERSION = 4.1.3
CATEGORIES = lib
DESCRIPTION = Machine-independent data formats for array-oriented scientific data
SPKG_SOURCEURL = http://www.unidata.ucar.edu/software/netcdf/
MASTER_SITES = ftp://ftp.unidata.ucar.edu/pub/netcdf/
DISTFILES  += $(NAME)-$(VERSION).tar.gz
DISTFILES  += CSWlibnetcdf6.cswreleasemgr
DISTFILES  += CSWlibnetcdff5.cswreleasemgr
DISTFILES  += CSWlibnetcdf-c++5.cswreleasemgr
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = COPYRIGHT

BUILD_DEP_PKGS += CSWhdf5rt CSWlibhdf5-dev CSWzlib
#BUILD_DEP_PKGS += CSWgcc4gfortranrt CSWgcc4corert CSWgcc4g++rt
BUILD_DEP_PKGS += CSWtetex 
#BUILD_DEP_PKGS += CSWgcc4gfortran

PACKAGES = CSWnetcdf
CATALOGNAME_CSWnetcdf = netcdf
SPKG_DESC_CSWnetcdf = NetCDF - Machine-independent data formats for array-oriented scientific data
RUNTIME_DEP_PKGS_CSWnetcdf += CSWhdf5rt
RUNTIME_DEP_PKGS_CSWnetcdf += CSWzlib
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibnetcdf6

PACKAGES += CSWlibnetcdf6
CATALOGNAME_CSWlibnetcdf6 = libnetcdf6
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6.0.0
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6\.[0-9\.]+
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/libnetcdf.so.6
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6.0.0
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6\.[0-9\.]+
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/sparcv9/libnetcdf.so.6
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/amd64/libnetcdf.so.6.0.0
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/amd64/libnetcdf.so.6\.[0-9\.]+
PKGFILES_CSWlibnetcdf6 += /opt/csw/lib/amd64/libnetcdf.so.6
SPKG_DESC_CSWlibnetcdf6 = C shared library for netcdf - libnetcdf.so.6 
RUNTIME_DEP_PKGS_CSWlibnetcdf6  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdf6 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibnetcdf6 += CSWgcc4core # Mantis Bug #4497, missing 64 symlink

PACKAGES += CSWlibnetcdf-c++5
CATALOGNAME_CSWlibnetcdf-c++5 = libnetcdf_c++5
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5.0.0
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/libnetcdf_c\+\+.so.5
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5.0.0
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so.5
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/amd64/libnetcdf_c\+\+.so.5.0.0
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/amd64/libnetcdf_c\+\+.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdf-c++5 += /opt/csw/lib/amd64/libnetcdf_c\+\+.so.5
SPKG_DESC_CSWlibnetcdf-c++5 += C++ shared library for netcdf - libnetcdf_c++.so.5
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5 += CSWgcc4corert CSWgcc4core CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++5 += CSWlibnetcdf6

PACKAGES += CSWlibnetcdff5
CATALOGNAME_CSWlibnetcdff5 = libnetcdff5
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5.0.0
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/libnetcdff.so.5
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5.0.0
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/sparcv9/libnetcdff.so.5
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/amd64/libnetcdff.so.5.0.0
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/amd64/libnetcdff.so.5\.[0-9\.]+
PKGFILES_CSWlibnetcdff5 += /opt/csw/lib/amd64/libnetcdff.so.5
SPKG_DESC_CSWlibnetcdff5 = Fortran shared libraries for netcdf - libnetcdff.so.5 
RUNTIME_DEP_PKGS_CSWlibnetcdff5  = CSWhdf5rt
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWgcc4gfortranrt CSWgcc4corert CSWgcc4core
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibnetcdf6

PACKAGES += CSWnetcdf-devel
CATALOGNAME_CSWnetcdf-devel = netcdf_devel
SPKG_DESC_CSWnetcdf-devel = Development files for NetCDF 
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdf.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdf_c\+\+.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/libnetcdff.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdf.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdf_c\+\+.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/sparcv9/libnetcdff.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/amd64/libnetcdf.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/amd64/libnetcdf_c\+\+.so
PKGFILES_CSWnetcdf-devel += /opt/csw/lib/amd64/libnetcdff.so
PKGFILES_CSWnetcdf-devel += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWnetcdf-devel += CSWlibnetcdf6
RUNTIME_DEP_PKGS_CSWnetcdf-devel += CSWlibnetcdff5
RUNTIME_DEP_PKGS_CSWnetcdf-devel += CSWlibnetcdf-c++5

## CFLAGS AND LDFLAGS are necessary due to problems with the fortran bindings when
## building 64-bit
BUILD_ARGS  = CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" 
BUILD_ARGS += FFLAGS="$(FFLAGS)" FCFLAGS="$(FCFLAGS)"
## CXXFLAGS are necessary due to the gcc3core_rt problem noted below
BUILD_ARGS += CXXFLAGS="$(CXXFLAGS)"

## Test args need to be the same otherwise various tests don't link
#TEST_ARGS = $(BUILD_ARGS)

GARCOMPILER = GCC4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += F77=$(F77) FC=$(FC) CC=$(CC) CXX=$(CXX)
CONFIGURE_ARGS += CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" FFLAGS="$(FFLAGS)" FCFLAGS="$(FCFLAGS)"
CONFIGURE_ARGS += --enable-netcdf-4
## DAP is disabled due to bugs on Sparc Solaris 9 GCC4. Bug filed with UCAR:
## netCDF #ARO-502165
#CONFIGURE_ARGS += --enable-dap
CONFIGURE_ARGS += --disable-dap
CONFIGURE_ARGS += --enable-ncgen4
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --enable-separate-fortran
CONFIGURE_ARGS += --enable-cxx4
CONFIGURE_ARGS += --enable-docs-install
CONFIGURE_ARGS += --enable-udunits
CONFIGURE_ARGS += --disable-logging
CONFIGURE_ARGS += --with-hdf5=/opt/csw
CONFIGURE_ARGS += --with-zlib=/opt/csw

BUILD64 = 1

## Needed for "Large file support" in NetCDF
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

## During the 32-bit sparc build, the C++ bindings were barfing with an error 
## about undefined symbol __sync_fetch_and_add_4 in libnetcdf_c++
## From Porting FAQ: http://wiki.opencsw.org/porting-faq#toc5
## OPT_FLAGS_GCC = -O2 -pipe
#OPT_FLAGS_GCC = 

## Git patching is failing on a remerge/repackage
NOGITPATCH = 1

include gar/category.mk
