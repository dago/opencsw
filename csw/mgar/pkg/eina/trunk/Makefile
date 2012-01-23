NAME = eina
VERSION = 0.9.9.063
CATEGORIES = lib

DESCRIPTION = Provides optimized data types
define BLURB
endef

MASTER_SITES = http://download.enlightenment.org/snapshots/2009-12-02/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibeina
CATALOGNAME = libeina

VENDOR_URL = http://trac.enlightenment.org/e/wiki/Eina

EXTRA_CPPFLAGS = -D__FUNCTION__=

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
