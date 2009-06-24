GARNAME = Devel-Caller
GARVERSION = 2.03
CATEGORIES = cpan
AUTHOR = RCLAMP

DESCRIPTION = Meatier versions of caller
define BLURB
endef

PACKAGES = CSWpmdevelcaller
CATALOGNAME = pm_develcaller

REQUIRED_PKGS = CSWpmpadwalker

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
