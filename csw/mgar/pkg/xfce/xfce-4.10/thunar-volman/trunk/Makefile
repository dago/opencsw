# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = thunar-volman
VERSION = 0.7.0
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Thunar Volume Manager
define BLURB
  The Thunar Volume Manager is an extension for the Thunar file manager, which enables automatic management of removable drives and media. For example, if thunar-volman is installed and configured properly, and you plug in your digital camera, it will automatically launch your preferred photo application and import the new pictures from the camera into your photo collection. 
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS  = $(DIRPATHS)

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# Catalog description
PACKAGES = CSWthunarvolman CSWthunarvolman-doc

# Package description
SPKG_DESC_CSWthunarvolman       = $(DESCRIPTION)
SPKG_DESC_CSWthunarvolman-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWthunarvolman-doc     = 1
PKGFILES_CSWthunarvolman-doc    = /opt/csw/share/gtk-doc/.*

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)
