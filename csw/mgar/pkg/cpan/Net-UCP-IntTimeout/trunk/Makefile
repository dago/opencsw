NAME = Net-UCP-IntTimeout
VERSION = 0.05
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Perl Timeout Manager for Net::UCP Module
define BLURB
  Perl Timeout Manager for Net::UCP Module
endef

PACKAGES = CSWpmnetucpinttimeout
CATALOGNAME = pm_netucpinttimeout

CHECKPKG_OVERRIDES_CSWpmnetucpinttimeout += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucpinttimeout|catalogname=pm_netucpinttimeout|expected-catalogname=pmnetucpinttimeout

DISTFILES += LICENSE
ARCHALL = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)/license

include gar/category.mk
