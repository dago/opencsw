NAME = lensfun
VERSION = 0.2.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library to correct images based on intimate knowledge of lens characteristics
define BLURB
  The project provides a database of photographic lenses and a library that allows
  advanced access to the database including functions to correct images based on
  intimate knowledge of lens characteristics and calibration data.
endef

MASTER_SITES = $(BERLIOS_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWzlib CSWpng
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpython CSWdoxygen

PACKAGES = CSWliblensfun
CATALOGNAME = liblensfun

SPKG_SOURCEURL = http://developer.berlios.de/projects/lensfun/

LD=$(CC)
EXTRA_COMMON_EXPORTS = LD

BUILD64_LIBS_ONLY = 1
# This is not autoconf, but some hand-hacked Python thingie.
CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --includedir=$(includedir)
CONFIGURE_ARGS += --libexecdir=$(libexecdir)
CONFIGURE_ARGS += --docdir=$(docdir)
CONFIGURE_ARGS += --verbose
CONFIGURE_ARGS += --mode=release
# CONFIGURE_ARGS += --compiler=$(CC)
#    [ "CC",       None,  "Override the C compiler name/path" ],
#    [ "CXX",      None,  "Override the C++ compiler name/path" ],
#    [ "LD",       None,  "Override the linker name/path" ]
CONFIGURE_ARGS += --cflags="$(CFLAGS)"
CONFIGURE_ARGS += --cxxflags="$(CXXFLAGS)"
CONFIGURE_ARGS += --ldflags="$(LDFLAGS)"
CONFIGURE_ARGS += --target=posix
CONFIGURE_ARGS += --staticlibs=NO
# --libs=LIBS        Additional libraries to link with

BUILD_ARG = all

include gar/category.mk

# Make sure we have GNU make with name "make" before /usr/ccs/bin/make
PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	perl -pi -e "s,#!/usr/bin/python,#!/opt/csw/bin/python," $(WORKSRC)/configure
	@$(MAKECOOKIE)
