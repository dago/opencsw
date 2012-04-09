# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfdesktop
VERSION = 4.9.2
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION =  Xfce Desktop Manager
define BLURB
   Xfce Desktop Manager
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

CONFIGURE_ARGS +=   --enable-desktop-icons 
CONFIGURE_ARGS +=   --enable-file-icons
CONFIGURE_ARGS +=   --enable-thunarx 
CONFIGURE_ARGS +=   --enable-exo
CONFIGURE_ARGS +=   --enable-menueditor 
CONFIGURE_ARGS +=   --enable-desktop-menu
CONFIGURE_ARGS +=   --enable-panel-plugin

CONFIGURE_ARGS = $(DIRPATHS)

# Catalog description
PACKAGES = CSWxfdesktop

# Package description
SPKG_DESC_CSWxfdesktop       = $(DESCRIPTION)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)

