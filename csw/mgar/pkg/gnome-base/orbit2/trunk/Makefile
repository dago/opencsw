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

PACKAGES = CSWorbit2
CATALOGNAME = orbit2

RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWlibidl

# No package split yet
CHECKPKG_OVERRIDES_CSWorbit2 += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWorbit2 += shared-lib-package-contains-so-symlink

VENDOR_URL = http://projects.gnome.org/ORBit2/

CPP = /usr/lib/cpp
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS = CPP CXXCPP

STRIP_LIBTOOL = 1

BUILD64 = 1

EXTRA_MERGE_INCLUDE_FILES  = $(libdir)/libname-server-2.a

include gar/category.mk
