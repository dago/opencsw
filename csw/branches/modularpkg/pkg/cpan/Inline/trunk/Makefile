GARNAME = Inline
GARVERSION = 0.44
CATEGORIES = cpan
AUTHOR = INGY

DESCRIPTION = write Perl subroutines in other programming languages.
define BLURB
  The Inline module allows you to put source code from other programming
  languages directly "inline" in a Perl script or module. The code is
  automatically compiled as needed, and then loaded for immediate access from
  Perl.
endef

DISTFILES += CSWpminline.gspec CSWpminline.depend

# Enable building included Inline::C
PATCHFILES += inline.diff

DEPENDS += cpan/Parse-RecDescent

include gar/category.mk
