NAME = Net-DNS
VERSION = 0.68
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = OLAF

DESCRIPTION = Interface to the DNS resolver
define BLURB
  Net::DNS is a collection of Perl modules that act as a Domain Name System
  (DNS) resolver. It allows the programmer to perform DNS queries that are
  beyond the capabilities of gethostbyname and gethostbyaddr.
endef

PACKAGES = CSWpm-net-dns
SPKG_DESC_CSWpm-net-dns = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-net-dns = CSWpmnetdns
CATALOGNAME_CSWpmnetdns = pm_netdns

DISTFILES += COPYING

RUNTIME_DEP_PKGS = CSWpmdigesthmac CSWpmnetip

CONFIGURE_ARGS  = --no-online-tests
CONFIGURE_ARGS += --no-IPv6-tests

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
