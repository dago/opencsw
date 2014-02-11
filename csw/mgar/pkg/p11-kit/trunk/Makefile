# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = p11-kit
VERSION = 0.20.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Load and enumerate PKCS#11 modules

MASTER_SITES = http://p11-glue.freedesktop.org/releases/
DISTFILES  = $(DISTNAME).tar.gz

# Use patch until this has been fixed:
#   http://bugs.freedesktop.org/show_# PATCHFILES += 0001-Use-getexecname-instead-of-directly-accessing-__argv.patch
PATCHFILES += 0002-remove-include-paths.h-accessing-__argv.patch

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

EXTRA_CPPFLAGS = -features=extensions -D__PRETTY_FUNCTION_CPPFLAGS += -xc99 -D_POSIX_PTHREAD_SEMANTICS -D__FUNCTION__=__func__
NCTION__=__func__
EXTRA_LINKER_FLAGS += -lintl

# For fabs(3m)
EXTRA_LINKER_FLAGS += -lm

# For nanosleep(3rt)
EXTRA_LINKER_FLAGS += -lrt

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARCONFIGURE_ARGS += --without-trust-paths 

EXTRA_BUILD_ENV = V=1RGS = $(DIRPATHS)

EXTRA_PAX_ARGS = -s ,pkcs11.conf.example,pkcs11.conf,

PRESERVECONF += $(sysconfdir)/pkcs11.conf

include 