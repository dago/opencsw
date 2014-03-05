NAME = gnutls
VERSION = 2.12.23
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Transport Layer Security libraries and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS working group.
endef

MASTER_SITES = $(GNU_MIRROR)ftp://ftp.gnutls.org/gcrypt/gnutls/v2.12/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
#PATCHFILES += 0001-Do-not-strip-norunpath.patch
PATCHFILES += 0002-Use-AF_UNIX-instead-of-AF_LOCAL-on-Solaris.patch
# certtool uses fprintf to print the keyid but when 
# the key id is null it segfaults under Solaris
# (where it prints (null) under Linux)
# This patchs fixes this (and is taken from gnutls3)
PATCHFILES += 0003-correctly-handle-the-null-key-caset-strip# Some certificates used in the test suite are expired,
# so the chainverify test fails.
# The is supposed to be workarounded in the gnutls test
# suite by redefining the time function, but this doesn't work
# here because libgnutls has been compiled with direct binding 
# hence it only links the time function with the original library.
# We workaround the problem by changing the test so it expects
# the certificates to be expired (another solution is to use LD_PRELOAD).
PATCHFILES += 0004-workaround-certificate-expiration-issue-in-the-test-.patch

# Security fixes
PATCHFILES += 0005-CVE-2013-2116.patch
PATCHFILES += 0006-CVE-2014-1959.patch
PATCHFILES += 0007-CVE-2014-0092.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.gnu.org/software/gnutls/cy|CSWlibgnutls13

PACKAGES += CSWlibgnutls26
CATALOGNAME_CSWlibgnutls = libgnutls26
SPKG_DESC_CSWlibgnutls26 = GNU Transport Layer Security libraries and tools providing libgnutls*.so.26
PKGFILES_CScall baseisadirs,$(libdir),[^/-]*\.so\.\d+(\.\d+)*)
PKGFILES_CSWlibgnutls26 += $(call baseisadirs,$(libdir),[^/-]*-extra\.so\.\d+(\.\d+)**\.so\.26(\.\d+)*)
RUNTIME_DEP_PKGS_CSWllibz1
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibnettle4
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibhogweed2
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibtasn1-6
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibp11kit0
RUNTIME_DEP_PKGS_CSWlibgnutls26 += CSWlibgmp10
all-devel-package

BUILD_DEP_PKGS += CSWreadline
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibgnutls26)
BUILD_DEP_PK-dev
BUILD_DEP_PKGS += CSWlibnettle-dev
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibp11kit-dev
BUILD_DEP_PKGS += CSWlibgmp-dev

GARCOMPILER = GNU

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-guile

# If defined with the default value, the test breaks
# so we only keep the required items
LD_OPTIONS = $(LINKER_MAPS) $(LINKER_DIRECT) $(LINKER_IGNOREAR# Workaround to make sure gnutls26 extra libraries
# are linked against gnutls26 and not gnutls28
LD_OPTIONS += -L$(abspath $(WORKSRC))/lib/.libsRGS = $(DIRPATHS)

# We put all libs in one package as they are .so.26 and are all bumped together
CHECKPKG_OVERRIDES_CSWlibgnutls26 += shared-lib-pkgname-mismatch

include
