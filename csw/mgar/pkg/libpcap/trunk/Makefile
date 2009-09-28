GARNAME = libpcap
GARVERSION = 1.0.0
CATEGORIES = lib

DESCRIPTION = Libraries for network diagnostics
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

# Shared libraries patch
#PATCHFILES  = Makefile.in.diff
#PATCHFILES += scanner.l.diff

# No test target for libpcap
TEST_SCRIPTS =

BUILD64 = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus sparcv8plus+vis 
EXTRA_BUILD_ISAS_i386  = pentium pentium_pro+mmx

TEST_TARGET = check

EXTRA_CFLAGS = -I.

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ipv6

INSTALL_ARGS = install-shared

include gar/category.mk
