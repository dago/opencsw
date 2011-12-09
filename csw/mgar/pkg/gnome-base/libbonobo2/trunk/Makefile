NAME = libbonobo
VERSION = 2.32.1
CATEGORIES = gnome

DESCRIPTION = GNOME component and compound document system
define BLURB
endef

VENDOR_URL = http://live.gnome.org/Bonobo
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Use-bash-on-test.patch

# New glib2 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWlibbonobo2
SPKG_DESC_CSWlibbonobo2 = GNOME component and compound document system
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgio2-0-0

BUILD64 = 1

CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
