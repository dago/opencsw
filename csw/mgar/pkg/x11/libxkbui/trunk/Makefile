NAME = libxkbui
VERSION = 1.0.2
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = X11 keyboard UI presentation library
define BLURB
  X11 keyboard UI presentation library
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISUITE_PKGS = CSWlibxkbfiledevel

PACKAGES = CSWlibxkbui CSWlibxkbui

CATALOGNAME_CSWlibxkbui = libxkbui
CATALOGNAME_CSWlibxkbuidevel = libxkbui_devel

SPKG_DESC_CSWlibxkbui = X11 keyboard UI presentation library
SPKG_DESC_CSWlibxkbuidevel = X11 keyboard UI presentation library development files

RUNTIME_DEP_PKGS_CSWlibxkbui = CSWlibice CSWlibsm CSWlibx11 CSWlibxkbfile CSWlibxt
RUNTIME_DEP_PKGS_CSWlibxkbuidevel = CSWlibxkbui

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxkbuidevel = $(PKGFILES_DEVEL)

include gar/category.mk
