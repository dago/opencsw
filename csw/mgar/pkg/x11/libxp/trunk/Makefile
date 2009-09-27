GARNAME = libXp
GARVERSION = 1.0.0
CATEGORIES = x11

DESCRIPTION = X Print Library
define BLURB
  libXp provides public APIs to allow client applications to render to non-display devices. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxp CSWlibxpdevel

CATALOGNAME_CSWlibxp = libxp
CATALOGNAME_CSWlibxpdevel = libxp_devel

SPKG_DESC_CSWlibxp = $(DESCRIPTION)
SPKG_DESC_CSWlibxpdevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWdamageproto

REQUIRED_PKGS_CSWlibxp      = CSWlibx11 CSWlibxau CSWlibxext
REQUIRED_PKGS_CSWlibxpdevel = CSWlibxp

PKGFILES_CSWlibxpdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
