GARNAME = diffutils
GARVERSION = 2.8.1
CATEGORIES = utils

DESCRIPTION = Diff utilities
define BLURB
 The diff package provides the diff, diff3, sdiff, and cmp programs.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
