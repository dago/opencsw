# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = googlemock
GARVERSION = 1.4.0
CATEGORIES = lib
DESCRIPTION = a library for writing and using C++ mock classes
define BLURB
  Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics
  in mind, Google C++ Mocking Framework (or Google Mock for short) is a library
  for writing and using C++ mock classes.
endef
SPKG_SOURCEURL = http://code.google.com/p/googlemock/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = gmock-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/gmock-$(GARVERSION)
UFILES_REGEX = gmock-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)

# Compilation unfortunately fails:
#
# "./include/gmock/gmock-printers.h", line 480: Error: static
# testing::internal::TuplePrefixPrinter<1>::PrintPrefixTo<testing::internal::TuplePrefixPrinter<1>::Tuple>(const
# testing::internal::TuplePrefixPrinter<1>::Tuple&, std::ostream *) already had
# a body defined.
#
# include gar/category.mk
