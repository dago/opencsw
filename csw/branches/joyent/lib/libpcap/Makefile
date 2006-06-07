GARNAME = libpcap
GARVERSION = 0.8.3
CATEGORIES = lib

SPKG_PKGNAME = CSWlibpcap
SPKG_BITNAME = libpcap

DESCRIPTION = Libraries for network diagnostics
define BLURB
  A system-independent interface for user-level network packet capture.
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Shared libraries patch
PATCHFILES = solib.diff

# No test target for libpcap
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = prefix exec_prefix includedir libdir mandir 

include ../category.mk

post-install:
	rm -f $(DESTDIR)$(libdir)/$(GARNAME).a
