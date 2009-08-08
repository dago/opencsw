# Locale-Maketext-Simple 0.19 lacks Makefile.PL
# Locale-Maketext-Simple 0.20 requires higher MakeMaker rev than we have
#   Warning: prerequisite ExtUtils::MakeMaker 6.42 not found. We have 6.30.
#
GARNAME = Locale-Maketext-Simple
GARVERSION = 0.18
CATEGORIES = cpan
AUTHOR = $(AUTHOR_$(GARVERSION))
AUTHOR_0.18 = AUDREYT
AUTHOR_0.19 = JESSE
AUTHOR_0.20 = JESSE

DESCRIPTION = Simple interface to Locale::Maketext::Lexicon
define BLURB
  This module is a simple wrapper around Locale::Maketext::Lexicon, designed
  to alleviate the need of creating Language Classes for module authors.
endef

PACKAGES = CSWpmlclemktxtsimple
CATALOGNAME = pm_lclemktxtsimple 
ARCHALL = 1

REQUIRED_PKGS = CSWpmlclemktxtlex

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
