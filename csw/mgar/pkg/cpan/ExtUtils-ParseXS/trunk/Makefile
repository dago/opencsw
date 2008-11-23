GARNAME = ExtUtils-ParseXS
GARVERSION = 2.18
CATEGORIES = cpan
AUTHOR = KWILLIAMS

DESCRIPTION = converts Perl XS code into C code
define BLURB
  ExtUtils::ParseXS will compile XS code into C code by embedding the
  constructs necessary to let C functions manipulate Perl values and creates
  the glue necessary to let Perl access those functions. The compiler uses
  typemaps to determine how to map C function parameters and variables to Perl
  values.
endef

DISTFILES += $(call admfiles,CSWpmextutparsexs,prototype)

BUILDDEPS += cpan/ExtUtils-CBuilder

include gar/category.mk
