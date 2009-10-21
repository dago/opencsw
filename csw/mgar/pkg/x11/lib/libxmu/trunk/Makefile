GARNAME = libxmu
GARVERSION = 1.0.4
CATEGORIES = x11

DESCRIPTION = A set of miscellaneous utility convenience functions for X libraries to use
define BLURB
  LibXmu provides a set of miscellaneous utility convenience functions for X libraries to use.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXmu-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWlibxtdevel CSWlibxextdevel

PACKAGES = CSWlibxmu CSWlibxmudevel

CATALOGNAME_CSWlibxmu = libxmu
CATALOGNAME_CSWlibxmudevel = libxmu_devel

SPKG_DESC_CSWlibxmu = X11 miscellaneous utility library
SPKG_DESC_CSWlibxmudevel = X11 miscellaneous utility library development files

REQUIRED_PKGS_CSWlibxmu = CSWlibice CSWlibsm CSWlibx11 CSWlibxext CSWlibxt
REQUIRED_PKGS_CSWlibxmudevel = CSWlibxmu

PKGFILES_CSWlibxmudevel = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
