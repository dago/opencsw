GARNAME = balance
GARVERSION = 3.11
CATEGORIES = net

DESCRIPTION = A TCP proxy and load balancer.
define BLURB
  Balance is a simple but powerful generic TCP proxy with round-robin load
  balancing and failover mechanisms. Its behaviour can be controlled at runtime
  using a simple command line syntax.
endef

MASTER_SITES = http://www.inlab.de/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWbalance,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Configure for build with SunONE
PATCHFILES = build.diff

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk
