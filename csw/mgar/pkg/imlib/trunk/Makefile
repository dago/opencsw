NAME = imlib
VERSION = 1.9.15
CATEGORIES = lib

DESCRIPTION = An advanced replacement library for libraries like libXpm
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# EXTRA_LINKER_FLAGS = -L$(libdir) -l/usr/openwin/lib/libXext.so

STRIP_LIBTOOL = 1

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))


RUNTIME_DEP_PKGS_CSWimlib  = CSWgiflib CSWjpeg CSWpng CSWtiff CSWzlib
RUNTIME_DEP_PKGS_CSWimlib += CSWlibice CSWlibsm CSWlibxext

# Building the test cases misses -lX11, disable for now
SKIPTEST ?= 1

TEST_TARGET = check

include gar/category.mk
