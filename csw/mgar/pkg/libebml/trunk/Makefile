GARNAME = libebml
GARVERSION = 0.7.8
CATEGORIES = lib

DESCRIPTION = Library for Extensible Binary Meta Language
define BLURB
endef

MASTER_SITES = http://dl.matroska.org/downloads/libebml/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
PATCHFILES = libebml-shared-library.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.matroska.org/

BUILD64 = 1
NOISALIST = 1

CONFIGURE_SCRIPTS = 

# Needed for shared library
EXTRA_CFLAGS = -xcode=pic32
EXTRA_CXXFLAGS = -xcode=pic32

WARNINGFLAGS =
BUILD_OVERRIDE_DIRS = CC CXX LD CFLAGS WARNINGFLAGS
BUILD_SCRIPTS = $(WORKSRC)/make/linux/Makefile

TEST_SCRIPTS = 

INSTALL_OVERRIDE_VARS = CC CXX LD CFLAGS WARNINGFLAGS INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall
INSTALL_OVERRIDE_DIRS = prefix libdir includedir
INSTALL_SCRIPTS = $(WORKSRC)/make/linux/Makefile

include gar/category.mk
