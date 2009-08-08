GARNAME = Params-Check
GARVERSION = 0.26
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = A generic input parsing/checking mechanism.
define BLURB
  Params::Check is a generic input parsing/checking mechanism.  It allows you
  to validate input via a template. The only requirement is that the arguments
  must be named.
endef

PACKAGES = CSWpmprmscheck 
CATALOGNAME = pm_prmscheck 
ARCHALL = 1

REQUIRED_PKGS = CSWpmlclemktxtsimple

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
