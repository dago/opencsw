# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nettle
VERSION = 3.0
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = A low-level cryptographic library
define BLURB
  Nettle is a cryptographic library that is designed to fit easily in more or less any context:
  In crypto toolkits for object-oriented languages (C++, Python, Pike, ...), in applications
  like LSH or GNUPG, or even in kernel space.
endef

MASTER_SITES = http://www.lysator.liu.se/~nisse/archive/
DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.lysator.liu.se/~nisse/nettle/

ESSERv3

PACKAGES += CSWlibhogweed3
PKGFILES_CSWlibhogweed3 += $(call pkgfiles_lib,libhogweed.so.3)
SPKG_DESC_CSWlibhogweed3 += A low-level cryptographic library, libhogweed.so.3
RUNTIME_DEP_PKGS_CSWlibhogweed3 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibhogweed3 += CSWlibnettle5

PACKAGES += CSWlibnettle5
PKGFILES_CSWlibnettle5 += $(call pkgfiles_lib,libnettle.so.5)
SPKG_DESC_CSWlibnettle5 += A low-level cryptographic library, libnettle.so.5ary, libnettle.so.4

PACKAGES += CSWlibnettle-dev
PKGFILES_CSWlibnettle-dev = $(PKGFILES_DEVEL)
SPKG_DESC_CSWlibnettle-dev = Development file5 and libhogweed.so.3
RUNTIME_DEP_PKGS_CSWlibnettle-dev += CSWlibhogweed3
RUNTIME_DEP_PKGS_CSWlibnettle-dev += CSWlibnettle5ev += CSWlibnettle4

PACKAGES += CSWlibnettle-utils
SPKG_DESC_CSWlibnettle-utils = Utility programs for libnettle
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibnettle-uti3
RUNTIME_DEP_PKGS_CSWlibnettle-utils += CSWlibnettle5
RUNTIME_DEP_PKGS_CSWlibnettle-utils += CSWlibgmp10l
# This is just the default locationion after configure
CHECKPKG_OVERRIDES_CSWlibnettle-utils += file-with-bad-content|/usr/local|root/opt/csw/sharels += CSWlibgmp10

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

# x86 assembly does not work with Sun Studio
CONFIGURE_ARGS += --disable-assembler

# This is the default install locati6n after configure
CHECKPKG_OVERRIDES_CSWlibnettle-utils += file-with-bad-content|/usr/local|root/opt/csw/share/info/nettle.info

includ