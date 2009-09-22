GARNAME = libICE
GARVERSION = 1.0.6
CATEGORIES = x11

DESCRIPTION = X11 Inter-Client Exchange Library
define BLURB
  X Inter-Client Exchange (ICE) protocol library
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibice CSWlibicedevel

CATALOGNAME_CSWlibice = libice
CATALOGNAME_CSWlibicedevel = libice_devel

SPKG_DESC_CSWlibice = X11 Inter-Client Exchange library
SPKG_DESC_CSWlibicedevel = X11 Inter-Client Exchange library development files

REQUIRED_PKGS_CSWlibicedevel = CSWlibice

PKGFILES_CSWlibicedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
