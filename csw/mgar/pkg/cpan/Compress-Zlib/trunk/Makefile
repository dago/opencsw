GARNAME = Compress-Zlib
GARVERSION = 2.015
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Interface to zlib compression library
define BLURB
  The Compress::Zlib module provides a Perl interface to the zlib compression
  library (see /AUTHOR for details about where to get zlib). Most of the
  functionality provided by zlib is available in Compress::Zlib.
endef

DISTFILES += COPYING

CATALOGNAME = pm_compresszlib
PACKAGES = CSWpmcompresszlib
ARCHALL = 1

REQUIRED_PKGS = CSWpmiocompresszlib CSWpmcompressrawzlib CSWpmiocompressbase

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

DEPENDS += cpan/Compress-Raw-Zlib
DEPENDS += cpan/IO-Compress-Base
DEPENDS += cpan/IO-Compress-Zlib

CONFIGURE_ARGS =

SKIPTEST = 1

include gar/category.mk
