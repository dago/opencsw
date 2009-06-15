GARNAME = libXft
GARVERSION = 2.1.13
CATEGORIES = x11

DESCRIPTION = X11 authorisation library
define BLURB
  Xft provides a client-side font API for X applications, making the
  FreeType font rasterizer available to X clients. Fontconfig is used
  for font specification resolution. Where available, the RENDER
  extension handles glyph drawing; otherwise, the core X protocol is used.
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibxft2 CSWlibxft2devel

CATALOGNAME_CSWlibxft2 = libxft2
CATALOGNAME_CSWlibxft2devel = libxft2_devel

REQUIRED_PKGS_CSWlibxft2 = CSWfconfig CSWftype2 CSWlibx11 CSWlibxrender
REQUIRED_PKGS_CSWlibxft2devel = CSWlibxft2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxft2devel = $(PKGFILES_DEVEL)

include gar/category.mk

