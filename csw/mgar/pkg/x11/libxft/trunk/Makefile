GARNAME = libXft
GARVERSION = 2.1.13
CATEGORIES = x11

DESCRIPTION = X11 authorisation library
define BLURB
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibxft2

REQUIRED_PKGS = CSWfconfig CSWftype2 CSWlibx11 CSWlibxrender

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

