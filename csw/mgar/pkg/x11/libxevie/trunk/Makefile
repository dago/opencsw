GARNAME = libXevie
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 EvIE extension library
define BLURB
  libXevie provides an X Window System client interface to the EvIE extension to the X protocol. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxevie CSWlibxeviedevel

CATALOGNAME_CSWlibxevie = libxevie
CATALOGNAME_CSWlibxeviedevel = libxevie_devel

SPKG_DESC_CSWlibxevie = $(DESCRIPTION)
SPKG_DESC_CSWlibxeviedevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWevieext

REQUIRED_PKGS_CSWlibxeviedevel = CSWlibxevie
REQUIRED_PKGS_CSWlibxevie      = CSWlibx11 CSWlibxext

PKGFILES_CSWlibxeviedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
