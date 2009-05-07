GARNAME = openjpeg
GARVERSION = 1.3
CATEGORIES = lib

DESCRIPTION = Open-source JPEG 2000 codec written in C
define BLURB
endef

MASTER_SITES = http://www.openjpeg.org/
DISTFILES  = $(GARNAME)_v1_3.tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1
NORUNPATH = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
