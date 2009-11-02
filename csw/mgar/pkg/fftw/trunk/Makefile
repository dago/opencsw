GARNAME = fftw
GARVERSION = 3.2.2
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.fftw.org/

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(bindir)

include gar/category.mk
