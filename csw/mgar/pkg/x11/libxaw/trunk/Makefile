GARNAME = libxaw
GARVERSION = 1.0.6
CATEGORIES = x11

DESCRIPTION = X Athena Widgets
define BLURB
  Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXaw-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# xproto x11 xext xextproto xt xmu xpm
PREREQUISITE_PKGS = CSWlibxpmdevel

PACKAGES = CSWlibxaw CSWlibxawdevel

CATALOGNAME_CSWlibxaw = libxaw
CATALOGNAME_CSWlibxawdevel = libxaw_devel

SPKG_DESC_CSWlibxaw = X Athena Widgets
SPKG_DESC_CSWlibxawdevel = X Athena Widgets development files

REQUIRED_PKGS_CSWlibxaw = CSWlibice CSWlibsm CSWlibx11 CSWlibxext CSWlibxmu CSWlibxt
REQUIRED_PKGS_CSWlibxawdevel = CSWlibxpm

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxawdevel = $(PKGFILES_DEVEL)

include gar/category.mk
