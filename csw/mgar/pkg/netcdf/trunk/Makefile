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
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = COPYRIGHT
PATCHFILES += 0001-Replace-usr-local-with-opt-csw-in-docs.patch
PATCHFILES += 0002-Fix-ftst_vars4-vlen-size.patch

BUILD_DEP_PKGS += CSWhdf5rt CSWlibhdf5-dev CSWzlib
#BUILD_DEP_PKGS += CSWgcc4gfortranrt CSWgcc4corert CSWgcc4g++rt
BUILD_DEP_PKGS += CSWtetex 
#BUILD_DEP_PKGS += CSWgcc4gfortran

PACKAGES = CSWnetcdf
CATALOGNAME_CSWnetcdf = netcdf
SPKG_DESC_CSWnetcdf = NetCDF - Machine-independent data formats for array-oriented scientific data
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibz1
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWnetcdf += CSWlibhdf5hl7

PACKAGES += CSWlibnetcdf7
CATALOGNAME_CSWlibnetcdf7 = libnetcdf7
PKGFILES_CSWlibnetcdf7 += $(call baseisadirs,$(libdir),libnetcdf\.so\.7\.1\.1)
PKGFILES_CSWlibnetcdf7 += $(call baseisadirs,$(libdir),libnetcdf\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibnetcdf7 += $(DESCRIPTION), libnetcdf.so.7
RUNTIME_DEP_PKGS_CSWlibnetcdf7 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibnetcdf7 += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibnetcdf7 += CSWlibhdf5hl7
RUNTIME_DEP_PKGS_CSWlibnetcdf7 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibnetcdf7 += CSWlibz1


PACKAGES += CSWlibnetcdf-c++4
CATALOGNAME_CSWlibnetcdf-c++4 = libnetcdf_c++4
PKGFILES_CSWlibnetcdf-c++4 += $(call baseisadirs,$(libdir),libnetcdf_c\+\+\.so\.4\.1\.0)
PKGFILES_CSWlibnetcdf-c++4 += $(call baseisadirs,$(libdir),libnetcdf_c\+\+\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibnetcdf-c++4 += $(DESCRIPTION), libnetcdf_c++.so.4
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibhdf5hl7
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibnetcdf-c++4 += CSWlibgcc-s1

PACKAGES += CSWlibnetcdff5
CATALOGNAME_CSWlibnetcdff5 = libnetcdff5
PKGFILES_CSWlibnetcdff5 += $(call baseisadirs,$(libdir),libnetcdff\.so\.5\.0\.0)
PKGFILES_CSWlibnetcdff5 += $(call baseisadirs,$(libdir),libnetcdff\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibnetcdff5 = Fortran shared libraries for netcdf - libnetcdff.so.5 
RUNTIME_DEP_PKGS_CSWlibnetcdff5_i386 += CSWlibquadmath0
# GARCH is either sparc or i386, covers 32 and 64 bit
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += $(RUNTIME_DEP_PKGS_CSWlibnetcdff5_$(GARCH))
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibhdf5-7
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibhdf5hl7
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibnetcdff5 += CSWlibnetcdf7


PACKAGES += CSWnetcdf-dev
CATALOGNAME_CSWnetcdf-dev = netcdf_dev
SPKG_DESC_CSWnetcdf-dev = Development files for NetCDF 
PKGFILES_CSWnetcdf-dev += $(call baseisadirs,$(libdir),libnetcdf\.so)
PKGFILES_CSWnetcdf-dev += $(call baseisadirs,$(libdir),libnetcdf_c\+\+\.so)
PKGFILES_CSWnetcdf-dev += $(call baseisadirs,$(libdir),libnetcdff\.so)
PKGFILES_CSWnetcdf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWnetcdf-dev += CSWlibnetcdf6
RUNTIME_DEP_PKGS_CSWnetcdf-dev += CSWlibnetcdff5
RUNTIME_DEP_PKGS_CSWnetcdf-dev += CSWlibnetcdf7
RUNTIME_DEP_PKGS_CSWnetcdf-dev += CSWlibnetcdf-c++4
RUNTIME_DEP_PKGS_CSWnetcdf-dev += CSWnetcdf

GARCOMPILER = GCC4

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-netcdf-4
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

BUILD64_LIBS_ONLY = 1

## Needed for "Large file support" in NetCDF
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

## During the 32-bit sparc build, the C++ bindings were barfing with an error 
## about undefined symbol __sync_fetch_and_add_4 in libnetcdf_c++
## From Porting FAQ: http://wiki.opencsw.org/porting-faq#toc5
## OPT_FLAGS_GCC = -O2 -pipe
#OPT_FLAGS_GCC = 

## Git patching is failing on a remerge/repackage
NOGITPATCH = 1

# netcdf-install is installation instructions, no need to replace /usr/local
# there
CHECKPKG_OVERRIDES_CSWnetcdf += file-with-bad-content|/usr/local|root/opt/csw/share/info/netcdf-install.info

# Begin various approaches to get around __sync_fetch_and_add_4
#
# Compile on Solaris 10 due to __sync_fetch_and_add_4 problems on solaris9-i386
# Builds fine on solaris9-sparc, but CSW tries to keep i386 and sparc catalogs
# identical and csw-upload-pkg won't accept it solaris-10-i386 solaris9-sparc.
#PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc
#
# Alternate approach: raise default ISA on solaris9-i386 from i386 to 
# pentium_pro
ISA_DEFAULT_i386-5.9 = pentium_pro

include gar/category.mk
