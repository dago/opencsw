NAME = libserf
VERSION = 1.0.1
DISTNAME = serf-$(VERSION)
CATEGORIES = lib
GARTYPE = v2

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
LICENSE = LICENSE
VENDOR_URL = http://code.google.com/p/serf/

PACKAGES += CSWlibserf1-0
CATALOGNAME_CSWlibserf1-0 = libserf1_0
SPKG_DESC_CSWlibserf1-0 += HTTP client library built on APR, multiplexes connections, libserf-1.so.0
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWapr
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWapr-util
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWbdb48
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibserf1-0 += CSWzlib

PACKAGES += CSWlibserf-dev
CATALOGNAME_CSWlibserf-dev = libserf_dev
SPKG_DESC_CSWlibserf-dev = Development files for libserf.so.1
PKGFILES_CSWlibserf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibserf-dev = CSWlibserf1-0
OBSOLETED_BY_CSWlibserf-dev += CSWlibserf-devel

EXTRA_LIB = $(prefix)/bdb48/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr=$(bindir)/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-1-config

include gar/category.mk
