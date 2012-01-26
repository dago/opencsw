# $Id$
NAME = cpptest
VERSION = 1.1.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Unit testing framework for handling automated tests in C++
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Keep-norunpath-during-linking.patch

PACKAGES = CSWlibcpptest0
SPKG_DESC_CSWlibcpptest0 = Unit testing framework for handling automated tests in C++, libcpptest.so.0
PKGFILES_CSWlibcpptest0 = $(call pkgfiles_lib,libcpptest.so.0)

PACKAGES += CSWlibcpptest-dev
SPKG_DESC_CSWlibcpptest-dev = Development files for libcpptest.so.0
RUNTIME_DEP_PKGS_CSWlibcpptest-dev = CSWlibcpptest0
OBSOLETED_BY_CSWlibcpptest-dev += CSWlibcpptestdevel
CATALOGNAME_CSWlibcpptestdevel = libcpptest_devel_stub

BUILD64_LIBS_ONLY = 1

EXTRA_CXXFLAGS = -norunpath

include gar/category.mk
