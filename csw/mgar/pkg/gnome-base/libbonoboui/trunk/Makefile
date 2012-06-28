NAME = libbonoboui
VERSION = 2.24.5
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = UI code for the GNOME 2 Object Activation Framework
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTNAME = $(GNOME_PROJ)-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2

# New glib only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --enable-static=no
#CONFIGURE_ARGS += --enable-gtk-doc

EXTRA_TEST_EXPORTS = DISPLAY

include gar/category.mk

# For GNU gettext
PATH := /opt/csw/gnu:$(PATH)
