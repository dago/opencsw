GARNAME = patch
GARVERSION = 2.6.1
CATEGORIES = utils

DESCRIPTION = GNU patch utility
define BLURB
  The GNU patch utility.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
PATCHFILES = 0001-Add-missing-strnlen.c-from-GNUlib.patch

PACKAGES = CSWgpatch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWlibgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

EXTRA_LINKER_FLAGS = -lgnugetopt
BUILD_ARGS = SHELL=bash

TEST_TARGET = check

include gar/category.mk
