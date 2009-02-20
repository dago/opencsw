GARNAME = gmp
GARVERSION = 4.2.4
CATEGORIES = lib

DESCRIPTION = GNU Multiple Precision Arithmetic Library
define BLURB
  GMP is a free library for arbitrary precision arithmetic, operating on signed
  integers, rational numbers, and floating point numbers. There is no limit to
  the precision, except for the ones implied by available memory. It has a rich
  set of functions, and the functions have a regular interface. It is designed
  to be as fast as possible, both for small operands and for huge operands. The
  speed is achieved by using fullwords as the basic arithmetic type, by using
  fast algorithms with carefully optimized assembly code for the most common
  inner loops for a lot of CPUs, and by a general emphasis on speed (instead of
  simplicity or elegance). It is believed to be faster than any other similar
  library. The advantage increases with the operand sizes for certain
  operations, since GMP in many cases has asymptotically faster algorithms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://gmplib.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1

TEST_TARGET = check

MPN_sparcv8 = "sparc32/v8 sparc32 generic"
MPN_sparcv9 = "sparc64/v9 generic"

#CONFIGURE_ARGS = ABI=32 $(DIRPATHS)
CONFIGURE_ARGS = MPN_PATH=$(MPN_$(ISA)) $(DIRPATHS)

PACKAGES = CSWlibgmp

include gar/category.mk
