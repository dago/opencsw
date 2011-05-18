NAME = fftw
VERSION = 3.2.2
CATEGORIES = lib

DESCRIPTION = Library for computing the discrete Fourier transform (DFT)
define BLURB
  FFTW is a C subroutine library for computing the discrete Fourier transform (DFT)
  in one or more dimensions, of arbitrary input size, and of both real and complex
  data (as well as of even/odd data, i.e. the discrete cosine/sine transforms or
  DCT/DST). We believe that FFTW, which is free software, should become the FFT
  library of choice for most applications.
endef

MASTER_SITES = http://www.fftw.org/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.fftw.org/

PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWlibfftw3-3
SPKG_DESC_CSWlibfftw3-3 = Library for computing the discrete Fourier transform (DFT), libfftw3.so.3
PKGFILES_CSWlibfftw3-3 = $(call pkgfiles_lib,libfftw3.so.3)

PACKAGES += CSWlibfftw3threads3
SPKG_DESC_CSWlibfftw3threads3 = Library for computing the discrete Fourier transform (DFT), libfftw3_threads.so.3
PKGFILES_CSWlibfftw3threads3 = $(call pkgfiles_lib,libfftw3_threads.so.3)

PACKAGES += CSWlibfftw-dev
SPKG_DESC_CSWlibfftw-dev = Development files for libfftw3.so.3
PKGFILES_CSWlibfftw-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibfftw-dev += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWlibfftw-dev += CSWlibfftw3threads3

PACKAGES += CSWfftw
SPKG_DESC_CSWfftw = Utilities for computing the discrete Fourier transform (DFT)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfftw += CSWlibfftw3-3
RUNTIME_DEP_PKGS_CSWfftw += CSWlibfftw3threads3

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += --enable-alloca
CONFIGURE_ARGS += --enable-portable-binary
# CONFIGURE_ARGS += --disable-fortran
#CONFIGURE_ARGS += --enable-mpi
#CONFIGURE_ARGS += --enable-openmp
CONFIGURE_ARGS += --enable-threads

# This is only available for Solaris 10
CONFIGURE_ARGS-5.10 += --enable-long-double

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))

MERGE_DIRS_isa-extra = $(bindir) $(libdir)

include gar/category.mk
