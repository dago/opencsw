GARNAME = Net-DNS
GARVERSION = 0.48
CATEGORIES = cpan
AUTHOR = CREIN

DESCRIPTION = interface to the DNS resolver
define BLURB
  Net::DNS is a collection of Perl modules that act as a Domain Name System
  (DNS) resolver. It allows the programmer to perform DNS queries that are
  beyond the capabilities of gethostbyname and gethostbyaddr.
endef

DISTFILES += CSWpmnetdns.gspec CSWpmnetdns.depend

DEPENDS += cpan/Digest-HMAC

CONFIGURE_ARGS = --no-online-tests

include ../category.mk
