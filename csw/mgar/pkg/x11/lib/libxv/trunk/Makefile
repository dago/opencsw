GARNAME = libxv
GARVERSION = 1.0.4
CATEGORIES = x11

DESCRIPTION = The Xv Library
define BLURB
  The Xv Library
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXv-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# PREREQUISITE_PKGS = CSWxvideoproto

PACKAGES = CSWlibxv CSWlibxvdevel

CATALOGNAME_CSWlibxv = libxv
CATALOGNAME_CSWlibxvdevel = libxv_devel

SPKG_DESC_CSWlibxv = The Xv Library
SPKG_DESC_CSWlibxvdevel = The Xv Library development files

REQUIRED_PKGS_CSWlibxv = CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibxvdevel = CSWlibxv

PKGFILES_CSWlibxvdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
