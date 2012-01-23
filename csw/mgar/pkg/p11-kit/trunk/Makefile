# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = p11-kit
VERSION = 0.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Load and enumerate PKCS#11 modules
define BLURB
endef

MASTER_SITES = http://p11-glue.freedesktop.org/releases/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Hack-around-missing-__argv.patch

VENDOR_URL = http://p11-glue.freedesktop.org/p11-kit.html

PACKAGES += CSWlibp11kit0
SPKG_DESC_CSWlibp11kit0 = Load and enumerate PKCS#11 modules, libp11-kit.so.0
PKGFILES_CSWlibp11kit0 += $(call pkgfiles_lib,libp11-kit.so.0)
PKGFILES_CSWlibp11kit0 += $(sysconfdir)/.*
RUNTIME_DEP_PKGS_CSWlibp11kit0 += CSWlibintl8

PACKAGES += CSWlibp11kit-dev
SPKG_DESC_CSWlibp11kit-dev = Development files for libp11-kit.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibp11kit-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibp11kit-dev += CSWlibp11kit0 

EXTRA_CPPFLAGS = -features=extensions -D__PRETTY_FUNCTION__=__func__
EXTRA_LINKER_FLAGS += -lintl

# For fabs(3m)
EXTRA_LINKER_FLAGS += -lm

# For nanosleep(3rt)
EXTRA_LINKER_FLAGS += -lrt

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS = -s ,pkcs11.conf.example,pkcs11.conf,

PRESERVECONF += $(sysconfdir)/pkcs11.conf

include gar/category.mk

