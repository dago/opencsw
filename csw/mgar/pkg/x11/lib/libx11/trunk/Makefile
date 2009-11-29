GARNAME = libx11
GARVERSION = 1.3.2
CATEGORIES = x11

DESCRIPTION = X11 client-side library
define BLURB
  This package provides a client interface to the X Window System,
  otherwise known as 'Xlib'. It provides a complete API for the basic
  functions of the window system. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libX11-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = patch-stdint.diff
# Add workaround for http://bugs.sourcemage.org/show_bug.cgi?id=13476
PATCHFILES += patch-xlib-sentinel.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS =  CSWx11xextproto CSWxtrans CSWx11inputproto CSWlibpthreadstubs CSWlibxcbdevel

PACKAGES = CSWlibx11 CSWlibx11devel

SPKG_DESC_CSWlibx11 = $(DESCRIPTION)
SPKG_DESC_CSWlibx11devel = $(DESCRIPTION) development package

CATALOGNAME_CSWlibx11 = libx11
CATALOGNAME_CSWlibx11devel = libx11_devel

PKGFILES_CSWlibx11devel  = $(PKGFILES_DEVEL)

REQUIRED_PKGS_CSWlibx11      = CSWx11common CSWlibxcb
REQUIRED_PKGS_CSWlibx11devel = CSWlibx11

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_CFLAGS = -D__solaris__

include gar/category.mk

