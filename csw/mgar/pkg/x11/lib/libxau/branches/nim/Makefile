NAME = libxau
VERSION = 1.0.4
CATEGORIES = x11
GARTYPE = bts

DESCRIPTION = X11 authorisation library
define BLURB
  This package provides the main interface to the X11 authorisation handling,
  which controls authorisation for X connections, both client-side and server-side. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXau-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# BUILD_DEP_PKGS = NIMOSSinputproto NIMOSSxkbproto NIMOSSxrenderproto NIMOSSxcbproto
# BUILD_DEP_PKGS += NIMOSSxextproto NIMOSSx11xproto NIMOSSxtrans NIMOSSlibpthreadstubs

PACKAGES = NIMOSSlibxau NIMOSSlibxaudevel

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_NIMOSSlibxau = NIMOSSx11common NIMOSSx11xproto
RUNTIME_DEP_PKGS_NIMOSSlibxaudevel = NIMOSSlibxau 

CATALOGNAME_NIMOSSlibxau = libxau
CATALOGNAME_NIMOSSlibxaudevel = libxau_devel

SPKG_DESC_NIMOSSlibxau = X11 authorisation library
SPKG_DESC_NIMOSSlibxaudevel = X11 authorisation library development package

PKGFILES_NIMOSSlibxaudevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

