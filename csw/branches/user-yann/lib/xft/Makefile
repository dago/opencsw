GARNAME = xft
GARVERSION = 2.1.2
CATEGORIES = lib

SPKG_PKGNAME = CSWlibxft2
SPKG_BITNAME = libxft2

DESCRIPTION = X FreeType library.
define BLURB
  Part of the FreeDesktop.org project.
endef

MASTER_SITES = http://pdx.freedesktop.org/~xlibs/release/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LIBDEPS += lib/xrender
LIBDEPS += lib/freetype
LIBDEPS += lib/fontconfig

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
