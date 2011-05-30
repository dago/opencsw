# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! ./configure fails, check for GeoIP doesn't include -lsocket
#
NAME = ipv6calc
VERSION = 0.90.0
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Utility for manipulating and querying IPv6 addresses
define BLURB
  ipv6calc is a small utility written in programming language C to
  manipulate (not only) IPv6 addresses. Intentions were convering a given
  IPv6 address into compressed format, convering a given IPv6 address into
  the same format like shown in /proc/net/if_inet6 and (because it was not
  difficulty) migrating the Perl program ip6_int into. Now only one
  utiltity is needed to do a lot.
endef

VENDOR_URL   = http://www.deepspace6.net/projects/ipv6calc.html
MASTER_SITES = ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/
DISTFILES    = $(DISTNAME).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-geoip
CONFIGURE_ARGS += --with-geoip-headers=$(includedir)
CONFIGURE_ARGS += --with-geoip-lib=$(libdir)

include gar/category.mk
