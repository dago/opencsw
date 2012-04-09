# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce4-dev-tools
VERSION = 4.9.1
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Development Tools
define BLURB
  Xfce Development Tools
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

# Catalog description
PACKAGES = CSWxfcedevtools

# Package description
SPKG_DESC_CSWxfcedevtools       = $(DESCRIPTION)

include gar/category.mk
