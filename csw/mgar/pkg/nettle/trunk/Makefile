# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nettle
VERSION = 2.1
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = A low-level cryptographic library
define BLURB
  Nettle is a cryptographic library that is designed to fit easily in more or less any context:
  In crypto toolkits for object-oriented languages (C++, Python, Pike, ...), in applications
  like LSH or GNUPG, or even in kernel space.
endef

MASTER_SITES = http://www.lysator.liu.se/~nisse/archive/
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Add-dynamic-linkage-information-for-Solaris.patch

VENDOR_URL = http://www.lysator.liu.se/~nisse/nettle/

PACKAGES += CSWlibhogweed2
PKGFILES_CSWlibhogweed2 += $(call pkgfiles_lib,libhogweed.so.2)
SPKG_DESC_CSWlibhogweed2 += A low-level cryptographic library, libhogweed.so.2
RUNTIME_DEP_PKGS_CSWlibhogweed2 += CSWlibgmp
RUNTIME_DEP_PKGS_CSWlibhogweed2 += CSWlibnettle4

PACKAGES += CSWlibnettle4
PKGFILES_CSWlibnettle4 += $(call pkgfiles_lib,libnettle.so.4)
SPKG_DESC_CSWlibnettle4 += A low-level cryptographic library, libnettle.so.4

PACKAGES += CSWlibnettle-dev
PKGFILES_CSWlibnettle-dev = $(PKGFILES_DEVEL)
SPKG_DESC_CSWlibnettle-dev = Development files for libnettle.so.4 and libhogweed.so.2
RUNTIME_DEP_PKGS_CSWlibnettle-dev += CSWlibhogweed2
RUNTIME_DEP_PKGS_CSWlibnettle-dev += CSWlibnettle4

PACKAGES += CSWlibnettle-utils
SPKG_DESC_CSWlibnettle-utils = Utility programs for libnettle
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibnettle-utils += CSWlibhogweed2
RUNTIME_DEP_PKGS_CSWlibnettle-utils += CSWlibnettle4
RUNTIME_DEP_PKGS_CSWlibnettle-utils += CSWlibgmp

BUILD64 = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

# This is the default install location after configure
CHECKPKG_OVERRIDES_CSWlibnettle-utils += file-with-bad-content|/usr/local|root/opt/csw/share/info/nettle.info

include gar/category.mk

