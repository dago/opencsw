GARNAME = Math-Pari
GARVERSION = 2.010603
CATEGORIES = cpan
AUTHOR = ILYAZ

DESCRIPTION = interface to PARI numerical analysis library
define BLURB
  This package is a Perl interface to famous library PARI for
  numerical/scientific/number-theoretic calculations. It allows use of most
  PARI functions as Perl functions, and (almost) seamless merging of PARI and
  Perl data. In what follows we suppose prior knowledge of what PARI is (see
  ftp://megrez.math.u-bordeaux.fr/pub/pari, or Math::libPARI).
endef

MASTER_SITES = $(CPAN_MIRROR) http://pari.math.u-bordeaux.fr/pub/pari/unix/
DISTFILES += pari-2.1.6.tgz
DISTFILES += CSWpmmathpari.gspec

CONFIGURE_ARGS = paridir=../pari-2.1.6

# Avoid oddness - check for updates manually
MANUAL_UPDATE = 1

include ../category.mk

# Modify AUTHOR ID
AUTHOR_ID := $(AUTHOR_ID)/modules

