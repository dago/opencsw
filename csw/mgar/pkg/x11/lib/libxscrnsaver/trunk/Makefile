GARNAME = libXScrnSaver
GARVERSION = 1.1.3
CATEGORIES = x11

DESCRIPTION = The XScrnSaver Library
define BLURB
  libXScrnSaver provides an X Window System client interface to the MIT-SCREEN-SAVER extension to the X protocol. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxscrnsaver CSWlibxscrnsaverdevel

CATALOGNAME_CSWlibxscrnsaver = libxscrnsaver
CATALOGNAME_CSWlibxscrnsaverdevel = libxscrnsaver_devel

SPKG_DESC_CSWlibxscrnsaver = $(DESCRIPTION)
SPKG_DESC_CSWlibxscrnsaverdevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWscrnsaverproto
REQUIRED_PKGS_CSWlibxscrnsaver      = CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibxscrnsaverdevel = CSWlibxscrnsaver

PKGFILES_CSWlibxscrnsaverdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
