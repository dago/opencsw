NAME = libmemcached
VERSION = 0.51
VENDOR_URL = http://libmemcached.org/
CATEGORIES = lib
DESCRIPTION = Library memcached interface
define BLURB
  memcached url
endef
SPKG_SOURCEURL = http://libmemcached.org/
MASTER_SITES = http://launchpad.net/libmemcached/1.0/$(VERSION)/+download/
PATCHFILES = 0001-Do-not-use-Wstrict-prototypes-warning.patch
#PATCHFILES += 0002-use-stdnamespace-for-index.patch
#PATCHFILES += 0003-use-opt-csw-bin-ggrep.patch
#PATCHFILES += 0004-use-opt-csw-bin-ggrep-for-pandora.patch
#PATCHFILES += 0006-fix-tests.patch
#PATCHFILES += 0007-fix-test_h.patch

DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-dtrace

BUILD64 = 1
SKIPTEST = 1

OPT_FLAGS_SOS = -xO3
OPT_FLAGS_GCC = -O2 -pipe

GARCOMPILER = GCC4

LDFLAGS_32="-R/opt/csw/lib/i386"
LDFLAGS_64="-R/opt/csw/lib/amd64"

PACKAGES = CSWlibmemcached
SPKG_DESC_CSWlibmemcached = libmemcached library
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcached8
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibhashkit1
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcachedutil2
RUNTIME_DEP_PKGS_CSWlibmemcached += CSWlibmemcachedprotocol0

PACKAGES += CSWlibhashkit1
CATALOGNAME_CSWlibhashkit1 = libhashkit1
VENDOR_URL_CSWlibhashkit1 = http://libmemcached.org/libMemcached.html
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1\.0\.0)
PKGFILES_CSWlibhashkit1 += $(call baseisadirs,$(libdir),libhashkit\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibhashkit1 += $(DESCRIPTION), libhashkit.so.1

PACKAGES += CSWlibmemcached8
CATALOGNAME_CSWlibmemcached8 = libmemcached8
VENDOR_URL_CSWlibmemcached8 = http://libmemcached.org/libMemcached.html
PKGFILES_CSWlibmemcached8 += $(call baseisadirs,$(libdir),libmemcached\.so\.8\.0\.0)
PKGFILES_CSWlibmemcached8 += $(call baseisadirs,$(libdir),libmemcached\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibmemcached8 += $(DESCRIPTION), libmemcached.so.8

PACKAGES += CSWlibmemcachedprotocol0
CATALOGNAME_CSWlibmemcachedprotocol0 = libmemcachedprotocol0
VENDOR_URL_CSWlibmemcachedprotocol0 = http://libmemcached.org/
PKGFILES_CSWlibmemcachedprotocol0 += $(call baseisadirs,$(libdir),libmemcachedprotocol\.so\.0\.0\.0)
PKGFILES_CSWlibmemcachedprotocol0 += $(call baseisadirs,$(libdir),libmemcachedprotocol\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibmemcachedprotocol0 += $(DESCRIPTION), libmemcachedprotocol.so.0

PACKAGES += CSWlibmemcachedutil2
CATALOGNAME_CSWlibmemcachedutil2 = libmemcachedutil2
VENDOR_URL_CSWlibmemcachedutil2 = http://libmemcached.org/
PKGFILES_CSWlibmemcachedutil2 += $(call baseisadirs,$(libdir),libmemcachedutil\.so\.2\.0\.0)
PKGFILES_CSWlibmemcachedutil2 += $(call baseisadirs,$(libdir),libmemcachedutil\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibmemcachedutil2 += $(DESCRIPTION), libmemcachedutil.so.2
RUNTIME_DEP_PKGS_CSWlibmemcachedutil2 += CSWlibmemcached8

include gar/category.mk

