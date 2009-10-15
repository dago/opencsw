# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = googletest
GARVERSION = 1.4.0
CATEGORIES = lib
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
DISTFILES  = gtest-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/gtest-$(GARVERSION)
UFILES_REGEX = gtest-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
