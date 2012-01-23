# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = rtmpdump
VERSION = 2.3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A toolkit for RTMP streams
define BLURB
endef

MASTER_SITES = http://rtmpdump.mplayerhq.hu/download/
DISTFILES  = $(DISTNAME).tgz

PATCHFILES += 0001-Use-inttypes.h-on-Solaris.patch
PATCHFILES += 0002-Use-Solaris-ld-syntax-for-shared-libs.patch

VENDOR_URL = http://rtmpdump.mplayerhq.hu/

PACKAGES += CSWlibrtmp0
SPKG_DESC_CSWlibrtmp0 = A toolkit for RTMP streams, librtmp.so.0
PKGFILES_CSWlibrtmp0 += $(call pkgfiles_lib,librtmp.so.0)
RUNTIME_DEP_PKGS_CSWlibrtmp0 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibrtmp0 += CSWzlib

PACKAGES += CSWlibrtmp-dev
SPKG_DESC_CSWlibrtmp-dev = Development files for librtmp.so.0
PKGFILES_CSWlibrtmp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibrtmp-dev += CSWlibrtmp0

PACKAGES += CSWrtmpdump
SPKG_DESC_CSWrtmpdump = A toolkit for RTMP streams
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrtmpdump += CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWrtmpdump += CSWosslrt
RUNTIME_DEP_PKGS_CSWrtmpdump += CSWzlib

BUILD64_LIBS_ONLY = 1

EXTRA_CFLAGS += -features=extensions -D__FUNCTION__=__func__
EXTRA_CFLAGS += -DINADDR_NONE=0xffffffffU

BYTE_ORDER_sparc = __BIG_ENDIAN
BYTE_ORDER_i386 = __LITTLE_ENDIAN
EXTRA_CFLAGS += -DBYTE_ORDER=$(BYTE_ORDER_$(GARCH))

# Otherwise "R_SPARC_H44: relocations based on the ABS44 coding model can not be used in building a shared object"
EXTRA_CFLAGS += -KPIC

# The build system is pretty spartanic
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_OVERRIDE_VARS = CC LD CFLAGS LDFLAGS LIBS_posix XLIBS
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_LD = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS) -DRTMPDUMP_VERSION=\\\"v$(VERSION)\\\" -DUSE_OPENSSL
BUILD_OVERRIDE_VAR_LDFLAGS = $(LDFLAGS)
BUILD_OVERRIDE_VAR_LIBS_posix = -lsocket -lnsl
BUILD_OVERRIDE_VAR_XLIBS = -lgnugetopt

INSTALL_OVERRIDE_VARS = prefix bindir sbindir libdir mandir
INSTALL_OVERRIDE_VAR_prefix = $(prefix)
INSTALL_OVERRIDE_VAR_bindir = $(bindir)
INSTALL_OVERRIDE_VAR_sbindir = $(sbindir)
INSTALL_OVERRIDE_VAR_libdir = $(libdir)
INSTALL_OVERRIDE_VAR_mandir = $(mandir)

include gar/category.mk
