NAME = libXScrnSaver
VERSION = 1.2.0
CATEGORIES = x11

DESCRIPTION = The XScrnSaver Library
define BLURB
  libXScrnSaver provides an X Window System client interface to the MIT-SCREEN-SAVER extension to the X protocol. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxscrnsaver CSWlibxscrnsaverdev

CATALOGNAME_CSWlibxscrnsaver = libxscrnsaver
CATALOGNAME_CSWlibxscrnsaverdev = libxscrnsaver_devel

SPKG_DESC_CSWlibxscrnsaver = $(DESCRIPTION)
SPKG_DESC_CSWlibxscrnsaverdev = $(DESCRIPTION) development files

# BUILD_DEP_PKGS = CSWscrnsaverproto
RUNTIME_DEP_PKGS_CSWlibxscrnsaver      = CSWlibx11 CSWlibxext
RUNTIME_DEP_PKGS_CSWlibxscrnsaverdev = CSWlibxscrnsaver

PKGFILES_CSWlibxscrnsaverdev  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
