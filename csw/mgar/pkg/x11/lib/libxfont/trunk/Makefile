NAME = libXfont
VERSION = 1.4.1
CATEGORIES = x11

DESCRIPTION = X11 font rasterisation library
define BLURB
  libXfont provides various services for X servers, most notably font selection and rasterisation (through external libraries). 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxfont CSWlibxfontdevel

CATALOGNAME_CSWlibxfont = libxfont
CATALOGNAME_CSWlibxfontdevel = libxfont_devel

SPKG_DESC_CSWlibxfont = $(DESCRIPTION)
SPKG_DESC_CSWlibxfontdevel = $(DESCRIPTION) development files

PATCHFILES = pcfread.c.diff

#
# BUILD_DEP_PKGS = CSWlibfontencdevel
RUNTIME_DEP_PKGS_CSWlibxfontdevel = CSWlibxfont
RUNTIME_DEP_PKGS_CSWlibxfont = CSWftype2 CSWlibfontenc CSWzlib

PKGFILES_CSWlibxfontdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

EXTRA_CFLAGS = -D__solaris__

include gar/category.mk
