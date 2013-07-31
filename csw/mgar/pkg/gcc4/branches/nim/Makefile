# $Id$

NAME      = gcc
VERSION   = 4.8.0
GARTYPE = bts
BASE_VERSION = $(shell echo $(VERSION) | gsed -e 's/^\([0-9]\+\.[0-9]\+\)\(.*\)/\1/')
PKG_VERSION_TOKEN = gcc4
PKG_BASENAME = NIMOSS$(PKG_VERSION_TOKEN)
# PKG_BASENAME = NIMOSSgcc-$(subst .,-,$(BASE_VERION))

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++,
	Objective-C, Fortran, Java, and Ada, as well as libraries
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(DISTNAME).tar.bz2
# MASTER_SITES = $(GNU_MIRROR)/$(NAME)-$(VERSION)/
# MASTER_SITES += http://ftp.heanet.ie/mirrors/gnu/gcc/$(NAME)-$(VERSION)/
MASTER_SITES += ftp://ftp.gnu.org/gnu/gcc/gcc-$(VERSION)/

LIBOBJC = 4

# We're not building GCC-4.7 on Solaris 9, because GCC-4.7 requires the
# sparcv8+ architecture.
# PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# there is  a problem with direct linking on amd64 libs
LINKER_DIRECT =

# GIT init takes a long time.
NOGITPATCH ?= 1

## Source URLs
VENDOR_URL = http://gcc.gnu.org

## Copyright File
LICENSE = COPYING3

BUILD_DEP_PKGS += NIMOSSbinutils
BUILD_DEP_PKGS += NIMOSScloog-dev
BUILD_DEP_PKGS += NIMOSSgnulinks
BUILD_DEP_PKGS += NIMOSSlibgmp-dev
BUILD_DEP_PKGS += NIMOSSlibmpc-dev
BUILD_DEP_PKGS += NIMOSSlibmpfr-dev
BUILD_DEP_PKGS += NIMOSSlibppl-dev
BUILD_DEP_PKGS += NIMOSSlibz-dev

# Could be used to break out of the /opt/csw/$(PKG_VERSION_TOKEN) prefix
PROGRAM_SUFFIX = -$(BASE_VERSION)

## build options
# http://gcc.gnu.org/install/configure.html

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-cloog-backend=isl
CONFIGURE_ARGS += --enable-java-awt=xlib
CONFIGURE_ARGS += --enable-languages=ada,c,c++,fortran,go,java,objc
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix
CONFIGURE_ARGS += --program-suffix=$(PROGRAM_SUFFIX)
CONFIGURE_ARGS += --with-cloog=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-gmp=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-included-gettext
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-libiconv-prefix=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-mpfr=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-ppl=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-system-zlib=$(BUILD_PREFIX)

# Using ccs/bin/bas on x86 results in this problem:
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=35531
CONFIGURE_ARGS_sparc += --with-as=/usr/ccs/bin/as
CONFIGURE_ARGS_sparc += --without-gnu-as
CONFIGURE_ARGS_i386 += --with-gnu-as
CONFIGURE_ARGS_i386 += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# GCC can't be built in the same directory with the sources.
# It also can't be built in a subdirectory of the sources.
OBJDIR          = $(abspath $(WORKDIR)/objdir)

# bash must be used, otherwise:
# http://fixunix.com/solaris/490396-gcc-build-fails-cannot-compute-suffix-object-files.html
CONFIG_SHELL = /opt/csw/bin/bash
EXTRA_EXPORTS += CONFIG_SHELL

# Bootstrapping with Sun Studio has issues
# http://gcc.gnu.org/ml/gcc-help/2011-08/msg00191.html
GARCOMPILER = GNU

# There's a lot of failing checks. Probably a lot of porting work.
SKIPTEST ?= 1

# Used multiple times in package definitions
JAVA_LIB_VERSION = 14

ALTERNATIVES_PRIO = 470

PACKAGES = $(PKG_BASENAME)core
SPKG_DESC_$(PKG_BASENAME)core = GNU C compiler
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibatomic1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibffi4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgo3
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibgomp1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibitm1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibssp0
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibz1

# checkpkg-undetectable dependencies
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSbinutils
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSScoreutils
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSggrep
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSgsed

ALTERNATIVES_$(PKG_BASENAME)core += $(PKG_VERSION_TOKEN)core
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/cpp gcc_core $(bindir)/cpp$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gcc gcc_core $(bindir)/gcc$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gcov gcc_core $(bindir)/gcov$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gccgo gcc_core $(bindir)/gccgo$(PROGRAM_SUFFIX)

# Because I can.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += file-with-bad-content
CHECKPKG_OVERRIDES_NIMOSSlibgcj$(JAVA_LIB_VERSION) += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/i386-pc-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.10/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += file-with-bad-content
# Due to complex regular expressions
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += file-collision|$(includedir)/c++/$(VERSION)/sun/awt/CausedFocusEvent.h|$(PKG_BASENAME)g++|$(PKG_BASENAME)java
CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += file-collision|$(includedir)/c++/$(VERSION)/sun/awt/CausedFocusEvent.h|$(PKG_BASENAME)g++|$(PKG_BASENAME)java
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += missing-dependency|NIMOSSpython
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|NIMOSSbinutils
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|NIMOSScoreutils
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|NIMOSSggrep
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|NIMOSSgsed

# Only man pages, so not a big problem. Alternatives could be used, but it
# requires rebuilding libffi.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi_call.3|$(PKG_BASENAME)core|NIMOSSlibffi-dev
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi.3|$(PKG_BASENAME)core|NIMOSSlibffi-dev
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi_prep_cif.3|$(PKG_BASENAME)core|NIMOSSlibffi-dev
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|/opt/csw/nimoss/share/info/libffi.info|$(PKG_BASENAME)core|NIMOSSlibffi-dev

# The .a files are necessary
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += discouraged-path-in-pkgmap

CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += discouraged-path-in-pkgmap

# From the 'hopeless errors' department:
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libffi.so|NIMOSSgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libgcc_s.so|NIMOSSgcc3core|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libgcj.so|NIMOSSgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libobjc.so|NIMOSSgcc3objcrt|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/lib-gnu-awt-xlib.so|NIMOSSgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libffi.so|NIMOSSgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libgcj.so|NIMOSSgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libobjc.so|NIMOSSgcc3objcrt|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-collision|$(libdir)/libobjc.so|NIMOSSgcc3objcrt|$(PKG_BASENAME)objc
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-collision|$(libdir)/sparcv9/libobjc.so|NIMOSSgcc3objcrt|$(PKG_BASENAME)objc
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/lib-gnu-awt-xlib.so|NIMOSSgcc3javart|$(PKG_BASENAME)core

# Some static libraries are required to build binaries with gcc, for example
# libgcc.a and libgcc_eh.a. Otherwise: ld: fatal: library -lgcc: not found
MERGE_EXCLUDE_LIBTOOL =
MERGE_EXCLUDE_STATICLIBS =
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/libiberty\.a

# Catch-all package

PACKAGES += NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
CATALOGNAME_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) = lib_gnu_awt_xlib$(JAVA_LIB_VERSION)
PKGFILES_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),lib-gnu-awt-xlib\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(DESCRIPTION), lib-gnu-awt-xlib.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibffi4
CATALOGNAME_NIMOSSlibffi4 = libffi4
PKGFILES_NIMOSSlibffi4 += $(call baseisadirs,$(libdir),libffi\.so\.4(\.\d+)*)
SPKG_DESC_NIMOSSlibffi4 += $(DESCRIPTION), libffi.so.4
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += NIMOSSlibffi4
RUNTIME_DEP_PKGS_NIMOSSlibffi4 += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibgcc-s1
CATALOGNAME_NIMOSSlibgcc-s1 = libgcc_s1
PKGFILES_NIMOSSlibgcc-s1 += $(call baseisadirs,$(libdir),libgcc_s\.so\.1(\.\d+)*)
SPKG_DESC_NIMOSSlibgcc-s1 += $(DESCRIPTION), libgcc_s.so.1
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibgcj-tools$(JAVA_LIB_VERSION)
CATALOGNAME_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) = libgcj_tools$(JAVA_LIB_VERSION)
PKGFILES_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj-tools\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj-tools.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += NIMOSSlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += NIMOSSlibgcc-s1
RUNTIME_DEP_PKGS_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += NIMOSSlibgcj$(JAVA_LIB_VERSION)

PACKAGES += NIMOSSlibgcj$(JAVA_LIB_VERSION)
CATALOGNAME_NIMOSSlibgcj$(JAVA_LIB_VERSION) = libgcj$(JAVA_LIB_VERSION)
PKGFILES_NIMOSSlibgcj$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_NIMOSSlibgcj$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_NIMOSSlibgcj$(JAVA_LIB_VERSION) += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibgfortran3
CATALOGNAME_NIMOSSlibgfortran3 = libgfortran3
PKGFILES_NIMOSSlibgfortran3 += $(call baseisadirs,$(libdir),libgfortran\.so\.3(\.\d+)*)
SPKG_DESC_NIMOSSlibgfortran3 += $(DESCRIPTION), libgfortran.so.3
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += NIMOSSlibgfortran3
RUNTIME_DEP_PKGS_NIMOSSlibgfortran3 += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibgij$(JAVA_LIB_VERSION)
CATALOGNAME_NIMOSSlibgij$(JAVA_LIB_VERSION) = libgij$(JAVA_LIB_VERSION)
PKGFILES_NIMOSSlibgij$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgij\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_NIMOSSlibgij$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgij.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_NIMOSSlibgij$(JAVA_LIB_VERSION) += NIMOSSlibgcj$(JAVA_LIB_VERSION)

PACKAGES += NIMOSSlibgomp1
CATALOGNAME_NIMOSSlibgomp1 = libgomp1
PKGFILES_NIMOSSlibgomp1 += $(call baseisadirs,$(libdir),libgomp\.so\.1(\.\d+)*)
SPKG_DESC_NIMOSSlibgomp1 += $(DESCRIPTION), libgomp.so.1
RUNTIME_DEP_PKGS_NIMOSSlibgomp1 += NIMOSSlibgcc-s1


PACKAGES += NIMOSSlibobjc$(LIBOBJC)
CATALOGNAME_NIMOSSlibobjc$(LIBOBJC) = libobjc$(LIBOBJC)
PKGFILES_NIMOSSlibobjc$(LIBOBJC) += $(call baseisadirs,$(libdir),libobjc\.so\.$(LIBOBJC)(\.\d+)*)
SPKG_DESC_NIMOSSlibobjc$(LIBOBJC) += $(DESCRIPTION), libobjc.so.$(LIBOBJC)
RUNTIME_DEP_PKGS_NIMOSSlibobjc$(LIBOBJC) += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibobjc-gc$(LIBOBJC)
CATALOGNAME_NIMOSSlibobjc-gc$(LIBOBJC) = libobjc_gc$(LIBOBJC)
PKGFILES_NIMOSSlibobjc-gc$(LIBOBJC) += $(call baseisadirs,$(libdir),libobjc_gc\.so\.$(LIBOBJC)(\.\d+)*)
SPKG_DESC_NIMOSSlibobjc-gc$(LIBOBJC) += $(DESCRIPTION), libobjc_gc.so.$(LIBOBJC)
RUNTIME_DEP_PKGS_NIMOSSlibobjc-gc$(LIBOBJC) += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibssp0
CATALOGNAME_NIMOSSlibssp0 = libssp0
PKGFILES_NIMOSSlibssp0 += $(call baseisadirs,$(libdir),libssp\.so\.0(\.\d+)*)
SPKG_DESC_NIMOSSlibssp0 += $(DESCRIPTION), libssp.so.0
RUNTIME_DEP_PKGS_NIMOSSlibssp0 += NIMOSSlibgcc-s1

PACKAGES += NIMOSSlibgo3
PKGFILES_NIMOSSlibgo3 += $(call baseisadirs,$(libdir),libgo\.so\.3(\.\d+)*)
SPKG_DESC_NIMOSSlibgo3 += $(DESCRIPTION), libgo.so.3
RUNTIME_DEP_PKGS_NIMOSSlibgo3 += NIMOSSlibgcc-s1
# Hasn't been investigated. I feel lucky.
CHECKPKG_OVERRIDES_NIMOSSlibgo3 += file-with-bad-content

PACKAGES += NIMOSSlibitm1
PKGFILES_NIMOSSlibitm1 += $(call baseisadirs,$(libdir),libitm\.so\.1(\.\d+)*)
SPKG_DESC_NIMOSSlibitm1 += $(DESCRIPTION), libitm.so.1
RUNTIME_DEP_PKGS_NIMOSSlibitm1 += NIMOSSlibgcc-s1

LIBSTDCXX_VERSION = 6

PACKAGES += NIMOSSlibstdc++$(LIBSTDCXX_VERSION)
CATALOGNAME_NIMOSSlibstdc++$(LIBSTDCXX_VERSION) = libstdc++$(LIBSTDCXX_VERSION)
PKGFILES_NIMOSSlibstdc++$(LIBSTDCXX_VERSION) += $(call baseisadirs,$(libdir),libstdc\+\+\.so\.$(LIBSTDCXX_VERSION)(\.\d+)*)
SPKG_DESC_NIMOSSlibstdc++$(LIBSTDCXX_VERSION) += $(DESCRIPTION), libstdc++.so.$(LIBSTDCXX_VERSION)
RUNTIME_DEP_PKGS_NIMOSSlibstdc++$(LIBSTDCXX_VERSION) += NIMOSSlibgcc-s1

# The libquadmath.so.0 library is only build on Intel
PACKAGES_i386 += NIMOSSlibquadmath0
CATALOGNAME_NIMOSSlibquadmath0 = libquadmath0
PKGFILES_NIMOSSlibquadmath0 += $(call baseisadirs,$(libdir),libquadmath\.so\.0(\.\d+)*)
SPKG_DESC_NIMOSSlibquadmath0 += GNU C compiler, libquadmath.so.0
RUNTIME_DEP_PKGS_NIMOSSlibquadmath0 += NIMOSSlibgcc-s1

# Dependencies only on Intel
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core_i386 += NIMOSSlibquadmath0
RUNTIME_DEP_PKGS_NIMOSSlibgfortran3_i386 += NIMOSSlibquadmath0
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += $(RUNTIME_DEP_PKGS_$(PKG_BASENAME)core_$(GARCH))
RUNTIME_DEP_PKGS_NIMOSSlibgfortran3 += $(RUNTIME_DEP_PKGS_NIMOSSlibgfortran3_$(GARCH))

PACKAGES += NIMOSSlibatomic1
PKGFILES_NIMOSSlibatomic1 += $(call baseisadirs,$(libdir),libatomic\.so\.1(\.\d+)*)
SPKG_DESC_NIMOSSlibatomic1 += $(DESCRIPTION), libatomic.so.1
RUNTIME_DEP_PKGS_NIMOSSlibatomic1 += NIMOSSlibgcc-s1

PACKAGES += $(PKG_BASENAME)g++
SPKG_DESC_$(PKG_BASENAME)g++ = GNU C++ Compiler
PKGFILES_$(PKG_BASENAME)g++  = $(foreach F,$(CXX_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)g++ += $(foreach F,$(CXX_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)g++ += $(bindir)/\w+-\w+-solaris[\d\.]+-[cg]\+\+$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)g++ += $(libexecdir)/.*cc1plus
PKGFILES_$(PKG_BASENAME)g++ += $(libdir)/.*libstdc.*a
PKGFILES_$(PKG_BASENAME)g++ += $(call baseisadirs,$(libdir),libstdc\+\+\.so)
PKGFILES_$(PKG_BASENAME)g++ += $(mandir)/.*g\+\+.1
# I do not understand this regular expression.
PKGFILES_$(PKG_BASENAME)g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_$(PKG_BASENAME)g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/ostream.*
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibstdc++$(LIBSTDCXX_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibz1

# The C++ compiler needs the C compiler.
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += $(PKG_BASENAME)core

ALTERNATIVES_$(PKG_BASENAME)g++ += $(PKG_VERSION_TOKEN)g++
ALTERNATIVE_$(PKG_VERSION_TOKEN)g++ += $(bindir)/g++ gcc_gplusplus $(bindir)/g++$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

RUNTIME_DEP_PKGS_NIMOSSlibgij$(JAVA_LIB_VERSION) += NIMOSSlibgcc-s1

PACKAGES += $(PKG_BASENAME)gfortran
SPKG_DESC_$(PKG_BASENAME)gfortran   = GNU Fortran Compiler
PKGFILES_$(PKG_BASENAME)gfortran += $(foreach F,$(FORTRAN_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)gfortran += $(foreach F,$(FORTRAN_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)gfortran += $(bindir)/\w+-\w+-solaris[\d\.]+-gfortran$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)gfortran += $(libdir)/.*libgfortran.*a
PKGFILES_$(PKG_BASENAME)gfortran += $(libexecdir)/.*f951
PKGFILES_$(PKG_BASENAME)gfortran += $(mandir)/.*gfortran.1
PKGFILES_$(PKG_BASENAME)gfortran += $(infodir)/gfortran.*
PKGFILES_$(PKG_BASENAME)gfortran += $(call baseisadirs,$(libdir),libgfortran\.so)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibgfortran3
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibz1

ALTERNATIVES_$(PKG_BASENAME)gfortran += gfortran
ALTERNATIVE_gfortran += $(bindir)/gfortran gcc_gfortran $(bindir)/gfortran$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

PACKAGES += $(PKG_BASENAME)java
SPKG_DESC_$(PKG_BASENAME)java       = GNU Java Compiler
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSecj
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibz1
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += surplus-dependency|NIMOSSecj

PKGFILES_$(PKG_BASENAME)java  = $(foreach F,$(JAVA_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)java += $(foreach F,$(JAVA_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)java += $(bindir)/\w+-\w+-solaris[\d\.]+-gcj$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gcj.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gij.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/jv.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/jcf.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/grmi.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*jar.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*jni.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*java.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gorbd.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gapplet.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gkeytool.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gserialver.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gtnameserv.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gnative2ascii.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gc-analyze.*
PKGFILES_$(PKG_BASENAME)java += $(datadir)/java/.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libgij.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libffi.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*lib-gnu-awt.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*security.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*logging.properties
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*pkgconfig.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*gcj.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libgcj.*a
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*collect.*
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*jvgenmain
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*jc1.*
PKGFILES_$(PKG_BASENAME)java += $(infodir)/gcj.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*gcj/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*awt/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*classpath/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*java.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*ffi.h
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*org/.*

# The following list could be probably expanded from $(JAVA_BINARIES)
ALTERNATIVES_$(PKG_BASENAME)java += $(PKG_VERSION_TOKEN)java
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/aot-compile gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gappletviewer gcc_gjava $(bindir)/gappletviewer$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gc-analyze gcc_gjava $(bindir)/gc-analyze$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcj gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcj-dbtool gcc_gjava $(bindir)/gcj-dbtool$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcjh gcc_gjava $(bindir)/gcjh$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gij gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjar gcc_gjava $(bindir)/gjar$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjarsigner gcc_gjava $(bindir)/gjarsigner$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjavah gcc_gjava $(bindir)/gjavah$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gkeytool gcc_gjava $(bindir)/gkeytool$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gnative2ascii gcc_gjava $(bindir)/$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gorbd gcc_gjava $(bindir)/gorbd$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmic gcc_gjava $(bindir)/grmic$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmid gcc_gjava $(bindir)/grmid$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmregistry gcc_gjava $(bindir)/grmregistry$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmregistry gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gserialver gcc_gjava $(bindir)/gserialver$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gtnameserv gcc_gjava $(bindir)/gtnameserv$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/jcf-dump gcc_gjava $(bindir)/jcf-dump$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/jv-convert gcc_gjava $(bindir)/jv-convert$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/rebuild-gcj-db gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)

PACKAGES += $(PKG_BASENAME)objc
SPKG_DESC_$(PKG_BASENAME)objc       = GNU Objective C Compiler
PKGFILES_$(PKG_BASENAME)objc  = $(libexecdir)/.*cc1obj
PKGFILES_$(PKG_BASENAME)objc += $(libdir)/.*libobjc.*a
PKGFILES_$(PKG_BASENAME)objc += $(includedir)/.*objc/.*
PKGFILES_$(PKG_BASENAME)objc += $(libdir)/.*/include/objc/.*
PKGFILES_$(PKG_BASENAME)objc += $(call baseisadirs,$(libdir),libobjc.so)
PKGFILES_$(PKG_BASENAME)objc += $(call baseisadirs,$(libdir),libobjc_gc.so)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibobjc$(LIBOBJC)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibobjc-gc$(LIBOBJC)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibz1

# libiconv deps cropped up relatively late in the porting process. Perhaps
# they apply to all arch/OS combinations.
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += NIMOSSlibiconv2

PACKAGES += $(PKG_BASENAME)ada
SPKG_DESC_$(PKG_BASENAME)ada       = GCC Ada compiler (GNAT)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada         = $(PKG_BASENAME)core
PKGFILES_$(PKG_BASENAME)ada  = $(prefix)/libexec/.*gnat1
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/lib/.*libgnat.*a
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/lib/.*libgnarl.*a
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/.*/adalib/.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/.*/adainclude/.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/info/.*gnat.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/bin/gnat(?!ive).*
# There are static libraries, .a files in the ada package. Let them be.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += discouraged-path-in-pkgmap
# It needs the core compiler.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += surplus-dependency|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += file-with-bad-content

RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += NIMOSSlibz1

# This is an obsolete package. Nothing depends on it, so we can remove it.
INCOMPATIBLE_PKGS_$(PKG_BASENAME)ada = $(PKG_BASENAME)adart

PACKAGES += $(PACKAGES_$(GARCH))
CORE_BINARIES = cpp gcc gcov
CXX_BINARIES = g\+\+ c\+\+
FORTRAN_BINARIES = gfortran
JAVA_BINARIES  = gcj gij aot-compile grmiregistry
JAVA_BINARIES += gappletviewer gc-analyze gcj-dbtool gcjh gjar gjarsigner gjavah
JAVA_BINARIES += gkeytool gnative2ascii gorbd grmic grmid grmregistry
JAVA_BINARIES += gserialver gtnameserv jcf-dump jv-convert rebuild-gcj-db

# GCC-4.7 contains assembler specific to sparcv9, incompatible with sparcv8.
# If we wanted to build it on Solaris 9, we would have to add these overrides.
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibffi4 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgcc-s1 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgcj$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgfortran3 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgij$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibgomp1 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibobjc$(LIBOBJC) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibobjc-gc$(LIBOBJC) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibssp0 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_NIMOSSlibstdc++6 += binary-architecture-does-not-match-placement

# We're building with the default GAR maps, currently U5.
# LINKER_MAP_RELEASE = solaris10u8

#Direct binding is disabled to to problem with amd64 libs
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += no-direct-binding
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += soname-unused
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += no-direct-binding
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += soname-unused
CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += no-direct-binding
CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += no-direct-binding
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += no-direct-binding
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += soname-unused
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += soname-unused
CHECKPKG_OVERRIDES_NIMOSSlibatomic1 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibffi4 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgcj$(JAVA_LIB_VERSION) += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgcj-tools$(JAVA_LIB_VERSION) += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgfortran3 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgij$(JAVA_LIB_VERSION) += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgo3 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibgomp1 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibitm1 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibobjc-gc4 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibobjc4 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibquadmath0 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibssp0 += no-direct-binding
CHECKPKG_OVERRIDES_NIMOSSlibstdc++6 += no-direct-binding

include files/scripts.mk
include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)$(prefix)/$(PKG_VERSION_TOKEN)/bin
	for b in $(CORE_BINARIES) $(CXX_BINARIES) \
		$(FORTRAN_BINARIES) $(JAVA_BINARIES); do \
		gln -v -s -f ../../bin/$${b}$(PROGRAM_SUFFIX) \
		$(DESTDIR)$(prefix)/$(PKG_VERSION_TOKEN)/bin/$${b}; \
	done
	bash $(FILEDIR)/customize_specs.sh $(DESTDIR) $(PROGRAM_SUFFIX) $(VERSION)
	@$(MAKECOOKIE)

# Use NIMOSS or Solaris tools explicitly:
AR = /usr/ccs/bin/ar
AS = /usr/ccs/bin/as
NM = /usr/ccs/bin/nm
RANLIB = /usr/ccs/bin/ranlib
STRIP = /usr/css/bin/strip
OBJCOPY = /opt/csw/bin/gobjcopy
OBJDUMP = /opt/csw/bin/gobjdump
READELF = /opt/csw/bin/greadelf

CONFIGURE_ENV := PATH=$(PATH) CC=$(CC) LD_OPTIONS="$(LD_OPTIONS)" AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
BUILD_ENV := PATH=$(PATH) LD_OPTIONS="$(LD_OPTIONS)" AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
INSTALL_ENV := PATH=$(PATH) AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
