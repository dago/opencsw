NAME = Net-NIS
VERSION = 0.43
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ESM

DESCRIPTION = Interface to Sun's Network Information Service
define BLURB
  Long description
endef

PACKAGES = CSWpmnetnis
CATALOGNAME = pm_netnis

RUNTIME_DEP_PKGS = SUNWnisu

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
