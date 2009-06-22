GARNAME = PadWalker
GARVERSION = 1.7
CATEGORIES = cpan
AUTHOR = ROBIN

DESCRIPTION = Play with other peoples' lexical variables
define BLURB
  PadWalker is a module which allows you to inspect (and even change!)
  lexical variables in any subroutine which called you. It will only show
  those variables which are in scope at the point of the call.
endef

PACKAGES = CSWpmpadwalker
CATALOGNAME = pm_padwalker

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
