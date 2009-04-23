GARNAME = rcs
GARVERSION = 5.7
CATEGORIES = apps

DESCRIPTION = GNU Revision Control System
define BLURB
endef

MASTER_SITES = http://www.cs.purdue.edu/homes/trinkle/RCS/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.Z

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = --prefix=$(prefix)

include gar/category.mk
