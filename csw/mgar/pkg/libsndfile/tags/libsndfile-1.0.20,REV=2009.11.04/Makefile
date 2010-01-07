# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = libsndfile
GARVERSION = 1.0.20

CATEGORIES = lib

DESCRIPTION = a C library for reading and writing files containing sampled sound

define BLURB
  Libsndfile is a C library for reading and writing files containing sampled
  sound (such as MS Windows WAV and the Apple/SGI AIFF format) through one
  standard library interface. It is released in source code format under the Gnu
  Lesser General Public License.

  The library was written to compile and run on a Linux system but should
  compile and run on just about any Unix (including MacOSX). It can also be
  compiled and run on Win32 systems using the Microsoft compiler and MacOS (OS9
  and earlier) using the Metrowerks compiler. There are directions for compiling
  libsndfile on these platforms in the Win32 and MacOS directories of the source
  code distribution.

  It was designed to handle both little-endian (such as WAV) and big-endian
  (such as AIFF) data, and to compile and run correctly on little-endian (such
  as Intel and DEC/Compaq Alpha) processor systems as well as big-endian
  processor systems such as Motorola 68k, Power PC, MIPS and Sparc. Hopefully
  the design of the library will also make it easy to extend for reading and
  writing new sound file formats. 
endef

MASTER_SITES = http://www.mega-nerd.com/libsndfile/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Add-lrintf-workaround-to-regtest.patch
PATCHFILES += 0002-Add-workaround-for-missing-libm-function-lrint-and-l.patch
PATCHFILES += 0003-Workaround-mising-stdint.h-and-Sun-Studio-shortcomin.patch
PATCHFILES += 0004-Disable-stop-on-error-until-cpp_test-refcount-error-.patch

# TODO: The __func__ replacement may be enhanced with
#   http://mail-index.netbsd.org/pkgsrc-users/2009/05/18/msg009885.html
# PATCHFILES += sunpro-extensions.patch

REQUIRED_PKGS = CSWvorbis CSWflac CSWlibogg CSWsqlite3rt
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

SPKG_SOURCEURL = http://www.mega-nerd.com/libsndfile/

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# EXTRA_CFLAGS = -features=extensions
# EXTRA_CXXFLAGS = -features=extensions

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# We want only 64 bit libs, no 64 bit executables
MERGE_DIRS_isa-extra = $(libdir)

# Relocate docs to standard location
EXTRA_PAX_ARGS += -s ',^\.$(prefix)/share/doc/libsndfile1-dev,.$(BUILD_PREFIX)/share/doc/$(GARNAME),'

include gar/category.mk
