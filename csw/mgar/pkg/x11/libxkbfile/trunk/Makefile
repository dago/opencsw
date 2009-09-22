GARNAME = libxkbfile
GARVERSION = 1.0.5
CATEGORIES = x11

DESCRIPTION = X11 keyboard file manipulation library
define BLURB
  Libxkbfile provides an interface to read and manipulate description
  files for XKB, the X11 keyboard configuration extension.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibxkbfile CSWlibxkbfiledevel

CATALOGNAME_CSWlibxkbfile = libxkfileb
CATALOGNAME_CSWlibxkbfiledevel = libxkbfile_devel

SPKG_DESC_CSWlibxkbfile = X11 keyboard file manipulation library
SPKG_DESC_CSWlibxkbfiledevel = X11 keyboard file manipulation library development files

REQUIRED_PKGS_CSWlibxkbfile = CSWlibx11
REQUIRED_PKGS_CSWlibxkbfiledevel = CSWlibxkbfile

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxkbfiledevel = $(PKGFILES_DEVEL)

include gar/category.mk
