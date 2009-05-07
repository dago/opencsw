GARNAME = Compress-Raw-Zlib
GARVERSION = 2.019
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Low-Level Interface to zlib compression library
define BLURB
  The Compress::Raw::Zlib module provides a Perl interface to the zlib
  compression library.
endef

DISTFILES += COPYING

CATALOGNAME = pm_compressrawzlib
PACKAGES = CSWpmcompressrawzlib

REQUIRED_PKGS = CSWzlib

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

CONFIGURE_ARGS =

#SKIPTEST = 1

# Use CSWzlib instead of the dist version
#PATCHFILES += cswzlib.diff

include gar/category.mk
