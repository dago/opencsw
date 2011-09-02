# $Id$
#
# ! Ada is not built yet, it requires PPL which isn't built yet.
#
# amd64 compilation fails
# potentially related bug:
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=39048

NAME      = gcc
VERSION   = 4.7-20110820
CATEGORIES   = lang
GARTYPE = v2
BASE_VERSION = $(shell echo $(VERSION) | gsed -e 's/^\([0-9]\+\.[0-9]\+\)\(.*\)/\1/')

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++, 
	Objective-C, Fortran, Java, and Ada, as well as libraries 
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(DISTNAME).tar.bz2
# MASTER_SITES = $(GNU_MIRROR)/$(NAME)-$(VERSION)/
MASTER_SITES = ftp://ftp.fu-berlin.de/unix/languages/gcc/snapshots/$(VERSION)/

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# GIT init takes a long time, disable for now, reenable if build works
NOGITPATCH ?= 1

## Source URLs
VENDOR_URL = http://gcc.gnu.org

## Copyright File
LICENSE = COPYING3

# prefix = $(BUILD_PREFIX)/gcc4
# libdir_install = $(BUILD_PREFIX)/lib
# libdir = $(abspath $(BUILD_PREFIX)/lib/$(MM_LIBDIR))
# CONFIGURE_ARGS += --prefix=$(prefix)
# CONFIGURE_ARGS += --libdir=$(libdir)
# CONFIGURE_ARGS += --exec-prefix=$(BUILD_PREFIX)/gcc4

## build options
# http://gcc.gnu.org/install/configure.html

# Could be used to break out of the /opt/csw/gcc4 prefix
PROGRAM_SUFFIX = -$(BASE_VERSION)
CONFIGURE_ARGS += --program-suffix=$(PROGRAM_SUFFIX)

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-gnu-as
CONFIGURE_ARGS += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --with-included-gettext
CONFIGURE_ARGS += --with-libiconv-prefix=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-x
CONFIGURE_ARGS += --with-mpfr=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-gmp=$(BUILD_PREFIX)
# To be enabled when PPL is built
# CONFIGURE_ARGS += --with-ppl=$(BUILD_PREFIX)
CONFIGURE_ARGS += --enable-java-awt=xlib
# CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix 
CONFIGURE_ARGS += --enable-stage1-languages=c
# We'll build ada later. It requires the PPL library.
# CONFIGURE_ARGS += --enable-languages=ada,c,c++,fortran,java,objc
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc,go
CONFIGURE_ARGS += --enable-bootstrap
CONFIGURE_ARGS += --with-system-zlib

# there could be some abstractions in gar.conf.mk, but at the moment there
# aren't so let's specify architectures by hand.
#
# This avoids the sparcv8+ binaries.
CPU_sparc_32 = v8
CPU_sparc_64 = v9
CPU_i386_32 = i386
CPU_i386_64 = x86-64

CONFIGURE_ARGS_sparc += --with-cpu=$(CPU_$(GARCH)_32)
# These two should not be defined, otherwise the Intel build breaks.
# CONFIGURE_ARGS_i386 += --with-cpu-32=$(CPU_$(GARCH)_32)
# CONFIGURE_ARGS_i386 += --with-cpu-64=$(CPU_$(GARCH)_64)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# GCC can't be built in the same directory with the sources.
# It also can't be built in a subdirectory of the sources.
OBJDIR          = $(abspath $(WORKDIR)/objdir)

# These flags are passed when gcc is built with gcc.
# Needed to remove FLAVOR_FLAGS, because they were Sun Studio specific.
CFLAGS_FOR_TARGET_sparc = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CC_FLAGS) $(EXTRA_GCC_CC_FLAGS) $(EXTRA_CC_FLAGS)
CXXFLAGS_FOR_TARGET_sparc = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CXX_FLAGS) $(EXTRA_GCC_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
CFLAGS_FOR_TARGET = $(CFLAGS_FOR_TARGET_$(GARCH))
CXXFLAGS_FOR_TARGET = $(CXXFLAGS_FOR_TARGET_$(GARCH))
EXTRA_EXPORTS += CFLAGS_FOR_TARGET
EXTRA_EXPORTS += CXXFLAGS_FOR_TARGET

# The theory goes that the CFLAGS and others cause problems with the multilib
# builds where 64-bit binaries are built.  This is triggered by the gcc build;
# the compiler binaries are 32-bit only, but since the compiler can generate
# 32-bit and 64-bit binaries, the libraries have to be built for both
# architectures.
ifeq ($(MODULATION),isa-i386)
CFLAGS =
CXXFLAGS =
FFLAGS =
FCFLAGS =
OPTFLAGS =
endif

# Might be necessary, but CFLAGS_FOR_TARGET seem to be enough for now.
# BOOT_CFLAGS = $(CFLAGS_FOR_TARGET)
# EXTRA_EXPORTS += BOOT_FLAGS

# bash must be used, otherwise:
# http://fixunix.com/solaris/490396-gcc-build-fails-cannot-compute-suffix-object-files.html
CONFIG_SHELL = /opt/csw/bin/bash
EXTRA_EXPORTS += CONFIG_SHELL

EXTRA_CONFIGURE_EXPORTS += CFLAGS_FOR_TARGET
EXTRA_CONFIGURE_EXPORTS += CXXFLAGS_FOR_TARGET

# Only required for Sun Studio bootstrapping
# PATCHFILES += 0001-clear-AM_CFLAGS-in-lto-plugin.patch

# Bootstrapping with Sun Studio has issues
# http://gcc.gnu.org/ml/gcc-help/2011-08/msg00191.html
GARCOMPILER = GNU

# There's a lot of failing checks. Probably a lot of porting work.
SKIPTEST = 1

# Used multiple times in package definitions
JAVA_LIB_VERSION = 13

ALTERNATIVES_PRIO = 460

PACKAGES = CSWgcc4core
SPKG_DESC_CSWgcc4core = GNU C compiler
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibffi4
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibssp0
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibz1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWpython

ALTERNATIVES_CSWgcc4core += gcc4core
ALTERNATIVE_gcc4core += $(bindir)/cpp gcc_core $(bindir)/cpp$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_gcc4core += $(bindir)/gcc gcc_core $(bindir)/gcc$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4core += $(bindir)/gcov gcc_core $(bindir)/gcov$(PROGRAM_SUFFIX)

# Because I can.
CHECKPKG_OVERRIDES_CSWgcc4core += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4g++ += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4java += file-with-bad-content
CHECKPKG_OVERRIDES_CSWlibgcj$(JAVA_LIB_VERSION) += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/i386-pc-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.10/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_CSWgcc4objc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4gfortran += file-with-bad-content
# Due to complex regular expressions
CHECKPKG_OVERRIDES_CSWgcc4java += file-collision|$(includedir)/c++/$(VERSION)/sun/awt/CausedFocusEvent.h|CSWgcc4g++|CSWgcc4java
CHECKPKG_OVERRIDES_CSWgcc4java += file-collision|/opt/csw/include/c++/4.7.0/sun/awt/CausedFocusEvent.h|CSWgcc4g++|CSWgcc4java
CHECKPKG_OVERRIDES_CSWgcc4g++ += file-collision|/opt/csw/include/c++/4.7.0/sun/awt/CausedFocusEvent.h|CSWgcc4g++|CSWgcc4java

# Only man pages, so not a big problem. Alternatives could be used, but it
# requires rebuilding libffi.
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(mandir)/man3/ffi_call.3|CSWgcc4core|CSWlibffi-dev
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(mandir)/man3/ffi.3|CSWgcc4core|CSWlibffi-dev
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(mandir)/man3/ffi_prep_cif.3|CSWgcc4core|CSWlibffi-dev

# The .a files are necessary
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_CSWgcc4objc += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_CSWgcc4java += discouraged-path-in-pkgmap

CHECKPKG_OVERRIDES_CSWgcc4gfortran += discouraged-path-in-pkgmap

# From the 'hopeless errors' department:
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/libffi.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/libgcc_s.so|CSWgcc3core|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/libgcj.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/libobjc.so|CSWgcc3objcrt|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/sparcv9/lib-gnu-awt-xlib.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/sparcv9/libffi.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/sparcv9/libgcj.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/sparcv9/libobjc.so|CSWgcc3objcrt|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4objc += file-collision|$(libdir)/libobjc.so|CSWgcc3objcrt|CSWgcc4objc
CHECKPKG_OVERRIDES_CSWgcc4objc += file-collision|$(libdir)/sparcv9/libobjc.so|CSWgcc3objcrt|CSWgcc4objc
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|$(libdir)/lib-gnu-awt-xlib.so|CSWgcc3javart|CSWgcc4core

# Some static libraries are required to build binaries with gcc, for example
# libgcc.a and libgcc_eh.a. Otherwise: ld: fatal: library -lgcc: not found
MERGE_EXCLUDE_LIBTOOL =
MERGE_EXCLUDE_STATICLIBS =
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/libiberty\.a

# Catch-all package

PACKAGES += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) = lib_gnu_awt_xlib$(JAVA_LIB_VERSION)
PKGFILES_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),lib-gnu-awt-xlib\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(DESCRIPTION), lib-gnu-awt-xlib.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += CSWlibgcc-s1

PACKAGES += CSWlibffi4
CATALOGNAME_CSWlibffi4 = libffi4
PKGFILES_CSWlibffi4 += $(call baseisadirs,$(libdir),libffi\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibffi4 += $(DESCRIPTION), libffi.so.4
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibffi4
RUNTIME_DEP_PKGS_CSWlibffi4 += CSWlibgcc-s1

PACKAGES += CSWlibgcc-s1
CATALOGNAME_CSWlibgcc-s1 = libgcc_s1
PKGFILES_CSWlibgcc-s1 += $(call baseisadirs,$(libdir),libgcc_s\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgcc-s1 += $(DESCRIPTION), libgcc_s.so.1
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgcc-s1
# For reference, the old CSWgcc3corert:
# http://buildfarm.opencsw.org/pkgdb/srv4/1991387f2cb9f545b2a1b254b50638ef/
OBSOLETED_BY_CSWlibgcc-s1 = CSWgcc3corert

PACKAGES += CSWlibgcj-tools$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgcj-tools$(JAVA_LIB_VERSION) = libgcj_tools$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgcj-tools$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj-tools\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgcj-tools$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj-tools.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgcj-tools$(JAVA_LIB_VERSION) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgcj-tools$(JAVA_LIB_VERSION) += CSWlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgcj-tools$(JAVA_LIB_VERSION) += CSWlibz1

PACKAGES += CSWlibgcj$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgcj$(JAVA_LIB_VERSION) = libgcj$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgcj$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgcj$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgcj$(JAVA_LIB_VERSION) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgcj$(JAVA_LIB_VERSION) += CSWlibz1

PACKAGES += CSWlibgfortran3
CATALOGNAME_CSWlibgfortran3 = libgfortran3
PKGFILES_CSWlibgfortran3 += $(call baseisadirs,$(libdir),libgfortran\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibgfortran3 += $(DESCRIPTION), libgfortran.so.3
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWlibgfortran3 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgfortran3 = CSWgcc4gfortranrt

PACKAGES += CSWlibgij$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgij$(JAVA_LIB_VERSION) = libgij$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgij$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgij\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgij$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgij.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgij$(JAVA_LIB_VERSION) += CSWlibz1

PACKAGES += CSWlibgomp1
CATALOGNAME_CSWlibgomp1 = libgomp1
PKGFILES_CSWlibgomp1 += $(call baseisadirs,$(libdir),libgomp\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgomp1 += $(DESCRIPTION), libgomp.so.1
RUNTIME_DEP_PKGS_CSWlibgomp1 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgomp1 += CSWgcc4corert

PACKAGES += CSWlibobjc4
CATALOGNAME_CSWlibobjc4 = libobjc4
PKGFILES_CSWlibobjc4 += $(call baseisadirs,$(libdir),libobjc\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibobjc4 += $(DESCRIPTION), libobjc.so.4
RUNTIME_DEP_PKGS_CSWlibobjc4 += CSWlibgcc-s1

PACKAGES += CSWlibobjc-gc4
CATALOGNAME_CSWlibobjc-gc4 = libobjc_gc4
PKGFILES_CSWlibobjc-gc4 += $(call baseisadirs,$(libdir),libobjc_gc\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibobjc-gc4 += $(DESCRIPTION), libobjc_gc.so.4
RUNTIME_DEP_PKGS_CSWlibobjc-gc4 += CSWlibgcc-s1

PACKAGES += CSWlibssp0
CATALOGNAME_CSWlibssp0 = libssp0
PKGFILES_CSWlibssp0 += $(call baseisadirs,$(libdir),libssp\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibssp0 += $(DESCRIPTION), libssp.so.0
RUNTIME_DEP_PKGS_CSWlibssp0 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibssp0 += CSWgcc4corert

PACKAGES += CSWlibstdc++6
CATALOGNAME_CSWlibstdc++6 = libstdc++6
PKGFILES_CSWlibstdc++6 += $(call baseisadirs,$(libdir),libstdc\+\+\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibstdc++6 += $(DESCRIPTION), libstdc++.so.6
RUNTIME_DEP_PKGS_CSWlibstdc++6 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibstdc++6 = CSWgcc4g++rt

# The libquadmath.so.0 library is only build on Intel
PACKAGES_i386 += CSWlibquadmath0
CATALOGNAME_CSWlibquadmath0 = libquadmath0
PKGFILES_CSWlibquadmath0 += $(call baseisadirs,$(libdir),libquadmath\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibquadmath0 += GNU C compiler, libquadmath.so.0
RUNTIME_DEP_PKGS_CSWlibquadmath0 += CSWlibgcc-s1

# Dependencies only on Intel
RUNTIME_DEP_PKGS_CSWgcc4core_i386 += CSWlibquadmath0
RUNTIME_DEP_PKGS_CSWlibgfortran3_i386 += CSWlibquadmath0
RUNTIME_DEP_PKGS_CSWgcc4core += $(RUNTIME_DEP_PKGS_CSWgcc4core_$(GARCH))
RUNTIME_DEP_PKGS_CSWlibgfortran3 += $(RUNTIME_DEP_PKGS_CSWlibgfortran3_$(GARCH))

PACKAGES += CSWgcc4g++
CATALOGNAME_CSWgcc4g++ = gcc4g++
SPKG_DESC_CSWgcc4g++ = GNU C++ Compiler
PKGFILES_CSWgcc4g++  = $(foreach F,$(CXX_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_CSWgcc4g++ += $(foreach F,$(CXX_BINARIES),$(prefix)/gcc4/bin/$(F))
PKGFILES_CSWgcc4g++ += $(bindir)/\w+-\w+-solaris[\d\.]+-[cg]\+\+$(PROGRAM_SUFFIX)
PKGFILES_CSWgcc4g++ += $(libexecdir)/.*cc1plus
PKGFILES_CSWgcc4g++ += $(libdir)/.*libstdc.*a
PKGFILES_CSWgcc4g++ += $(call baseisadirs,$(libdir),libstdc\+\+\.so)
PKGFILES_CSWgcc4g++ += $(mandir)/.*g\+\+.1
# I do not understand this regular expression.
PKGFILES_CSWgcc4g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_CSWgcc4g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/ostream.*
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibz1

ALTERNATIVES_CSWgcc4g++ += gcc4g++
ALTERNATIVE_gcc4g++ += $(bindir)/g++ gcc_gplusplus $(bindir)/g++$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

OBSOLETED_BY_CSWlibgcc-s1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibgij$(JAVA_LIB_VERSION) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgij$(JAVA_LIB_VERSION) += CSWlibgcj$(JAVA_LIB_VERSION)

PACKAGES += CSWgcc4gfortran
CATALOGNAME_CSWgcc4gfortran   = gcc4gfortran
SPKG_DESC_CSWgcc4gfortran   = GNU Fortran Compiler
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibz1
PKGFILES_CSWgcc4gfortran += $(foreach F,$(FORTRAN_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_CSWgcc4gfortran += $(foreach F,$(FORTRAN_BINARIES),$(prefix)/gcc4/bin/$(F))
PKGFILES_CSWgcc4gfortran += $(bindir)/\w+-\w+-solaris[\d\.]+-gfortran$(PROGRAM_SUFFIX)
PKGFILES_CSWgcc4gfortran += $(libdir)/.*libgfortran.*a
PKGFILES_CSWgcc4gfortran += $(libexecdir)/.*f951
PKGFILES_CSWgcc4gfortran += $(mandir)/.*gfortran.1
PKGFILES_CSWgcc4gfortran += $(infodir)/gfortran.*
PKGFILES_CSWgcc4gfortran += $(call baseisadirs,$(libdir),libgfortran\.so)
OBSOLETED_BY_CSWgcc4gfortran  = CSWgcc4g95
OBSOLETED_BY_CSWgcc4gfortran += CSWgcc4g95rt

ALTERNATIVES_CSWgcc4gfortran += gfortran
ALTERNATIVE_gfortran += $(bindir)/gfortran gcc_gfortran $(bindir)/gfortran$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

PACKAGES += CSWgcc4java
CATALOGNAME_CSWgcc4java       = gcc4java
SPKG_DESC_CSWgcc4java       = GNU Java Compiler
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibz1

PKGFILES_CSWgcc4java  = $(foreach F,$(JAVA_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_CSWgcc4java += $(foreach F,$(JAVA_BINARIES),$(prefix)/gcc4/bin/$(F))
PKGFILES_CSWgcc4java += $(bindir)/\w+-\w+-solaris[\d\.]+-gcj$(PROGRAM_SUFFIX)
PKGFILES_CSWgcc4java += $(mandir)/.*/gcj.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gij.*
PKGFILES_CSWgcc4java += $(mandir)/.*/jv.*
PKGFILES_CSWgcc4java += $(mandir)/.*/jcf.*
PKGFILES_CSWgcc4java += $(mandir)/.*/grmi.*
PKGFILES_CSWgcc4java += $(mandir)/.*jar.*
PKGFILES_CSWgcc4java += $(mandir)/.*jni.*
PKGFILES_CSWgcc4java += $(mandir)/.*java.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gorbd.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gapplet.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gkeytool.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gserialver.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gtnameserv.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gnative2ascii.*
PKGFILES_CSWgcc4java += $(mandir)/.*/gc-analyze.*
PKGFILES_CSWgcc4java += $(datadir)/java/.*
PKGFILES_CSWgcc4java += $(libdir)/.*libgij.*a
PKGFILES_CSWgcc4java += $(libdir)/.*libffi.*a
PKGFILES_CSWgcc4java += $(libdir)/.*lib-gnu-awt.*a
PKGFILES_CSWgcc4java += $(libdir)/.*security.*
PKGFILES_CSWgcc4java += $(libdir)/.*logging.properties
PKGFILES_CSWgcc4java += $(libdir)/.*pkgconfig.*
PKGFILES_CSWgcc4java += $(libdir)/.*gcj.*a
PKGFILES_CSWgcc4java += $(libdir)/.*libgcj.*a
PKGFILES_CSWgcc4java += $(libexecdir)/.*collect.*
PKGFILES_CSWgcc4java += $(libexecdir)/.*jvgenmain
PKGFILES_CSWgcc4java += $(libexecdir)/.*jc1.*
PKGFILES_CSWgcc4java += $(infodir)/gcj.*
PKGFILES_CSWgcc4java += $(includedir)/.*gcj/.*
PKGFILES_CSWgcc4java += $(includedir)/.*awt/.*
PKGFILES_CSWgcc4java += $(includedir)/.*classpath/.*
PKGFILES_CSWgcc4java += $(includedir)/.*java.*
PKGFILES_CSWgcc4java += $(includedir)/.*ffi.h
PKGFILES_CSWgcc4java += $(includedir)/.*org/.*

# The following list could be probably expanded from $(JAVA_BINARIES)
ALTERNATIVES_CSWgcc4java += gcc4java
ALTERNATIVE_gcc4java += $(bindir)/aot-compile gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_gcc4java += $(bindir)/gappletviewer gcc_gjava $(bindir)/gappletviewer$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gc-analyze gcc_gjava $(bindir)/gc-analyze$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gcj gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gcj-dbtool gcc_gjava $(bindir)/gcj-dbtool$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gcjh gcc_gjava $(bindir)/gcjh$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gij gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gjar gcc_gjava $(bindir)/gjar$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gjarsigner gcc_gjava $(bindir)/gjarsigner$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gjavah gcc_gjava $(bindir)/gjavah$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gkeytool gcc_gjava $(bindir)/gkeytool$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gnative2ascii gcc_gjava $(bindir)/$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gorbd gcc_gjava $(bindir)/gorbd$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/grmic gcc_gjava $(bindir)/grmic$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/grmid gcc_gjava $(bindir)/grmid$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/grmregistry gcc_gjava $(bindir)/grmregistry$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/grmregistry gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gserialver gcc_gjava $(bindir)/gserialver$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/gtnameserv gcc_gjava $(bindir)/gtnameserv$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/jcf-dump gcc_gjava $(bindir)/jcf-dump$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/jv-convert gcc_gjava $(bindir)/jv-convert$(PROGRAM_SUFFIX)
ALTERNATIVE_gcc4java += $(bindir)/rebuild-gcj-db gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)

PACKAGES += CSWgcc4objc
CATALOGNAME_CSWgcc4objc       = gcc4objc
SPKG_DESC_CSWgcc4objc       = GNU Objective C Compiler
PKGFILES_CSWgcc4objc  = $(libexecdir)/.*cc1obj
PKGFILES_CSWgcc4objc += $(libdir)/.*libobjc.*a
PKGFILES_CSWgcc4objc += $(includedir)/.*objc/.*
PKGFILES_CSWgcc4objc += $(libdir)/.*/include/objc/.*
PKGFILES_CSWgcc4objc += $(call baseisadirs,$(libdir),libobjc.so)
PKGFILES_CSWgcc4objc += $(call baseisadirs,$(libdir),libobjc_gc.so)
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibobjc-gc4
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibobjc4
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibz1

PACKAGES += CSWlibgo0
CATALOGNAME_CSWlibgo0 = libgo0
PKGFILES_CSWlibgo0 += $(call baseisadirs,$(libdir),libgo\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgo0 += $(DESCRIPTION), libgo.so.0
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgo0
RUNTIME_DEP_PKGS_CSWlibgo0 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibgo0 += file-with-bad-content

# libiconv deps cropped up relatively late in the porting process. Perhaps
# they apply to all arch/OS combinations.
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibiconv2

# Maybe it's unnecessary.
# # Solaris 10 on i386 specific:
# RUNTIME_DEP_PKGS_CSWgcc4core_i386_5.10 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4g++_i386_5.10 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4gfortran_i386_5.10 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4objc_i386_5.10 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4java_i386_5.10 += CSWlibiconv2
# RUNTIME_DEP_PKGS_CSWgcc4core += $(RUNTIME_DEP_PKGS_CSWgcc4core_$(GARCH)_$(GAROSREL))
# RUNTIME_DEP_PKGS_CSWgcc4g++ += $(RUNTIME_DEP_PKGS_CSWgcc4g++_$(GARCH)_$(GAROSREL))
# RUNTIME_DEP_PKGS_CSWgcc4gfortran += $(RUNTIME_DEP_PKGS_CSWgcc4gfortran_$(GARCH)_$(GAROSREL))
# RUNTIME_DEP_PKGS_CSWgcc4objc += $(RUNTIME_DEP_PKGS_CSWgcc4objc_$(GARCH)_$(GAROSREL))
# RUNTIME_DEP_PKGS_CSWgcc4java += $(RUNTIME_DEP_PKGS_CSWgcc4java_$(GARCH)_$(GAROSREL))

PACKAGES += $(PACKAGES_$(GARCH))
CORE_BINARIES = cpp gcc gcov
CXX_BINARIES = g\+\+ c\+\+
FORTRAN_BINARIES = gfortran
JAVA_BINARIES  = gcj gij aot-compile grmiregistry
JAVA_BINARIES += gappletviewer gc-analyze gcj-dbtool gcjh gjar gjarsigner gjavah
JAVA_BINARIES += gkeytool gnative2ascii gorbd grmic grmid grmregistry
JAVA_BINARIES += gserialver gtnameserv jcf-dump jv-convert rebuild-gcj-db

include files/scripts.mk
include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)$(prefix)/gcc4/bin
	for b in $(CORE_BINARIES) $(CXX_BINARIES) \
		$(FORTRAN_BINARIES) $(JAVA_BINARIES); do \
		gln -v -s ../../bin/$${b}$(PROGRAM_SUFFIX) \
		$(DESTDIR)$(prefix)/gcc4/bin/$${b}; \
	done
	@$(MAKECOOKIE)

# We need GNU find as find
PATH := /opt/csw/gnu:$(PATH)
