NAME = cfitsio
VERSION = 3.24
CATEGORIES = lib

DESCRIPTION = A library of C and Fortran subroutines for reading and writing data files in FITS
define BLURB
  CFITSIO provides simple high-level routines for reading and writing FITS files that
  insulate the programmer from the internal complexities of the FITS format.
  CFITSIO also provides many advanced features for manipulating and filtering the
  information in FITS files
endef

MASTER_SITES = ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/
DISTFILES  = $(NAME)3240.tar.gz

DISTNAME = $(NAME)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://heasarc.gsfc.nasa.gov/fitsio/

LICENSE = License.txt

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_ARGS = all testprog

TEST_SCRIPTS = custom

include gar/category.mk

# Test procedure taken from README
test-custom:
	(cd $(WORKSRC); ./testprog > testprog.lis; diff testprog.lis testprog.out && cmp testprog.fit testprog.std)
	@$(MAKECOOKIE)
