GARNAME = Crypt-IDEA
GARVERSION = 1.02
CATEGORIES = cpan
AUTHOR = DPARIS

DESCRIPTION = Perl interface to IDEA block cipher
define BLURB
  This perl extension is an implementation of the IDEA block cipher algorithm.
endef

DISTFILES += CSWpmcryptidea.gspec

# Allow IDEA to build on Solaris
PATCHFILES  = solaris.diff

# Full IDEA test suite
PATCHFILES += test_suite.diff

include ../category.mk
