NAME = Net-DNS
VERSION = 0.74
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NLNETLABS

DESCRIPTION = Interface to the DNS resolver
define BLURB
endef

PACKAGES = CSWpm-net-dns
SPKG_DESC_CSWpm-net-dns = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-net-dns = CSWpmnetdns
CATALOGNAME_CSWpmnetdns = pm_netdns

DISTFILES += COPYING

RUNTIME_DEP_PKGS  = CSWpm-digest-hmac
RUNTIME_DEP_PKGS += CSWpm-net-ip

CONFIGURE_ARGS  = --no-online-tests
CONFIGURE_ARGS += --no-IPv6-tests

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
