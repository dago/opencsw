NAME = libebml
VERSION = 1.2.0
CATEGORIES = lib

DESCRIPTION = Library for Extensible Binary Meta Language
define BLURB
endef

MASTER_SITES = http://dl.matroska.org/downloads/libebml/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Adjust-for-Solaris-shared-library.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://www.matroska.org/

PACKAGES += CSWlibebml
CATALOGNAME_CSWlibebml = libebml
SPKG_DESC_CSWlibebml = Transitional package as contents moved to CSWlibebml3
RUNTIME_DEP_PKGS_CSWlibebml += CSWlibebml3
CHECKPKG_OVERRIDES_CSWlibebml += surplus-dependency|CSWlibebml3
PKGFILES_CSWlibebml = NOFILES
ARCHALL_CSWlibebml = 1

PACKAGES += CSWlibebml-dev
CATALOGNAME_CSWlibebml-dev = libebml_dev
SPKG_DESC_CSWlibebml-dev = Development files for libebml
RUNTIME_DEP_PKGS_CSWlibebml-dev = CSWlibebml3

PACKAGES += CSWlibebml3
CATALOGNAME_CSWlibebml3 = libebml3
SPKG_DESC_CSWlibebml3 = Library for Extensible Binary Meta Language providing libebml.so.3
PKGFILES_CSWlibebml3 = $(call baseisadirs,$(libdir),libebml\.so\.3(\.\d+)*)

LICENSE = LICENSE.LGPL

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_SCRIPTS = 

# Needed for shared library
EXTRA_CFLAGS = -xcode=pic32
EXTRA_CXXFLAGS = -xcode=pic32

EXTRA_LINKER_FLAGS = -norunpath

WARNINGFLAGS =
BUILD_OVERRIDE_DIRS = CC CXX LD CFLAGS WARNINGFLAGS
BUILD_SCRIPTS = $(WORKSRC)/make/linux/Makefile

TEST_SCRIPTS = 

INSTALL_OVERRIDE_VARS = CC CXX LD CFLAGS WARNINGFLAGS INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /opt/csw/bin/ginstall
INSTALL_OVERRIDE_DIRS = prefix libdir includedir
includedir = $(prefix)/include/ebml
INSTALL_SCRIPTS = $(WORKSRC)/make/linux/Makefile

include gar/category.mk
