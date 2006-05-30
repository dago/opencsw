GARNAME = xft
GARVERSION = 2.1.2
CATEGORIES = lib

DESCRIPTION = X FreeType library.
define BLURB
  Part of the FreeDesktop.org project.
endef

# XXX: Obsolete
#MASTER_SITES = http://pdx.freedesktop.org/~xlibs/release/
#DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

DEPENDS += lib/libxrender
DEPENDS += lib/freetype
DEPENDS += lib/fontconfig

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
