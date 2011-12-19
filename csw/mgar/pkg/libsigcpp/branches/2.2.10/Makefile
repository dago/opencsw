# $Id$
NAME = libsigc++
VERSION = 2.2.10
CATEGORIES = lib

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.xz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES  = CSWlibsigc++ CSWlibsigc++-dev CSWlibsigc++-doc

SPKG_DESC_CSWlibsigc++      = Typesafe signal and callback system for C++
SPKG_DESC_CSWlibsigc++-dev = Header files for libsigc++
SPKG_DESC_CSWlibsigc++-doc  = Docs for libsigc++

# CSWsigc++ is the previous package name
INCOMPATIBLE_PKGS_CSWlibsigc++ = CSWsigc++
RUNTIME_DEP_PKGS_CSWlibsigc++-dev = CSWlibsigc++

BUILD64 = 1
EXTRA_CONFIGURE_ENV = MAKE=gmake
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

PKGFILES_CSWlibsigc++-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsigc++-dev += .*\.h
OBSOLETED_BY_CSWlibsigc++-dev = CSWlibsigc++devel
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel_stub

PKGFILES_CSWlibsigc++-doc  = $(docdir)/.*
PKGFILES_CSWlibsigc++-doc += $(sharedstatedir)/devhelp/.*
ARCHALL_CSWlibsigc++-doc = 1

CHECKPKG_OVERRIDES_CSWlibsigc++-dev += surplus-dependency|CSWlibsigc++

include gar/category.mk

post-configure-modulated:
	@# Make sure libtool keeps -norunpath during linking
	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
	@$(MAKECOOKIE)
