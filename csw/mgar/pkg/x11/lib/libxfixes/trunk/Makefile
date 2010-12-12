NAME = libXfixes
VERSION = 4.0.4
CATEGORIES = x11

DESCRIPTION = X11 miscellaneous 'fixes' extension library
define BLURB
  libXfixes provides an X Window System client interface to the 'XFIXES' extension to the X protocol.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxfixes CSWlibxfixesdevel

CATALOGNAME_CSWlibxfixes = libxfixes
CATALOGNAME_CSWlibxfixesdevel = libxfixes_devel

SPKG_DESC_CSWlibxfixes = $(DESCRIPTION)
SPKG_DESC_CSWlibxfixesdevel = $(DESCRIPTION) development files

# BUILD_DEP_PKGS = CSWfixesproto

RUNTIME_DEP_PKGS_CSWlibxfixes      = CSWlibx11
RUNTIME_DEP_PKGS_CSWlibxfixesdevel = CSWlibxfixes

PKGFILES_CSWlibxfixesdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
