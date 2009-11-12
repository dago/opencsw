GARNAME = dnstracer
GARVERSION = 1.9
CATEGORIES = apps

DESCRIPTION = Trace a chain of DNS servers to the source
define BLURB
  Dnstracer determines where a given Domain Name Server (DNS) gets its
  information from, and follows the chain of DNS servers back to the
  servers which know the data.
endef

MASTER_SITES = http://www.mavetju.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

SPKG_SOURCEURL = http://www.mavetju.org/unix/general.php

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-ipv6

EXTRA_LDFLAGS = -lresolv

TEST_TARGET = check

include gar/category.mk
