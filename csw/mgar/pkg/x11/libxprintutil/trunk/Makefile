GARNAME = libXprintUtil
GARVERSION = 1.0.1
CATEGORIES = x11

DESCRIPTION = The XprintUtil Library
define BLURB
  libxprintutil provides utility Xpu APIs allowing client applications to access and manipulate information about printer capabilities from an Xprint server. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxprintutil CSWlibxprintutildevel

CATALOGNAME_CSWlibxprintutil = libxprintutil
CATALOGNAME_CSWlibxprintutildevel = libxprintutil_devel

SPKG_DESC_CSWlibxprintutil = $(DESCRIPTION)
SPKG_DESC_CSWlibxprintutildevel = $(DESCRIPTION) development files


PREREQUISITE_PKGS = CSWlibxpdevel CSWlibicedevel
REQUIRED_PKGS_CSWlibxprintutil = CSWlibice CSWlibx11 CSWlibxau CSWlibxp CSWlibxt
REQUIRED_PKGS_CSWlibxprintutildevel = CSWlibxprintutil

PKGFILES_CSWlibxprintutildevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
