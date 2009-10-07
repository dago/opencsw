GARNAME = wireshark
GARVERSION = 1.2.2
CATEGORIES = apps

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.wireshark.org/

#SED = /opt/csw/bin/gsed
#EXTRA_COMMON_EXPORTS = SED

EXTRA_INC = /opt/csw/include/gtk-2.0
EXTRA_INC += /opt/csw/lib/gtk-2.0/include
EXTRA_INC += /opt/csw/include/glib-2.0
EXTRA_INC += /opt/csw/lib/glib-2.0/include
EXTRA_INC += /opt/csw/include/cairo
EXTRA_INC += /opt/csw/include/pango-1.0
EXTRA_INC += /opt/csw/include/atk-1.0

EXTRA_LINKER_FLAGS = -lgtk-x11-2.0

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
