# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gflags
VERSION = 2.0
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = a library that implements commandline flags processing
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
MERGE_DIRS_isa-amdd64   = $(libdir)
include