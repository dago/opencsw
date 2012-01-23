NAME = libgsf
VERSION = 1.14.21
CATEGORIES = gnome

DESCRIPTION = GNOME Structured File Library
define BLURB
	The GNOME Structured File Library (GSF) is an I/O abstraction for
	reading/writing compound files. GSF is released under the GNU Lesser
	General Public License (GNU LGPL), which allows for flexible licensing of
	client applications. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# New glib is Solaris 10 only
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWgtk-doc
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibxml2devel

PACKAGES += CSWlibgsf1-114
SPKG_DESC_CSWlibgsf1-114 = GNOME structured file library, libgsf-1.so.114
PKGFILES_CSWlibgsf1-114 += $(call pkgfiles_lib,libgsf-1.so.114)
PKGFILES_CSWlibgsf1-114 += $(sharedstatedir)/locale/.*\.mo
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgsf1-114 += CSWlibgio2-0-0

PACKAGES += CSWlibgsf-gnome1-114
SPKG_DESC_CSWlibgsf-gnome1-114 = GNOME structured file library, libgsf-gnome1.so.114
PKGFILES_CSWlibgsf-gnome1-114 += $(call pkgfiles_lib,libgsf-gnome-1.so.114)
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibgsf-gnome1-114 += CSWlibgio2-0-0

PACKAGES += CSWlibgsf-dev
SPKG_DESC_CSWlibgsf-dev = Development files for libgsf-1.so.114 and libgsf-gnome1.so.114
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgsf1-114
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgsf-gnome1-114
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgsf-dev += CSWlibgio2-0-0

# The -L/opt/csw/lib is too early and disturbs the build with the installed libgsf
LINKER_FLAGS =

CONFIGURE_ARGS += $(DIRPATHS)

# There are link errors on newly built gnomemodule.la, disable for now
CONFIGURE_ARGS += --without-python

# Missing 64-bit libs:
# libgnomevfs-2.so libgconf-2.so libbonobo-2.so libbonobo-activation.so
BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
