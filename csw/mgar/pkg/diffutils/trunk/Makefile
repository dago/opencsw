GARNAME = diffutils
GARVERSION = 2.9
CATEGORIES = utils

DESCRIPTION = Diff utilities
define BLURB
 The diff package provides the diff, diff3, sdiff, and cmp programs.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWggettextrt CSWiconv CSWlibsigsegv

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/lib/charset.alias

include gar/category.mk
