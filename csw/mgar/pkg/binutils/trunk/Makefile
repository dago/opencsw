GARNAME = binutils
GARVERSION = 2.19.1
CATEGORIES = utils

DESCRIPTION = GNU binary utilities: gas, gld, gprof, and others
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

REQUIRED_PKGS = CSWzlib CSWiconv CSWggettextrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
