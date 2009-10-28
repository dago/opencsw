GARNAME = mhash
GARVERSION = 0.9.9.9
CATEGORIES = lib

DESCRIPTION = A uniform interface to a large number of hash algorithms
define BLURB
  Mhash is a free (under GNU Lesser GPL) library which provides a uniform
  interface to a large number of hash algorithms. These algorithms can be
  used to compute checksums, message digests, and other signatures.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_CPPFLAGS = -D__const=const

BUILD64 = 1
NOISALIST = 1

# sparcv9 compile fails with optimization beyond -xO1 at HAVAL256: FAIL: frag_test
# Please see files/README for details.

ifeq ($(ISA),sparcv9)
OPT_FLAGS_SOS = -xO1
endif

CONFIGURE_ARGS = $(DIRPATHS)

# Always run testsuite as the code is prone to optimization errors
TEST_TARGET = check

PACKAGES = CSWlibmhash

include gar/category.mk
