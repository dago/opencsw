NAME = less
VERSION = 436
CATEGORIES = utils

DESCRIPTION = Less is a free, open-source file pager
define BLURB
  Less is a free, open-source file pager. It can be found on most
  versions of Linux, Unix and Mac OS, as well as on many other operating systems.
endef

MASTER_SITES = http://www.greenwoodsoftware.com/$(NAME)/
DISTFILES = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWncurses CSWggettextrt

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk
