NAME = libwnck
VERSION = 2.18.3
# 2.18.3 = .so.18
# 2.19.92 = so.22
# 2.20.3 = .so.22
# 2.24.2 = .so.22
# 2.28.0 = .so.22
CATEGORIES = lib

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

PACKAGES += CSWlibwnck1-18
SPKG_DESC_CSWlibwnck1-18 = Library used for writing pagers and tasks lists, libwnck-1.so.18
PKGFILES_CSWlibwnck1-18 += $(call pkgfiles_lib,libwnck-1.so.18)
PKGFILES_CSWlibwnck1-18 += $(sharedstatedir)/locale/.*/libwnck\.mo
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWstartupnotif
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwnck1-18 += CSWpango
OBSOLETED_BY_CSWlibwnck1-18 += CSWlibwnck

PACKAGES += CSWlibwnck-dev
SPKG_DESC_CSWlibwnck-dev = Development files for libwnck-1.so.18
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWlibwnck1-18
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWglib2devel
RUNTIME_DEP_PKGS_CSWlibwnck-dev += CSWgtk2devel

# For cos(3m)
EXTRA_LINKER_FLAGS = -lm 

BUILD64 = 1

include gar/category.mk

# Needed for GNU gettext
PATH := /opt/csw/gnu:$(PATH)
