NAME = gnutls
VERSION = 2.10.4
CATEGORIES = lib

DESCRIPTION = GNU Transport Layer Security libraries and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS working group.
endef

MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += http://alpha.gnu.org/gnu/gnutls/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES += 0001-Do-not-strip-norunpath.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.gnu.org/software/gnutls/

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
CATALOGNAME_CSWlibgnutls-dev = libgnutls_dev
SPKG_DESC_CSWlibgnutls-dev = Development Files for GNU TLS
PKGFILES_CSWlibgnutls-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgnutls-dev += CSWlibgnutls26

PACKAGES += CSWgnutlsdevel
CATALOGNAME_CSWgnutlsdevel = gnutls_devel
SPKG_DESC_CSWgnutlsdevel = Legacy development package for GNU TLS now provided by CSWlibgnutls-dev
PKGFILES_CSWgnutlsdevel = NOFILES
ARCHALL_CSWgnutlsdevel = 1
RUNTIME_DEP_PKGS_CSWgnutlsdevel = CSWlibgnutls-dev
# This is empty, shut up!
CHECKPKG_OVERRIDES_CSWgnutlsdevel += archall-devel-package

BUILD_DEP_PKGS += CSWreadline
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibgnutls26)
BUILD_DEP_PKGS += CSWlibtasn1devel 

# We don't need it and if defined the test breaks
LD_OPTIONS =

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# We put all libs in one package as they are .so.26 and are all bumped together
CHECKPKG_OVERRIDES_CSWlibgnutls26 += shared-lib-pkgname-mismatch

include gar/category.mk
