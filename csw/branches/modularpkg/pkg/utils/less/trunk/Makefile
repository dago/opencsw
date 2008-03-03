GARNAME = less
GARVERSION = 418
CATEGORIES = utils

DESCRIPTION = Less is a free, open-source file pager
define BLURB
  Less is a free, open-source file pager. It can be found on most
  versions of Linux, Unix and Mac OS, as well as on many other operating systems.
endef

MASTER_SITES = http://www.greenwoodsoftware.com/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWless,depend)

PREREQUISITE_PKGS = CSWncurses CSWggettext

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk
