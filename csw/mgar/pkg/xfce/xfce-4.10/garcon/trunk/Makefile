# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = garcon
VERSION = 0.1.11
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce's freedesktop.org specification compatible menu implementation library
define BLURB
  Xfce's freedesktop.org specification compatible menu implementation library
endef

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Catalog description
PACKAGES = CSWgarcon CSWgarcon-dev CSWgarcon-doc

# Package description
SPKG_DESC_CSWgarcon       = $(DESCRIPTION)
SPKG_DESC_CSWgarcon-dev   = $(DESCRIPTION) development package
SPKG_DESC_CSWgarcon-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWgarcon-doc   = 1
ARCHALL_CSWgarcon-dev   = 1

# Dynamic prototype
PKGFILES_CSWgarcon-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWgarcon-dev += /opt/csw/include/xfce4/garcon/.*
PKGFILES_CSWgarcon-doc  = /opt/csw/share/gtk-doc/.*

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)

