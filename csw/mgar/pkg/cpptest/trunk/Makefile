# $Id$
GARNAME = cpptest
GARVERSION = 1.1.1
CATEGORIES = utils

DESCRIPTION = Unit testing framework for handling automated tests in C++
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibcpptest0 CSWlibcpptestdevel

CATALOGNAME_CSWlibcpptest0 = libcpptest0
CATALOGNAME_CSWlibcpptestdevel = libcpptest_devel

SPKG_DESC_CSWlibcpptest0 = $(DESCRIPTION) Runtime Library
SPKG_DESC_CSWlibcpptestdevel = $(DESCRIPTION) Development Files

RUNTIME_DEP_PKGS_CSWlibcpptestdevel = CSWlibcpptest0
CHECKPKG_OVERRIDES_CSWlibcpptestdevel += surplus-dependency|CSWlibcpptest0

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibcpptest0 = $(call baseisadirs,$(libdir),[^/]*\.so\.\d+(\.\d+)*)

include gar/category.mk
