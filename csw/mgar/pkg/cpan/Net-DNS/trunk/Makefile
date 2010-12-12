NAME = Net-DNS
VERSION = 0.66
CATEGORIES = cpan
AUTHOR = OLAF

DESCRIPTION = Interface to the DNS resolver
define BLURB
  Net::DNS is a collection of Perl modules that act as a Domain Name System
  (DNS) resolver. It allows the programmer to perform DNS queries that are
  beyond the capabilities of gethostbyname and gethostbyaddr.
endef

PACKAGES = CSWpmnetdns
CATALOGNAME = pm_netdns

DISTFILES += COPYING

RUNTIME_DEP_PKGS = CSWpmdigesthmac CSWpmnetip

DEPENDS += cpan/Net-IP

CONFIGURE_ARGS  = --no-online-tests
CONFIGURE_ARGS += --no-IPv6-tests

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

# Weird problem on sparc
TEST_SCRIPTS =

include gar/category.mk
