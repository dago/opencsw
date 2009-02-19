GARNAME = ilmbase
GARVERSION = 1.0.1
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWilmbase,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES = ImathMath.patch

LDFLAGS += -lCstd -lCrun -lc -lm
export LDFLAGS

TEST_TARGET = check

include gar/category.mk
