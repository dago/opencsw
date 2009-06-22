GARNAME = Perl-Tidy
GARVERSION = 20090616
CATEGORIES = cpan
AUTHOR = SHANCOCK

DESCRIPTION = Indent and reformat Perl scripts.
define BLURB
  Perltidy is a Perl script which indents and reformats Perl scripts. The
  formatting is controlled by command line parameters; the default formatting
  follows the suggestions in perlstyle(1).
endef

PACKAGES = CSWperltidy
CATALOGNAME = perltidy
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
