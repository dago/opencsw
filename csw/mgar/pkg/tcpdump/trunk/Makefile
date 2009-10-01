GARNAME = tcpdump
GARVERSION = 4.0.0
CATEGORIES = utils

DESCRIPTION = tcpdump allows you to dump the traffic on a network
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

PREREQUISITE_PKGS = CSWlibpcap CSWosslrt CSWossldevel
REQUIRED_PKGS = CSWlibpcap CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.tcpdump.org/

# No test target for libpcap
TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

EXTRA_MERGE_EXCLUDE_FILES = $(sbindir)/tcpdump\..*

include gar/category.mk
