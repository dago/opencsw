# $Id$
GARNAME = ccache
GARVERSION = 3.0pre1
CATEGORIES = utils

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://samba.org/ftp/ccache/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
SPKG_VERSION = $(subst p,,$(GARVERSION))

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_CFLAGS = -D__EXTENSIONS__

# Unset $PWD (which isn't changed on gmake -C) so that test.sh uses `pwd`
PWD=
TEST_EXPORTS=PWD

include gar/category.mk
