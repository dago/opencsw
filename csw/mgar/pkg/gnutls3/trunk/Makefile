NAME = gnutls
VERSION = 3.1.10
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

# Sun Studio 12 bails out on .deinit_func
GARCOMPILER = GCC4

VENDOR_URL = http://gnutls.org/software/gnutls/

BUILD_DEP_PKGS += CSWlibnettle-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibtasn1-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibp11kit-dev

PACKAGES += CSWgnutls
CATALOGNAME_gnutls = gnutls
SPKG_DESC_CSWgnutls = GNU Transport Layer Security Utility Programs
RUNTIME_DEP_PKGS_CSWgnutls += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWgnutls += CSWgpgerr
RUNTIME_DEP_PKGS_CSWgnutls += CSWreadline
RUNTIME_DEP_PKGS_CSWgnutls += CSWzlib
RUNTIME_DEP_PKGS_CSWgnutls += CSWlibtasn1-3
RUNTIME_DEP_PKGS_CSWgnutls += CSWgcrypt
RUNTIME_DEP_PKGS_CSWgnutls += CSWggettextrt
# This is a dependency for legacy packages expecting to find libgnutls*.so.13 in CSWgnutls.
# CSWlibgnutls13 is built from a branch
RUNTIME_DEP_PKGS_CSWgnutls += CSWlibgnutls13
CHECKPKG_OVERRIDES_CSWgnutls += unidentified-dependency|CSWlibgnutls13
CHECKPKG_OVERRIDES_CSWgnutls += surplus-dependency|CSWlibgnutls13

PACKAGES += CSWlibgnutls26
CATALOGNAME_CSWlibgnutls = libgnutls26
SPKG_DESC_CSWlibgnutls26 = GNU Transport Layer Security libraries and tools providing libgnutls*.so.26
PKGFILES_CSWlibgnutls26 = $(call baseisadirs,$(libdir),libgnutls.*\.so\.26(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibtasn1-3
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWzlib

PACKAGES += CSWlibgnutls-dev
SPKG_DESC_CSWlibgnutls-dev = Development Files for GNU TLS
PKGFILES_CSWlibgnutls-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgnutls-dev += CSWlibgnutls26
OBSOLETED_BY_CSWlibgnutls-dev = CSWgnutlsdevel
CATALOGNAME_CSWgnutlsdevel = gnPATCHFILES += 0001-no-gets-warning.patchgnutls_devel_stub

# We don't need it and if defined# the test breaks
LD_OPTIONS =

# EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-lzo

# We put all libs in one package as they are .so.26 and are all bumped together
CHECKPKG_OVERRIDES_CSWlibgnutls26 += shared-lib-pkgname-mismatch

include pre-configure:
	cd $(WORKSRC) && autoconf
	@${MAKECOOKIE}

