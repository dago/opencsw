GARNAME = Locale-Maketext-Lexicon
GARVERSION = 0.77
CATEGORIES = cpan
AUTHOR = DRTECH

DESCRIPTION = Use other catalog formats in Maketext
define BLURB
  This module provides lexicon-handling modules to read from other
  localization formats, such as Gettext, Msgcat, and so on.
endef

PACKAGES = CSWpmlclemktxtlex 
CATALOGNAME = pm_lclemktxtlex 
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
