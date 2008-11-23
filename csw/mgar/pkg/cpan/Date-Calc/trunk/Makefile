GARNAME = Date-Calc
GARVERSION = 5.4
CATEGORIES = cpan
AUTHOR = STBEY

DESCRIPTION = Gregorian calendar date calculations.
define BLURB
  This package consists of a C library and a Perl module (which uses the C
  library, internally) for all kinds of date calculations based on the
  Gregorian calendar (the one used in all western countries today), thereby
  complying with all relevant norms and standards: ISO/R 2015-1971, DIN 1355
  and, to some extent, ISO 8601 (where applicable).
endef

DISTFILES += $(call admfiles,CSWpmdatecalc,depend prototype)

DEPENDS += cpan/Carp-Clan
DEPENDS += cpan/Bit-Vector

include gar/category.mk
