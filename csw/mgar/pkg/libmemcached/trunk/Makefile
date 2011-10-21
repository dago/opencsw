# $Id$
#
NAME = libmemcached
VERSION = 0.52
VENDOR_URL = http://libmemcached.org/
CATEGORIES = lib
DESCRIPTION = Library memcached interface
define BLURB
  memcached url
endef
SPKG_SOURCEURL = http://libmemcached.org/
MASTER_SITES = http://launchpad.net/libmemcached/1.0/$(VERSION)/+download/

PATCHFILES += 0001-Do-not-do-PANDORA_TEST_VC_DIR.patch
PATCHFILES += 0002-Use-opt-csw-bin-ggrep.patch

BUILD_DEP_PKGS += CSWlibevent-dev
RUNTIME_DEP_PKGS += CSWlibgcc-s1
RUNTIME_DEP_PKGS += CSWlibstdc++6

DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dtrace
CONFIGURE_ARGS += --disable-rpath

BUILD64 = 1
SKIPTEST = 1

OPT_FLAGS_SOS = -xO3
OPT_FLAGS_GCC = -O2 -pipe

GARCOMPILER = GCC4
GARTYPE = 2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-amd64

PACKAGES += CSWlibhashkit1
CATALOGNAME_CSWlibhashkit1 = libhashkit1
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1\.0\.0)
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibhashkit1 += $(DESCRIPTION), libhashkit.so.1
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibhashkit1

include gar/category.mk

