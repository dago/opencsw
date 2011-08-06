# $Id$

NAME = gmp
VERSION = 5.0.2
CATEGORIES = lib

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

#GARCOMPILER = GCC4
BUILD64 = 1

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

# For 64-bit compilation, we need /opt/csw/include/sparcv9/gmp.h
EXTRA_MERGE_DIRS_isa-extra = $(includedir)

PACKAGES += CSWlibgmp10
CATALOGNAME_CSWlibgmp10 = libgmp10
SPKG_DESC_CSWlibgmp10 = GNU Multiple Precision Arithmetic Library, libgmp.so.10
PKGFILES_CSWlibgmp10 = $(call baseisadirs,$(libdir),libgmp\.so\.10(\.\d+)*)

PACKAGES += CSWlibgmp-dev
CATALOGNAME_CSWlibgmp-dev = libgmp_dev
SPKG_DESC_CSWlibgmp-dev = Development Files for libgmp
# Catchall PKGFILES
RUNTIME_DEP_PKGS_CSWlibgmp-dev = CSWlibgmp10

#RUNTIME_DEP_PKGS = CSWgcc4corert

# It's only an .info file.
CHECKPKG_OVERRIDES_CSWlibgmp-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/gmp.info-1

include gar/category.mk

#ifeq ($(ISA), sparcv8plus)
#	ARCHFLAGS_$(GARCOMPILER)_$(ISA) = -mcpu=v9 -mv8plus
#endif
#ifeq ($(ISA), sparcv8plus+vis)
#	ARCHFLAGS_$(GARCOMPILER)_$(ISA) = -mcpu=ultrasparc -mvis
#endif

