GARNAME = Math-Pari
GARVERSION = 2.010709
CATEGORIES = cpan
AUTHOR = ILYAZ

# Note: This package does not use CSWparigp -- it builds a local
# static pari library, which gets linked with the Pari module shared
# object.  Passing 'parilib' to Makefile.PL won't find the CSW
# includes.  CSWparigp doesn't have the static lib, and linking with
# a shared libpari does't appear to be supported.
PARIGP_VERSION = 2.1.7

DESCRIPTION = interface to PARI numerical analysis library
define BLURB
  This package is a Perl interface to famous library PARI for
  numerical/scientific/number-theoretic calculations. It allows use of most
  PARI functions as Perl functions, and (almost) seamless merging of PARI and
  Perl data. In what follows we suppose prior knowledge of what PARI is (see
  ftp://megrez.math.u-bordeaux.fr/pub/pari, or Math::libPARI).
endef

MASTER_SITES  = http://pari.math.u-bordeaux.fr/pub/pari/unix/
MASTER_SITES += $(CPAN_MIRRORS)
DISTFILES += pari-$(PARIGP_VERSION).tgz
DISTFILES += $(call admfiles,CSWpmmathpari,depend prototype)

# Fix PariBuild to work with sun4u/v
#PATCHFILES += rt12324.diff

CONFIGURE_ARGS = paridir=../pari-$(PARIGP_VERSION)

# Avoid oddness - check for updates manually
MANUAL_UPDATE = 1

include gar/category.mk

# Modify AUTHOR ID
AUTHOR_ID := $(AUTHOR_ID)/modules

