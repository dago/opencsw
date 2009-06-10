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
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PACKAGES = CSWlibmhash

include gar/category.mk
