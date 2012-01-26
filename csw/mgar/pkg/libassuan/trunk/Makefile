NAME = libassuan
VERSION = 2.0.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = IPC library used by some GnuPG related software
define BLURB
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libassuan/
DISTFILES  = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.gnupg.org/download/#libassuan

BUILD_DEP_PKGS += CSWlibgpgerr-dev

PACKAGES += CSWlibassuan0
SPKG_DESC_CSWlibassuan0 = IPC library used by some GnuPG related software, libassuan.so.0
PKGFILES_CSWlibassuan0 += $(call pkgfiles_lib,libassuan.so.0)
RUNTIME_DEP_PKGS_CSWlibassuan0 += CSWlibgpg-error0
OBSOLETED_BY_CSWlibassuan0 += CSWlibassuan

PACKAGES += CSWlibassuan-dev
SPKG_DESC_CSWlibassuan-dev = Development files for libassuan.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibassuan-dev += CSWlibassuan0

BUILD64_LIBS_ONLY = 1

# Disable tests until this is fixed:
#   https://bugs.g10code.com/gnupg/msg4081
SKIPTEST ?= 1

include gar/category.mk
