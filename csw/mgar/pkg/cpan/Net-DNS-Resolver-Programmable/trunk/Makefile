NAME = Net-DNS-Resolver-Programmable
VERSION = 0.003
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JMEHNLE

DESCRIPTION = Programmable DNS resolver class for offline emulation of DNS
define BLURB
endef

MASTER_SITES = $(addsuffix net-dns-resolver-programmable/,$(CPAN_MIRRORS))
DISTNAME = $(NAME)-v$(VERSION)

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-net-dns-resolver-programma
SPKG_DESC_CSWpm-net-dns-resolver-programma = Programmable DNS resolver class for offline emulation of DNS
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-net-dns-resolver-programma = 1
RUNTIME_DEP_PKGS_CSWpm-net-dns-resolver-programma += CSWpm-net-dns
OBSOLETED_BY_CSWpm-net-dns-resolver-programma += CSWpmnetdnsreslvprg
CATALOGNAME_CSWpmnetdnsreslvprg = pm_netdnsreslvprg_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
