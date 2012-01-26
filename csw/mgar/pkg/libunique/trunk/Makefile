NAME = libunique
VERSION = 1.1.6
CATEGORIES = gnome
GARTYPE = v2

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

# New glib2 is Solaris 10 only
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://live.gnome.org/LibUnique

BUILD_DEP_PKGS += CSWlibdbus-glib-dev

PACKAGES += CSWlibunique1-0-0
SPKG_DESC_CSWlibunique1-0-0 += Library for writing single instance application
PKGFILES_CSWlibunique1-0-0 += $(call pkgfiles_lib,libunique-1.0.so.0)
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWlibunique1-0-0 += CSWlibatk1-0-0

PACKAGES += CSWlibunique-dev
SPKG_DESC_CSWlibunique-dev = Development files for libunique-1.0.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibunique1-0-0
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWgtk2devel
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibatk-dev
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWlibcairo-dev
RUNTIME_DEP_PKGS_CSWlibunique-dev += CSWpangodevel

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

EXTRA_LINKER_FLAGS = -lsocket -lnsl

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
