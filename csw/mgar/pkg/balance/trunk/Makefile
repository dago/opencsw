GARNAME = balance
GARVERSION = 3.42
CATEGORIES = net

DESCRIPTION = A TCP proxy and load balancer
define BLURB
  Balance is a simple but powerful generic TCP proxy with round-robin load
  balancing and failover mechanisms. Its behaviour can be controlled at runtime
  using a simple command line syntax.
endef

MASTER_SITES = http://www.inlab.de/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Adjust-Makefile.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =

TEST_SCRIPTS =

include gar/category.mk
