NAME = Lexical-Persistence
VERSION = 0.98
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCAPUTO

DESCRIPTION = Persistent lexical variable values for arbitrary calls
define BLURB
endef

PACKAGES = CSWpmlexicalpersist
CATALOGNAME = pm_lexicalpersist
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmpadwalker CSWpmdevellexalias

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
