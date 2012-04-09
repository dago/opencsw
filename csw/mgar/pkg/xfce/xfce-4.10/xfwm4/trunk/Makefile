# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfwm4
VERSION = 4.9.0
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Window Manager
define BLURB
  Xfce Window Manager
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --enable-xsync --enable-render --enable-randr --enable-xinerama --enable-compositor

# Catalog description
PACKAGES = CSWxfwm4 

# Package description
SPKG_DESC_CSWxfwm4       = $(DESCRIPTION)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)
