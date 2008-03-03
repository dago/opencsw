GARNAME = xrender
GARVERSION = 0.8.3
CATEGORIES = lib

DESCRIPTION = X Render extension library
define BLURB
  Part of the FreeDesktop.org project.
endef

# XXX: Obsolete
#MASTER_SITES = http://pdx.freedesktop.org/~xlibs/release/
#DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

LIBDEPS += lib/render

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
