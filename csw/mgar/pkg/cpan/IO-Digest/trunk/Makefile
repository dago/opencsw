GARNAME = IO-Digest
GARVERSION = 0.10
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = calculate digests while reading or writing
define BLURB
  This module allows you to calculate digests while reading or writing file
  handles. This avoids the case you need to reread the same content to compute
  the digests after written a file.
endef

DISTFILES = $(call admfiles,CSWpmiodigest,depend prototype)

DEPENDS += cpan/PerlIO-via-dynamic

include gar/category.mk
