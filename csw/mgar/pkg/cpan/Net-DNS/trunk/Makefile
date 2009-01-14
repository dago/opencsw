GARNAME = Net-DNS
GARVERSION = 0.64
CATEGORIES = cpan
AUTHOR = OLAF

DESCRIPTION = Interface to the DNS resolver
define BLURB
  Net::DNS is a collection of Perl modules that act as a Domain Name System
  (DNS) resolver. It allows the programmer to perform DNS queries that are
  beyond the capabilities of gethostbyname and gethostbyaddr.
endef

DISTFILES += $(call admfiles,CSWpmnetdns,)

REQUIRED_PKGS = CSWpmdigesthmac CSWpmnetip

# Update watch
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = --no-online-tests
CONFIGURE_ARGS += --no-IPv6-tests

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
