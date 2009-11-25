GARNAME = libmikmod
GARVERSION = 3.1.11
CATEGORIES = lib

DESCRIPTION = library for MOD audio files and other types
define BLURB
  Long description
endef

MASTER_SITES = http://mikmod.raphnet.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
