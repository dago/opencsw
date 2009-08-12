GARNAME = diffstat
GARVERSION = 1.48
CATEGORIES = utils

DESCRIPTION = A utility which provides statistics based on the output of diff
define BLURB
endef

MASTER_SITES = ftp://invisible-island.net/diffstat/
DISTFILES  = $(GARNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://invisible-island.net/diffstat/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-install-prefix=$(DESTDIR)

TEST_TARGET = check

include gar/category.mk
