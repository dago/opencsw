GARNAME = libxft2
GARVERSION = 2.1.13
CATEGORIES = lib

DESCRIPTION = FreeType-based font drawing library for X
define BLURB
  Xft provides a client-side font API for X applications, making the
  FreeType font rasterizer available to X clients. Fontconfig is used
  for font specification resolution. Where available, the RENDER
  extension handles glyph drawing; otherwise, the core X protocol is used.
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTNAME = libXft-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXft-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxft2 CSWlibxft2devel

REQUIRED_PKGS_CSWlibxft2 = CSWfconfig CSWftype2 CSWlibxrender CSWzlib CSWlibx11
REQUIRED_PKGS_CSWlibxft2devel = CSWlibxft2

EXTRA_CFLAGS   = -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
EXTRA_CXXFLAGS = -xlibmil -xlibmopt -features=tmplife -norunpath

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

GREP = ggrep

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

PKGFILES_CSWlibxft2devel = $(PKGFILES_DEVEL)

include gar/category.mk
