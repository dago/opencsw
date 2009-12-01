GARNAME = Mail-SPF
GARVERSION = 2.007
CATEGORIES = cpan
AUTHOR = JMEHNLE

DISTNAME = $(GARNAME)-v$(GARVERSION)
MODDIST = $(DISTNAME).tar.gz

DESCRIPTION = Perl extension for Sender Policy Framework
define BLURB
endef

PACKAGES = CSWpmmailspf
CATALOGNAME = pm_mailspf

ARCHALL = 1

EXTRA_PAX_ARGS = '-s,spfquery,spfquery-cpan,p'
EXTRA_PAX_ARGS += '-s,spfd,spfd-cpan,p'

include gar/category.mk
