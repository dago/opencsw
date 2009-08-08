GARNAME = IPC-Cmd
GARVERSION = 0.46
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Finding and running system commands made easy
define BLURB
  IPC::Cmd allows you to run commands, interactively if desired, platform
  independent but have them still work.
endef

PACKAGES = CSWpmipccmd
CATALOGNAME = pm_ipccmd 
ARCHALL = 1

REQUIRED_PKGS = CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
