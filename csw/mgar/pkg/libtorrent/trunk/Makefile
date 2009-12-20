GARNAME = libtorrent
GARVERSION = 0.12.6
CATEGORIES = lib

DESCRIPTION = BitTorrent library written in C++ for *nix.
define BLURB
  BitTorrent library written in C++ for *nix, with a focus on high performance and good code.
  The library differentiates itself from other implementations by transfering directly from
  file pages to the network stack. On high-bandwidth connections it is able to seed at 3 times
  the speed of the official client. 
endef

MASTER_SITES = http://libtorrent.rakshasa.no/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
