GARNAME = IO-Zlib
GARVERSION = 1.05
CATEGORIES = cpan
AUTHOR = TOMHUGHES

DESCRIPTION = IO:: style interface to Compress::Zlib
define BLURB
  IO::Zlib provides an IO:: style interface to Compress::Zlib and hence to
  gzip/zlib compressed files. It provides many of the same methods as the
  IO::Handle interface.
endef

DISTFILES += $(call admfiles,CSWpmiozlib,depend prototype)

DEPENDS += cpan/Compress-Zlib

include ../category.mk
