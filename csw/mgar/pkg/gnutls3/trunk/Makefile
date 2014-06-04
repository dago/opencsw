NAME = gnutls
VERSION = 3.1.25
CATEGORIES = lib

DESCRIPTION = GNU Transport Layer Security libraries and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS workiSUBV = $(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')
MASTER_SITES = ftp://ftp.gnutls.org/gcrypt/gnutls/v$(SUBV)/
DISTFILES += $(DISTNAME).tar.xz
# PATCHFILES += 0001-Do-not-strip-norunpath.patch
PATCHFILES += 0002-Use-AF_UNIX-instead-of-AF_LOCAL-on-Solaris.patch

# Some test scripts now uses some bashisms, so we make
# sure that bash is used instead of sh
PATCHFILES += 0003-force-use-of-bash-shell-in-non-portable-test-scripts.patch

# Sun Studio 12 bails out on .deinit_func
GARCOMPILER = GCC4

VENDOR_URL = http://gnutls.org/software/gnutls/

BUILD_DEP_PKGS += CSWlibnettle-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibtasn1-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += BUILD_DEP_PKGS += CSWlibiconvS += CSWlibp11kit-dev

PACKAGES += CSWgnutls
CATALOGNAME_gnutls = gnutls
SPKG_DESC_CSWgnutls = GNU Transport Layer Security Utility Programs
RUNTIME_DEP_PKGS_CSWgnutls8
RUNTIME_DEP_PKGS_CSWgnutls += CSWlibintl8 y|CSWlibgnutls13

PACKAGES8
CATALOGNAME_CSWlibgnutls = libgnutls28
SPKG_DESC_CSWlibgnutls28 = GNU Transport Layer Security libraries and tools providing libgnutls*.so.28
PKGFILES_CSWlibgnutls28  = $(PKGFILES_RT)
PKGFILES_CSWlibgnutls28 += $(docdir)/libgnutls28/.*
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibhogweed2
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibp11kit0
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgnutls28 += CSWlibnettle4

# We put all libs in one package as they are .so.28 and are all bumped together
CHECKPKG_OVERRIDES_CSWlibgnutls28 += shared-lib-pkgname-mismatchutls26 += CSWzlib

PACKAGES += CSWlibgnutls-dev
SPKG_DESC_CSWlibgnutls-dev = Development Files for GNU TLS
PKGFILES_CSWlibgnutls-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgnutls-dev8
n# The compilation complains with 
# "gets is a security hole - use fgets instead"
# even if it is not used, so we remove this warningnPATCHFILES += 0001-no-gets-warning.patchgnut
LD_OPTIONS =

# EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARCONFIGURE_ARGS += --disable-guileRCONFIGURE_ARGS += --disable-libdaneRCONFIGURE_ARGS += --with-default-trust-store-file=$(sysconfdir)/ssl/certs/ca-certificates.crt
CONFIGURE_ARGS += --with-unbound-root-key-file=$(sysconfdir)/unbound/root.keyR# libopts doesn't contains yet 64 bits libraries so we have to use
# the included one meanwhile: see https://www.opencsw.org/mantis/view.php?id=5156
CONFIGURE_ARGS += --enable-local-liboptsR# Workaround a host detection bug in configure for amd64
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(ISA))
CONFIGURE_ARGS_amd64 += --build=x86_64-pc-solaris2$(shell uname -r |sed -e 's/[^.]*//')

# If defined with the default value, the test breaks
# # so we only keep the required items
LD_OPTIONS = $(LINKER_MAPS) $(LINKER_DIRECT) $(LINKER_IGNORE)

include gar/category.mk

