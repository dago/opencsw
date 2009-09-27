GARNAME = libXTrap
GARVERSION = 1.0.0
CATEGORIES = x11

DESCRIPTION = X11 event trapping extension library
define BLURB
  libXTrap provides an interface to the DEC-XTRAP extension, which allows for capture and synthesis of core input events.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxtrap CSWlibxtrapdevel

CATALOGNAME_CSWlibxtrap = libxtrap
CATALOGNAME_CSWlibxtrapdevel = libxtrap_devel

SPKG_DESC_CSWlibxtrap = $(DESCRIPTION)
SPKG_DESC_CSWlibxtrapdevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWtrapproto CSWlibxtdevel CSWlibsmdevel CSWlibicedevel
REQUIRED_PKGS_CSWlibxtrap      = CSWlibice CSWlibx11 CSWlibxext CSWlibxt
REQUIRED_PKGS_CSWlibxtrapdevel = CSWlibxtrap

PKGFILES_CSWlibxtrapdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
