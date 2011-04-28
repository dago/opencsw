NAME = Net-UCP-IntTimeout
VERSION = 0.05
CATEGORIES = cpan
AUTHOR = NEMUX

DESCRIPTION = Perl Timeout Manager for Net::UCP Module
define BLURB
  Perl Timeout Manager for Net::UCP Module
endef

PACKAGES = CSWpm-net-ucp-inttimeout
CATALOGNAME = pm_net_ucp_inttimeout

DISTFILES += LICENSE
ARCHALL = 1

# temporary entries for the package renaming
INCOMPATIBLE_PKGS_CSWpm-net-ucp-inttimeout = CSWpmnetucpinttimeout
CHECKPKG_OVERRIDES_CSWpm-net-ucp-inttimeout += file-collision|/opt/csw/share/man/man3/Net::UCP::IntTimeout.3perl|CSWpm-net-ucp-inttimeout|CSWpmnetucpinttimeout
CHECKPKG_OVERRIDES_CSWpm-net-ucp-inttimeout += file-collision|/opt/csw/share/perl/csw/Net/UCP/IntTimeout.pm|CSWpm-net-ucp-inttimeout|CSWpmnetucpinttimeout

post-install-modulated:
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)
	@ginstall -m 644 $(FILEDIR)/LICENSE $(DESTDIR)/opt/csw/share/doc/$(CATALOGNAME)/license

include gar/category.mk
