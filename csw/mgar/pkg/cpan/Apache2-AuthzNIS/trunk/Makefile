GARNAME = Apache2-AuthzNIS
GARVERSION = 0.13
CATEGORIES = cpan
AUTHOR = ITEAHAUS

DESCRIPTION = mod_perl2 NIS Group Authorization module
define BLURB
  Long description
endef

PACKAGES = CSWpmap2authznis
CATALOGNAME = pm_ap2authznis
ARCHALL = 1

REQUIRED_PKGS = CSWpmnetnis

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
