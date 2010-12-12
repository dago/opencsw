NAME = libXcomposite
VERSION = 0.4.1
CATEGORIES = x11

DESCRIPTION = X11 Composite extension library
define BLURB
  libXcomposite provides an X Window System client interface to the Composite extension to the X protocol.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxcomposite CSWlibxcompositedev

CATALOGNAME_CSWlibxcomposite = libxcomposite
CATALOGNAME_CSWlibxcompositedev = libxcomposite_devel

SPKG_DESC_CSWlibxcomposite = $(DESCRIPTION)
SPKG_DESC_CSWlibxcompositedev = $(DESCRIPTION) development files

# BUILD_DEP_PKGS = CSWcompositeproto
RUNTIME_DEP_PKGS_CSWlibxcompositedev = CSWlibxcomposite
RUNTIME_DEP_PKGS_CSWlibxcomposite    = CSWlibx11 CSWlibxext CSWlibxfixes

PKGFILES_CSWlibxcompositedev  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk

