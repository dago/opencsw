NAME = ORBit2
VERSION = 2.14.19
CATEGORIES = lib

DESCRIPTION = ORBit 2.x CORBA tools and libs
define BLURB
  ORBit2 is a CORBA 2.4-compliant Object Request Broker (ORB) featuring
  mature C, C++ and Python bindings.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.bz2

PATCHFILES += 0001-Make-test-non-interactive-on-Solaris.patch

# New glib is only Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibidl-dev

PACKAGES = CSWorbit2
SPKG_DESC_CSWorbit2 = ORBit 2.x CORBA tools and libs
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWorbit2 += CSWlibidl2-0

# No package split yet
CHECKPKG_OVERRIDES_CSWorbit2 += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWorbit2 += shared-lib-package-contains-so-symlink

VENDOR_URL = http://projects.gnome.org/ORBit2/

CPP = /usr/lib/cpp
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS = CPP CXXCPP

BUILD64 = 1

EXTRA_MERGE_INCLUDE_FILES  = $(libdir)/libname-server-2.a
EXTRA_MERGE_DIRS_isa-extra = $(bindir)

include gar/category.mk
