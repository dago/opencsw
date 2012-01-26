# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = googletest
VERSION = 1.4.0
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = a framework for writing C++ tests on a variety of platforms
define BLURB
  Google's framework for writing C++ tests on a variety of platforms (Linux,
  Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on the xUnit
  architecture. Supports automatic test discovery, a rich set of assertions,
  user-defined assertions, death tests, fatal and non-fatal failures, value-
  and type-parameterized tests, various options for running the tests, and XML
  test report generation.
endef
SPKG_SOURCEURL = http://code.google.com/p/googletest/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = gtest-$(VERSION).tar.gz
DISTNAME = gtest-$(VERSION)
UFILES_REGEX = gtest-(\d+(?:\.\d+)*).tar.gz
EXTRA_CXXFLAGS = -library=stlport4 -library=no%Cstd
# EXTRA_LDFLAGS = -lCrun -lm
BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
