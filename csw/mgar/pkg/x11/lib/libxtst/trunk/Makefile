NAME = libxtst
VERSION = 1.1.0
CATEGORIES = x11

DESCRIPTION = The Xtst Library
define BLURB
  The Xtst Library
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXtst-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxtst CSWlibxtstdevel

CATALOGNAME_CSWlibxtst = libxtst
CATALOGNAME_CSWlibxtstdevel = libxtst_devel

SPKG_DESC_CSWlibxtst = The Xtst Library
SPKG_DESC_CSWlibxtstdevel = The Xtst Library development files

RUNTIME_DEP_PKGS_CSWlibxtstdevel = CSWlibxtst
RUNTIME_DEP_PKGS_CSWlibxtst += CSWlibx11
RUNTIME_DEP_PKGS_CSWlibxtst += CSWlibxext
RUNTIME_DEP_PKGS_CSWlibxtst += CSWlibxi

BUILD_DEP_PKGS_CSWlibxtst += CSWlibxi
BUILD_DEP_PKGS_CSWlibxtst += CSWlibxidevel

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxtstdevel = $(PKGFILES_DEVEL)

include gar/category.mk
