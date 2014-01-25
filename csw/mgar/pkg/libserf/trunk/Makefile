NAME = libserf
VERSION = 1.3.3
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

MASTER_SITES = http://serf.googlecode.com/f  = $(DISTNAME).tar.bz2
PATCHFILES  += 0001-mark-solaris-as-posix-for-scons.patch
LICENSE      = LICENSE
VENDOR_URL  ICENSE
VENDOR_URL = http://code.gooCONFIGURE_SCRIPTS =
BUILD_SCRIPTS = serf
INSTALL_SCRIPTS = serf
TEST_SCRIPTS =oogle.com/p/serf/

# openssl-1.0 only available for sol-10
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGE3
CATALOGNAME_CSWlibserf1-3 = libserf1_3
SPKG_DESC_CSWlibserf1-3ESC_CSWlibserf1-0 += HTTP client library built on APR, multiplexes connections, libserf-1.so.0
RUNTIME_DEP_3 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibserf1-3 += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibserf1-3 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibserf1-3 += CSWlibz1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += bad-rpath-entry|/opt/csw/bdb48/lib/|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libserf-1.so.1.3.0
rBUILD_DEP_PKGS += CSWscons
BUILD_DEP_PKGS += CSWlibapr-dev
BUILD_DEP_PKGS += CSWlibaprutil-devrff1-0 += CSWlibz1

PACKAGES += CSWlibserf-dev
CATALOGNAME_CSWlibserf-dev = libserf_dev
SPKG_DESC_CSWlibserf-dev = Development files for libserf.so.1
PKGFILES_CSWlibserf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibserf-d3v = CSWlibserf1-0

EXTRA_LIB = $(prSCONS_FLAGS += APR=$(bindir)/apr-1-config
SCONS_FLAGS += APU=$(bindir)/apu-1-config

CHECKPKG_OVERRIDES_CSWlibserf1-3 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libserf-1.so.1.3.0|soname=libserf-1.so.1|pkgname=CSWlibserf1-3|expected=CSWlibserf1-1

include gar/category.mk

build-serf:
	(cd $(WORKSRC); \
		scons \
		$(SCONS_FLAGS) LINKFLAGS="$(LD_OPTIONS)" CFLAGS="$(CFLAGS)" PREFIX=$(prefix) )
	@$(MAKECOOKIE)

install-serf:
	(cd $(WORKSRC); \
		scons  \
		$(SCONS_FLAGS) \
		-Q PREFIX=$(DESTDIR)$(BUILD_PREFIX) \
		install)
	@$(MAKECOOKIE)

