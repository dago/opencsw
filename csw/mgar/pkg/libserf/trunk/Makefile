NAME = libserf
VERSION = 0.7.2
DISTNAME = serf-$(VERSION)
CATEGORIES = lib

DESCRIPTION = HTTP client library built on APR, multiplexes connections
define BLURB
    The serf library is a C-based HTTP client library built upon the
    Apache Portable Runtime (APR) library. It multiplexes connections,
    running the read/write communication asynchronously. Memory copies
    and transformations are kept to a minimum to provide high performance
    operation.
endef

MASTER_SITES = http://serf.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.bz2

DEP_PKGS = CSWapr CSWapr-util CSWbdb48 CSWexpat CSWiconv CSWoldaprt CSWosslrt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(DISTNAME)-(\d+(?:\.\d+)*).tar.bz2

OBSOLETED_BY_CSWlibserf0-0 = CSWlibserf
OBSOLETED_BY_CSWlibserf-dev = CSWlibserf

PACKAGES += CSWlibserf0-0
CATALOGNAME_CSWlibserf0-0 = libserf0_0
SPKG_DESC_CSWlibserf0-0 += HTTP client library built on APR, multiplexes connections, provides libserf-0.so.0
PKGFILES_CSWlibserf0-0 += $(call baseisadirs,$(libdir),libserf-0\.so\.0(\.\d+)*)

PACKAGES += CSWlibserf-dev
CATALOGNAME_CSWlibserf-dev = libserf_dev
SPKG_DESC_CSWlibserf-dev = Development files for libserf
PKGFILES_CSWlibserf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibserf-dev = CSWlibserf0-0

LICENSE = LICENSE

VENDOR_URL = http://code.google.com/p/serf/

# Make sure the current directory comes before everything else
INCLUDE_FLAGS = -I. -I$(includedir)

EXTRA_LIB = $(prefix)/bdb48/lib

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-1-config

TEST_TARGET = check

include gar/category.mk

post-configure-modulated: APR_LIBTOOL = $(shell $(bindir)/apr-1-config --apr-libtool)
post-configure-modulated:
	gcp $(APR_LIBTOOL) $(WORKSRC)
	perl -i -pne 's|$(APR_LIBTOOL)|$(abspath $(WORKSRC)/libtool)|' $(WORKSRC)/Makefile
	$(GARBIN)/fixlibtool $(WORKSRC)
	@$(MAKECOOKIE)
