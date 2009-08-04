GARNAME = Net-NIS
GARVERSION = 0.43
CATEGORIES = cpan
AUTHOR = ESM

DESCRIPTION = Interface to Sun's Network Information Service
define BLURB
  Long description
endef

PACKAGES = CSWpmnetnis
CATALOGNAME = pm_netnis

REQUIRED_PKGS = SUNWnisu

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
