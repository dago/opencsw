NAME = Net-UCP-TransactionManager
VERSION = 0.02
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Perl extension to manage UCP session transaction numbers 
define BLURB
  Perl extension to manage UCP session transaction numbers 
endef

PACKAGES = CSWpmnetucptransactionmanager
CATALOGNAME = pm_netucptransactionmanager

CHECKPKG_OVERRIDES_CSWpmnetucptransactionmanager += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucptransactionmanager|catalogname=pm_netucptransactionmanager|expected-catalogname=pmnetucptransactionmanager

DISTFILES += LICENSE
ARCHALL = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)/license

include gar/category.mk
