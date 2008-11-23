GARNAME = gperf
GARVERSION = 3.0.3
CATEGORIES = devel

DESCRIPTION = A perfect hash function generator
define BLURB
  GNU gperf is a perfect hash function generator. For a given list of strings,
  it produces a hash function and hash table, in form of C or C++ code, for
  looking up a value depending on the input string. The hash function is perfect,
  which means that the hash table has no collisions, and the hash table lookup
  needs a single string comparison only.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWgperf)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

