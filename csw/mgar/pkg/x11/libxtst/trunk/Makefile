GARNAME = libxtst
GARVERSION = 1.0.99.2
CATEGORIES = x11

DESCRIPTION = 
define BLURB
  Long description
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXtst-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
