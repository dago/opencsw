GARNAME = swftools
GARVERSION = 0.8.1
CATEGORIES = lib

DESCRIPTION = SWF manipulation and generation utilities
define BLURB
  SWF manipulation and generation utilities
endef

MASTER_SITES = http://www.swftools.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWswftools,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER = GCC3

include gar/category.mk
