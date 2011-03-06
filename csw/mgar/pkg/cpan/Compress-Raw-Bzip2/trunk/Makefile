NAME = Compress-Raw-Bzip2
VERSION = 2.033
CATEGORIES = cpan
AUTHOR = PMQS

DESCRIPTION = Low-Level Interface to bzip2 compression library
define BLURB
  Compress-Raw-Bzip2 provides the interface to the bzip2 library for the modules
  IO::Compress::Bzip2 and IO::Compress::Bunzip2.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-compress-raw-bzip2
CATALOGNAME = pm_compress_raw_bzip2
SPKG_DESC_CSWpm-compress-raw-bzip2 = $(DESCRIPTION)
OBSOLETES_CSWpm-compress-raw-bzip2 = CSWpmcompressrawbz2
CATALOGNAME_CSWpmcompressrawbz2 = pm_compressrawbz2

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
