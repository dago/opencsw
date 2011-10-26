# $Id$
#
NAME = libmemcached
VERSION = 0.53
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

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

PACKAGES += CSWlibmemcached
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibevent2-0-5
SPKG_DESC_CSWlibmemcached = $(DESCRIPTION), main library
SPKG_FULL_REVSTAMP_CSWlibmemcached = 1
CHECKPKG_OVERRIDES_CSWlibmemcached += surplus-dependency|CSWlibevent2-0-5

PACKAGES += CSWlibhashkit1
CATALOGNAME_CSWlibhashkit1 = libhashkit1
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1\.0\.0)
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibhashkit1 += $(DESCRIPTION), libhashkit.so.1
SPKG_FULL_REVSTAMP_CSWlibhashkit1 = 1
RUNTIME_DEP_PKGS_CSWlibhashkit1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibhashkit1 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibhashkit1

PACKAGES += CSWlibmemcached8
CATALOGNAME_CSWlibmemcached8 = libmemcached8
PKGFILES_CSWlibmemcached8 += $(call baseisadirs,$(libdir),libmemcached\.so\.8\.0\.0)
PKGFILES_CSWlibmemcached8 += $(call baseisadirs,$(libdir),libmemcached\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibmemcached8 += $(DESCRIPTION), libmemcached.so.8
SPKG_FULL_REVSTAMP_CSWlibmemcached8 = 1
RUNTIME_DEP_PKGS_CSWlibmemcached8 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmemcached8 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcached8

PACKAGES += CSWlibmemcachedutil2
CATALOGNAME_CSWlibmemcachedutil2 = libmemcachedutil2
PKGFILES_CSWlibmemcachedutil2 += $(call baseisadirs,$(libdir),libmemcachedutil\.so\.2\.0\.0)
PKGFILES_CSWlibmemcachedutil2 += $(call baseisadirs,$(libdir),libmemcachedutil\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibmemcachedutil2 += $(DESCRIPTION), libmemcachedutil.so.2
SPKG_FULL_REVSTAMP_CSWlibmemcachedutil2 = 1
RUNTIME_DEP_PKGS_CSWlibmemcachedutil2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmemcachedutil2 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmemcachedutil2 += CSWlibmemcached8
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcachedutil2

PACKAGES += CSWlibmemcachedprotocol0
CATALOGNAME_CSWlibmemcachedprotocol0 = libmemcachedprotocol0
PKGFILES_CSWlibmemcachedprotocol0 += $(call baseisadirs,$(libdir),libmemcachedprotocol\.so\.0\.0\.0)
PKGFILES_CSWlibmemcachedprotocol0 += $(call baseisadirs,$(libdir),libmemcachedprotocol\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibmemcachedprotocol0 += $(DESCRIPTION), libmemcachedprotocol.so.0
SPKG_FULL_REVSTAMP_CSWlibmemcachedprotocol0 = 1
RUNTIME_DEP_PKGS_CSWlibmemcachedprotocol0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmemcachedprotocol0 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcachedprotocol0

include gar/category.mk

