GARNAME = Log-Message-Simple
GARVERSION = 0.04
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Standardized logging facilities using the Log::Message module
define BLURB
  This module provides standardized logging facilities using the Log::Message
  module.
endef

PACKAGES = CSWpmlogmsgsimple 
CATALOGNAME = pm_logmsgsimple 
ARCHALL = 1

REQUIRED_PKGS = CSWpmlogmessage

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
