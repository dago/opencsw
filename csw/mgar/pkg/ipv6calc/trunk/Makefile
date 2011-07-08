# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Final linking fails
#   /opt/SUNWspro/bin/cc -m32 -xarch=386 -L/opt/csw/lib -o ipv6calc ipv6calc.o showinfo.o ../getopt/getopt.o ../getopt/getopt1.o ../md5/md5.o -lipv6calc -L../lib/ -L/opt/csw/lib -lGeoIP
#   ld: fatal: library -lipv6calc: not found
#
#   ^^ Happens in ipv6calc subdir, ../lib has a static libipv6calc
#   $ cd .. && find . -name libipv6calc.a
#   ./lib/libipv6calc.a
#
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

PATCHFILES += 0001-Include-lsocket-and-lnsl-in-.-configure-checks.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-geoip
CONFIGURE_ARGS += --with-geoip-headers=$(includedir)
CONFIGURE_ARGS += --with-geoip-lib=$(libdir)

# ipv6calc pre-sets DEFAULT_CFLAGS with gcc'isms, override these
BUILD_OVERRIDE_VARS = DEFAULT_CFLAGS
DEFAULT_CFLAGS =

include gar/category.mk

pre-configure-modulated:
	@cd $(WORKSRC) && autoreconf -fi
	@$(MAKECOOKIE)
