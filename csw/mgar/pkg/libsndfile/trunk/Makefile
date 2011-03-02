# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libsndfile
VERSION = 1.0.23
CATEGORIES = lib

DESCRIPTION = C library for reading and writing files containing sampled sound

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

MASTER_SITES = http://www.mega-nerd.com/libsndfile/files/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Add-lrintf-workaround-to-regtest.patch
PATCHFILES += 0002-Add-workaround-for-missing-libm-function-lrint-and-l.patch
PATCHFILES += 0003-Workaround-mising-stdint.h-and-Sun-Studio-shortcomin.patch
PATCHFILES += 0004-Add-branch-for-inttypes.h.patch
PATCHFILES += 0005-Test-for-unsigned-or-test-will-fail.patch

PACKAGES += CSWlibsndfile
CATALOGNAME_CSWlibsndfile = libsndfile
SPKG_DESC_CSWlibsndfile = Tools for reading and writing files containing sampled sound
RUNTIME_DEP_PKGS_CSWlibsndfile += CSWlibogg
RUNTIME_DEP_PKGS_CSWlibsndfile += CSWflac
RUNTIME_DEP_PKGS_CSWlibsndfile += CSWvorbis
RUNTIME_DEP_PKGS_CSWlibsndfile += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWlibsndfile += CSWlibsndfile1

PACKAGES += CSWlibsndfile1
CATALOGNAME_CSWlibsndfile1 = libsndfile1
SPKG_DESC_CSWlibsndfile1 = Library for reading and writing files containing sampled sound, libsndfile.so.1
PKGFILES_CSWlibsndfile1 = $(call baseisadirs,$(libdir),libsndfile\.so\.1(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibsndfile1 += CSWlibogg
RUNTIME_DEP_PKGS_CSWlibsndfile1 += CSWflac
RUNTIME_DEP_PKGS_CSWlibsndfile1 += CSWvorbis

PACKAGES += CSWlibsndfile-dev
CATALOGNAME_CSWlibsndfile-dev = libsndfile_dev
SPKG_DESC_CSWlibsndfile-dev = Development files for libsndfile.so.1
PKGFILES_CSWlibsndfile-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibsndfile-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWlibsndfile-dev += CSWlibsndfile1

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibsndfile)

VENDOR_URL = http://www.mega-nerd.com/libsndfile/

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# We want only 64 bit libs, no 64 bit executables
MERGE_DIRS_isa-extra = $(libdir)

# Relocate docs to standard location
EXTRA_PAX_ARGS += -s ',^\.$(prefix)/share/doc/libsndfile1-dev,.$(prefix)/share/doc/$(NAME),'

# These are all examples
CHECKPKG_OVERRIDES_CSWlibsndfile-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libsndfile/html/FAQ.html
CHECKPKG_OVERRIDES_CSWlibsndfile-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libsndfile/html/octave.html
CHECKPKG_OVERRIDES_CSWlibsndfile-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/libsndfile/html/pkgconfig.html

include gar/category.mk
