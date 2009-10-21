GARNAME = libxi
GARVERSION = 1.1.3
CATEGORIES = x11

DESCRIPTION = Client library for XInput
define BLURB
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXi-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#PREREQUISITE_PKGS = CSWlibxpmdevel

PACKAGES = CSWlibxi CSWlibxidevel

CATALOGNAME_CSWlibxi = libxi
CATALOGNAME_CSWlibxidevel = libxi_devel

SPKG_DESC_CSWlibxi = Client library for XInput
SPKG_DESC_CSWlibxi = Client library for XInput development files

#REQUIRED_PKGS_CSWlibxi = 
REQUIRED_PKGS_CSWlibxidevel = CSWlibxi

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxidevel = $(PKGFILES_DEVEL)

include gar/category.mk
