NAME = Devel-LexAlias
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCLAMP

DESCRIPTION = Alias lexical variables
define BLURB
  Devel::LexAlias provides the ability to alias a lexical variable in a
  subroutines scope to one of your choosing.
endef

PACKAGES = CSWpmdevellexalias
CATALOGNAME = pm_devellexalias

RUNTIME_DEP_PKGS = CSWpmdevelcaller CSWpmpadwalker
BUILD_DEP_PKGS = CSWpmdevelcaller CSWpmpadwalker

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
