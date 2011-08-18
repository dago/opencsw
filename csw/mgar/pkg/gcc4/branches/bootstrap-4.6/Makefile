# $Id$
#
# ! Ada is not built yet, it requires PPL which isn't built yet.

NAME      = gcc
VERSION   = 4.6.1
CATEGORIES   = lang
GARTYPE = v2

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++, 
	Objective-C, Fortran, Java, and Ada, as well as libraries 
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(DISTNAME).tar.bz2
MASTER_SITES = $(GNU_MIRROR)/$(NAME)-$(VERSION)/

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# GIT init takes a long time, disable for now, reenable if build works
NOGITPATCH ?= 1

## Source URLs
VENDOR_URL = http://gcc.gnu.org

## Copyright File
LICENSE = COPYING3

prefix = $(BUILD_PREFIX)/gcc4
libdir_install = $(BUILD_PREFIX)/lib
libdir = $(abspath $(BUILD_PREFIX)/lib/$(MM_LIBDIR))

## build options
# http://gcc.gnu.org/install/configure.html

# Could be used to break out of the /opt/csw/gcc4 prefix
# CONFIGURE_ARGS += --program-prefix=gcc4-

CONFIGURE_ARGS += --with-pkgversion=OpenCSW
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --exec-prefix=$(BUILD_PREFIX)/gcc4
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
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc
CONFIGURE_ARGS += --enable-bootstrap
CONFIGURE_ARGS += --with-system-zlib

# there could be some abstractions in gar.conf.mk, but at the moment there
# aren't so let's specify architectures by hand.
#
# This avoids the sparcv8+ binaries.
CPU_sparc_32 = v8
CPU_sparc_64 = v9
CPU_i386_32 = i386
CPU_i386_64 = amd64

CONFIGURE_ARGS_sparc += --with-cpu=$(CPU_$(GARCH)_32)
CONFIGURE_ARGS_i386 += --with-cpu-32=$(CPU_$(GARCH)_32)
CONFIGURE_ARGS_i386 += --with-cpu-64=$(CPU_$(GARCH)_64)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# GCC can't be built in the same directory with the sources.
OBJDIR          = objdir

# These flags are passed when gcc is built with gcc.
# Needed to remove FLAVOR_FLAGS, because they were Sun Studio specific.
CFLAGS_FOR_TARGET = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CC_FLAGS) $(EXTRA_GCC_CC_FLAGS) $(EXTRA_CC_FLAGS)
CXXFLAGS_FOR_TARGET = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CXX_FLAGS) $(EXTRA_GCC_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
EXTRA_EXPORTS += CFLAGS_FOR_TARGET
EXTRA_EXPORTS += CXXFLAGS_FOR_TARGET

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

PACKAGES = CSWgcc4core
SPKG_DESC_CSWgcc4core = GNU C compiler
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlib-gnu-awt-xlib12
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibffi4
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcj-tools12
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgcj12
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgij12
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibssp0
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibz1
RUNTIME_DEP_PKGS_CSWgcc4core += CSWpython
RUNTIME_DEP_PKGS_CSWgcc4core += CSWbinutils
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibobjc-gc3
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibobjc3
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgcj-tools12 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgcj12 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgij12 += CSWlibz1

# Because I can.
CHECKPKG_OVERRIDES_CSWgcc4core += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4g++ += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4java += file-with-bad-content
CHECKPKG_OVERRIDES_CSWlibgcj12 += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap|/opt/csw/gcc4/libexec/gcc/sparc-sun-solaris2.9/4.6.1/liblto_plugin.la
CHECKPKG_OVERRIDES_CSWgcc4core += discouraged-path-in-pkgmap|/opt/csw/gcc4/libexec/gcc/i386-pc-solaris2.9/4.6.1/liblto_plugin.la
CHECKPKG_OVERRIDES_CSWgcc4objc += file-with-bad-content
CHECKPKG_OVERRIDES_CSWgcc4gfortran += file-with-bad-content
# Due to complex regular expressions
CHECKPKG_OVERRIDES_CSWgcc4java += file-collision|/opt/csw/gcc4/include/c++/4.6.1/sun/awt/CausedFocusEvent.h|CSWgcc4g++|CSWgcc4java
CHECKPKG_OVERRIDES_CSWgcc4g++ += file-collision|/opt/csw/gcc4/include/c++/4.6.1/sun/awt/CausedFocusEvent.h|CSWgcc4g++|CSWgcc4java

# From the 'hopeless errors' department:
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/libffi.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/libgcc_s.so|CSWgcc3core|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/libgcj.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/libobjc.so|CSWgcc3objcrt|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/sparcv9/lib-gnu-awt-xlib.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/sparcv9/libffi.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/sparcv9/libgcj.so|CSWgcc3javart|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/sparcv9/libobjc.so|CSWgcc3objcrt|CSWgcc4core
CHECKPKG_OVERRIDES_CSWgcc4objc += file-collision|/opt/csw/lib/libobjc.so|CSWgcc3objcrt|CSWgcc4objc
CHECKPKG_OVERRIDES_CSWgcc4objc += file-collision|/opt/csw/lib/sparcv9/libobjc.so|CSWgcc3objcrt|CSWgcc4objc
CHECKPKG_OVERRIDES_CSWgcc4core += file-collision|/opt/csw/lib/lib-gnu-awt-xlib.so|CSWgcc3javart|CSWgcc4core


# Catch-all package

PACKAGES += CSWlib-gnu-awt-xlib12
CATALOGNAME_CSWlib-gnu-awt-xlib12 = lib_gnu_awt_xlib12
PKGFILES_CSWlib-gnu-awt-xlib12 += $(call baseisadirs,$(libdir),lib-gnu-awt-xlib\.so\.12(\.\d+)*)
SPKG_DESC_CSWlib-gnu-awt-xlib12 += The GNU Compiler Collection, lib-gnu-awt-xlib.so.12
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlib-gnu-awt-xlib12
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib12 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib12 += CSWlibgcc-s1

PACKAGES += CSWlibffi4
CATALOGNAME_CSWlibffi4 = libffi4
PKGFILES_CSWlibffi4 += $(call baseisadirs,$(libdir),libffi\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibffi4 += The GNU Compiler Collection, libffi.so.4
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibffi4
RUNTIME_DEP_PKGS_CSWlibffi4 += CSWlibgcc-s1

PACKAGES += CSWlibgcc-s1
CATALOGNAME_CSWlibgcc-s1 = libgcc_s1
PKGFILES_CSWlibgcc-s1 += $(call baseisadirs,$(libdir),libgcc_s\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgcc-s1 += The GNU Compiler Collection, libgcc_s.so.1
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgcc-s1
# For reference, the old CSWgcc3corert:
# http://buildfarm.opencsw.org/pkgdb/srv4/1991387f2cb9f545b2a1b254b50638ef/
OBSOLETED_BY_CSWlibgcc-s1 = CSWgcc3corert

PACKAGES += CSWlibgcj-tools12
CATALOGNAME_CSWlibgcj-tools12 = libgcj_tools12
PKGFILES_CSWlibgcj-tools12 += $(call baseisadirs,$(libdir),libgcj-tools\.so\.12(\.\d+)*)
SPKG_DESC_CSWlibgcj-tools12 += The GNU Compiler Collection, libgcj-tools.so.12
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgcj-tools12
RUNTIME_DEP_PKGS_CSWlibgcj-tools12 += CSWlibgcj12
RUNTIME_DEP_PKGS_CSWlibgcj-tools12 += CSWlibgcc-s1

PACKAGES += CSWlibgcj12
CATALOGNAME_CSWlibgcj12 = libgcj12
PKGFILES_CSWlibgcj12 += $(call baseisadirs,$(libdir),libgcj\.so\.12(\.\d+)*)
SPKG_DESC_CSWlibgcj12 += The GNU Compiler Collection, libgcj.so.12
RUNTIME_DEP_PKGS_CSWlibgcj12 += CSWlibgcc-s1

PACKAGES += CSWlibgfortran3
CATALOGNAME_CSWlibgfortran3 = libgfortran3
PKGFILES_CSWlibgfortran3 += $(call baseisadirs,$(libdir),libgfortran\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibgfortran3 += The GNU Compiler Collection, libgfortran.so.3
RUNTIME_DEP_PKGS_CSWgcc4 += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWlibgfortran3 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgfortran3 = CSWgcc4gfortranrt

PACKAGES += CSWlibgij12
CATALOGNAME_CSWlibgij12 = libgij12
PKGFILES_CSWlibgij12 += $(call baseisadirs,$(libdir),libgij\.so\.12(\.\d+)*)
SPKG_DESC_CSWlibgij12 += The GNU Compiler Collection, libgij.so.12

PACKAGES += CSWlibgomp1
CATALOGNAME_CSWlibgomp1 = libgomp1
PKGFILES_CSWlibgomp1 += $(call baseisadirs,$(libdir),libgomp\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgomp1 += The GNU Compiler Collection, libgomp.so.1
RUNTIME_DEP_PKGS_CSWlibgomp1 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibgomp1 += CSWgcc4corert

PACKAGES += CSWlibobjc3
CATALOGNAME_CSWlibobjc3 = libobjc3
PKGFILES_CSWlibobjc3 += $(call baseisadirs,$(libdir),libobjc\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibobjc3 += The GNU Compiler Collection, libobjc.so.3
RUNTIME_DEP_PKGS_CSWlibobjc3 += CSWlibgcc-s1

PACKAGES += CSWlibobjc-gc3
CATALOGNAME_CSWlibobjc-gc3 = libobjc_gc3
PKGFILES_CSWlibobjc-gc3 += $(call baseisadirs,$(libdir),libobjc_gc\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibobjc-gc3 += The GNU Compiler Collection, libobjc_gc.so.3
RUNTIME_DEP_PKGS_CSWlibobjc-gc3 += CSWlibgcc-s1

PACKAGES += CSWlibssp0
CATALOGNAME_CSWlibssp0 = libssp0
PKGFILES_CSWlibssp0 += $(call baseisadirs,$(libdir),libssp\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibssp0 += The GNU Compiler Collection, libssp.so.0
RUNTIME_DEP_PKGS_CSWlibssp0 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibssp0 += CSWgcc4corert

PACKAGES += CSWlibstdc++6
CATALOGNAME_CSWlibstdc++6 = libstdc++6
PKGFILES_CSWlibstdc++6 += $(call baseisadirs,$(libdir),libstdc\+\+\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibstdc++6 += The GNU Compiler Collection, libstdc++.so.6
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
RUNTIME_DEP_PKGS_CSWgcc4libgfortran3 += $(RUNTIME_DEP_PKGS_CSWgcc4libgfortran3_$(GARCH))

PACKAGES += CSWgcc4g++
CATALOGNAME_CSWgcc4g++ = gcc4g++
SPKG_DESC_CSWgcc4g++ = GNU C++ Compiler
PKGFILES_CSWgcc4g++  = $(bindir)/g\+\+
PKGFILES_CSWgcc4g++ += $(bindir)/c\+\+
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

OBSOLETED_BY_CSWlibgcc-s1 += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWlibgij12 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgij12 += CSWlibgcj12

PACKAGES += CSWgcc4gfortran
CATALOGNAME_CSWgcc4gfortran   = gcc4gfortran
SPKG_DESC_CSWgcc4gfortran   = GNU Fortran Compiler
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibz1
PKGFILES_CSWgcc4gfortran  = $(bindir)/gfortran
PKGFILES_CSWgcc4gfortran += $(libdir)/.*libgfortran.*a
PKGFILES_CSWgcc4gfortran += $(libexecdir)/.*f951
PKGFILES_CSWgcc4gfortran += $(mandir)/.*gfortran.1
PKGFILES_CSWgcc4gfortran += .*/gcc4/info/gfortran.*
PKGFILES_CSWgcc4gfortran += $(call baseisadirs,$(libdir),libgfortran\.so)
OBSOLETED_BY_CSWgcc4gfortran  = CSWgcc4g95
OBSOLETED_BY_CSWgcc4gfortran += CSWgcc4g95rt

PACKAGES += CSWgcc4java
CATALOGNAME_CSWgcc4java       = gcc4java
SPKG_DESC_CSWgcc4java       = GNU Java Compiler
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcj-tools12
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgcj12
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgij12
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibmpc2
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibz1

PKGFILES_CSWgcc4java  = $(bindir)/.*gcj.*
PKGFILES_CSWgcc4java += $(bindir)/.*jv-scan
PKGFILES_CSWgcc4java += $(bindir)/.*jv-convert
PKGFILES_CSWgcc4java += $(bindir)/.*jcf-dump
PKGFILES_CSWgcc4java += $(bindir)/.*grmi.*
PKGFILES_CSWgcc4java += $(bindir)/.*grepjar
PKGFILES_CSWgcc4java += $(bindir)/.*gjnih
PKGFILES_CSWgcc4java += $(bindir)/.*gij
PKGFILES_CSWgcc4java += $(bindir)/.*fastjar
PKGFILES_CSWgcc4java += $(bindir)/.*gjar.*
PKGFILES_CSWgcc4java += $(bindir)/.*gjavah
PKGFILES_CSWgcc4java += $(bindir)/.*gorbd
PKGFILES_CSWgcc4java += $(bindir)/.*addr2name.awk
PKGFILES_CSWgcc4java += $(bindir)/.*gappletviewer
PKGFILES_CSWgcc4java += $(bindir)/.*gkeytool
PKGFILES_CSWgcc4java += $(bindir)/.*gserialver
PKGFILES_CSWgcc4java += $(bindir)/.*gtnameserv
PKGFILES_CSWgcc4java += $(bindir)/.*gnative2ascii
PKGFILES_CSWgcc4java += $(bindir)/.*gc-analyze
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
PKGFILES_CSWgcc4java += .*/gcc4/share/java/.*
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
PKGFILES_CSWgcc4java += .*/gcc4/info/gcj.*
PKGFILES_CSWgcc4java += $(includedir)/.*gcj/.*
PKGFILES_CSWgcc4java += $(includedir)/.*awt/.*
PKGFILES_CSWgcc4java += $(includedir)/.*classpath/.*
PKGFILES_CSWgcc4java += $(includedir)/.*java.*
PKGFILES_CSWgcc4java += $(includedir)/.*ffi.h
PKGFILES_CSWgcc4java += $(includedir)/.*org/.*

PACKAGES += CSWgcc4objc
CATALOGNAME_CSWgcc4objc       = gcc4objc
SPKG_DESC_CSWgcc4objc       = GNU Objective C Compiler
PKGFILES_CSWgcc4objc  = $(libexecdir)/.*cc1obj
PKGFILES_CSWgcc4objc += $(libdir)/.*libobjc.*a
PKGFILES_CSWgcc4objc += $(includedir)/.*objc/.*
PKGFILES_CSWgcc4objc += $(libdir)/.*/include/objc/.*
PKGFILES_CSWgcc4objc += $(call baseisadirs,$(libdir),libobjc.so)
PKGFILES_CSWgcc4objc += $(call baseisadirs,$(libdir),libobjc_gc.so)
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibgmp10

PACKAGES += $(PACKAGES_$(GARCH))

include files/scripts.mk
include gar/category.mk

# We need GNU find as find
PATH := /opt/csw/gnu:$(PATH)
