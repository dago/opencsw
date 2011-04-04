NAME = Net-UCP-Common
VERSION = 0.05
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Common Stuff for Net::UCP Module
define BLURB
  Common Stuff for Net::UCP Module
endef

PACKAGES = CSWpmnetucpcommon
CATALOGNAME = pm_netucpcommon

CHECKPKG_OVERRIDES_CSWpmnetucpcommon += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucpcommon|catalogname=pm_netucpcommon|expected-catalogname=pmnetucpcommon

DISTFILES += LICENSE
ARCHALL = 1

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/pm_netucpcommon
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/pm_netucpcommon/license
	@$(MAKECOOKIE)

include gar/category.mk
