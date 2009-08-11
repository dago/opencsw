GARNAME = Cairo
GARVERSION = 1.061
CATEGORIES = cpan
AUTHOR = TSCH

DESCRIPTION = Perl interface to the cairo library
define BLURB
endef

# 3/73 skipped: Test::Number::Delta not available
# all skipped: need Cairo with FreeType support and Font::FreeType
PREREQUISITE_PKGS = CSWlibcairodevel
REQUIRED_PKGS = CSWfconfig CSWftype2 CSWlibcairo CSWzlib

PACKAGES = CSWpmcairo
CATALOGNAME = pm_cairo

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

include gar/category.mk





