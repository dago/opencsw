GARNAME = libxdmcp
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 display manager control protocol library
define BLURB
  This package provides the main interface to the X11 display manager control
  protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXdmcp-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxdmcp CSWlibxdmcpdevel
CATALOGNAME_CSWlibxdmcp = libxdmcp
CATALOGNAME_CSWlibxdmcpdevel = libxdmcp_devel

SPKG_DESC_CSWlibxdmcp = X11 display manager control protocol library
SPKG_DESC_CSWlibxdmcpdevel = X11 display manager control protocol library development package

REQUIRED_PKGS_CSWlibxdmcpdevel = CSWlibxdmcp

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)

PKGFILES_CSWlibxdmcpdevel  = $(PKGFILES_DEVEL)

include gar/category.mk
