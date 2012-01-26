NAME = Module-CoreList
VERSION = 2.26
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = What modules shipped with versions of Perl
define BLURB
  What modules shipped with versions of Perl
endef

DISTFILES += COPYING

PACKAGES = CSWpmmodcorelist
CATALOGNAME = pm_modcorelist
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
