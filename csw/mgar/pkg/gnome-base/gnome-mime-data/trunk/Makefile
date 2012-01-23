NAME = gnome-mime-data
VERSION = 2.18.0
CATEGORIES = gnome

DESCRIPTION = Contains the base set of file types and applications for GNOME-2
define BLURB
endef

GNOME_PROJ = gnome-mime-data
MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(GNOME_PROJ)-$(VERSION)

PACKAGES = CSWgmimedata 
CATALOGNAME_CSWgmimedata = gmimedata

SPKG_DESC_CSWgmimedata += $(DESCRIPTION)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/gmimedata

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

ARCHALL_CSWgmimedata = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
