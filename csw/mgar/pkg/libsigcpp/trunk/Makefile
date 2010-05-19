GARNAME = libsigc++
GARVERSION = 2.2.7
CATEGORIES = lib

DESCRIPTION = Typesafe signal and callback system for C++
define BLURB
  Typesafe signal and callback system for C++
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES  = CSWlibsigc++
PACKAGES += CSWlibsigc++devel
SPKG_DESC_CSWlibsigc++ = Typesafe signal and callback system for C++
SPKG_DESC_CSWlibsigc++devel = Header files and docs for libsigc++

CATALOGNAME_CSWlibsigc++= libsigc++
CATALOGNAME_CSWlibsigc++devel = libsigc++_devel 

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

TEST_TARGET = check

PKGFILES_CSWlibsigc++devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsigc++devel += $(docdir)/.*
PKGFILES_CSWlibsigc++devel += .*\.h
PKGFILES_CSWlibsigc++devel += $(sharedstatedir)/.*

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-configure-modulated:
	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
	@$(MAKECOOKIE)
