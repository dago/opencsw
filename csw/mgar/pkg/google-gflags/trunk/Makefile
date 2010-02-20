# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = gflags
GARVERSION = 1.3
CATEGORIES = lib
DESCRIPTION = a library that implements commandline flags processing
define BLURB
	The gflags package contains a library that implements commandline flags
	processing. As such it's a replacement for getopt(). It has increased
	flexibility, including built-in support for C++ types like string, and the
	ability to define flags in the source file in which they're used.
endef
SPKG_SOURCEURL = http://code.google.com/p/google-gflags/
MASTER_SITES = $(GOOGLE_MIRROR)
GOOGLE_PROJECT = google-gflags
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGING_PLATFORMS ?= solaris9-sparc solaris9-i386
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
include gar/category.mk
