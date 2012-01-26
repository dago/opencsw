NAME = IO-Zlib
VERSION = 1.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TOMHUGHES

DESCRIPTION = IO:: style interface to Compress::Zlib
define BLURB
  IO::Zlib provides an IO:: style interface to Compress::Zlib and hence to
  gzip/zlib compressed files. It provides many of the same methods as the
  IO::Handle interface.
endef

DISTFILES += COPYING

RUNTIME_DEP_PKGS = CSWpmiocompress

PACKAGES = CSWpmiozlib
CATALOGNAME = pm_iozlib

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = \/opt\/csw\/share\/man.*

include gar/category.mk
