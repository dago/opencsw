GARNAME = libthai
GARVERSION = 0.1.4
CATEGORIES = lib

DESCRIPTION = Thai language support routines
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=34448&package_id=26558
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
