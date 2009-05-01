GARNAME = libX11
GARVERSION = 1.2
CATEGORIES = x11

DESCRIPTION = X11 client-side library
define BLURB
  This package provides a client interface to the X Window System,
  otherwise known as 'Xlib'. It provides a complete API for the basic
  functions of the window system. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUSITE_PKGS = CSWxextproto CSWxtrans CSWkbproto CSWinputproto

PACKAGES = CSWlibx11 CSWlibx11devel

SPKG_DESC_CSWlibx11 = $(DESCRIPTION)
SPKG_DESC_CSWlibx11devel = $(DESCRIPTION) development package

CATALOGNAME_CSWlibx11 = libx11
CATALOGNAME_CSWlibx11devel = libx11_devel

PKGFILES_CSWlibx11devel  = $(PKGFILES_DEVEL)

REQUIRED_PKGS_CSWlibx11      = CSWlibxcb
REQUIRED_PKGS_CSWlibx11devel = CSWlibx11

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

