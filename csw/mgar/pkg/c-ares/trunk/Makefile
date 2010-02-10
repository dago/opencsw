GARNAME = c-ares
GARVERSION = 1.7.0
CATEGORIES = lib

DESCRIPTION = c-ares library to perform DNS requests and name resolves asynchronously
define BLURB
endef

MASTER_SITES = http://c-ares.haxx.se/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibcares CSWlibcaresdevel

CATALOGNAME_CSWlibcares = libcares
CATALOGNAME_CSWlibcaresdevel = libcares_devel

SPKG_DESC_CSWlibcares = $(DESCRIPTION)
SPKG_DESC_CSWlibcaresdevel = c-ares library developer files

RUNTIME_DEP_PKGS_CSWlibcaresdevel = CSWlibcares

LICENSE = README.cares

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

PKGFILES_CSWlibcaresdevel = $(PKGFILES_DEVEL)

include gar/category.mk
