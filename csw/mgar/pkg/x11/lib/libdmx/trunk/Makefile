NAME = libdmx
VERSION = 1.1.0
CATEGORIES = x11

DESCRIPTION = X11 Distributed Multihead extension library
define BLURB
  libdmx is an interface to the DMX extension for X, which allows a single server to be set up as a proxy spanning multiple servers -- not unlike Xinerama across discrete physical machines. It can be reconfigured on the fly to change the layout, and it is presented as a single logical display to clients. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibdmx CSWlibdmxdevel

CATALOGNAME_CSWlibdmx = libdmx
CATALOGNAME_CSWlibdmxdevel = libdmx_devel

SPKG_DESC_CSWlibdmx = $(DESCRIPTION)
SPKG_DESC_CSWlibdmxdevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWx11dmxproto

RUNTIME_DEP_PKGS_CSWlibdmx      =  CSWlibx11 CSWlibxext
RUNTIME_DEP_PKGS_CSWlibdmxdevel = CSWlibdmx

PKGFILES_CSWlibdmxdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
