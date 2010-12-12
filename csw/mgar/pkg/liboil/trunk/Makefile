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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWliboil CSWliboildevel

CATALOGNAME_CSWliboil = liboil
CATALOGNAME_CSWliboildevel = liboil_devel

SPKG_DESC_CSWliboil = $(DESCRIPTION)
SPKG_DESC_CSWliboildevel = Development files for liboil

RUNTIME_DEP_PKGS_CSWliboildevel = CSWliboil

SPKG_SOURCEURL = http://liboil.freedesktop.org/

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PKGFILES_CSWliboildevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWliboildevel += $(sharedstatedir)/gtk-doc/.*

include gar/category.mk
