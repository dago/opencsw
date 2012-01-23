NAME = liboil
VERSION = 0.3.17
CATEGORIES = lib

DESCRIPTION = A library of simple functions that are optimized for various CPUs
define BLURB
  Liboil is a library of simple functions that are optimized for various CPUs.
  These functions are generally loops implementing simple algorithms, such as
  converting an array of N integers to floating-point numbers or multiplying
  and summing an array of N numbers. Such functions are candidates for significant
  optimization using various techniques, especially by using extended instructions
  provided by modern CPUs (Altivec, MMX, SSE, etc.).
endef

MASTER_SITES = http://liboil.freedesktop.org/download/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES = 0001-Use-inttypes.h.patch
PATCHFILES += 0002-Enable-getisax-only-for-Solaris-10.patch

VENDOR_URL = http://liboil.freedesktop.org/

PACKAGES += CSWliboil0-3-0
SPKG_DESC_CSWliboil0-3-0 = A library of simple functions that are optimized for various CPUs, liboil-0.3.so.0
PKGFILES_CSWliboil0-3-0 += $(call pkgfiles_lib,liboil-0.3.so.0)
OBSOLETED_BY_CSWliboil0-3-0 = CSWliboil

PACKAGES += CSWliboil-dev
SPKG_DESC_CSWliboil-dev = Development files for liboil-0.3.so.0
RUNTIME_DEP_PKGS_CSWliboil-dev += CSWliboil0-3-0
# PKGFILES is catchall
OBSOLETED_BY_CSWliboil-dev += CSWliboildevel
CATALOGNAME_CSWliboildevel = liboil_devel_stub

BUILD64_LIBS_ONLY = 1

include gar/category.mk
