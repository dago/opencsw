NAME = Net-UCP-Common
VERSION = 0.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NEMUX

DESCRIPTION = Common Stuff for Net::UCP Module
define BLURB
  Common Stuff for Net::UCP Module
endef

PACKAGES = CSWpm-net-ucp-common
CATALOGNAME = pm_net_ucp_common

DISTFILES += LICENSE
ARCHALL = 1

# temporary entries fo the package renaming
INCOMPATIBLE_PKGS_CSWpm-net-ucp-common = CSWpmnetucpcommon
CHECKPKG_OVERRIDES_CSWpm-net-ucp-common += file-collision|/opt/csw/share/man/man3/Net::UCP::Common.3perl|CSWpm-net-ucp-common|CSWpmnetucpcommon
CHECKPKG_OVERRIDES_CSWpm-net-ucp-common += file-collision|/opt/csw/share/perl/csw/Net/UCP/Common.pm|CSWpm-net-ucp-common|CSWpmnetucpcommon

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)/license
	@$(MAKECOOKIE)

include gar/category.mk
