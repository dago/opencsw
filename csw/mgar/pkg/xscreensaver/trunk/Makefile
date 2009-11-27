GARNAME = xscreensaver
GARVERSION = 5.10
CATEGORIES = utils

DESCRIPTION = The ultimate screensaver collection
define BLURB
  A collection of free screen savers for X11 and MacOS.
endef

MASTER_SITES = http://www.jwz.org/xscreensaver/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWxsave
CATALOGNAME = xscreensaver

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
