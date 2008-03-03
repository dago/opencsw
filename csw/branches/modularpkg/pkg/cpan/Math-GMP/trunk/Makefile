GARNAME = Math-GMP
GARVERSION = 2.04
CATEGORIES = cpan
AUTHOR = CHIPT

DESCRIPTION = high speed arbitrary size integer math
define BLURB
  Math::GMP was designed to be a drop-in replacement both for Math::BigInt and
  for regular integer arithmetic. Unlike BigInt, though, Math::GMP uses the
  GNU gmp library for all of its calculations, as opposed to straight Perl
  functions. This can result in speed improvements.
endef

DISTFILES += CSWpmmathgmp.gspec CSWpmmathgmp.depend

DEPENDS += lib/gmp

include gar/category.mk
