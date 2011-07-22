# $Id$
NAME = openldap
VERSION = 2.4.26
CATEGORIES = server

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
DISTFILES  = $(NAME)-$(VERSION).tgz
LICENSE = COPYRIGHT
PACKAGES = CSWopenldap24

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

EXTRA_LIB  = $(prefix)/bdb48/lib
EXTRA_INC  = $(prefix)/bdb48/include


RUNTIME_DEP_PKGS_CSWopenldap24   += CSWsasl CSWosslrt CSWlibnet CSWbdb48 CSWlibicu
# where does this come from????
CHECKPKG_OVERRIDES_CSWopenldap24 += missing-dependency|CSWoldaprt


CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
