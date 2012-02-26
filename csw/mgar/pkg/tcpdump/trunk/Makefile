NAME = tcpdump
VERSION = 4.2.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Dump network traffic
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3494835&group_id=53066&atid=469573
PATCHFILES += 0001-Use-expr-instead-of-bashism.patch

VENDOR_URL = http://www.tcpdump.org/

LICENSE = LICENSE

PACKAGES += CSWtcpdump
SPKG_DESC_CSWtcpdump = Dump network traffic
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibsmi2

BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibsmi-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-crypto=$(prefix)
CONFIGURE_ARGS += --with-smi

# There is a versioned tcpdump, which is not a hardlink. No need for that.
EXTRA_MERGE_EXCLUDE_FILES = $(sbindir)/tcpdump\..*

include gar/category.mk
