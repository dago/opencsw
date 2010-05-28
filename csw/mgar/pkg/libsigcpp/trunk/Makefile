GARNAME = libsigc++
GARVERSION = 2.2.7
CATEGORIES = lib

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-Comment-out-define-as-we-are-on-Sun-Studio.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES  = CSWlibsigc++ CSWlibsigc++devel

SPKG_DESC_CSWlibsigc++      = Typesafe signal and callback system for C++
SPKG_DESC_CSWlibsigc++devel = Header files and docs for libsigc++

CATALOGNAME_CSWlibsigc++      = libsigc++
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel 

# CSWsigc++ is the previous package name
INCOMPATIBLE_PKGS_CSWlibsigc++ = CSWsigc++
RUNTIME_DEP_PKGS_CSWlibsigc++devel = CSWlibsigc++

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

TEST_TARGET = check

PKGFILES_CSWlibsigc++devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsigc++devel += $(docdir)/.*
PKGFILES_CSWlibsigc++devel += .*\.h
PKGFILES_CSWlibsigc++devel += $(sharedstatedir)/.*

CHECKPKG_OVERRIDES_CSWlibsigc++devel += surplus-dependency|CSWlibsigc++

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-configure-modulated:
	@# Make sure libtool keeps -norunpath during linking
	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
	@$(MAKECOOKIE)
