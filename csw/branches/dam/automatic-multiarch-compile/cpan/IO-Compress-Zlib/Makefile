GARNAME = IO-Compress-Zlib
GARVERSION = 2.004
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Read and write gzip and zip files/buffers.
define BLURB
  This module provides a Perl interface to allow reading and writing of RFC
  1950, 1951, 1952 (i.e. gzip) and zip files/buffers.
endef

DISTFILES = $(call admfiles,CSWpmiocompzlib,prototype)

DEPENDS += cpan/IO-Compress-Base
DEPENDS += cpan/Compress-Raw-Zlib

include ../category.mk
