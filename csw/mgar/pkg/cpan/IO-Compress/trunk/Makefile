NAME = IO-Compress
VERSION = 2.033
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

DISTFILES += COPYING

PACKAGES = CSWpm-io-compress
CATALOGNAME = pm_io_compress
SPKG_DESC_CSWpm-io-compress = $(DESCRIPTION)
OBSOLETES_CSWpm-io-compress = CSWpmiocompress
CATALOGNAME_CSWpmiocompress = pm_iocompress

ARCHALL = 1

RUNTIME_DEP_PKGS  = CSWpm-compress-raw-zlib
RUNTIME_DEP_PKGS += CSWpm-compress-raw-bzip2

# Uncomment if all packages who depend on these have switched to depend on this package
#INCOMPATIBLE_PKGS  = CSWpmcompresszlib
INCOMPATIBLE_PKGS += CSWpmiocompressbase
INCOMPATIBLE_PKGS += CSWpmiocompresszlib

# Not yet released, remove these next build
CHECKPKG_OVERRIDES_CSWpm-io-compress += unidentified-dependency|CSWpm-compress-raw-zlib
CHECKPKG_OVERRIDES_CSWpm-io-compress += unidentified-dependency|CSWpm-compress-raw-bzip2

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
