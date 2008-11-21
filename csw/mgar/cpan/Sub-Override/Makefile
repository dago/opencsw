GARNAME = Sub-Override
GARVERSION = 0.08
CATEGORIES = cpan
AUTHOR = OVID

DESCRIPTION = Perl extension for easily overriding subroutines
define BLURB
Sometimes subroutines need to be overridden. In fact, your author does
this constantly for tests. Particularly when testing, using a Mock
Object can be overkill when all you want to do is override one tiny,
little function.
endef

DISTFILES += CSWpmsuboverride.gspec CSWpmsuboverride.depend

DEPENDS += cpan/Sub-Uplevel cpan/Test-Exception

include ../category.mk
