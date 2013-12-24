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
RUNTIME_DEP_2 += CSWbdb48
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWlibserf1-2 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibserf1-2KGS_CSWlibserf1-0 += CSWlibz1

PACKAGES += CSWlibserf-dev
CATALOGNAME_CSWlibserf-dev = libserf_dev
SPKG_DESC_CSWlibserf-dev = Development files for libserf.so.1
PKGFILES_CSWlibserf-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibserf-d3v = CSWlibserf1-0

EXTRA_LIB = $(prSCONS_FLAGS += APR=$(bindir)/apr-1-config
SCONS_FLAGS += APU=$(bindir)/apu-1-config

CHECKPKG_OVERRIDES_CSWlibserf1-3 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libserf-1.so.1.3.0|soname=libserf-1.so.1|pkgname=CSWlibserf1-3|expected=CSWlibserf1-1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libapr-1.so.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libaprutil-1.so.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libcrypto.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libdb-4.8.so
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libexpat.so.1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|liblber-2.4.so.2
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libldap-2.4.so.2
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libsendfile.so.1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libssl.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libuuid.so.1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += no-direct-binding|/opt/csw/lib/libserf-1.so.1.3.0|is|not|directly|bound|to|soname|libz.so.1
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|liblber-2.4.so.2|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libapr-1.so.0|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libdb-4.8.so|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libldap-2.4.so.2|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libssl.so.1.0.0|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libaprutil-1.so.0|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libcrypto.so.1.0.0|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0
CHECKPKG_OVERRIDES_CSWlibserf1-3 += soname-not-found|libexpat.so.1|is|needed|by|opt/csw/lib/libserf-1.so.1.3.0

include gar/category.mk

build-serf:
	(cd $(WORKSRC); \
		scons \
		$(SCONS_FLAGS) PREFIX=$(prefix) )
	@$(MAKECOOKIE)

install-serf:
	(cd $(WORKSRC); \
		scons  \
		$(SCONS_FLAGS) \
		-Q PREFIX=$(DESTDIR)$(BUILD_PREFIX) \
		install)
	@$(MAKECOOKIE)

