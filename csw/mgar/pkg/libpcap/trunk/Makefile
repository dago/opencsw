GARNAME = libpcap
GARVERSION = 1.0.0
CATEGORIES = lib

DESCRIPTION = System-independent interface for user-level packet capture
define BLURB
  A system-independent interface for user-level network packet capture.
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES  = sf-bugtrack-2224954-fix-autoconf-header.diff
PATCHFILES += sf-bugtrack-2504874-create-dir-patch.diff
PATCHFILES += shared-library.diff

PACKAGES = CSWlibpcap CSWlibpcapdevel

CATALOGNAME_CSWlibpcap = libpcap
CATALOGNAME_CSWlibpcapdevel = libpcap_devel

SPKG_DESC_CSWlibpcap = System-independent interface for user-level packet capture
SPKG_DESC_CSWlibpcapdevel = libpcap development files

BUILD64 = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus
EXTRA_BUILD_ISAS_i386  = pentium

TEST_TARGET = check

EXTRA_CFLAGS = -I.

EXTRA_CFLAGS_isa-sparcv9 = -xcode=pic32
EXTRA_CFLAGS_isa-amd64 = -xcode=pic32
EXTRA_CFLAGS += $(EXTRA_CFLAGS_isa-$(ISA))

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

REQUIRED_PKGS_CSWlibpcapdevel = CSWlibpcap

include gar/category.mk

post-install-modulated:
	ln -s libpcap.so.1.0.0 $(DESTDIR)$(libdir)/libpcap.so
	@$(MAKECOOKIE)
