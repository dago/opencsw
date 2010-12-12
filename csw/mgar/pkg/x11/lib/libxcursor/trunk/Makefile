NAME = libXcursor
VERSION = 1.1.10
CATEGORIES = x11

DESCRIPTION = X client-side cursor loading library
define BLURB
  Xcursor is a simple library designed to help locate and load cursors for the X Window System.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxcursor CSWlibxcursordevel

CATALOGNAME_CSWlibxcursor = libxcursor
CATALOGNAME_CSWlibxcursordevel = libxcursor_devel

SPKG_DESC_CSWlibxcursor = $(DESCRIPTION)
SPKG_DESC_CSWlibxcursordevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWlibxcursordevel = CSWlibxcursor
RUNTIME_DEP_PKGS_CSWlibxcursor      = CSWlibx11 CSWlibxcomposite CSWlibxfixes CSWlibxrender

PKGFILES_CSWlibxcursordevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
