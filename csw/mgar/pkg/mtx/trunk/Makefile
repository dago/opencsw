GARNAME = mtx
GARVERSION = 1.3.12
CATEGORIES = utils

DESCRIPTION = Control tape autoloaders
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://mtx.opensource-sw.net/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
