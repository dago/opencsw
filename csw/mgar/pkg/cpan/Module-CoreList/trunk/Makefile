GARNAME = Module-CoreList
GARVERSION = 2.17
CATEGORIES = cpan
AUTHOR = RGARCIA

DESCRIPTION = What modules shipped with versions of Perl
define BLURB
  What modules shipped with versions of Perl
endef

PACKAGES = CSWpmmodcorelist
CATALOGNAME = pm_modcorelist
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
