GARNAME = Compress-Zlib
GARVERSION = 2.004
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Interface to zlib compression library
define BLURB
  The Compress::Zlib module provides a Perl interface to the zlib compression
  library (see /AUTHOR for details about where to get zlib). Most of the
  functionality provided by zlib is available in Compress::Zlib.
endef

DISTFILES = $(call admfiles,CSWpmcompresszlib,depend prototype)

DEPENDS += cpan/Compress-Raw-Zlib
DEPENDS += cpan/IO-Compress-Base
DEPENDS += cpan/IO-Compress-Zlib

include gar/category.mk
