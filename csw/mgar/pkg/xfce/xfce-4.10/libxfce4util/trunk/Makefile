# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libxfce4util
VERSION = 4.9.0
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce Utilities Library
define BLURB
  Xfce Utilities Library
endef

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD_DEP_PKGS  += CSWggettext

# Catalog description
PACKAGES = CSWlibxfce4util CSWlibxfce4util-dev CSWlibxfce4util-doc

# Package description
SPKG_DESC_CSWlibxfce4util       = $(DESCRIPTION)
SPKG_DESC_CSWlibxfce4util-dev   = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfce4util-doc   = $(DESCRIPTION) documentation package

ARCHALL_CSWlibxfce4util-doc   = 1
ARCHALL_CSWlibxfce4util-dev   = 1

# Dynamic prototype
PKGFILES_CSWlibxfce4util-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfce4util-dev += /opt/csw/include/xfce4/libxfce4util/.*
PKGFILES_CSWlibxfce4util-doc  = /opt/csw/share/gtk-doc/.*

# Defines dependencies
RUNTIME_DEP_PKGS_CSWlibxfce4util-doc =
RUNTIME_DEP_PKGS_CSWlibxfce4util-dev += CSWlibxfce4util
RUNTIME_DEP_PKGS_CSWlibxfce4util     += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibxfce4util     += CSWlibglib2-0-0

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWlibxfce4util-doc += file-with-bad-content|/usr/local|root/opt/csw/share/gtk-doc/html/libxfce4util/libxfce4util-Internationalisation.html
CHECKPKG_OVERRIDES_CSWlibxfce4util-dev += archall-devel-package

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)


