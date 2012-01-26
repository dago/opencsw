NAME = Devel-Caller
VERSION = 2.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCLAMP

DESCRIPTION = Meatier versions of caller
define BLURB
endef

PACKAGES = CSWpmdevelcaller
CATALOGNAME = pm_develcaller

RUNTIME_DEP_PKGS = CSWpmpadwalker
BUILD_DEP_PKGS = CSWpmpadwalker

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
