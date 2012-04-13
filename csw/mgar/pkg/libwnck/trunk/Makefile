NAME = libwnck
VERSION = 2.30.7
# 2.18.3 = .so.18
# 2.19.92 = so.22
# 2.20.3 = .so.22
# 2.24.2 = .so.22
# 2.28.0 = .so.22
# 2.30.7 = .so.22
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library used for writing pagers and tasks lists
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# New glib2 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://ftp.gnome.org/pub/GNOME/sources/libwnck/

BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWgtk2devel

PACKAGES += CSWlibwnck1-22
SPKG_DESC_CSWlibwnck1-22 = Library used for writing pagers and tasks lists, libwnck-1.so.22
PKGFILES_CSWlibwnck1-22 += $(call pkgfiles_lib,libwnck-1.so.22)
PKGFILES_CSWlibwnck1-22 += $(sharedstatedir)/locale/.*/libwnck\.mo
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWstartupnotif
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwnck1-22 += CSWpango
OBSOLETED_BY_CSWlibwnck1-22 += CSWlibwnck

PACKAGES += CSWlibwnck-dev
SPKG_DESC_CSWlibwnck-dev = Development files for libwnck-1.so.22
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWlibwnck1-22
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWglib2devel
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWgtk2devel

CPPFLAGS += -I/opt/csw/include/glib-2.0
CPPFLAGS += -I/opt/csw/lib/glib-2.0/include/
CPPFLAGS += -I/opt/csw/lib/gtk-2.0/include/
CPPFLAGS += -I/opt/csw/include/gdk-pixbuf-2.0/
CPPFLAGS += -I/opt/csw/include/gtk-2.0/
CPPFLAGS += -I/opt/csw/include/cairo
CPPFLAGS += -I/opt/csw/include/pango-1.0
CPPFLAGS += -I/opt/csw/include/atk-1.0/
CPPFLAGS += -I/opt/csw/include/startup-notification-1.0/

# For cos(3m)
EXTRA_LINKER_FLAGS = -lm 

BUILD64_LIBS_ONLY = 1

include gar/category.mk

# Needed for GNU gettext
PATH := /opt/csw/gnu:$(PATH)
