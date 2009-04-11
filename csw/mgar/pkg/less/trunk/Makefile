GARNAME = less
GARVERSION = 429
CATEGORIES = utils

DESCRIPTION = Less is a free, open-source file pager
define BLURB
  Less is a free, open-source file pager. It can be found on most
  versions of Linux, Unix and Mac OS, as well as on many other operating systems.
endef

MASTER_SITES = http://www.greenwoodsoftware.com/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWncurses CSWggettextrt

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk
