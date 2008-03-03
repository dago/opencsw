GARNAME = Compress-Raw-Zlib
GARVERSION = 2.004
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Low-Level Interface to zlib compression library
define BLURB
  The Compress::Raw::Zlib module provides a Perl interface to the zlib
  compression library.
endef

DISTFILES = $(call admfiles,CSWpmcomprawzlib,depend prototype)

# Use CSWzlib instead of the dist version
PATCHFILES += cswzlib.diff

#DEPEND += lib/zlib

include gar/category.mk
