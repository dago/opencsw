GARNAME = xcursor
GARVERSION = 1.0.2
CATEGORIES = lib

SPKG_PKGNAME = CSWxcursor
SPKG_BITNAME = xcursor

DESCRIPTION = Client-side cursor loading library
define BLURB
  Part of the FreeDesktop.org project.
endef

MASTER_SITES = http://pdx.freedesktop.org/~xlibs/release/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LIBDEPS += lib/xrender

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
