GARNAME = gconfeditor
GNOME_PROJ = gconf-editor
GARVERSION = 2.30.0
CATEGORIES = gnome

DESCRIPTION = GNOME configuration system editor
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GNOME_PROJ)-$(GARVERSION).tar.bz2
DISTNAME = $(GNOME_PROJ)-$(GARVERSION)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

#SPKG_SOURCEURL = http://projects.gnome.org/gconf/

BUILD64 = 1
NOISAEXEC = 1

TEST_TARGET = check

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))


include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
