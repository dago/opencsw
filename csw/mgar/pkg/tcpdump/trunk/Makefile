NAME = tcpdump
VERSION = 4.1.1
CATEGORIES = utils

DESCRIPTION = Dump network traffic
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.tcpdump.org/

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWlibpcap
BUILD_DEP_PKGS += CSWosslrt
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibsmi
RUNTIME_DEP_PKGS += CSWlibpcap
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWlibsmi

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-crypto=$(prefix)
CONFIGURE_ARGS += --with-smi

# We don't have a proper uudecode
TEST_SCRIPTS =

# There is a versioned tcpdump, which is not a hardlink. No need for that.
EXTRA_MERGE_EXCLUDE_FILES = $(sbindir)/tcpdump\..*

include gar/category.mk
