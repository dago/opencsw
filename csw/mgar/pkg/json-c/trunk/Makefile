# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = json-c
VERSION = 0.10
GARTYPE = v2

DESCRIPTION = JSON objects in C
define BLURB
	JSON-C implements a reference counting object model that allows you to easily construct JSON objects in C, output them as JSON formatted strings and parse JSON formatted strings back into the C representation of JSON objects.
endef

MASTER_SITES = https://s3.amazonaws.com/json-c_releases/releases/
# GIT_REPOS = git://github.com/json-c/json-c.git

DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

PATCHFILES = 0001-allow-to-use-public-vasprintf-symbol.patch

PACKAGES += CSWlibjson0
CATALOGNAME_CSWlibjson0 = libjson0
PKGFILES_CSWlibjson0 += $(call baseisadirs,$(libdir),libjson\.so\.0\.1\.0)
PKGFILES_CSWlibjson0 += $(call baseisadirs,$(libdir),libjson\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibjson0 += $(DESCRIPTION), libjson.so.0
RUNTIME_DEP_PKGS_CSWlibjson0 += CSWlibgcc-s1

PACKAGES += CSWjson-c-dev
CATALOGNAME_CSWjson-c-dev = json_c_dev
SPKG_DESC_CSWjson-c-dev += $(DESCRIPTION), development files
PKGFILES_CSWjson-c-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWjson-c-dev += CSWlibjson0

# vasprintf test failes with: 
# symbol belongs to unavailable version /lib/libc.so (SUNW_1.22.7)
# EXTRA_CONFIGURE_ENV = LD_OPTIONS=

# EXTRA_CFLAGS = -xnorunpath

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

