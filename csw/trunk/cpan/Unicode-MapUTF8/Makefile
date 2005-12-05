GARNAME = Unicode-MapUTF8
GARVERSION = 1.11
CATEGORIES = cpan
AUTHOR = SNOWHARE

DESCRIPTION = conversions to and from arbitrary character sets and UTF8
define BLURB
  Provides an adapter layer between core routines for converting to and from
  UTF8 and other encodings. In essence, a way to give multiple existing
  Unicode modules a single common interface so you don't have to know the
  underlaying implementations to do simple UTF8 to-from other character set
  encoding conversions. As such, it wraps the Unicode::String, Unicode::Map8,
  Unicode::Map and Jcode modules in a standardized and simple API.
endef

DISTFILES += CSWpmumutf8.gspec CSWpmumutf8.depend

DEPENDS += cpan/Unicode-String cpan/Unicode-Map cpan/Unicode-Map8 cpan/Jcode

include ../category.mk
