GARNAME = gzip
GARVERSION = 1.4
CATEGORIES = utils

DESCRIPTION = GNU zip
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Force-ggrep-as-Solaris-grep-doesn-t-understand-the-f.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggrep

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
