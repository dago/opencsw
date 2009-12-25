GARNAME = wireshark
GARVERSION = 1.2.3
CATEGORIES = apps

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
  Wireshark is the world's foremost network protocol analyzer, and is the
  de facto (and often de jure) standard across many industries and
  educational institutions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

REQUIRED_PKGS += CSWgcrypt CSWgeoip CSWggettextrt CSWglib2 CSWgnutls
REQUIRED_PKGS += CSWgpgerr CSWgtk2 CSWkrb5lib CSWlibpcap CSWlibxext
REQUIRED_PKGS += CSWlua CSWpango CSWpcrert CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.wireshark.org/

#SED = /opt/csw/bin/gsed
#EXTRA_COMMON_EXPORTS = SED

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

#EXTRA_INC += /opt/csw/include/gtk-2.0
#EXTRA_INC += /opt/csw/lib/gtk-2.0/include
#EXTRA_INC += /opt/csw/include/glib-2.0
#EXTRA_INC += /opt/csw/lib/glib-2.0/include
#EXTRA_INC += /opt/csw/include/cairo
#EXTRA_INC += /opt/csw/include/pango-1.0
#EXTRA_INC += /opt/csw/include/atk-1.0

#EXTRA_LINKER_FLAGS = -lgtk-x11-2.0 -lX11 /usr/openwin/lib/libXext.so
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
