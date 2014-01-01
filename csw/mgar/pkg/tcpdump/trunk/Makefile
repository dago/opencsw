NAME = tcpdump
VERSION = 4.5.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Dump network traffic
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/r+= $(DISTNAME).tar.gzparc solaris10-i386

VENDOR_URL = http://www.tcpdump.org/

LICENSE = LICENSE

PACKAGES += CSWtcpdump
SPKG_DESC_CSWtcpdump = Dump network traffic
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibsmi2

BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibsmi-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-crypto=$(prefix)
CONFIGURE_ARGS += --with-smi

# There is a versioned tcpdump, which is not a hardlink. No need for that.
EXTRA_MERGE_EXCLUDE_FILES = $(sbi# There is a failing test:
#   https://github.com/the-tcpdump-group/tcpdump/issues/351
SKIPTEST ?= 1

include gar/category.mk
