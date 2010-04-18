GARNAME = quilt
GARVERSION = 0.48
CATEGORIES = utils

DESCRIPTION = A patch management tooln
define BLURB
Quilt allows you to easily manage large numbers of patches by keeping
track of the changes each patch makes. Patches can be applied,
un-applied, refreshed, and more.

Quilt originally was based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/.
endef

MASTER_SITES = http://mirror.csclub.uwaterloo.ca/nongnu/quilt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
