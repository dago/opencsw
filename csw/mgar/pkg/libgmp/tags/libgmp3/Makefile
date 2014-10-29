NAME = gmp
VERSION = 4.3.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Multiple Precision Arithmetic Library
define BLURB
  GMP is a free library for arbitrary precision arithmetic, operating on signed
  integers, rational numbers, and floating point numbers. There is no limit to
  the precision, except for the ones implied by available memory. It has a rich
  set of functions, and the functions have a regular interface. It is designed
  to be as fast as possible, both for small operands and for huge operands. The
  speed is achieved by using fullwords as the basic arithmetic type, by using
  fast algorithms with carefully optimized assembly code for the most common
  inner loops for a lot of CPUs, and by a general emphasis on speed (instead of
  simplicity or elegance). It is believed to be faster than any other similar
  library. The advantage increases with the operand sizes for certain
  operations, since GMP in many cases has asymptotically faster algorithms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_SOURCEURL = http://gmplib.org/

GARCOMPILER = GCC4
BUILD64_LIBS_ONLY = 1

EXTRA_BUILD_ISAS_sparc = sparcv8plus sparcv8plus+vis 
EXTRA_BUILD_ISAS_i386  = pentium

BUILD_DEP_PKGS = CSWgm4

# Solaris m4 seems to fail on Solaris 10 amd64 only, use gm4 for all builds
M4 = /opt/csw/bin/gm4
EXTRA_CONFIGURE_EXPORTS = M4

MPN_sparcv8 = "sparc32/v8 sparc32 generic"
MPN_sparcv8plus = "sparc32/v9 sparc32 generic"
MPN_sparcv8plus+vis = "sparc32/v9 sparc32 generic"
MPN_sparcv9 = "sparc64 generic"

ABI_sparcv8 = 32
ABI_sparcv9 = 64
ABI_i386 = 32
ABI_pentium = 32
ABI_amd64 = 64
MPN_i386 = "x86 generic"
MPN_pentium = "x86/pentium x86 generic"
MPN_amd64 = "x86_64 generic"

CONFIGURE_ARGS = ABI=$(ABI_$(ISA)) MPN_PATH=$(MPN_$(ISA)) $(DIRPATHS)

PACKAGES += CSWlibgmp
CATALOGNAME_CSWlibgmp = libgmp
SPKG_DESC_CSWlibgmp = Legacy GNU Multiple Precision Arithmetic Library, libgmp.so.3
PKGFILES_CSWlibgmp = $(call baseisadirs,$(libdir),libgmp\.so\.3(\.\d+)*)
# This is a legacy package, tolerate the wrong name until this is obsoleted
CHECKPKG_OVERRIDES_CSWlibgmp += shared-lib-pkgname-mismatch

PACKAGES += CSWlibgmp-dev
CATALOGNAME_CSWlibgmp-dev = libgmp_dev
SPKG_DESC_CSWlibgmp-dev = GNU Multiple Precision Arithmetic Library, development files
RUNTIME_DEP_PKGS_CSWlibgmp-dev += CSWlibgmp
# /usr/local mentioned content in .info file.
CHECKPKG_OVERRIDES_CSWlibgmp-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/gmp.info-1

RUNTIME_DEP_PKGS = CSWgcc4corert

include gar/category.mk

ARCHFLAGS_GCC4_sparcv8plus = -mcpu=v9 -mv8plus
ARCHFLAGS_GCC4_sparcv8plus+vis = -mcpu=ultrasparc -mvis
