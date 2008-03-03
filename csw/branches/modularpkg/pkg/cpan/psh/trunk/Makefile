GARNAME = psh
GARVERSION = 1.8
CATEGORIES = cpan
AUTHOR = GREGOR

DESCRIPTION = simple interactive Perl shell
define BLURB
  The Perl Shell (psh) combines aspects of bash and other shells with the
  power of Perl scripting. It aspires to be your primary login shell.
endef

DISTFILES += $(call admfiles,CSWpsh,depend)

DEPENDS += cpan/Term-ReadLine-Gnu cpan/BSD-Resource

include gar/category.mk
