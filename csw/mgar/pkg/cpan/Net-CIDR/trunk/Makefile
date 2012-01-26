NAME = Net-CIDR
VERSION = 0.14
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MRSAM

DESCRIPTION = Manipulate IPv4/IPv6 netblocks in CIDR notation
define BLURB
  Manipulate IPv4/IPv6 netblocks in CIDR notation
endef

# For some reason it's in a testing subdir even though it's an official release
MASTER_SITES = http://search.cpan.org/CPAN/authors/id/M/MR/MRSAM/testing/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PACKAGES = CSWpm-net-cidr
CATALOGNAME = pm_net_cidr
SPKG_DESC_CSWpm-net-cidr = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-net-cidr = CSWpmnetcidr
CATALOGNAME_CSWpmnetcidr = pm_netcidr

ARCHALL = 1

include gar/category.mk
