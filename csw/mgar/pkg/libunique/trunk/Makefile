NAME = libunique
VERSION = 1.1.6
CATEGORIES = gnome

DESCRIPTION = Library for writing single instance application
define BLURB
	Unique is a library for writing single instance application. If you launch
	a single instance application twice, the second instance will either just
	quit or will send a message to the running instance.

	Unique makes it easy to write this kind of applications, by providing a
	base class, taking care of all the IPC machinery needed to send messages
	to a running instance, and also handling the startup notification side. 
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES += CSWlibunique
SPKG_DESC_CSWlibunique += Library for writing single instance application
RUNTIME_DEP_PKGS_CSWlibunique += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibunique += CSWftype2
RUNTIME_DEP_PKGS_CSWlibunique += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibunique += CSWglib2
RUNTIME_DEP_PKGS_CSWlibunique += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibunique += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibunique += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibunique += CSWpango
RUNTIME_DEP_PKGS_CSWlibunique += CSWdbusglib
RUNTIME_DEP_PKGS_CSWlibunique += CSWlibdbus

PACKAGES += CSWlibunique-dev
SPKG_DESC_CSWlibunique-dev = Development files for lib
PKGFILES_CSWlibunique-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibunique-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibunique
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWglib2devel
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWgtk2devel
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibatkdevel
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibcairodevel
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWpangodevel

BUILD_DEP_PKGS += CSWdbusglibdev

VENDOR_URL = http://live.gnome.org/LibUnique

BUILD64 = 1
NOISALIST = 1

EXTRA_LINKER_FLAGS = -lsocket -lnsl

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
# This needs a newer GTK, 2.18.x does not have it, reenable when GTK has been updated
CONFIGURE_ARGS += --enable-introspection=no

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
