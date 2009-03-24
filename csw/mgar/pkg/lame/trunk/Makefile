GARNAME = lame
GARVERSION = 398-2
SPKG_VERSION = 3.98.2
CATEGORIES = apps

DESCRIPTION = LAME is an LGPL MP3 encoder
define BLURB
  LAME is a high quality MPEG Audio Layer III (MP3) encoder licensed under the LGPL.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=628063
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
