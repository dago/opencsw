# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = snappy
VERSION = 1.0.5
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

prefix = $(BUILD_PREFIX)/gxx
GARCOMPILER = GNU

# Undefined                       first referenced
#  symbol                             in file
# __sync_fetch_and_add_4              snappy_unittest-snappy_unittest.o
ISA_DEFAULT_i386 = pentium_pro

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWsnappy-gcc-dev
SPKG_DESC_CSWsnappy-gcc-dev += $(DESCRIPTION), development files
PKGFILES_CSWsnappy-gcc-dev += /opt/csw/gxx/lib/libsnappy.so
PKGFILES_CSWsnappy-gcc-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsnappy-gcc-dev += CSWlibsnappy1-gxx

PACKAGES += CSWlibsnappy1-gxx
PKGFILES_CSWlibsnappy1-gxx += $(call baseisadirs,$(libdir),libsnappy\.so\.1\.1\.3)
PKGFILES_CSWlibsnappy1-gxx += $(call baseisadirs,$(libdir),libsnappy\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsnappy1-gxx += $(DESCRIPTION), libsnappy.so.1
RUNTIME_DEP_PKGS_CSWlibsnappy1-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsnappy1-gxx += CSWlibstdc++6

include gar/category.mk

