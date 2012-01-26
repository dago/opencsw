NAME = Parse-CPAN-Meta
VERSION = 1.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SMUELLER

DESCRIPTION = Parse META.yml and other similar CPAN metadata files
define BLURB
  Long description
endef

PACKAGES = CSWpmparsecpanmeta
CATALOGNAME = pm_parsecpanmeta
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
