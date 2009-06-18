GARNAME = gmp
GARVERSION = 4.3.1
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

GARCOMPILER = GCC4
BUILD64 = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus sparcv8plus+vis 
EXTRA_BUILD_ISAS_i386  = pentium

TEST_TARGET = check

MPN_sparcv8 = "sparc32/v8 sparc32 generic"
MPN_sparcv8plus = "sparc32/v9 sparc32 generic"
MPN_sparcv8plus+vis = "sparc32/v9 sparc32 generic"
MPN_sparcv9 = "sparc64 generic"

ABI_i386 = 32
ABI_pentium = 32
ABI_amd64 = 64
MPN_i386 = "x86 generic"
MPN_pentium = "x86/pentium x86 generic"
MPN_amd64 = "x86_64 generic"

CONFIGURE_ARGS = ABI=$(ABI_$(ISA)) MPN_PATH=$(MPN_$(ISA)) $(DIRPATHS)

EXTRA_MERGE_DIRS_isa-sparcv8plus = $(includedir)
EXTRA_MERGE_DIRS_isa-sparcv8plus+vis = $(includedir)
EXTRA_MERGE_DIRS_isa-sparcv9 = $(includedir)
EXTRA_MERGE_DIRS_isa-amd64 = $(includedir)
EXTRA_MERGE_DIRS_isa-pentium = $(includedir)

PACKAGES = CSWlibgmp

include gar/category.mk
ifeq ($(ISA), sparcv8plus)
	ARCHFLAGS_$(GARCOMPILER)_$(ISA) = -mcpu=v9 -mv8plus
endif
ifeq ($(ISA), sparcv8plus+vis)
	ARCHFLAGS_$(GARCOMPILER)_$(ISA) = -mcpu=v9 -mvis
endif

