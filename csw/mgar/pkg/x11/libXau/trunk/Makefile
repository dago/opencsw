GARNAME = libXau
GARVERSION = 1.0.4
CATEGORIES = x11

DESCRIPTION = X11 authorisation library
define BLURB
  This package provides the main interface to the X11 authorisation handling,
  which controls authorisation for X connections, both client-side and server-side. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS = CSWinputproto CSWkbproto CSWrenderproto CSWxcbproto
PREREQUISITE_PKGS += CSWxextproto CSWxproto CSWxtrans CSWlibpthreadstubs

PACKAGES = CSWlibxau CSWlibxaudevel

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS_CSWlibxau = CSWx11common
REQUIRED_PKGS_CSWlibxaudevel = CSWlibxau

CATALOGNAME_CSWlibxau = libxau
CATALOGNAME_CSWlibxaudevel = libxau_devel

SPKG_DESC_CSWlibxau = X11 authorisation library
SPKG_DESC_CSWlibxaudevel = X11 authorisation library development package

PKGFILES_CSWlibxaudevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

