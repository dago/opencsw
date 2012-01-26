NAME = Apache2-AuthzNIS
VERSION = 0.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ITEAHAUS

DESCRIPTION = mod_perl2 NIS Group Authorization module
define BLURB
  Long description
endef

PACKAGES = CSWpmap2authznis
CATALOGNAME = pm_ap2authznis
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmnetnis CSWap2_modperl

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
