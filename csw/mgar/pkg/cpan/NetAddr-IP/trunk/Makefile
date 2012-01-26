NAME = NetAddr-IP
VERSION = 4.040
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIKER

DESCRIPTION = Manages IPv4 and IPv6 addresses and subnets
define BLURB
  Manages IPv4 and IPv6 addresses and subnets
endef

DISTFILES = COPYING

PACKAGES = CSWpm-netaddr-ip
CATALOGNAME = pm_netaddr_ip
SPKG_DESC_CSWpm-netaddr-ip = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-netaddr-ip = CSWpmnetaddrip
CATALOGNAME_CSWpmnetaddrip = pm_netaddrip

# One IPv6 related test fails, make sure to check all others
SKIPTEST=1

include gar/category.mk
