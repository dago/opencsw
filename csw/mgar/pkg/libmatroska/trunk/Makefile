NAME = libmatroska
VERSION = 1.1.0
CATEGORIES = lib

DESCRIPTION = A C++ libary to parse Matroska files (.mkv and .mka)
define BLURB
endef

MASTER_SITES = http://dl.matroska.org/downloads/libmatroska/
DISTFILES += $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Adjust-for-Solaris-shared-library.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.matroska.org/

PACKAGES += CSWlibmatroska
CATALOGNAME_CSWlibmatroska = libmatroska
SPKG_DESC_CSWlibmatroska = Transitional package as contents moved to CSWlibmatroska3
RUNTIME_DEP_PKGS_CSWlibmatroska += CSWlibmatroska3
CHECKPKG_OVERRIDES_CSWlibmatroska += surplus-dependency|CSWlibmatroska3
PKGFILES_CSWlibmatroska = NOFILES
ARCHALL_CSWlibmatroska = 1

PACKAGES += CSWlibmatroska-dev
CATALOGNAME_CSWlibmatroska-dev = libmatroska_dev
SPKG_DESC_CSWlibmatroska-dev = Development files for libmatroska
RUNTIME_DEP_PKGS_CSWlibmatroska-dev = CSWlibmatroska3

PACKAGES += CSWlibmatroska3
CATALOGNAME_CSWlibmatroska3 = libmatroska3
SPKG_DESC_CSWlibmatroska3 = Library for Extensible Binary Meta Language providing libmatroska.so.3
PKGFILES_CSWlibmatroska3 = $(call baseisadirs,$(libdir),libmatroska\.so\.3(\.\d+)*)

# These will go away after libebml has been released. We must release
# matroska and ebml at the same time as I missed out setting a SONAME in libebml
# which is references as simple .so by matroska ATM
CHECKPKG_OVERRIDES_CSWlibmatroska3 += unidentified-dependency|CSWlibebml3
CHECKPKG_OVERRIDES_CSWlibmatroska3 += soname-not-found|libebml.so.3|is|needed|by|opt/csw/lib/libmatroska.so.3
CHECKPKG_OVERRIDES_CSWlibmatroska3 += soname-not-found|libebml.so.3|is|needed|by|opt/csw/lib/amd64/libmatroska.so.3
CHECKPKG_OVERRIDES_CSWlibmatroska3 += surplus-dependency|CSWlibebml3

LICENSE = LICENSE.LGPL

EXTRA_LINKER_FLAGS = -norunpath

RUNTIME_DEP_PKGS = CSWlibebml3
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

BUILD64 = 1
NOISALIST = 1

CONFIGURE_SCRIPTS = 

# Needed for shared library
EXTRA_CFLAGS = -xcode=pic32
EXTRA_CXXFLAGS = -xcode=pic32

WARNINGFLAGS =
BUILD_OVERRIDE_DIRS = CC CXX LD CFLAGS WARNINGFLAGS
BUILD_SCRIPTS = $(WORKSRC)/make/linux/Makefile

TEST_SCRIPTS = 

INSTALL_OVERRIDE_VARS = CC CXX LD CFLAGS WARNINGFLAGS INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall
INSTALL_OVERRIDE_DIRS = prefix libdir includedir
INSTALL_SCRIPTS = $(WORKSRC)/make/linux/Makefile

include gar/category.mk
