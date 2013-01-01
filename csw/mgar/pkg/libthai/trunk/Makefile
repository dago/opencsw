NAME = libthai
VERSION = 0.1.18
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Thai language support routines
define BLURB
  LibThai is a set of Thai language support routines aimed to ease
  developers tasks to incorporate Thai language support in their applications.
  It includes important Thai-specific functions e.g. word breaking, input
  and output methods as well as basic character and string supports.
  LibThai is an Open Source and collaborative effort initiated by
  Thai Linux Working Group and opened for all contributors.
endef

MASTER_SITES = http://linux.thai.net/pub/thailinux/software/libthai/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Remove-unknown-compiler-macro.patch
PATCHFILES += 0002-Use-stdint.h-only-when-available-and-use-limits.h-fo.patch

VENDOR_URL = http://linux.thai.net/projects/libthai/

BUILD_DEP_PKGS += CSWlibdatrie-dev
BUILD_DEP_PKGS += CSWlibdatrie-utils

PACKAGES += CSWlibthai0
SPKG_DESC_CSWlibthai0 = Thai language support routines, libthai.so.0
PKGFILES_CSWlibthai0 += $(call pkgfiles_lib,libthai.so.0)
PKGFILES_CSWlibthai0 += $(sharedstatedir)/libthai/thbrk.tri
RUNTIME_DEP_PKGS_CSWlibthai0 = CSWlibdatrie1
OBSOLETED_BY_CSWlibthai0 += CSWlibthai

PACKAGES += CSWlibthai-dev
SPKG_DESC_CSWlibthai-dev = Thai language support routines development files
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibthai-dev = CSWlibthai0
OBSOLETED_BY_CSWlibthai-dev += CSWlibthaidevel
CATALOGNAME_CSWlibthaidevel = libthai_devel_stub

BUILD64_LIBS_ONLY = 1

include