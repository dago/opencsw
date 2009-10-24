GARNAME = libXcomposite
GARVERSION = 0.4.0
CATEGORIES = x11

DESCRIPTION = X11 Composite extension library
define BLURB
  libXcomposite provides an X Window System client interface to the Composite extension to the X protocol.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxcomposite CSWlibxcompositedevel

CATALOGNAME_CSWlibxcomposite = libxcomposite
CATALOGNAME_CSWlibxcompositedevel = libxcomposite_devel

SPKG_DESC_CSWlibxcomposite = $(DESCRIPTION)
SPKG_DESC_CSWlibxcompositedevel = $(DESCRIPTION) development files

# PREREQUISITE_PKGS = CSWcompositeproto
REQUIRED_PKGS_CSWlibxcompositedevel = CSWlibxcomposite
REQUIRED_PKGS_CSWlibxcomposite      = CSWlibx11 CSWlibxext CSWlibxfixes

PKGFILES_CSWlibxcompositedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk

