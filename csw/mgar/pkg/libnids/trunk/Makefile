GARNAME = libnids
GARVERSION = 1.23
CATEGORIES = net

DESCRIPTION = implementation of an e-component of network intrusion detection
define BLURB
  Long description
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://libnids.sourceforge.net/

REQUIRED_PKGS += CSWggettextrt CSWglib2 CSWlibnet CSWlibpcap

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=92215
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

#GARCOMPILER = GCC3

PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

TEST_TARGET = 

include gar/category.mk
