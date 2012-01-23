# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = adns
VERSION = 1.4
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Advanced, easy to use, asynchronous-capable DNS client library and utilities
define BLURB
endef

MASTER_SITES = http://www.chiark.greenend.org.uk/~ian/adns/ftp/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnu.org/s/adns/

PACKAGES += CSWadns
SPKG_DESC_CSWadns = Advanced, easy to use, asynchronous-capable DNS utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWadns = CSWlibadns1

PACKAGES += CSWlibadns-dev
SPKG_DESC_CSWlibadns-dev = Development files for libadns.so.1
PKGFILES_CSWlibadns-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibadns-dev += CSWlibadns1

PACKAGES += CSWlibadns1
SPKG_DESC_CSWlibadns1 = Advanced, easy to use, asynchronous-capable DNS client library, libadns.so.1
PKGFILES_CSWlibadns1 += $(call pkgfiles_lib,libadns.so.1)

BUILD64_LIBS_ONLY = 1

BUILD_OVERRIDE_VARS = MKSHLIB_1 MKSHLIB_3
BUILD_OVERRIDE_VAR_MKSHLIB_1 = $(CC) $(LDFLAGS) -G -h $$(SHLIBSONAME) -o
BUILD_OVERRIDE_VAR_MKSHLIB_3 =

# The makefile doesn't honour DESTDIR
INSTALL_OVERRIDE_DIRS += bindir
INSTALL_OVERRIDE_DIRS += libdir
INSTALL_OVERRIDE_DIRS += includedir

include gar/category.mk

