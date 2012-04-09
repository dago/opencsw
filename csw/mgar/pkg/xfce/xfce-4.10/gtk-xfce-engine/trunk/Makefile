# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtk-xfce-engine
VERSION = 2.99.2
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION =  Xfce GTK theme engine 
define BLURB
   Xfce GTK theme engine 
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Catalog description
PACKAGES = CSWgtkxfceengine 

# Package description
SPKG_DESC_CSWgtkxfceengine       = $(DESCRIPTION)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)


