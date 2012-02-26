NAME = libpcap
VERSION = 1.2.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = System-independent interface for user-level packet capture
define BLURB
  A system-independent interface for user-level network packet capture.
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.tcpdump.org/

LICENSE = LICENSE

PACKAGES += CSWlibpcap1
SPKG_DESC_CSWlibpcap1 = System-independent interface for user-level packet capture, libpcap.so.1
PKGFILES_CSWlibpcap1 += $(call pkgfiles_lib,libpcap.so.1)
PKGFILES_CSWlibpcap1 += $(mandir)/man5/.*
OBSOLETED_BY_CSWlibpcap1 += CSWlibpcap

PACKAGES += CSWlibpcap-dev
SPKG_DESC_CSWlibpcap-dev = Development files for libpcap
RUNTIME_DEP_PKGS_CSWlibpcap-dev = CSWlibpcap1
# PKGFILES is catchall
# Lots of packages require libpcap.so as the old library didn't have a SONAME set.
# As this link is only in CSWlibpcap-dev the old CSWlibpcap needs to depend on it.
OBSOLETED_BY_CSWlibpcap-dev += CSWlibpcap
OBSOLETED_BY_CSWlibpcap-dev += CSWlibpcapdevel
CATALOGNAME_CSWlibpcapdevel = libpcap_devel_stub

BUILD64 = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus
EXTRA_BUILD_ISAS_i386  = pentium

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

# Make sure shared libraries are built
BUILD_ARGS = shared
INSTALL_ARGS = install-shared

# No test target for libpcap
TEST_SCRIPTS =

MERGE_DIRS_isa-sparcv8plus = $(libdir)
MERGE_DIRS_isa-pentium = $(libdir)

# These are in the binaries only and specifiy compiler lines for unused includes
CHECKPKG_OVERRIDES_CSWlibpcap1 += file-with-bad-content

include gar/category.mk
