GARNAME = c-ares
GARVERSION = 1.7.0
CATEGORIES = lib

DESCRIPTION = Perform DNS requests and name resolves asynchronously
define BLURB
endef

MASTER_SITES = http://c-ares.haxx.se/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibcares
CATALOGNAME = libcares

LICENSE = README.cares

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
