GARNAME = IO-Compress
GARVERSION = 2.020
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = A Perl interface to allow reading and writing of compressed data
define BLURB
  This distribution provides a Perl interface to allow reading and writing of
  compressed data created with the zlib and bzip2 libraries.

  IO-Compress supports reading and writing of bzip2, RFC 1950, RFC
  1951, RFC 1952 (i.e. gzip) and zip files/buffers.

  The following modules used to be distributed separately, but are now
  included with the IO-Compress distribution.

    Compress-Zlib
    IO-Compress-Zlib
    IO-Compress-Bzip2
    IO-Compress-Base

endef

REQUIRED_PKGS  = CSWpmcompressrawzlib
REQUIRED_PKGS += CSWpmcompressrawbz2

PACKAGES = CSWpmiocompress
CATALOGNAME = pm_iocompress

ARCHALL = 1

include gar/category.mk
