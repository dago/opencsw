NAME = tcpdump
VERSION = 4.2.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Dump network traffic
define BLURB
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(DISTNAME).tar.gz

# Use patches until this is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=3444149&group_id=53066&atid=469573
PATCHFILES += 0001-Do-not-use-unnamed-unions.patch
PATCHFILES += 0002-Add-missing-ppi.h-from-upstream-GIT.patch
PATCHFILES += 0003-Add-missing-testsuite-files-from-upstream-GIT.patch

VENDOR_URL = http://www.tcpdump.org/

LICENSE = LICENSE

PACKAGES += CSWtcpdump
SPKG_DESC_CSWtcpdump = Dump network traffic
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWtcpdump += CSWosslrt
RUNTIME_DEP_PKGS_CSWtcpdump += CSWlibsmi2

BUILD_DEP_PKGS += CSWlibpcap-dev
BUILD_DEP_PKGS += CSWosslrt
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibsmi-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-crypto=$(prefix)
CONFIGURE_ARGS += --with-smi

# There is a versioned tcpdump, which is not a hardlink. No need for that.
EXTRA_MERGE_EXCLUDE_FILES = $(sbindir)/tcpdump\..*

include gar/category.mk
