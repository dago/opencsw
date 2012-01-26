NAME = Net-UCP-TransactionManager
VERSION = 0.02
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NEMUX

DESCRIPTION = Perl extension to manage UCP session transaction numbers 
define BLURB
  Perl extension to manage UCP session transaction numbers 
endef

PACKAGES = CSWpm-net-ucp-transactionmanager
CATALOGNAME = pm_net_ucp_transactionmanager

#CHECKPKG_OVERRIDES_CSWpmnetucptransactionmanager += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucptransactionmanager|catalogname=pm_netucptransactionmanager|expected-catalogname=pmnetucptransactionmanager

# temporary entries for the package renaming
INCOMPATIBLE_PKGS_CSWpm-net-ucp-transactionmanager = CSWpmnetucptransactionmanager
CHECKPKG_OVERRIDES_CSWpm-net-ucp-transactionmanager += file-collision|/opt/csw/share/man/man3/Net::UCP::TransactionManager.3perl|CSWpm-net-ucp-transactionmanager|CSWpmnetucptransactionmanager
CHECKPKG_OVERRIDES_CSWpm-net-ucp-transactionmanager += file-collision|/opt/csw/share/perl/csw/Net/UCP/TransactionManager.pm|CSWpm-net-ucp-transactionmanager|CSWpmnetucptransactionmanager

DISTFILES += LICENSE
ARCHALL = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)/license

include gar/category.mk
