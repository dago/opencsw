GARNAME = cswcommon
GARVERSION = 1.4.6
CATEGORIES = utils

DESCRIPTION = Installs some useful standard CSW filesystem symlinks and files
define BLURB
endef

#MASTER_SITES = http://mirror.opencsw.org/opencsw/current/$(shell uname -p)/5.8
MASTER_SITES = http://mirror.opencsw.org/opencsw/current/sparc/5.8/
DISTFILES  = common-1.4.6,REV=2008.04.28-SunOS5.8-sparc-CSW.pkg

PACKAGES = common

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
