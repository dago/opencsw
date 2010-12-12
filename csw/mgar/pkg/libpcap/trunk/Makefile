NAME = libpcap
VERSION = 1.1.1
CATEGORIES = lib

DESCRIPTION = System-independent interface for user-level packet capture
define BLURB
  A system-independent interface for user-level network packet capture.
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibpcap CSWlibpcapdevel

CATALOGNAME_CSWlibpcap = libpcap
CATALOGNAME_CSWlibpcapdevel = libpcap_devel

SPKG_DESC_CSWlibpcap = System-independent interface for user-level packet capture
SPKG_DESC_CSWlibpcapdevel = Development files for libpcap

RUNTIME_DEP_PKGS_CSWlibpcapdevel = CSWlibpcap

BUILD64 = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus
EXTRA_BUILD_ISAS_i386  = pentium

TEST_TARGET = check

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

# Make sure shared libraries are built
BUILD_ARGS = shared
INSTALL_ARGS = install-shared

# No test target for libpcap
TEST_SCRIPTS =

MERGE_DIRS_isa-sparcv8plus = $(libdir)
MERGE_DIRS_isa-pentium = $(libdir)

PKGFILES_CSWlibpcapdevel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibpcapdevel += surplus-dependency|CSWlibpcap

include gar/category.mk
