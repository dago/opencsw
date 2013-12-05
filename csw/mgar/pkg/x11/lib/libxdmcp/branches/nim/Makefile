NAME = libxdmcp
VERSION = 1.0.3
CATEGORIES = x11
GARTYPE = bts


DESCRIPTION = X11 display manager control protocol library
define BLURB
  This package provides the main interface to the X11 display manager control
  protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXdmcp-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = NIMOSSlibxdmcp NIMOSSlibxdmcpdevel
CATALOGNAME_NIMOSSibxdmcp = libxdmcp
CATALOGNAME_NIMOSSlibxdmcpdevel = libxdmcp_devel

SPKG_DESC_NIMOSSlibxdmcp = X11 display manager control protocol library
SPKG_DESC_NIMOSSlibxdmcpdevel = X11 display manager control protocol library development package

RUNTIME_DEP_PKGS_NIMOSSlibxdmcpdevel = NIMOSSlibxdmcp

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)

PKGFILES_NIMOSSlibxdmcpdevel  = $(PKGFILES_DEVEL)

include gar/category.mk
