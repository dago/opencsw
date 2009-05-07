GARNAME = IO-Compress-Zlib
GARVERSION = 2.015
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Read and write gzip and zip files/buffers.
define BLURB
  This module provides a Perl interface to allow reading and writing of RFC
  1950, 1951, 1952 (i.e. gzip) and zip files/buffers.
endef

DISTFILES += COPYING

CATALOGNAME = pm_iocompresszlib
PACKAGES = CSWpmiocompresszlib
ARCHALL = 1

REQUIRED_PKGS = CSWpmiocompressbase CSWpmcompressrawzlib

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

CONFIGURE_ARGS =

SKIPTEST = 1

include gar/category.mk
