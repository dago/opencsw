GARNAME = SilverCity
GARVERSION = 0.9.7
CATEGORIES = utils

DESCRIPTION = Lexical analysis package for Python
define BLURB
	SilverCity is a lexing package, based on Scintilla, that can provide lexical
	analysis for over 20 programming and markup langauges.
endef

SF_PROJ = $(call TOLOWER,$(GARNAME))
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PACKAGES = CSWsilvercity

REQUIRED_PKGS_CSWsilvercity = CSWpython
CATALOGNAME_CSWsilvercity = silvercity
SPKG_DESC_CSWsilvercity = Lexical analysis package for Python

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

NOISALIST = 1
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
