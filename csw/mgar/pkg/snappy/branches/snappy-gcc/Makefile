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

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES += CSWsnappy-dev
CATALOGNAME_CSWsnappy-dev = snappy_dev
SPKG_DESC_CSWsnappy-dev += $(DESCRIPTION), development files
PKGFILES_CSWsnappy-dev += /opt/csw/gxx/lib/libsnappy.so
PKGFILES_CSWsnappy-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWsnappy-dev += CSWlibsnappy1-gxx

PACKAGES += CSWlibsnappy1-gxx
CATALOGNAME_CSWlibsnappy1-gxx = libsnappy1_gxx
PKGFILES_CSWlibsnappy1-gxx += $(call baseisadirs,$(libdir),libsnappy\.so\.1\.1\.3)
PKGFILES_CSWlibsnappy1-gxx += $(call baseisadirs,$(libdir),libsnappy\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsnappy1-gxx += $(DESCRIPTION), libsnappy.so.1
RUNTIME_DEP_PKGS_CSWlibsnappy1-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsnappy1-gxx += CSWlibstdc++6

include gar/category.mk

