GARNAME = SilverCity
GARVERSION = 0.9.7
CATEGORIES = utils

DESCRIPTION = Lexical analysis package for Python
define BLURB
	SilverCity is a lexing package, based on Scintilla, that can provide lexical
	analysis for over 20 programming and markup langauges.
endef

MASTER_SITES = $(SF_MIRROR)/silvercity/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsilvercity,depend prototype copyright)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

GARCOMPILER = SUN

include gar/category.mk

# When you pass a C++ source file to gcc, it invokes g++ for you
# without complaints.  However, passing a C++ source file to cc just
# results in an error.  So we fool python into using CC instead.
CC = $(CXX)
CFLAGS = $(CXXFLAGS)
