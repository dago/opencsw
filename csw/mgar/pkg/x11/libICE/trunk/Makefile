GARNAME = libICE
GARVERSION = 1.0.6
CATEGORIES = x11

DESCRIPTION = X11 Inter-Client Exchange Library
define BLURB
  Long description
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibice CSWlibicedevel

CATALOGNAME_CSWlibice = libice
CATALOGNAME_CSWlibice = libice_devel

SPKG_DESC_CSWlibice = X11 Inter-Client Exchange library
SPKG_DESC_CSWlibicedevel = X11 Inter-Client Exchange library development files

PKGFILES_CSWlibicedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
