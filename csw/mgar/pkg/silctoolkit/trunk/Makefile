GARNAME = silc-toolkit
GARVERSION = 1.1.8
CATEGORIES = lib
SPKG_SOURCEURL = http://silcnet.org/software/download/toolkit/

DESCRIPTION = secure internet live conferencing toolkit
define BLURB
  SILC Project develops the Secure Internet Live Conferencing protocol, which provides secure conferencing services. 
endef

MASTER_SITES = http://silcnet.org/download/toolkit/sources/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsilctoolkit,prototype)
PATCHFILES += function.patch

#No tests
TEST_SCRIPTS =

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
