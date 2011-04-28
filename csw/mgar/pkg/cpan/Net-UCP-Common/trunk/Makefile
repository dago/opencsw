NAME = Net-UCP-Common
VERSION = 0.05
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Common Stuff for Net::UCP Module
define BLURB
  Common Stuff for Net::UCP Module
endef

PACKAGES = CSWpm-net-ucp-common
CATALOGNAME = pm_net_ucp_common

#CHECKPKG_OVERRIDES_CSWpmnetucpcommon += catalogname-does-not-match-pkgname|pkgname=CSWpmnetucpcommon|catalogname=pm_netucpcommon|expected-catalogname=pmnetucpcommon

DISTFILES += LICENSE
ARCHALL = 1

# temporary entries fo the package renaming
INCOMPATIBLE_PKGS_CSWpm-netucpcommon = CSWpmnetucpcommon
CHECKPKG_OVERRIDES_CSWpm-net-ucp-common += file-collision|/opt/csw/share/man/man3/Net::UCP::Common.3perl|CSWpm-net-ucp-common|CSWpmnetucpcommon
CHECKPKG_OVERRIDES_CSWpm-net-ucp-common += file-collision|/opt/csw/share/perl/csw/Net/UCP/Common.pm|CSWpm-net-ucp-common|CSWpmnetucpcommon

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/pm_net_ucp_common
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/pm_net_ucp_common/license
	@$(MAKECOOKIE)

include gar/category.mk
