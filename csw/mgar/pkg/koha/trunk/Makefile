GARNAME = koha
GARVERSION = 3.00.06
CATEGORIES = apps

DESCRIPTION = Integrated Library System
define BLURB
  Integrated Library System
endef

MASTER_SITES = http://downloads.ptfsinc.com/harley/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
