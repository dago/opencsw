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

BUILD64_LIBS_ONLY = 1

# Disabling sparcv8plus with GCC
# /var/tmp//ccPKyHnL.s: Assembler messages:
# /var/tmp//ccPKyHnL.s:11: Error: Architecture mismatch on "return".
# /var/tmp//ccPKyHnL.s:11:  (Requires v9|v9a|v9b; requested architecture is
# v8.)
# EXTRA_BUILD_ISAS_sparc = sparcv8plus
# EXTRA_BUILD_ISAS_sparc += sparcv8plus+vis 
#
# If you believe that a sparcv8plus build is necessary, feel free to develop
# this recipe so that these ISAs successfully build.
EXTRA_BUILD_ISAS_i386  = pentium_pro

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
ABI_pentium_pro = 32
ABI_amd64 = 64
MPN_i386 = "x86 generic"
MPN_pentium_pro = "x86/pentium_pro x86 generic"
MPN_amd64 = "x86_64 generic"

CONFIGURE_ARGS  = ABI=$(ABI_$(ISA))
CONFIGURE_ARGS += MPN_PATH=$(MPN_$(ISA))
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-cxx

EXTRA_PAX_ARGS_32  = -s ",^\.$(includedir)/gmp.h$$,.$(includedir)/gmp-32.h,p"
EXTRA_PAX_ARGS_32 += -s ",^\.$(includedir)/gmpxx.h$$,.$(includedir)/gmpxx-32.h,p"
EXTRA_PAX_ARGS_64  = -s ",^\.$(includedir)/gmp.h$$,.$(includedir)/gmp-64.h,p"
EXTRA_PAX_ARGS_64 += -s ",^\.$(includedir)/gmpxx.h$$,.$(includedir)/gmpxx-64.h,p"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

PACKAGES += CSWlibgmp10
CATALOGNAME_CSWlibgmp10 = libgmp10
SPKG_DESC_CSWlibgmp10 = GNU Multiple Precision Arithmetic Library, libgmp.so.10
PKGFILES_CSWlibgmp10 = $(call baseisadirs,$(libdir),libgmp\.so\.10(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibgmp10 += CSWlibgcc-s1

PACKAGES += CSWlibgmpxx4
CATALOGNAME_CSWlibgmpxx4 = libgmpxx4
PKGFILES_CSWlibgmpxx4 += $(call baseisadirs,$(libdir),libgmpxx\.so\.4\.2\.2)
PKGFILES_CSWlibgmpxx4 += $(call baseisadirs,$(libdir),libgmpxx\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibgmpxx4 += Development Files for libgmp, libgmpxx.so.4
RUNTIME_DEP_PKGS_CSWlibgmpxx4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgmpxx4 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibgmpxx4 += CSWlibstdc++6

PACKAGES += CSWlibgmp-dev
CATALOGNAME_CSWlibgmp-dev = libgmp_dev
SPKG_DESC_CSWlibgmp-dev = Development Files for libgmp
# Catchall PKGFILES
RUNTIME_DEP_PKGS_CSWlibgmp-dev = CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibgmp-dev += CSWlibgmpxx4

# It's only an .info file.
CHECKPKG_OVERRIDES_CSWlibgmp-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/gmp.info-1

# To work around a problem with __attribute__((const)) being in the
# C compiler, but not the C++ compiler in Solaris Studio.
# http://gmplib.org/list-archives/gmp-discuss/2009-January/003518.html
# EXTRA_CXXFLAGS = -D__GMP_NO_ATTRIBUTE_CONST_PURE

# GMP needs to be able to propagate exceptions to PPL
EXTRA_CXXFLAGS = -fexceptions

# We cannot compile libgmp with Solaris Studio, because we need to build the
# C++ bindings, which will be used by gcc later on.
GARCOMPILER = GNU

# It's necessary to propagate exceptions from GMP to PPL
EXTRA_CPPFLAGS = -fexceptions

# Building for i386 or sparcv8 with optimization causes trouble.
# http://wiki.opencsw.org/porting-faq#toc6
# See also below.
# Here's an idea how to build it, but unfortunately, building for sparcv8plus
# fails too.
ISA_DEFAULT_i386 = pentium_pro
# ISA_DEFAULT_sparc = sparcv8plus

include gar/category.mk

## Undefined symbol __sync_fetch_and_add_4
## http://www.mail-archive.com/maintainers@lists.opencsw.org/msg06095.html
## http://opencsw.wikidot.com/porting-faq#toc6
# ifeq ($(ISA),sparcv8)
# OPT_FLAGS_GCC =
# endif
# ifeq ($(ISA),i386)
# OPT_FLAGS_GCC =
# endif

post-merge:
	ginstall $(FILEDIR)/gmp.h $(PKGROOT)$(includedir)/gmp.h
	ginstall $(FILEDIR)/gmpxx.h $(PKGROOT)$(includedir)/gmpxx.h
	@$(MAKECOOKIE)
