GARNAME = libXres
GARVERSION = 1.0.3
CATEGORIES = x11

DESCRIPTION = X11 Resource extension library
define BLURB
  libXRes provides an X Window System client interface to the Resource extension to the X protocol.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxres CSWlibxresdevel

CATALOGNAME_CSWlibxres = libxres
CATALOGNAME_CSWlibxresdevel = libxres_devel

SPKG_DESC_CSWlibxres = $(DESCRIPTION)
SPKG_DESC_CSWlibxresdevel = $(DESCRIPTION) development files

REQUIRED_PKGS_CSWlibxres      = CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibxresdevel = CSWlibxres

PKGFILES_CSWlibxresdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
