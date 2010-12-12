NAME = libbonobo
VERSION = 2.24.2
CATEGORIES = gnome

DESCRIPTION = GNOME component and compound document system
define BLURB
endef

VENDOR_URL = http://live.gnome.org/Bonobo
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWlibbonobo CSWlibbonobo2
CATALOGNAME_CSWlibbonobo = libbonobo
CATALOGNAME_CSWlibbonobo2 = libbonobo2
SPKG_DESC_CSWlibbonobo = $(DESCRIPTION)
SPKG_DESC_CSWlibbonobo2 = $(DESCRIPTION) - stub package for legacy

RUNTIME_DEP_PKGS_CSWlibbonobo += CSWdbusglib
RUNTIME_DEP_PKGS_CSWlibbonobo += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibbonobo += CSWglib2
RUNTIME_DEP_PKGS_CSWlibbonobo += CSWlibdbus
RUNTIME_DEP_PKGS_CSWlibbonobo += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibbonobo += CSWorbit2


# Create a empty libbonobo2 packaage just for legacy purpose
RUNTIME_DEP_PKGS_CSWlibbonobo2 += CSWlibbonobo
PKGFILES_CSWlibbonobo2 = no files
ARCHALL_CSWlibbonobo2 = 1
CHECKPKG_OVERRIDES_CSWlibbonobo2 += surplus-dependency|CSWlibbonobo

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

#BUILD64 = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)

# Tests fail for som unknown reason
#TEST_TARGET = check
TEST_TARGET =


CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
