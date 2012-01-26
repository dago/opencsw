NAME = B-Keywords
VERSION = 1.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JJORE

DESCRIPTION = Lists of reserved barewords and symbol names
define BLURB
  Long description
endef

PACKAGES = CSWpmbkeywords
CATALOGNAME = pm_bkeywords
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
