GARNAME = libpcap
GARVERSION = 0.8.3
CATEGORIES = lib

DESCRIPTION = Libraries for network diagnostics
define BLURB
  A system-independent interface for user-level network packet capture.
endef

MASTER_SITES = http://www.tcpdump.org/release/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibpcap,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Shared libraries patch
PATCHFILES = solib.diff

# No test target for libpcap
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = prefix exec_prefix includedir libdir mandir 

include gar/category.mk

post-install:
	rm -f $(DESTDIR)$(libdir)/$(GARNAME).a
