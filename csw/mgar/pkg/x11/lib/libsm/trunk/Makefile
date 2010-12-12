NAME = libsm
VERSION = 1.1.1
CATEGORIES = x11

DESCRIPTION = X11 Session Management library
define BLURB
  This package provides the main interface to the X11 Session Management
  library, which allows for applications to both manage sessions, and make
  use of session managers to save and restore their state for later use.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libSM-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS_CSWlibsm       = CSWlibice
RUNTIME_DEP_PKGS_CSWlibsmdevel += CSWlibsm

PACKAGES = CSWlibsm CSWlibsmdevel

CATALOGNAME_CSWlibsm = libsm
CATALOGNAME_CSWlibsmdevel = libsm_devel

SPKG_DESC_CSWlibsm = X11 Session Management library
SPKG_DESC_CSWlibsmdevel = X11 Session Management library development files

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibsmdevel = $(PKGFILES_DEVEL)

include gar/category.mk
