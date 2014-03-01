# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gflags
VERSION = 2.0
CATEGORIES = lib
GARTYPE = Commandline flags module for C++ flags processing
define BLURB
	The gflags package contains a library that implements commandline flags
	processing. As such it's a replacement for getopt(). It has increased
	flexibility, including built-in support for C++ types like string, and the
	ability to define flags in the source file in which they're used.
endef
SPKG_SOURCEURL = http://code.google.com/p/google-gflags/
MASTER_SITES = DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

GARCOMPILER = GNU
PATCHFILES += 0000-Disable-a-test-that-doesn-t-work-on-Solaris.patch
PATCHFILES += 0001-Disable-the-same-test-again-inf-this-time.patch
PATCHFILES += 0002-One-more-test.patch
ATHS)
BUILD64 = 1
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amddPACKAGES += CSWlibgflags2
PKGFILES_CSWlibgflags2 += $(call baseisadirs,$(libdir),libgflags\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgflags2 += $(DESCRIPTION), libgflags.so.2
RUNTIME_DEP_PKGS_CSWlibgflags2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgflags2 += CSWlibstdc++6

PACKAGES += CSWlibgflags-nothreads2
PKGFILES_CSWlibgflags-nothreads2 += $(call baseisadirs,$(libdir),libgflags_nothreads\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgflags-nothreads2 += $(DESCRIPTION), libgflags_nothreads.so.2
RUNTIME_DEP_PKGS_CSWlibgflags-nothreads2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgflags-nothreads2 += CSWlibstdc++6

PACKAGES += CSWgflags-dev
SPKG_DESC_CSWgflags-dev = $(DESCRIPTION)
OBSOLETED_BY_CSWgflags-dev = CSWgflags
RUNTIME_DEP_PKGS_CSWgflags-dev += CSWlibgflags2
RUNTIME_DEP_PKGS_CSWgflags-dev += CSWlibgflags-nothreads2
CHECKPKG_OVERRIDES_CSWgflags-dev += file-with-bad-content|/usr/local|root/opt/csw/bin/gflags_completions.sh

include gar/category.mk
