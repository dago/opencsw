# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce4-panel
VERSION = 4.9.1
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Panel
define BLURB
  Xfce Panel
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# Catalog description
PACKAGES = CSWxfce4panel

# Package description
SPKG_DESC_CSWxfce4panel       = $(DESCRIPTION)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)

