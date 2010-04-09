GARNAME = Crypt-RC5
GARVERSION = 2.00
CATEGORIES = cpan
AUTHOR = SIFUKURT

DESCRIPTION = Perl implementation of the RC5 encryption algorithm
define BLURB
  Perl implementation of the RC5 encryption algorithm
endef

DISTFILES += COPYING

PACKAGES = CSWpmcryptrc5
CATALOGNAME = pm_cryptrc5
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk
