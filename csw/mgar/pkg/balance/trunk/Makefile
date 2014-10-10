NAME = balance
VERSION = 3.56
GARTYPE = v2

DESCRIPTION = A TCP proxy and load balancer
define BLURB
  Balance is a simple but powerful generic TCP proxy with round-robin load
  balancing and failover mechanisms. Its behaviour can be controlled at runtime
  using a simple command line syntax.
endef

MASTER_SITES = http://www.inlab.de/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-Use-Solaris-and-CSW-layout.patch
PATCHFILES += 0002-Allow-setting-of-SHMDIR-via-CFLAGS.patch

VENDOR_URL = http://www.inlab.de/balance.html

EXTRA_CFLAGS += -DSHMDIR=\\\"/var/tmp/balance\\\"

CONFIGURE_SCRIPTS =

TEST_SCRIPTS =

# This is a good location
CHECKPKG_OVERRIDES_CSWbalance += bad-location-of-file|file=/var/run/balance

include gar/category.mk
