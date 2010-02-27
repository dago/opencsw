GARNAME = ORBit2
GARVERSION = 2.14.17
CATEGORIES = lib

DESCRIPTION = ORBit 2.x CORBA tools and libs
define BLURB
  ORBit2 is a CORBA 2.4-compliant Object Request Broker (ORB) featuring
  mature C, C++ and Python bindings.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWorbit2
CATALOGNAME = orbit2

RUNTIME_DEP_PKGS = CSWggettextrt CSWglib2 CSWlibidl

SPKG_SOURCEURL = http://projects.gnome.org/ORBit2/

# Patch from
#   https://bugzilla.gnome.org/show_bug.cgi?id=563046
# This also solves
#   https://bugzilla.gnome.org/show_bug.cgi?id=558796
PATCHFILES = patch-test-foo.diff
PATCHDIRLEVEL = 0

CONFIGURE_ARGS  = $(DIRPATHS)
STRIP_LIBTOOL = 1

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NOISAEXEC = 1

TEST_TARGET = check

EXTRA_MERGE_INCLUDE_FILES  = $(libdir)/libname-server-2.a

CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk
