NAME = libbonobo
VERSION = 2.32.1
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GNOME component and compound document system
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Use-bash-on-test.patch

# New glib2 is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://live.gnome.org/Bonobo

PACKAGES += CSWlibbonobo2
SPKG_DESC_CSWlibbonobo2 = GNOME component and compound document system
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWorbit2
OBSOLETED_BY_CSWlibbonobo2 = CSWbonobo2
CATALOGNAME_CSWbonobo2 = libbonobo2_stub

# This is an example
CHECKPKG_OVERRIDES_CSWlibbonobo2 += file-with-bad-content|/usr/local|root/etc/opt/csw/bonobo-activation/bonobo-activation-config.xml
CHECKPKG_OVERRIDES_CSWlibbonobo2 += file-with-bad-content|/usr/local|root/opt/csw/share/gtk-doc/html/bonobo-activation/configuring.html

# No package split for now
CHECKPKG_OVERRIDES_CSWlibbonobo2 += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWlibbonobo2 += non-uniform-lib-versions-in-package

BUILD64_LIBS_ONLY = 1

CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

# Skip testsuite as there is one test failing, reenable when this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=665851
SKIPTEST ?= 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
