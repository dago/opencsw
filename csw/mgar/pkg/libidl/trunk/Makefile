NAME = libIDL
VERSION = 0.8.14
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library for handling CORBA IDL
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://ftp.gnome.org/pub/gnome/sources/libIDL/

PACKAGES += CSWlibidl2-0
SPKG_DESC_CSWlibidl2-0 = Library for handling CORBA IDL, libIDL-2.so.0
PKGFILES_CSWlibidl2-0 += $(call pkgfiles_lib,libIDL-2.so.0)
RUNTIME_DEP_PKGS_CSWlibidl2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibidl2-0 += CSWglib2
OBSOLETED_BY_CSWlibidl2-0 += CSWlibidl

PACKAGES += CSWlibidl-dev
SPKG_DESC_CSWlibidl-dev = Development files for libIDL-2.so.0
# pkgfiles is catchall
RUNTIME_DEP_PKGS_CSWlibidl-dev += CSWlibidl2-0

BUILD64_LIBS_ONLY = 1

CPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CPP
CXXCPP = /usr/lib/cpp
EXTRA_COMMON_EXPORTS += CXXCPP

include gar/category.mk
