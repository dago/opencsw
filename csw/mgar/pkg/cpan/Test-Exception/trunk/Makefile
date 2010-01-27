GARNAME = Test-Exception
GARVERSION = 0.29
CATEGORIES = cpan
AUTHOR = ADIE

DESCRIPTION = Test exception based code
define BLURB
  This module provides a few convenience methods for testing exception 
  based code. It is built with Test::Builder and plays happily with 
  Test::More and friends.
endef

PACKAGES = CSWpmtstexception
CATALOGNAME = pm_tstexception

# depends
REQUIRED_PKGS     = CSWpmsubuplevel
PREREQUISITE_PKGS = CSWpmsubuplevel

ARCHALL = 1

include gar/category.mk

# needed because of perl 5.8
pre-install-modulated:
	gsed -i'' 's,^DESTDIR =,DESTDIR = $(DESTDIR),' $(WORKSRC)/Makefile
	gsed -i'' 's,^\(MOD_INSTALL\) =,\1= PERL_INSTALL_ROOT=$(DESTDIR),'\
		$(WORKSRC)/Makefile
	perl -pi -e 's/install\(\[ from_to/install_default\(\[ from_to/' \
		$(WORKSRC)/Makefile
