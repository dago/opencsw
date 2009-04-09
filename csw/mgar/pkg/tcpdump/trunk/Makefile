GARNAME = tcpdump
GARVERSION = 3.9.8
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

# Shared libraries patch
#PATCHFILES = solib.diff

# No test target for libpcap
TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

#INSTALL_OVERRIDE_DIRS = prefix exec_prefix includedir libdir mandir 

include gar/category.mk
