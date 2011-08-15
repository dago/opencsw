# $Id$

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
# NOGITPATCH ?= 1

## build options
CONFIGURE_ARGS  = --prefix=$(BUILD_PREFIX)/gcc4
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
CONFIGURE_ARGS += --enable-java-awt=xlib
# CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix 
CONFIGURE_ARGS += --enable-stage1-languages=c
# We'll build ada later.
# CONFIGURE_ARGS += --enable-languages=ada,c,c++,fortran,java,objc
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc
CONFIGURE_ARGS += --enable-bootstrap
# CONFIGURE_ARGS += --with-arch=v8
# CONFIGURE_ARGS += --with-arch-32=v8

# GCC can't be built in the same directory with the sources.
OBJDIR          = objdir

# These flags are passed when gcc is built with gcc.
# Needed to remove FLAVOR_FLAGS, because they were Sun Studio specific.
CFLAGS_FOR_TARGET = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CC_FLAGS) $(EXTRA_GCC_CC_FLAGS) $(EXTRA_CC_FLAGS)
CXXFLAGS_FOR_TARGET = -O2 $(ARCHFLAGS_GCC4_$(ISA)) $(EXTRA_GCC4_CXX_FLAGS) $(EXTRA_GCC_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
EXTRA_EXPORTS += CFLAGS_FOR_TARGET
EXTRA_EXPORTS += CXXFLAGS_FOR_TARGET

# bash must be used, otherwise:
# http://fixunix.com/solaris/490396-gcc-build-fails-cannot-compute-suffix-object-files.html
CONFIG_SHELL = /opt/csw/bin/bash
EXTRA_EXPORTS += CONFIG_SHELL

# work/solaris9-sparc/build-isa-sparcv8/gcc-4.6.1/objdir/lto-plugin/libtool
# LIBTOOL = $(WORKSRC)/$(OBJDIR)/lto-plugin/libtool

EXTRA_CONFIGURE_EXPORTS += CFLAGS_FOR_TARGET
EXTRA_CONFIGURE_EXPORTS += CXXFLAGS_FOR_TARGET

# OBJDUMP=/opt/csw/bin/gobjdump
# EXTRA_EXPORTS += OBJDUMP

PATCHFILES += 0001-clear-AM_CFLAGS-in-lto-plugin.patch
PATCHFILES += 0002-use-system-libtool.patch

include gar/category.mk

# We need GNU find as find
PATH := /opt/csw/gnu:$(PATH)
