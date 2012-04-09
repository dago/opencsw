# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Thunar
VERSION = 1.3.1
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Thunar File Manager
define BLURB
  Xfce Thunar File Manager
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x --enable-dbus --with-volume-manager=auto

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# Catalog description
PACKAGES = CSWthunar CSWthunar-doc

# Package description
SPKG_DESC_CSWthunar       = $(DESCRIPTION)
SPKG_DESC_CSWthunar-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWthunar-doc     = 1
PKGFILES_CSWthunar-doc    = /opt/csw/share/gtk-doc/.*

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)
